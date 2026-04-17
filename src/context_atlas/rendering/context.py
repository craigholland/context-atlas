"""Derived text renderers for canonical packet artifacts."""

from __future__ import annotations

from ..domain.models import ContextPacket


def render_packet_context(packet: ContextPacket) -> str:
    """Render a packet's current context view without mutating canonical state."""

    if packet.compression_result is not None:
        return packet.compression_result.text
    return "\n\n".join(
        candidate.source.content for candidate in packet.selected_candidates
    )
