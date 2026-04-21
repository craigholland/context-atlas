"""Domain-model tests for canonical Context Atlas assembly artifacts."""

from __future__ import annotations

import unittest
import warnings

from pydantic import ValidationError

from context_atlas.domain.errors import ContextAtlasError, ErrorCode
from context_atlas.domain.messages import ErrorMessage, LogMessage
from context_atlas.domain.models import (
    AuthorityPrecedenceReasonCode,
    CompressionResult,
    CompressionStrategy,
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
    ContextSourceFamily,
    ContextSourceProvenance,
    ContextSourceSemanticsProfile,
    ContextTrace,
    ExclusionReasonCode,
    InclusionReasonCode,
    get_default_source_semantics,
    resolve_source_semantics,
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

    def test_context_source_provenance_carries_source_family(self) -> None:
        source = ContextSource(
            source_id="record-1",
            content="Row-backed source content.",
            provenance=ContextSourceProvenance(
                source_family=ContextSourceFamily.STRUCTURED_RECORD,
                source_uri="records://products/1",
                collector="structured_record_source_adapter",
            ),
        )

        self.assertEqual(
            source.provenance.source_family,
            ContextSourceFamily.STRUCTURED_RECORD,
        )
        self.assertEqual(
            source.provenance.collector, "structured_record_source_adapter"
        )

    def test_context_source_from_semantics_keeps_semantics_domain_owned(self) -> None:
        semantics = resolve_source_semantics(
            source_class=ContextSourceClass.REVIEWS,
            intended_uses=("triage",),
        )
        source = ContextSource.from_semantics(
            source_id="review-1",
            content="Review evidence from a structured record.",
            semantics=semantics,
            provenance=ContextSourceProvenance(
                source_family=ContextSourceFamily.STRUCTURED_RECORD,
                collector="structured_record_source_adapter",
            ),
            metadata={"table": "reviews"},
        )

        self.assertEqual(source.source_class, ContextSourceClass.REVIEWS)
        self.assertEqual(source.authority, ContextSourceAuthority.ADVISORY)
        self.assertEqual(source.durability, ContextSourceDurability.WORKING)
        self.assertEqual(source.intended_uses, ("review", "evidence", "triage"))
        self.assertEqual(source.metadata["table"], "reviews")

    def test_context_source_exposes_semantics_and_origin_helpers(self) -> None:
        source = ContextSource(
            source_id="record-2",
            content="Source content",
            source_class=ContextSourceClass.PLANNING,
            authority=ContextSourceAuthority.PREFERRED,
            durability=ContextSourceDurability.WORKING,
            intended_uses=("planning", "execution"),
            provenance=ContextSourceProvenance(
                source_family=ContextSourceFamily.STRUCTURED_RECORD,
                collector="structured_record_source_adapter",
            ),
        )

        self.assertEqual(source.collector_name, "structured_record_source_adapter")
        self.assertEqual(source.source_family, ContextSourceFamily.STRUCTURED_RECORD)
        self.assertEqual(source.source_family_name, "structured_record")
        self.assertEqual(
            source.semantics,
            ContextSourceSemanticsProfile(
                source_class=ContextSourceClass.PLANNING,
                authority=ContextSourceAuthority.PREFERRED,
                durability=ContextSourceDurability.WORKING,
                intended_uses=("planning", "execution"),
            ),
        )

    def test_default_source_semantics_are_defined_for_supported_classes(self) -> None:
        authoritative_defaults = get_default_source_semantics(
            ContextSourceClass.AUTHORITATIVE
        )
        code_defaults = get_default_source_semantics(ContextSourceClass.CODE)
        memory_defaults = get_default_source_semantics(ContextSourceClass.MEMORY)

        self.assertEqual(
            authoritative_defaults,
            ContextSourceSemanticsProfile(
                source_class=ContextSourceClass.AUTHORITATIVE,
                authority=ContextSourceAuthority.BINDING,
                durability=ContextSourceDurability.DURABLE,
                intended_uses=("implementation", "review", "planning"),
            ),
        )
        self.assertEqual(code_defaults.authority, ContextSourceAuthority.PREFERRED)
        self.assertEqual(code_defaults.intended_uses, ("implementation", "debugging"))
        self.assertEqual(memory_defaults.durability, ContextSourceDurability.SESSION)
        self.assertEqual(memory_defaults.intended_uses, ("continuity", "follow_up"))

    def test_resolve_source_semantics_merges_defaults_and_overrides(self) -> None:
        resolved = resolve_source_semantics(
            source_class=ContextSourceClass.REVIEWS,
            authority=ContextSourceAuthority.PREFERRED,
            intended_uses=("review", "triage", "triage"),
        )

        self.assertEqual(resolved.source_class, ContextSourceClass.REVIEWS)
        self.assertEqual(resolved.authority, ContextSourceAuthority.PREFERRED)
        self.assertEqual(resolved.durability, ContextSourceDurability.WORKING)
        self.assertEqual(resolved.intended_uses, ("review", "evidence", "triage"))

    def test_context_candidate_rejects_invalid_rank(self) -> None:
        source = ContextSource(source_id="source-1", content="useful content")

        with self.assertRaises(ContextAtlasError) as context:
            ContextCandidate(source=source, rank=0)

        self.assertEqual(context.exception.code, ErrorCode.INVALID_CANDIDATE_STATE)

    def test_context_budget_validates_fixed_slot_reservations_and_duplicates(
        self,
    ) -> None:
        fixed_history = ContextBudgetSlot(slot_name="history", token_limit=200)
        fixed_docs = ContextBudgetSlot(slot_name="docs", token_limit=400)

        budget = ContextBudget(total_tokens=800, slots=(fixed_history, fixed_docs))
        self.assertEqual(budget.fixed_reserved_tokens, 600)
        self.assertEqual(budget.unreserved_tokens, 200)
        with warnings.catch_warnings(record=True) as captured:
            warnings.simplefilter("always", DeprecationWarning)
            self.assertEqual(budget.reserved_tokens, 600)
            self.assertEqual(budget.remaining_tokens, 200)
        self.assertEqual(len(captured), 2)
        self.assertTrue(
            any("fixed_reserved_tokens" in str(warning.message) for warning in captured)
        )
        self.assertTrue(
            any("unreserved_tokens" in str(warning.message) for warning in captured)
        )

        with self.assertRaises(ContextAtlasError) as duplicate_context:
            ContextBudget(
                total_tokens=800,
                slots=(
                    fixed_history,
                    ContextBudgetSlot(slot_name="history", token_limit=100),
                ),
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
                ContextBudgetSlot(slot_name="system", token_limit=120),
                ContextBudgetSlot(
                    slot_name="docs",
                    token_limit=300,
                    mode=ContextBudgetSlotMode.ELASTIC,
                ),
            ),
        )

        self.assertEqual(budget.fixed_reserved_tokens, 120)
        self.assertEqual(budget.unreserved_tokens, 180)
        with warnings.catch_warnings(record=True) as captured:
            warnings.simplefilter("always", DeprecationWarning)
            self.assertEqual(budget.reserved_tokens, 120)
            self.assertEqual(budget.remaining_tokens, 180)
        self.assertEqual(len(captured), 2)

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

    def test_context_packet_distinguishes_compression_presence_from_application(
        self,
    ) -> None:
        packet = ContextPacket(
            packet_id="packet-compression-state",
            query="How should packet compression semantics behave?",
            compression_result=CompressionResult(
                text="Unchanged source text.",
                strategy_used=CompressionStrategy.EXTRACTIVE,
                original_chars=21,
                compressed_chars=21,
                estimated_tokens_saved=0,
                was_applied=False,
            ),
        )

        self.assertTrue(packet.has_compression)
        self.assertFalse(packet.compression_was_applied)

    def test_canonical_models_support_pydantic_validation_and_dump(self) -> None:
        source = ContextSource.model_validate(
            {
                "source_id": "  source-validated  ",
                "content": "  validated content  ",
                "source_class": ContextSourceClass.AUTHORITATIVE,
                "metadata": {"scope": "validated"},
                "provenance": {
                    "source_uri": "  docs/Authoritative/Identity/Context-Atlas-Charter.md  ",
                },
            }
        )

        self.assertEqual(source.source_id, "source-validated")
        self.assertEqual(source.content, "validated content")
        self.assertEqual(
            source.provenance.source_uri,
            "docs/Authoritative/Identity/Context-Atlas-Charter.md",
        )
        self.assertEqual(source.model_dump()["metadata"]["scope"], "validated")

    def test_canonical_models_are_frozen(self) -> None:
        source = ContextSource(source_id="source-1", content="locked")

        with self.assertRaises(ValidationError):
            source.source_id = "changed"

        with self.assertRaises(TypeError):
            source.metadata["scope"] = "identity"

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
