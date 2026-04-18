"""Tests for packet inspection rendering surfaces."""

from __future__ import annotations

import unittest

from context_atlas.domain.models import (
    CompressionResult,
    CompressionStrategy,
    ContextBudget,
    ContextBudgetSlot,
    ContextBudgetSlotMode,
    ContextPacket,
    ContextSource,
    ContextSourceAuthority,
    ContextSourceClass,
    ContextTrace,
)
from context_atlas.domain.models.memory import ContextMemoryEntry
from context_atlas.domain.models.sources import ContextCandidate
from context_atlas.rendering import render_packet_inspection


class PacketRenderingTests(unittest.TestCase):
    """Verify the first-class packet inspection surface."""

    def test_packet_inspection_highlights_packet_budget_and_compression_state(
        self,
    ) -> None:
        packet = ContextPacket(
            packet_id="packet-inspect-1",
            query="How should Atlas inspect a packet?",
            selected_candidates=(
                ContextCandidate(
                    source=ContextSource(
                        source_id="charter",
                        title="Charter",
                        content="Context Atlas should remain inspectable.",
                        source_class=ContextSourceClass.AUTHORITATIVE,
                        authority=ContextSourceAuthority.BINDING,
                    ),
                    score=0.91,
                    rank=1,
                ),
            ),
            selected_memory_entries=(
                ContextMemoryEntry(
                    entry_id="memory-1",
                    source=ContextSource(
                        source_id="session-note",
                        title="Session Note",
                        content="Recent inspection work was user-driven.",
                        source_class=ContextSourceClass.MEMORY,
                        authority=ContextSourceAuthority.PREFERRED,
                    ),
                    recorded_at_epoch_seconds=123.0,
                    importance=1.25,
                ),
            ),
            budget=ContextBudget(
                total_tokens=1200,
                slots=(
                    ContextBudgetSlot(
                        slot_name="memory",
                        token_limit=300,
                        mode=ContextBudgetSlotMode.FIXED,
                        priority=0,
                    ),
                    ContextBudgetSlot(
                        slot_name="documents",
                        token_limit=1200,
                        mode=ContextBudgetSlotMode.ELASTIC,
                        priority=10,
                    ),
                ),
            ),
            compression_result=CompressionResult(
                text="Compressed packet view.",
                strategy_used=CompressionStrategy.EXTRACTIVE,
                original_chars=500,
                compressed_chars=180,
                estimated_tokens_saved=80,
                source_ids=("charter",),
            ),
            trace=ContextTrace(trace_id="trace-inspect-1"),
        )

        rendered = render_packet_inspection(packet)

        self.assertIn("Packet", rendered)
        self.assertIn("- packet_id: packet-inspect-1", rendered)
        self.assertIn("- total_tokens: 1200", rendered)
        self.assertIn("Selected Sources", rendered)
        self.assertIn("charter: title=Charter", rendered)
        self.assertIn("Retained Memory", rendered)
        self.assertIn("memory-1: source_id=session-note", rendered)
        self.assertIn("Compression", rendered)
        self.assertIn("- strategy: extractive", rendered)
        self.assertIn("- compression_applied: yes", rendered)

    def test_packet_inspection_is_read_only_over_canonical_packet_state(self) -> None:
        packet = ContextPacket(
            packet_id="packet-inspect-2",
            query="How should Atlas render packet inspection?",
            selected_candidates=(),
            selected_memory_entries=(),
            trace=ContextTrace(trace_id="trace-inspect-2"),
        )
        before = packet.model_dump()

        rendered = render_packet_inspection(packet)
        after = packet.model_dump()

        self.assertEqual(before, after)
        self.assertIn("Selected Sources\n- none", rendered)
        self.assertIn("Retained Memory\n- none", rendered)
        self.assertIn("Compression\n- none", rendered)


if __name__ == "__main__":
    unittest.main()
