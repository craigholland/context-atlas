"""Derived text renderers for canonical packet artifacts.

This module derives a starter context string from canonical packet state.
It should remain a thin formatting layer rather than a second orchestration
boundary or an alternate source of canonical packet truth.
"""

from __future__ import annotations

from ..domain.models import ContextPacket


def render_packet_context(packet: ContextPacket) -> str:
    """Render a packet's current context view without mutating canonical state."""

    sections: list[str] = []

    memory_text = _render_memory_text(packet)
    if memory_text:
        sections.append(memory_text)

    candidate_text = _render_candidate_text(packet)
    if candidate_text:
        sections.append(candidate_text)

    return "\n\n".join(sections)


def _render_memory_text(packet: ContextPacket) -> str:
    """Render retained memory content directly from canonical packet state."""

    return "\n\n".join(
        entry.source.content for entry in packet.selected_memory_entries
    ).strip()


def _render_candidate_text(packet: ContextPacket) -> str:
    """Render candidate-facing content from packet state or its transform artifact."""

    if packet.compression_was_applied:
        compression_result = packet.compression_result
        assert compression_result is not None
        return compression_result.text.strip()

    return "\n\n".join(
        candidate.source.content for candidate in packet.selected_candidates
    ).strip()
