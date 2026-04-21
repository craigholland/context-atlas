"""Tests for budget-allocation and compression policy slices."""

from __future__ import annotations

import unittest

from context_atlas.domain.errors import ContextAtlasError, ErrorCode
from context_atlas.domain.messages import LogMessage
from context_atlas.domain.models import (
    BudgetPressureReasonCode,
    CompressionStrategy,
    ContextBudget,
    ContextBudgetSlot,
    ContextBudgetSlotMode,
    ContextPacket,
    ContextSource,
    ContextSourceAuthority,
    ContextSourceClass,
)
from context_atlas.domain.policies import (
    BudgetRequest,
    StarterBudgetAllocationPolicy,
    StarterCompressionPolicy,
)
from context_atlas.rendering import render_packet_context
from context_atlas.adapters import (
    InMemorySourceRegistry,
    LexicalRetrievalMode,
    LexicalRetriever,
)


class BudgetAndCompressionTests(unittest.TestCase):
    """Verify the PR 5 budget and compression policy slice."""

    def setUp(self) -> None:
        self.registry = InMemorySourceRegistry(
            (
                ContextSource(
                    source_id="charter",
                    content=(
                        "Context Atlas governs what enters model context. "
                        "Authoritative architecture and packet policy must remain explicit."
                    ),
                    source_class=ContextSourceClass.AUTHORITATIVE,
                    authority=ContextSourceAuthority.BINDING,
                ),
                ContextSource(
                    source_id="planning",
                    content=(
                        "Planning notes discuss compression strategy selection, "
                        "budgeting, and downstream packet rendering."
                    ),
                    source_class=ContextSourceClass.PLANNING,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
                ContextSource(
                    source_id="review",
                    content=(
                        "Reviews call out budget pressure, truncation risks, and the "
                        "need for query-aware extractive compression."
                    ),
                    source_class=ContextSourceClass.REVIEWS,
                    authority=ContextSourceAuthority.ADVISORY,
                ),
            )
        )

    def test_budget_allocation_respects_fixed_and_elastic_slots(self) -> None:
        budget = ContextBudget(
            total_tokens=1000,
            slots=(
                ContextBudgetSlot(slot_name="system", token_limit=200),
                ContextBudgetSlot(slot_name="history", token_limit=250),
                ContextBudgetSlot(
                    slot_name="memory",
                    token_limit=400,
                    mode=ContextBudgetSlotMode.ELASTIC,
                    priority=5,
                ),
                ContextBudgetSlot(
                    slot_name="docs",
                    token_limit=600,
                    mode=ContextBudgetSlotMode.ELASTIC,
                    priority=10,
                ),
            ),
        )

        outcome = StarterBudgetAllocationPolicy().allocate_budget(
            budget,
            trace_id="trace-budget-1",
            requests=(
                BudgetRequest(slot_name="system", requested_tokens=180),
                BudgetRequest(slot_name="history", requested_tokens=240),
                BudgetRequest(slot_name="memory", requested_tokens=400),
                BudgetRequest(slot_name="docs", requested_tokens=600),
            ),
        )

        self.assertEqual(outcome.total_allocated_tokens, 1000)
        self.assertEqual(outcome.unallocated_tokens, 0)
        self.assertEqual(outcome.remaining_tokens, 0)
        allocation_by_slot = {
            allocation.slot_name: allocation for allocation in outcome.allocations
        }
        self.assertEqual(allocation_by_slot["system"].allocated_tokens, 180)
        self.assertEqual(allocation_by_slot["memory"].allocated_tokens, 400)
        self.assertEqual(allocation_by_slot["docs"].allocated_tokens, 180)
        self.assertTrue(allocation_by_slot["docs"].was_reduced)
        self.assertEqual(outcome.trace.metadata["fixed_reserved_tokens"], "450")
        self.assertEqual(outcome.trace.metadata["unreserved_tokens"], "550")
        self.assertEqual(outcome.trace.metadata["unallocated_tokens"], "0")
        self.assertEqual(outcome.trace.metadata["remaining_tokens"], "0")
        self.assertIn(
            BudgetPressureReasonCode.ELASTIC_SLOT_REDUCED,
            outcome.trace.decisions[-1].reason_codes,
        )
        self.assertEqual(
            outcome.model_dump()["allocations"][0]["slot_name"],
            "system",
        )

    def test_budget_allocation_rejects_unknown_slot_requests(self) -> None:
        budget = ContextBudget(
            total_tokens=128,
            slots=(ContextBudgetSlot(slot_name="docs", token_limit=128),),
        )

        with self.assertRaises(ContextAtlasError) as context:
            StarterBudgetAllocationPolicy().allocate_budget(
                budget,
                trace_id="trace-budget-2",
                requests=(BudgetRequest(slot_name="unknown", requested_tokens=64),),
            )

        self.assertEqual(context.exception.code, ErrorCode.INVALID_BUDGET_ALLOCATION)

    def test_budget_request_validates_name_and_requested_tokens(self) -> None:
        with self.assertRaises(ContextAtlasError) as blank_name:
            BudgetRequest(slot_name="   ", requested_tokens=1)

        self.assertEqual(blank_name.exception.code, ErrorCode.INVALID_BUDGET_ALLOCATION)

        with self.assertRaises(ContextAtlasError) as negative_request:
            BudgetRequest(slot_name="docs", requested_tokens=-1)

        self.assertEqual(
            negative_request.exception.code,
            ErrorCode.INVALID_BUDGET_ALLOCATION,
        )

    def test_compression_policy_returns_structured_result(self) -> None:
        candidates = LexicalRetriever(
            self.registry,
            mode=LexicalRetrievalMode.TFIDF,
        ).retrieve("context architecture compression strategy", top_k=3)

        outcome = StarterCompressionPolicy(
            strategy=CompressionStrategy.SENTENCE
        ).compress_candidates(
            candidates,
            trace_id="trace-compression-1",
            max_tokens=18,
            query="architecture compression strategy",
        )

        self.assertTrue(outcome.compression_result.was_applied)
        self.assertGreater(
            outcome.compression_result.original_chars,
            outcome.compression_result.compressed_chars,
        )
        self.assertEqual(
            outcome.compression_result.strategy_used,
            CompressionStrategy.SENTENCE,
        )
        self.assertGreaterEqual(outcome.compression_result.estimated_tokens_saved, 1)
        self.assertEqual(
            outcome.trace.metadata["compression_strategy"],
            CompressionStrategy.SENTENCE.value,
        )

    def test_extractive_compression_falls_back_to_truncate_when_needed(self) -> None:
        candidates = LexicalRetriever(
            self.registry,
            mode=LexicalRetrievalMode.KEYWORD,
        ).retrieve("context compression", top_k=3)

        outcome = StarterCompressionPolicy(
            strategy=CompressionStrategy.EXTRACTIVE
        ).compress_candidates(
            candidates,
            trace_id="trace-compression-2",
            max_tokens=1,
            query="context compression",
        )

        self.assertTrue(outcome.compression_result.was_applied)
        self.assertEqual(
            outcome.compression_result.metadata["fallback_strategy"],
            CompressionStrategy.TRUNCATE.value,
        )
        self.assertIn(
            BudgetPressureReasonCode.ELASTIC_SLOT_REDUCED,
            outcome.trace.decisions[-1].reason_codes,
        )

    def test_compression_policy_validates_configuration_inputs(self) -> None:
        with self.assertRaises(ContextAtlasError) as invalid_chars:
            StarterCompressionPolicy(chars_per_token=0)

        self.assertEqual(
            invalid_chars.exception.code,
            ErrorCode.INVALID_COMPRESSION_REQUEST,
        )

        with self.assertRaises(ContextAtlasError) as invalid_chunk_size:
            StarterCompressionPolicy(min_chunk_chars=0)

        self.assertEqual(
            invalid_chunk_size.exception.code,
            ErrorCode.INVALID_COMPRESSION_REQUEST,
        )

    def test_compression_keeps_short_candidates_when_they_fit_budget(self) -> None:
        short_registry = InMemorySourceRegistry(
            (
                ContextSource(
                    source_id="short-note",
                    content="Atlas rules.",
                    source_class=ContextSourceClass.AUTHORITATIVE,
                    authority=ContextSourceAuthority.BINDING,
                ),
            )
        )
        candidates = LexicalRetriever(
            short_registry,
            mode=LexicalRetrievalMode.KEYWORD,
        ).retrieve("atlas rules", top_k=1)

        outcome = StarterCompressionPolicy(min_chunk_chars=20).compress_candidates(
            candidates,
            trace_id="trace-compression-short-1",
            max_tokens=8,
            query="atlas rules",
        )

        self.assertFalse(outcome.compression_result.was_applied)
        self.assertEqual(outcome.compression_result.text, "Atlas rules.")
        self.assertEqual(outcome.compression_result.metadata["outcome"], "fits_budget")
        self.assertEqual(outcome.compression_result.source_ids, ("short-note",))

    def test_compression_truncates_short_candidates_instead_of_dropping_them(
        self,
    ) -> None:
        short_registry = InMemorySourceRegistry(
            (
                ContextSource(
                    source_id="short-a",
                    content="Atlas keeps short docs visible.",
                    source_class=ContextSourceClass.AUTHORITATIVE,
                    authority=ContextSourceAuthority.BINDING,
                ),
                ContextSource(
                    source_id="short-b",
                    content="Short snippets should not disappear.",
                    source_class=ContextSourceClass.PLANNING,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
            )
        )
        candidates = LexicalRetriever(
            short_registry,
            mode=LexicalRetrievalMode.KEYWORD,
        ).retrieve("short docs atlas snippets", top_k=2)

        outcome = StarterCompressionPolicy(
            strategy=CompressionStrategy.EXTRACTIVE,
            min_chunk_chars=100,
        ).compress_candidates(
            candidates,
            trace_id="trace-compression-short-2",
            max_tokens=4,
            query="short docs atlas snippets",
        )

        self.assertTrue(outcome.compression_result.text)
        self.assertEqual(
            outcome.compression_result.metadata["compression_scope"],
            "all_candidates_below_min_chunk_chars",
        )
        self.assertEqual(
            outcome.compression_result.metadata["fallback_strategy"],
            CompressionStrategy.TRUNCATE.value,
        )
        self.assertNotEqual(
            outcome.compression_result.metadata["outcome"], "empty_input"
        )

    def test_packet_retains_structured_compression_metadata_when_rendered(self) -> None:
        candidates = LexicalRetriever(
            self.registry,
            mode=LexicalRetrievalMode.KEYWORD,
        ).retrieve("context compression rendering", top_k=2)
        compression_outcome = StarterCompressionPolicy().compress_candidates(
            candidates,
            trace_id="trace-compression-3",
            max_tokens=12,
            query="context compression rendering",
        )
        packet = ContextPacket(
            packet_id="packet-budget-1",
            query="How should Atlas compress context?",
            selected_candidates=candidates,
            compression_result=compression_outcome.compression_result,
            metadata={
                "compression_strategy": compression_outcome.compression_result.strategy_used.value
            },
        )

        rendered = render_packet_context(packet)

        self.assertEqual(rendered, packet.compression_result.text)
        self.assertEqual(
            packet.compression_result.source_ids[0], candidates[0].source.source_id
        )
        self.assertEqual(
            packet.metadata["compression_strategy"],
            CompressionStrategy.EXTRACTIVE.value,
        )

    def test_render_packet_context_uses_selected_candidates_when_compression_was_not_applied(
        self,
    ) -> None:
        candidates = LexicalRetriever(
            self.registry,
            mode=LexicalRetrievalMode.KEYWORD,
        ).retrieve("context architecture", top_k=1)
        packet = ContextPacket(
            packet_id="packet-budget-2",
            query="How should Atlas render non-applied compression?",
            selected_candidates=candidates,
            compression_result={
                "text": "Artifact text should not replace canonical candidate content.",
                "strategy_used": CompressionStrategy.EXTRACTIVE,
                "original_chars": 56,
                "compressed_chars": 56,
                "estimated_tokens_saved": 0,
                "was_applied": False,
                "source_ids": (candidates[0].source.source_id,),
            },
        )

        rendered = render_packet_context(packet)

        self.assertEqual(rendered, candidates[0].source.content)

    def test_budget_and_compression_templates_are_registered(self) -> None:
        self.assertEqual(
            LogMessage.BUDGET_ALLOCATED,
            "Budget allocated: trace_id=%s, total_tokens=%d, remaining_tokens=%d",
        )
        self.assertEqual(
            LogMessage.COMPRESSION_APPLIED,
            "Compression applied: trace_id=%s, strategy=%s, original_chars=%d, compressed_chars=%d",
        )


if __name__ == "__main__":
    unittest.main()
