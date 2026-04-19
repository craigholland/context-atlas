"""End-to-end tests for the starter Context Atlas assembly service."""

from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from context_atlas.adapters import (
    InMemorySourceRegistry,
    LexicalRetrievalMode,
    LexicalRetriever,
)
from context_atlas.domain.messages import LogMessage
from context_atlas.domain.models import (
    ContextBudget,
    ContextBudgetSlot,
    ContextBudgetSlotMode,
    ContextMemoryEntry,
    ContextSource,
    ContextSourceAuthority,
    ContextSourceClass,
)
from context_atlas.infrastructure.assembly import (
    assemble_with_starter_context_service,
    build_starter_context_assembly_service,
    write_standard_proof_artifacts,
)
from context_atlas.infrastructure.config import (
    AssemblySettings,
    ContextAtlasSettings,
    LoggingSettings,
    MemorySettings,
)
from context_atlas.rendering import render_packet_context


class ContextAssemblyServiceTests(unittest.TestCase):
    """Verify PR 7 orchestration across retrieval, ranking, budget, memory, and trace."""

    def setUp(self) -> None:
        self.sources = (
            ContextSource(
                source_id="charter",
                title="Context Atlas Charter",
                content=(
                    "Context Atlas governs what enters model context. "
                    "Authoritative sources should outrank planning notes when the "
                    "system assembles a packet for a model."
                ),
                source_class=ContextSourceClass.AUTHORITATIVE,
                authority=ContextSourceAuthority.BINDING,
            ),
            ContextSource(
                source_id="planning",
                title="Planning Notes",
                content=(
                    "Planning notes discuss retrieval, budgeting, and orchestration, "
                    "but they should not override binding architectural guidance."
                ),
                source_class=ContextSourceClass.PLANNING,
                authority=ContextSourceAuthority.PREFERRED,
            ),
            ContextSource(
                source_id="review",
                title="Review Findings",
                content=(
                    "Review findings mention compression risks, duplicate context, and "
                    "the need to keep selection decisions visible in packet traces."
                ),
                source_class=ContextSourceClass.REVIEWS,
                authority=ContextSourceAuthority.ADVISORY,
            ),
        )
        self.registry = InMemorySourceRegistry(self.sources)
        self.retriever = LexicalRetriever(
            self.registry,
            mode=LexicalRetrievalMode.TFIDF,
        )
        self.settings = ContextAtlasSettings(
            logging=LoggingSettings(logger_name="context_atlas.tests.assembly"),
            assembly=AssemblySettings(
                default_total_budget=128,
                default_retrieval_top_k=1,
            ),
            memory=MemorySettings(
                short_term_count=2,
                decay_rate=0.0,
                dedup_threshold=0.75,
            ),
        )

    def test_assemble_returns_empty_packet_when_no_sources_exist(self) -> None:
        service = build_starter_context_assembly_service(
            retriever=LexicalRetriever(InMemorySourceRegistry()),
            settings=self.settings,
        )

        packet = service.assemble(query="authority aware budgeting")

        self.assertEqual(packet.selected_candidates, ())
        self.assertEqual(packet.selected_memory_entries, ())
        self.assertIsNone(packet.compression_result)
        self.assertEqual(packet.item_count, 0)
        self.assertEqual(packet.trace.metadata["service"], "context_assembly_service")
        self.assertEqual(packet.trace.metadata["retrieved_candidate_count"], "0")
        self.assertIn("budget:documents", {d.source_id for d in packet.trace.decisions})

    def test_factory_uses_settings_defaults_for_retrieval_limit(self) -> None:
        service = build_starter_context_assembly_service(
            retriever=self.retriever,
            settings=self.settings,
        )

        packet = service.assemble(query="context model authoritative sources")

        self.assertEqual(len(packet.selected_candidates), 1)
        self.assertEqual(packet.selected_candidates[0].source.source_id, "charter")
        self.assertEqual(packet.metadata["ranked_candidate_count"], "1")

    def test_factory_passes_ranking_threshold_into_policy_surface(self) -> None:
        service = build_starter_context_assembly_service(
            retriever=self.retriever,
            settings=self.settings.model_copy(
                update={
                    "assembly": AssemblySettings(
                        default_total_budget=128,
                        default_retrieval_top_k=3,
                        ranking_minimum_score=2.0,
                    )
                }
            ),
        )

        packet = service.assemble(query="context model authoritative sources")

        self.assertEqual(packet.selected_candidates, ())
        self.assertEqual(packet.metadata["ranked_candidate_count"], "0")

    def test_one_shot_infrastructure_helper_reuses_shared_service_path(self) -> None:
        packet = assemble_with_starter_context_service(
            retriever=self.retriever,
            query="context model authoritative sources",
            settings=self.settings,
            metadata={"workflow": "codex_repository"},
        )

        self.assertEqual(len(packet.selected_candidates), 1)
        self.assertEqual(packet.selected_candidates[0].source.source_id, "charter")
        self.assertEqual(packet.trace.metadata["request_workflow"], "codex_repository")

    def test_assemble_applies_compression_when_budget_is_tight(self) -> None:
        service = build_starter_context_assembly_service(
            retriever=self.retriever,
            settings=self.settings.model_copy(
                update={
                    "assembly": AssemblySettings(
                        default_total_budget=64,
                        default_retrieval_top_k=3,
                    )
                }
            ),
        )

        packet = service.assemble(
            query="context packet compression retrieval authority planning review"
        )

        self.assertIsNotNone(packet.compression_result)
        self.assertTrue(packet.compression_result.was_applied)
        self.assertTrue(packet.compression_was_applied)
        self.assertLess(
            packet.compression_result.compressed_chars,
            packet.compression_result.original_chars,
        )
        self.assertEqual(packet.trace.metadata["compression_present"], "true")
        self.assertEqual(packet.trace.metadata["compression_applied"], "true")

    def test_assemble_includes_memory_entries_in_packet_and_rendered_output(
        self,
    ) -> None:
        service = build_starter_context_assembly_service(
            retriever=self.retriever,
            settings=self.settings.model_copy(
                update={
                    "assembly": AssemblySettings(
                        default_total_budget=256,
                        default_retrieval_top_k=2,
                    )
                }
            ),
        )
        memory_entries = (
            ContextMemoryEntry(
                entry_id="memory-1",
                source=ContextSource(
                    source_id="memory-source-1",
                    content=(
                        "Earlier work established that authoritative sources should be "
                        "favored when context packets are assembled."
                    ),
                    source_class=ContextSourceClass.MEMORY,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
                recorded_at_epoch_seconds=100.0,
                importance=1.0,
            ),
        )

        packet = service.assemble(
            query="authoritative packet assembly",
            memory_entries=memory_entries,
            budget=ContextBudget(
                total_tokens=256,
                slots=(
                    ContextBudgetSlot(
                        slot_name="memory",
                        token_limit=64,
                        mode=ContextBudgetSlotMode.FIXED,
                    ),
                    ContextBudgetSlot(
                        slot_name="documents",
                        token_limit=256,
                        mode=ContextBudgetSlotMode.ELASTIC,
                        priority=10,
                    ),
                ),
            ),
            now_epoch_seconds=150.0,
        )

        rendered = render_packet_context(packet)

        self.assertEqual(len(packet.selected_memory_entries), 1)
        self.assertEqual(packet.item_count, len(packet.selected_candidates) + 1)
        self.assertIn("authoritative sources should be favored", rendered)
        self.assertIn(
            "system assembles a packet for a model",
            rendered,
        )

    def test_rendering_does_not_mutate_canonical_packet_state(self) -> None:
        service = build_starter_context_assembly_service(
            retriever=self.retriever,
            settings=self.settings.model_copy(
                update={
                    "assembly": AssemblySettings(
                        default_total_budget=256,
                        default_retrieval_top_k=2,
                    )
                }
            ),
        )

        packet = service.assemble(query="authoritative packet assembly")
        before = packet.model_dump()

        rendered = render_packet_context(packet)
        after = packet.model_dump()

        self.assertTrue(rendered)
        self.assertEqual(before, after)

    def test_assemble_trace_captures_stage_metadata_and_budget_rejections(self) -> None:
        service = build_starter_context_assembly_service(
            retriever=self.retriever,
            settings=self.settings.model_copy(
                update={
                    "assembly": AssemblySettings(
                        default_total_budget=128,
                        default_retrieval_top_k=3,
                    )
                }
            ),
        )
        memory_entries = (
            ContextMemoryEntry(
                entry_id="memory-keep",
                source=ContextSource(
                    source_id="memory-keep-source",
                    content="Keep authoritative architecture decisions visible.",
                    source_class=ContextSourceClass.MEMORY,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
                recorded_at_epoch_seconds=100.0,
                importance=0.9,
            ),
            ContextMemoryEntry(
                entry_id="memory-drop",
                source=ContextSource(
                    source_id="memory-drop-source",
                    content=(
                        "This long memory entry repeats architectural guidance and should "
                        "overflow a tiny memory budget allocation in the packet service."
                    ),
                    source_class=ContextSourceClass.MEMORY,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
                recorded_at_epoch_seconds=101.0,
                importance=0.8,
            ),
        )

        packet = service.assemble(
            query="architecture packet trace compression",
            memory_entries=memory_entries,
            budget=ContextBudget(
                total_tokens=128,
                slots=(
                    ContextBudgetSlot(
                        slot_name="memory",
                        token_limit=2,
                        mode=ContextBudgetSlotMode.FIXED,
                    ),
                    ContextBudgetSlot(
                        slot_name="documents",
                        token_limit=128,
                        mode=ContextBudgetSlotMode.ELASTIC,
                        priority=10,
                    ),
                ),
            ),
            now_epoch_seconds=150.0,
        )

        decision_source_ids = {
            decision.source_id for decision in packet.trace.decisions
        }

        self.assertIn("ranking_ranking_policy", packet.trace.metadata)
        self.assertIn("memory_memory_policy", packet.trace.metadata)
        self.assertIn("budget_budget_total_tokens", packet.trace.metadata)
        self.assertIn("compression_present", packet.trace.metadata)
        self.assertIn("budget:documents", decision_source_ids)
        self.assertIn("compression", decision_source_ids)
        self.assertIn("memory-drop", decision_source_ids)

    def test_short_term_memory_survives_tight_memory_slot_budget(self) -> None:
        service = build_starter_context_assembly_service(
            retriever=self.retriever,
            settings=self.settings.model_copy(
                update={
                    "memory": MemorySettings(
                        short_term_count=1,
                        decay_rate=0.0,
                        dedup_threshold=0.75,
                    )
                }
            ),
        )
        memory_entries = (
            ContextMemoryEntry(
                entry_id="memory-old",
                source=ContextSource(
                    source_id="memory-old-source",
                    content=(
                        "Older long-term guidance about authoritative packet assembly "
                        "and memory governance that should remain eligible but lose "
                        "to the short-term keep window when only one entry fits."
                    ),
                    source_class=ContextSourceClass.MEMORY,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
                recorded_at_epoch_seconds=100.0,
                importance=1.1,
            ),
            ContextMemoryEntry(
                entry_id="memory-recent",
                source=ContextSource(
                    source_id="memory-recent-source",
                    content="Recent keep note.",
                    source_class=ContextSourceClass.MEMORY,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
                recorded_at_epoch_seconds=149.0,
                importance=0.7,
            ),
        )

        packet = service.assemble(
            query="authoritative packet assembly",
            memory_entries=memory_entries,
            budget=ContextBudget(
                total_tokens=128,
                slots=(
                    ContextBudgetSlot(
                        slot_name="memory",
                        token_limit=4,
                        mode=ContextBudgetSlotMode.FIXED,
                    ),
                    ContextBudgetSlot(
                        slot_name="documents",
                        token_limit=128,
                        mode=ContextBudgetSlotMode.ELASTIC,
                        priority=10,
                    ),
                ),
            ),
            now_epoch_seconds=150.0,
        )

        self.assertEqual(
            tuple(entry.entry_id for entry in packet.selected_memory_entries),
            ("memory-recent",),
        )
        memory_old_decisions = [
            decision
            for decision in packet.trace.decisions
            if decision.source_id == "memory-old"
        ]
        self.assertTrue(memory_old_decisions)
        self.assertTrue(
            any(
                "out_of_budget"
                in tuple(reason.value for reason in decision.reason_codes)
                for decision in memory_old_decisions
            )
        )

    def test_newest_recent_memory_is_kept_first_under_tight_budget(self) -> None:
        service = build_starter_context_assembly_service(
            retriever=self.retriever,
            settings=self.settings.model_copy(
                update={
                    "memory": MemorySettings(
                        short_term_count=2,
                        decay_rate=0.0,
                        dedup_threshold=0.75,
                    )
                }
            ),
        )
        memory_entries = (
            ContextMemoryEntry(
                entry_id="memory-recent-older",
                source=ContextSource(
                    source_id="memory-recent-older-source",
                    content="Older recent memory note.",
                    source_class=ContextSourceClass.MEMORY,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
                recorded_at_epoch_seconds=148.0,
                importance=0.8,
            ),
            ContextMemoryEntry(
                entry_id="memory-recent-newest",
                source=ContextSource(
                    source_id="memory-recent-newest-source",
                    content="Newest recent memory note.",
                    source_class=ContextSourceClass.MEMORY,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
                recorded_at_epoch_seconds=149.0,
                importance=0.7,
            ),
        )

        packet = service.assemble(
            query="authoritative packet assembly",
            memory_entries=memory_entries,
            budget=ContextBudget(
                total_tokens=128,
                slots=(
                    ContextBudgetSlot(
                        slot_name="memory",
                        token_limit=6,
                        mode=ContextBudgetSlotMode.FIXED,
                    ),
                    ContextBudgetSlot(
                        slot_name="documents",
                        token_limit=128,
                        mode=ContextBudgetSlotMode.ELASTIC,
                        priority=10,
                    ),
                ),
            ),
            now_epoch_seconds=150.0,
        )

        self.assertEqual(
            tuple(entry.entry_id for entry in packet.selected_memory_entries),
            ("memory-recent-newest",),
        )

    def test_service_uses_direct_log_message_constants(self) -> None:
        self.assertEqual(
            LogMessage.ASSEMBLY_FAILED,
            "Context assembly failed: trace_id=%s, error=%s",
        )

    def test_shared_proof_artifact_writer_emits_standard_files(self) -> None:
        packet = assemble_with_starter_context_service(
            retriever=self.retriever,
            query="authoritative packet assembly",
            settings=self.settings,
            metadata={"workflow": "codex_repository"},
        )
        rendered_context = render_packet_context(packet)

        with TemporaryDirectory() as temp_dir:
            output_dir = write_standard_proof_artifacts(
                output_dir=Path(temp_dir),
                packet=packet,
                rendered_context=rendered_context,
            )

            self.assertTrue((output_dir / "atlas_rendered_context.txt").is_file())
            self.assertTrue((output_dir / "atlas_packet.json").is_file())
            self.assertTrue((output_dir / "atlas_trace.json").is_file())

            packet_payload = json.loads(
                (output_dir / "atlas_packet.json").read_text(encoding="utf-8")
            )
            trace_payload = json.loads(
                (output_dir / "atlas_trace.json").read_text(encoding="utf-8")
            )

            self.assertEqual(packet_payload["metadata"]["workflow"], "codex_repository")
            self.assertEqual(
                trace_payload["metadata"]["request_workflow"],
                "codex_repository",
            )


if __name__ == "__main__":
    unittest.main()
