"""Domain-model tests for canonical Context Atlas assembly artifacts."""

from __future__ import annotations

import unittest

from context_atlas.domain.errors import ContextAtlasError, ErrorCode
from context_atlas.domain.messages import ErrorMessage, LogMessage
from context_atlas.domain.models import (
    AuthorityPrecedenceReasonCode,
    ContextAssemblyDecision,
    ContextBudget,
    ContextBudgetSlot,
    ContextBudgetSlotMode,
    ContextCandidate,
    ContextDecisionAction,
    ContextPacket,
    ContextSource,
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceDurability,
    ContextSourceProvenance,
    ContextTrace,
    ExclusionReasonCode,
    InclusionReasonCode,
)


class DomainModelTests(unittest.TestCase):
    """Verify the first canonical domain artifacts for Context Atlas."""

    def test_context_source_requires_identifier_and_content(self) -> None:
        with self.assertRaises(ContextAtlasError) as identifier_error:
            ContextSource(source_id="   ", content="valid content")

        self.assertEqual(
            identifier_error.exception.code, ErrorCode.EMPTY_SOURCE_IDENTIFIER
        )

        with self.assertRaises(ContextAtlasError) as content_error:
            ContextSource(source_id="source-1", content="   ")

        self.assertEqual(content_error.exception.code, ErrorCode.EMPTY_SOURCE_CONTENT)
        self.assertEqual(
            str(content_error.exception),
            "Context source 'source-1' has empty content.",
        )

    def test_context_source_normalizes_structured_fields(self) -> None:
        source = ContextSource(
            source_id="  source-1  ",
            title="  Atlas Charter  ",
            content="  Durable project truth.  ",
            source_class=ContextSourceClass.AUTHORITATIVE,
            authority=ContextSourceAuthority.BINDING,
            durability=ContextSourceDurability.DURABLE,
            provenance=ContextSourceProvenance(
                source_uri="docs/Authoritative/Identity"
            ),
            tags=("charter", "architecture"),
            intended_uses=("implementation", "review"),
            metadata={"scope": "identity"},
        )

        self.assertEqual(source.source_id, "source-1")
        self.assertEqual(source.title, "Atlas Charter")
        self.assertEqual(source.content, "Durable project truth.")
        self.assertEqual(source.tags, ("charter", "architecture"))
        self.assertEqual(source.metadata["scope"], "identity")

    def test_context_candidate_rejects_invalid_rank(self) -> None:
        source = ContextSource(source_id="source-1", content="useful content")

        with self.assertRaises(ContextAtlasError) as context:
            ContextCandidate(source=source, rank=0)

        self.assertEqual(context.exception.code, ErrorCode.INVALID_CANDIDATE_STATE)

    def test_context_budget_validates_fixed_slot_reservations_and_duplicates(
        self,
    ) -> None:
        fixed_history = ContextBudgetSlot("history", token_limit=200)
        fixed_docs = ContextBudgetSlot("docs", token_limit=400)

        budget = ContextBudget(total_tokens=800, slots=(fixed_history, fixed_docs))
        self.assertEqual(budget.reserved_tokens, 600)
        self.assertEqual(budget.remaining_tokens, 200)

        with self.assertRaises(ContextAtlasError) as duplicate_context:
            ContextBudget(
                total_tokens=800,
                slots=(fixed_history, ContextBudgetSlot("history", token_limit=100)),
            )

        self.assertEqual(
            duplicate_context.exception.code,
            ErrorCode.DUPLICATE_BUDGET_SLOT_NAME,
        )

        with self.assertRaises(ContextAtlasError) as over_reserved_context:
            ContextBudget(
                total_tokens=300,
                slots=(fixed_history, fixed_docs),
            )

        self.assertEqual(
            over_reserved_context.exception.code,
            ErrorCode.INVALID_BUDGET_TOTAL,
        )

    def test_context_budget_allows_elastic_slots_beyond_fixed_reservations(
        self,
    ) -> None:
        budget = ContextBudget(
            total_tokens=300,
            slots=(
                ContextBudgetSlot("system", token_limit=120),
                ContextBudgetSlot(
                    "docs",
                    token_limit=300,
                    mode=ContextBudgetSlotMode.ELASTIC,
                ),
            ),
        )

        self.assertEqual(budget.reserved_tokens, 120)
        self.assertEqual(budget.remaining_tokens, 180)

    def test_context_assembly_decision_requires_reason_codes(self) -> None:
        with self.assertRaises(ContextAtlasError) as context:
            ContextAssemblyDecision(
                source_id="source-1",
                action=ContextDecisionAction.INCLUDED,
                reason_codes=(),
            )

        self.assertEqual(context.exception.code, ErrorCode.INVALID_ASSEMBLY_DECISION)

    def test_context_packet_keeps_structured_candidates_and_trace(self) -> None:
        source = ContextSource(
            source_id="source-1",
            title="Atlas Charter",
            content="Context Atlas governs what enters model context.",
            source_class=ContextSourceClass.AUTHORITATIVE,
            authority=ContextSourceAuthority.BINDING,
        )
        candidate = ContextCandidate(
            source=source,
            score=0.98,
            rank=1,
            signals=("lexical_match", "authority_priority"),
        )
        trace = ContextTrace(
            trace_id="trace-1",
            decisions=(
                ContextAssemblyDecision(
                    source_id=source.source_id,
                    action=ContextDecisionAction.INCLUDED,
                    reason_codes=(
                        InclusionReasonCode.DIRECT_MATCH,
                        AuthorityPrecedenceReasonCode.HIGHER_AUTHORITY_PREFERRED,
                    ),
                    candidate_score=0.98,
                    position=1,
                ),
                ContextAssemblyDecision(
                    source_id="source-2",
                    action=ContextDecisionAction.EXCLUDED,
                    reason_codes=(ExclusionReasonCode.OUT_OF_BUDGET,),
                    explanation="Lower-ranked planning note fell outside the fixed docs slot.",
                ),
            ),
        )
        packet = ContextPacket(
            packet_id="packet-1",
            query="What should enter model context?",
            selected_candidates=(candidate,),
            budget=ContextBudget(total_tokens=512),
            trace=trace,
        )

        self.assertEqual(packet.item_count, 1)
        self.assertEqual(packet.selected_candidates[0].source.source_id, "source-1")
        self.assertEqual(
            packet.trace.decisions[0].action, ContextDecisionAction.INCLUDED
        )
        self.assertEqual(
            packet.trace.decisions[0].reason_codes[0],
            InclusionReasonCode.DIRECT_MATCH,
        )

    def test_new_domain_events_and_templates_are_registered(self) -> None:
        self.assertEqual(
            LogMessage.ASSEMBLY_STARTED,
            "Context assembly started: trace_id=%s, query=%s",
        )
        self.assertEqual(
            LogMessage.PACKET_CREATED,
            "Context packet created: packet_id=%s, selected_candidates=%d",
        )
        self.assertEqual(
            ErrorMessage.EMPTY_PACKET_QUERY,
            "Context packet query must not be empty.",
        )


if __name__ == "__main__":
    unittest.main()
