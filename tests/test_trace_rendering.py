"""Tests for trace inspection rendering surfaces."""

from __future__ import annotations

import unittest

from context_atlas.domain.models import (
    ContextAssemblyDecision,
    ContextDecisionAction,
    ContextTrace,
    ExclusionReasonCode,
    InclusionReasonCode,
)
from context_atlas.infrastructure.assembly import build_starter_context_assembly_service
from context_atlas.infrastructure.config import ContextAtlasSettings, LoggingSettings
from context_atlas.adapters import InMemorySourceRegistry, LexicalRetriever
from context_atlas.domain.models import (
    ContextSource,
    ContextSourceAuthority,
    ContextSourceClass,
)
from context_atlas.rendering import render_trace_inspection


class TraceRenderingTests(unittest.TestCase):
    """Verify the first-class trace inspection surface."""

    def test_trace_inspection_groups_decisions_and_metadata(self) -> None:
        trace = ContextTrace(
            trace_id="trace-render-1",
            decisions=(
                ContextAssemblyDecision(
                    source_id="charter",
                    action=ContextDecisionAction.INCLUDED,
                    reason_codes=(InclusionReasonCode.DIRECT_MATCH,),
                    explanation="Authoritative charter ranked highest.",
                    position=1,
                ),
                ContextAssemblyDecision(
                    source_id="planning",
                    action=ContextDecisionAction.EXCLUDED,
                    reason_codes=(ExclusionReasonCode.OUT_OF_BUDGET,),
                    explanation="Planning note did not fit the active budget.",
                    position=2,
                ),
            ),
            metadata={
                "service": "context_assembly_service",
                "budget_total_tokens": "128",
            },
        )

        rendered = render_trace_inspection(trace)

        self.assertIn("Trace", rendered)
        self.assertIn("- trace_id: trace-render-1", rendered)
        self.assertIn("Included Decisions", rendered)
        self.assertIn("[1] charter; action=included", rendered)
        self.assertIn("Excluded Decisions", rendered)
        self.assertIn("[2] planning; action=excluded", rendered)
        self.assertIn("Trace Metadata", rendered)
        self.assertIn("- budget_total_tokens: 128", rendered)

    def test_service_trace_decisions_receive_sequential_positions(self) -> None:
        source = ContextSource(
            source_id="charter",
            title="Charter",
            content="Authoritative packet traces should remain inspectable.",
            source_class=ContextSourceClass.AUTHORITATIVE,
            authority=ContextSourceAuthority.BINDING,
        )
        service = build_starter_context_assembly_service(
            retriever=LexicalRetriever(InMemorySourceRegistry((source,))),
            settings=ContextAtlasSettings(
                logging=LoggingSettings(logger_name="context_atlas.tests.trace")
            ),
        )

        packet = service.assemble(query="inspectable packet traces")

        positions = tuple(
            decision.position
            for decision in packet.trace.decisions
            if decision.position
        )

        self.assertTrue(positions)
        self.assertEqual(positions, tuple(range(1, len(positions) + 1)))


if __name__ == "__main__":
    unittest.main()
