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
            ("recent-user", "recent-assistant", "old-relevant"),
        )
        self.assertEqual(outcome.trace.metadata["selected_entry_count"], "3")
        self.assertEqual(outcome.trace.metadata["rejected_entry_count"], "1")
        self.assertIn(
            "short_term_priority",
            tuple(reason.value for reason in outcome.trace.decisions[0].reason_codes),
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


if __name__ == "__main__":
    unittest.main()
