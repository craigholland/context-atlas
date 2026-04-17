"""Tests for budget-allocation and compression policy slices."""

from __future__ import annotations

import unittest

from context_atlas.domain.errors import ContextAtlasError, ErrorCode
from context_atlas.domain.events import LogEvent
from context_atlas.domain.messages import get_log_message
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
                ContextBudgetSlot("system", token_limit=200),
                ContextBudgetSlot("history", token_limit=250),
                ContextBudgetSlot(
                    "memory",
                    token_limit=400,
                    mode=ContextBudgetSlotMode.ELASTIC,
                    priority=5,
                ),
                ContextBudgetSlot(
                    "docs",
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
                BudgetRequest("system", 180),
                BudgetRequest("history", 240),
                BudgetRequest("memory", 400),
                BudgetRequest("docs", 600),
            ),
        )

        self.assertEqual(outcome.total_allocated_tokens, 1000)
        self.assertEqual(outcome.remaining_tokens, 0)
        allocation_by_slot = {
            allocation.slot_name: allocation for allocation in outcome.allocations
        }
        self.assertEqual(allocation_by_slot["system"].allocated_tokens, 180)
        self.assertEqual(allocation_by_slot["memory"].allocated_tokens, 400)
        self.assertEqual(allocation_by_slot["docs"].allocated_tokens, 180)
        self.assertTrue(allocation_by_slot["docs"].was_reduced)
        self.assertEqual(outcome.trace.metadata["remaining_tokens"], "0")
        self.assertIn(
            BudgetPressureReasonCode.ELASTIC_SLOT_REDUCED,
            outcome.trace.decisions[-1].reason_codes,
        )

    def test_budget_allocation_rejects_unknown_slot_requests(self) -> None:
        budget = ContextBudget(
            total_tokens=128, slots=(ContextBudgetSlot("docs", 128),)
        )

        with self.assertRaises(ContextAtlasError) as context:
            StarterBudgetAllocationPolicy().allocate_budget(
                budget,
                trace_id="trace-budget-2",
                requests=(BudgetRequest("unknown", 64),),
            )

        self.assertEqual(context.exception.code, ErrorCode.INVALID_BUDGET_ALLOCATION)

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

    def test_budget_and_compression_templates_are_registered(self) -> None:
        self.assertEqual(
            get_log_message(LogEvent.BUDGET_ALLOCATED),
            "Budget allocated: trace_id=%s, total_tokens=%d, remaining_tokens=%d",
        )
        self.assertEqual(
            get_log_message(LogEvent.COMPRESSION_APPLIED),
            "Compression applied: trace_id=%s, strategy=%s, original_chars=%d, compressed_chars=%d",
        )


if __name__ == "__main__":
    unittest.main()
