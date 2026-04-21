"""Tests for canonical memory entries and starter memory retention policies."""

from __future__ import annotations

import unittest

from context_atlas.domain.errors import ContextAtlasError, ErrorCode
from context_atlas.domain.messages import ErrorMessage, LogMessage
from context_atlas.domain.models import (
    ContextDecisionAction,
    ContextMemoryEntry,
    ContextPacket,
    ContextSource,
    ContextSourceAuthority,
    ContextSourceClass,
)
from context_atlas.domain.policies import StarterMemoryRetentionPolicy


class MemoryPolicyTests(unittest.TestCase):
    """Verify PR 6 memory artifacts and starter retention behavior."""

    def setUp(self) -> None:
        self.now = 1_000_000.0

    def test_memory_entry_rejects_negative_importance(self) -> None:
        with self.assertRaises(ContextAtlasError) as context:
            ContextMemoryEntry(
                entry_id="memory-invalid",
                source=_memory_source(
                    "memory-invalid",
                    "A retained memory entry must validate importance.",
                ),
                recorded_at_epoch_seconds=self.now - 10,
                importance=-0.1,
            )

        self.assertEqual(context.exception.code, ErrorCode.INVALID_MEMORY_ENTRY)

    def test_memory_policy_retains_recent_and_scored_long_term_entries(self) -> None:
        entries = (
            _memory_entry(
                "old-relevant",
                (
                    "Atlas packet assembly depends on durable memory selection "
                    "and retention policy."
                ),
                recorded_at=self.now - 600,
                importance=1.4,
            ),
            _memory_entry(
                "old-stale",
                "A fading note that no longer affects current Atlas behavior.",
                recorded_at=self.now - 12_000,
                importance=0.1,
            ),
            _memory_entry(
                "recent-user",
                "Recent user instruction about packet assembly.",
                recorded_at=self.now - 20,
                importance=0.9,
            ),
            _memory_entry(
                "recent-assistant",
                "Recent assistant answer about policy layering.",
                recorded_at=self.now - 5,
                importance=0.8,
            ),
        )

        outcome = StarterMemoryRetentionPolicy(
            short_term_count=2,
            decay_rate=0.0001,
            dedup_threshold=0.72,
        ).select_memory(
            entries,
            trace_id="trace-memory-1",
            now_epoch_seconds=self.now,
        )

        self.assertEqual(
            tuple(entry.entry_id for entry in outcome.selected_entries),
            ("recent-assistant", "recent-user", "old-relevant"),
        )
        self.assertEqual(outcome.trace.metadata["selected_entry_count"], "3")
        self.assertEqual(outcome.trace.metadata["rejected_entry_count"], "1")
        self.assertIn(
            "short_term_priority",
            tuple(reason.value for reason in outcome.trace.decisions[0].reason_codes),
        )

    def test_memory_policy_orders_short_term_window_newest_first(self) -> None:
        entries = (
            _memory_entry(
                "recent-older",
                "Older recent memory entry.",
                recorded_at=self.now - 30,
                importance=0.9,
            ),
            _memory_entry(
                "recent-newest",
                "Newest recent memory entry.",
                recorded_at=self.now - 5,
                importance=0.8,
            ),
            _memory_entry(
                "recent-middle",
                "Middle recent memory entry.",
                recorded_at=self.now - 15,
                importance=0.85,
            ),
        )

        outcome = StarterMemoryRetentionPolicy(short_term_count=3).select_memory(
            entries,
            trace_id="trace-memory-order-1",
            now_epoch_seconds=self.now,
        )

        self.assertEqual(
            tuple(entry.entry_id for entry in outcome.selected_entries),
            ("recent-newest", "recent-middle", "recent-older"),
        )

    def test_memory_policy_deduplicates_against_recent_memory(self) -> None:
        entries = (
            _memory_entry(
                "older-duplicate",
                "Atlas keeps short-term memory visible even during ranking.",
                recorded_at=self.now - 500,
                importance=2.0,
            ),
            _memory_entry(
                "recent-winner",
                "Atlas keeps short-term memory visible even during ranking.",
                recorded_at=self.now - 10,
                importance=0.7,
            ),
        )

        outcome = StarterMemoryRetentionPolicy(
            short_term_count=1,
            decay_rate=0.0001,
            dedup_threshold=0.72,
        ).select_memory(
            entries,
            trace_id="trace-memory-2",
            now_epoch_seconds=self.now,
        )

        self.assertEqual(
            tuple(entry.entry_id for entry in outcome.selected_entries),
            ("recent-winner",),
        )
        duplicate_decision = next(
            decision
            for decision in outcome.trace.decisions
            if decision.source_id == "older-duplicate"
        )
        self.assertEqual(duplicate_decision.action, ContextDecisionAction.EXCLUDED)
        self.assertIn(
            "duplicate",
            tuple(reason.value for reason in duplicate_decision.reason_codes),
        )
        self.assertIn("exact_key_match", duplicate_decision.explanation or "")

    def test_memory_policy_deduplicates_reordered_token_variants(self) -> None:
        entries = (
            _memory_entry(
                "older-token-overlap",
                (
                    "Atlas retains durable planning context in memory when the "
                    "policy selects long term state."
                ),
                recorded_at=self.now - 700,
                importance=2.0,
            ),
            _memory_entry(
                "recent-token-overlap",
                (
                    "Memory policy selects long term state when Atlas retains "
                    "durable planning context."
                ),
                recorded_at=self.now - 15,
                importance=0.8,
            ),
        )

        outcome = StarterMemoryRetentionPolicy(
            short_term_count=1,
            decay_rate=0.0001,
            dedup_threshold=0.72,
        ).select_memory(
            entries,
            trace_id="trace-memory-2b",
            now_epoch_seconds=self.now,
        )

        self.assertEqual(
            tuple(entry.entry_id for entry in outcome.selected_entries),
            ("recent-token-overlap",),
        )
        duplicate_decision = next(
            decision
            for decision in outcome.trace.decisions
            if decision.source_id == "older-token-overlap"
        )
        self.assertEqual(duplicate_decision.action, ContextDecisionAction.EXCLUDED)
        self.assertIn(
            "duplicate",
            tuple(reason.value for reason in duplicate_decision.reason_codes),
        )
        self.assertIn("token_overlap", duplicate_decision.explanation or "")

    def test_memory_policy_deduplicates_matching_bodies_despite_front_matter(
        self,
    ) -> None:
        entries = (
            _memory_entry(
                "older-front-matter",
                (
                    "---\n"
                    "title: Atlas Canon\n"
                    "owners: [core]\n"
                    "---\n"
                    "Atlas duplicate handling should stay traceable after "
                    "front matter normalization."
                ),
                recorded_at=self.now - 540,
                importance=1.5,
            ),
            _memory_entry(
                "recent-front-matter",
                (
                    "---\n"
                    "title: Working Notes\n"
                    "owners: [planning]\n"
                    "---\n"
                    "Atlas duplicate handling should stay traceable after "
                    "front matter normalization."
                ),
                recorded_at=self.now - 15,
                importance=0.8,
            ),
        )

        outcome = StarterMemoryRetentionPolicy(
            short_term_count=1,
            decay_rate=0.0001,
            dedup_threshold=0.72,
        ).select_memory(
            entries,
            trace_id="trace-memory-2f",
            now_epoch_seconds=self.now,
        )

        self.assertEqual(
            tuple(entry.entry_id for entry in outcome.selected_entries),
            ("recent-front-matter",),
        )
        duplicate_decision = next(
            decision
            for decision in outcome.trace.decisions
            if decision.source_id == "older-front-matter"
        )
        self.assertEqual(duplicate_decision.action, ContextDecisionAction.EXCLUDED)
        self.assertIn("exact_key_match", duplicate_decision.explanation or "")

    def test_memory_policy_keeps_metadata_only_title_variants_distinct(self) -> None:
        entries = (
            _memory_entry(
                "metadata-title-canon",
                ("---\ntitle: Atlas Canon\nowners: [core]\n---\n"),
                recorded_at=self.now - 550,
                importance=1.6,
            ),
            _memory_entry(
                "metadata-title-canon-draft",
                ("---\ntitle: Atlas Canon Draft\nowners: [core]\n---\n"),
                recorded_at=self.now - 10,
                importance=0.8,
            ),
        )

        outcome = StarterMemoryRetentionPolicy(
            short_term_count=1,
            decay_rate=0.0001,
            dedup_threshold=0.72,
        ).select_memory(
            entries,
            trace_id="trace-memory-2g",
            now_epoch_seconds=self.now,
        )

        self.assertEqual(
            tuple(entry.entry_id for entry in outcome.selected_entries),
            ("metadata-title-canon-draft", "metadata-title-canon"),
        )
        self.assertEqual(outcome.trace.metadata["deduplicated_entry_count"], "0")

    def test_memory_policy_deduplicates_unicode_token_variants(self) -> None:
        entries = (
            _memory_entry(
                "older-unicode-overlap",
                (
                    "Атлас сохраняет долговременный контекст планирования, когда "
                    "политика выбирает состояние памяти."
                ),
                recorded_at=self.now - 650,
                importance=1.9,
            ),
            _memory_entry(
                "recent-unicode-overlap",
                (
                    "Политика выбирает состояние памяти, когда Атлас сохраняет "
                    "долговременный контекст планирования."
                ),
                recorded_at=self.now - 12,
                importance=0.8,
            ),
        )

        outcome = StarterMemoryRetentionPolicy(
            short_term_count=1,
            decay_rate=0.0001,
            dedup_threshold=0.72,
        ).select_memory(
            entries,
            trace_id="trace-memory-2d",
            now_epoch_seconds=self.now,
        )

        self.assertEqual(
            tuple(entry.entry_id for entry in outcome.selected_entries),
            ("recent-unicode-overlap",),
        )
        duplicate_decision = next(
            decision
            for decision in outcome.trace.decisions
            if decision.source_id == "older-unicode-overlap"
        )
        self.assertEqual(duplicate_decision.action, ContextDecisionAction.EXCLUDED)
        self.assertIn(
            "duplicate",
            tuple(reason.value for reason in duplicate_decision.reason_codes),
        )

    def test_memory_policy_keeps_lexically_distinct_related_entries(self) -> None:
        entries = (
            _memory_entry(
                "older-related",
                ("Atlas governs packet assembly under strict traceable budget limits."),
                recorded_at=self.now - 600,
                importance=1.6,
            ),
            _memory_entry(
                "recent-related",
                "Budget-aware packet construction stays visible to users.",
                recorded_at=self.now - 20,
                importance=0.8,
            ),
        )

        outcome = StarterMemoryRetentionPolicy(
            short_term_count=1,
            decay_rate=0.0001,
            dedup_threshold=0.72,
        ).select_memory(
            entries,
            trace_id="trace-memory-2c",
            now_epoch_seconds=self.now,
        )

        self.assertEqual(
            tuple(entry.entry_id for entry in outcome.selected_entries),
            ("recent-related", "older-related"),
        )
        self.assertEqual(outcome.trace.metadata["deduplicated_entry_count"], "0")

    def test_memory_policy_keeps_shared_header_entries_with_distinct_bodies(
        self,
    ) -> None:
        shared_prefix = (
            "---\n"
            "doc_class: guide\n"
            "owners: [core]\n"
            "---\n"
            "# Context Atlas Hardening\n"
            "Audience: Internal\n"
            "Workflow: Hardening\n"
        )
        entries = (
            _memory_entry(
                "older-shared-header",
                shared_prefix
                + (
                    "\n"
                    "Duplicate normalization should strip front matter before "
                    "comparison.\n"
                    "This note focuses on repeated header handling in governed docs."
                ),
                recorded_at=self.now - 550,
                importance=1.5,
            ),
            _memory_entry(
                "recent-shared-header",
                shared_prefix
                + (
                    "\n"
                    "Token estimation should stay provider-agnostic and query aware.\n"
                    "This note focuses on tokenizer seams rather than duplicate "
                    "handling."
                ),
                recorded_at=self.now - 18,
                importance=0.8,
            ),
        )

        outcome = StarterMemoryRetentionPolicy(
            short_term_count=1,
            decay_rate=0.0001,
            dedup_threshold=0.72,
        ).select_memory(
            entries,
            trace_id="trace-memory-2e",
            now_epoch_seconds=self.now,
        )

        self.assertEqual(
            tuple(entry.entry_id for entry in outcome.selected_entries),
            ("recent-shared-header", "older-shared-header"),
        )
        self.assertEqual(outcome.trace.metadata["deduplicated_entry_count"], "0")
        excluded_decisions = [
            decision
            for decision in outcome.trace.decisions
            if decision.action is ContextDecisionAction.EXCLUDED
        ]
        self.assertEqual(excluded_decisions, [])

    def test_memory_duplicate_proof_beats_reviewed_prior_baselines(self) -> None:
        with self.subTest("front_matter_variants_beat_exact_full_text_baseline"):
            older_content = (
                "---\n"
                "title: Atlas Canon\n"
                "owners: [core]\n"
                "---\n"
                "Atlas duplicate handling should stay traceable after "
                "front matter normalization."
            )
            recent_content = (
                "---\n"
                "title: Working Notes\n"
                "owners: [planning]\n"
                "---\n"
                "Atlas duplicate handling should stay traceable after "
                "front matter normalization."
            )
            self.assertFalse(
                _legacy_exact_full_text_duplicate(older_content, recent_content)
            )
            entries = (
                _memory_entry(
                    "proof-older-front-matter",
                    older_content,
                    recorded_at=self.now - 540,
                    importance=1.5,
                ),
                _memory_entry(
                    "proof-recent-front-matter",
                    recent_content,
                    recorded_at=self.now - 15,
                    importance=0.8,
                ),
            )

            outcome = StarterMemoryRetentionPolicy(
                short_term_count=1,
                decay_rate=0.0001,
                dedup_threshold=0.72,
            ).select_memory(
                entries,
                trace_id="trace-memory-2g",
                now_epoch_seconds=self.now,
            )

            self.assertEqual(
                tuple(entry.entry_id for entry in outcome.selected_entries),
                ("proof-recent-front-matter",),
            )

        with self.subTest("shared_headers_reject_prefix_heuristic_false_positive"):
            shared_prefix = (
                "---\n"
                "doc_class: guide\n"
                "owners: [core]\n"
                "---\n"
                "# Context Atlas Hardening\n"
                "Audience: Internal maintainers\n"
                "Workflow: Hardening\n"
                "Status: Reviewed baseline\n"
                "Review Lens: Duplicate handling\n"
                "Scope: Shared policy proof\n"
            )
            older_content = shared_prefix + (
                "\n"
                "Duplicate normalization should strip front matter before "
                "comparison.\n"
                "This note focuses on repeated header handling in governed docs."
            )
            recent_content = shared_prefix + (
                "\n"
                "Token estimation should stay provider-agnostic and query aware.\n"
                "This note focuses on tokenizer seams rather than duplicate "
                "handling."
            )
            self.assertTrue(
                _legacy_prefix_heuristic_duplicate(
                    older_content,
                    recent_content,
                    threshold=0.72,
                )
            )
            entries = (
                _memory_entry(
                    "proof-older-shared-header",
                    older_content,
                    recorded_at=self.now - 550,
                    importance=1.5,
                ),
                _memory_entry(
                    "proof-recent-shared-header",
                    recent_content,
                    recorded_at=self.now - 18,
                    importance=0.8,
                ),
            )

            outcome = StarterMemoryRetentionPolicy(
                short_term_count=1,
                decay_rate=0.0001,
                dedup_threshold=0.72,
            ).select_memory(
                entries,
                trace_id="trace-memory-2h",
                now_epoch_seconds=self.now,
            )

            self.assertEqual(
                tuple(entry.entry_id for entry in outcome.selected_entries),
                ("proof-recent-shared-header", "proof-older-shared-header"),
            )
            excluded_decisions = [
                decision
                for decision in outcome.trace.decisions
                if decision.action is ContextDecisionAction.EXCLUDED
            ]
            self.assertEqual(excluded_decisions, [])

    def test_query_relevance_boost_can_rescue_a_decayed_memory_entry(self) -> None:
        entries = (
            _memory_entry(
                "query-match",
                (
                    "Atlas memory governance should remain query aware when "
                    "selecting retained planning context."
                ),
                recorded_at=self.now - 9_000,
                importance=0.15,
            ),
            _memory_entry(
                "recent-anchor",
                "A recent note about packet rendering.",
                recorded_at=self.now - 15,
                importance=0.9,
            ),
        )

        outcome = StarterMemoryRetentionPolicy(
            short_term_count=1,
            decay_rate=0.0001,
            dedup_threshold=0.72,
        ).select_memory(
            entries,
            trace_id="trace-memory-3",
            now_epoch_seconds=self.now,
            query="atlas memory governance retained planning context",
        )

        self.assertEqual(
            tuple(entry.entry_id for entry in outcome.selected_entries),
            ("recent-anchor", "query-match"),
        )
        boosted_decision = next(
            decision
            for decision in outcome.trace.decisions
            if decision.source_id == "query-match"
        )
        self.assertIn(
            "query_relevance",
            tuple(reason.value for reason in boosted_decision.reason_codes),
        )

    def test_memory_policy_validates_configuration_inputs(self) -> None:
        with self.assertRaises(ContextAtlasError) as invalid_short_term_count:
            StarterMemoryRetentionPolicy(short_term_count=0)

        self.assertEqual(
            invalid_short_term_count.exception.code,
            ErrorCode.INVALID_MEMORY_SELECTION,
        )

        with self.assertRaises(ContextAtlasError) as invalid_decay_rate:
            StarterMemoryRetentionPolicy(decay_rate=-0.1)

        self.assertEqual(
            invalid_decay_rate.exception.code,
            ErrorCode.INVALID_MEMORY_SELECTION,
        )

    def test_memory_trace_can_be_attached_to_a_canonical_packet(self) -> None:
        entries = (
            _memory_entry(
                "memory-packet",
                "Memory packet traces should stay structured and inspectable.",
                recorded_at=self.now - 30,
                importance=1.0,
            ),
        )
        outcome = StarterMemoryRetentionPolicy(short_term_count=1).select_memory(
            entries,
            trace_id="trace-memory-4",
            now_epoch_seconds=self.now,
        )

        packet = ContextPacket(
            packet_id="packet-memory-1",
            query="How does Atlas retain memory?",
            trace=outcome.trace,
            metadata={"memory_entry_count": str(outcome.selected_count)},
        )

        self.assertEqual(packet.trace.trace_id, "trace-memory-4")
        self.assertEqual(packet.metadata["memory_entry_count"], "1")
        self.assertEqual(packet.trace.decisions[0].source_id, "memory-packet")
        self.assertEqual(
            packet.trace.decisions[0].action, ContextDecisionAction.INCLUDED
        )

    def test_memory_error_and_log_templates_are_registered(self) -> None:
        self.assertEqual(
            ErrorMessage.INVALID_MEMORY_SELECTION,
            "Invalid memory selection: %s",
        )
        self.assertEqual(
            LogMessage.MEMORY_REJECTED,
            "Memory rejected: trace_id=%s, source_id=%s, reason=%s",
        )


