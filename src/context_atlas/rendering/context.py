"""Derived text renderers for canonical packet artifacts.

This module derives a starter context string from canonical packet state.
It should remain a thin formatting layer rather than a second orchestration
boundary or an alternate source of canonical packet truth.
"""

from __future__ import annotations

from ..domain.models import ContextPacket


def render_packet_context(
    packet: ContextPacket,
    *,
    include_section_headers: bool = False,
) -> str:
    """Render a packet's current context view without mutating canonical state."""

    sections: list[str] = []

    memory_text = _render_memory_text(
        packet,
        include_section_headers=include_section_headers,
    )
    if memory_text:
        sections.append(memory_text)

    candidate_text = _render_candidate_text(
        packet,
        include_section_headers=include_section_headers,
    )
    if candidate_text:
        sections.append(candidate_text)

    return "\n\n".join(sections)


def _render_memory_text(
    packet: ContextPacket,
    *,
    include_section_headers: bool,
) -> str:
    """Render retained memory content directly from canonical packet state."""

    rendered = "\n\n".join(
        entry.source.content for entry in packet.selected_memory_entries
    ).strip()
    if not rendered:
        return ""
    return _with_header(
        rendered,
        header="Retained Memory",
        include_section_headers=include_section_headers,
    )


def _render_candidate_text(
    packet: ContextPacket,
    *,
    include_section_headers: bool,
) -> str:
    """Render candidate-facing content from packet state or its transform artifact."""

    if packet.compression_was_applied:
        compression_result = packet.compression_result
        assert compression_result is not None
        rendered = compression_result.text.strip()
        return _with_header(
            rendered,
            header="Repository Context",
            include_section_headers=include_section_headers,
        )

    rendered = "\n\n".join(
        candidate.source.content for candidate in packet.selected_candidates
    ).strip()
    return _with_header(
        rendered,
        header="Repository Context",
        include_section_headers=include_section_headers,
    )


def _with_header(
    rendered: str,
    *,
    header: str,
    include_section_headers: bool,
) -> str:
    """Optionally prefix a rendered section with a simple human-facing header."""

    if not rendered:
        return ""
    if not include_section_headers:
        return rendered
    return f"[{header}]\n{rendered}"
