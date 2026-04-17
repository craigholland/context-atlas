"""Derived text renderers for canonical packet artifacts."""

from __future__ import annotations

from ..domain.models import ContextPacket


def render_packet_context(packet: ContextPacket) -> str:
    """Render a packet's current context view without mutating canonical state."""

    sections: list[str] = []

    memory_text = "\n\n".join(
        entry.source.content for entry in packet.selected_memory_entries
    ).strip()
    if memory_text:
        sections.append(memory_text)

    if packet.compression_result is not None:
        candidate_text = packet.compression_result.text.strip()
    else:
        candidate_text = "\n\n".join(
            candidate.source.content for candidate in packet.selected_candidates
        ).strip()

    if candidate_text:
        sections.append(candidate_text)

    return "\n\n".join(sections)