def _memory_entry(
    entry_id: str,
    content: str,
    *,
    recorded_at: float,
    importance: float,
) -> ContextMemoryEntry:
    """Build a canonical memory entry for test scenarios."""

    return ContextMemoryEntry(
        entry_id=entry_id,
        source=_memory_source(entry_id, content),
        recorded_at_epoch_seconds=recorded_at,
        importance=importance,
    )


def _memory_source(source_id: str, content: str) -> ContextSource:
    """Build a source artifact suitable for retained memory tests."""

    return ContextSource(
        source_id=source_id,
        content=content,
        source_class=ContextSourceClass.MEMORY,
        authority=ContextSourceAuthority.ADVISORY,
    )


def _legacy_exact_full_text_duplicate(content_a: str, content_b: str) -> bool:
    """Return the old exact full-text duplicate check used before Story 2."""

    return content_a.casefold() == content_b.casefold()


def _legacy_prefix_heuristic_duplicate(
    content_a: str,
    content_b: str,
    *,
    threshold: float,
) -> bool:
    """Return the historical prefix-heavy duplicate heuristic for proof tests."""

    normalized_a = content_a.strip().lower()
    normalized_b = content_b.strip().lower()
    if not normalized_a or not normalized_b:
        return False
    if normalized_a in normalized_b or normalized_b in normalized_a:
        return True

    half = len(normalized_a) // 2
    if len(normalized_a) > 10 and len(normalized_b) >= half and half > 0:
        if normalized_a[:half] == normalized_b[:half]:
            return True

    tokens_a = set(normalized_a.split())
    tokens_b = set(normalized_b.split())
    union_size = len(tokens_a | tokens_b)
    if union_size == 0:
        return False
    return (len(tokens_a & tokens_b) / union_size) >= threshold


if __name__ == "__main__":
    unittest.main()
