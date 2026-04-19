"""Packet inspection renderers for canonical Context Atlas packets."""

from __future__ import annotations

from ..domain.models import ContextPacket


def render_packet_inspection(packet: ContextPacket) -> str:
    """Render a human-readable inspection view of a canonical packet."""

    sections = [
        _render_packet_summary(packet),
        _render_budget_section(packet),
        _render_sources_section(packet),
        _render_memory_section(packet),
        _render_compression_section(packet),
    ]
    return "\n\n".join(section for section in sections if section)


def _render_packet_summary(packet: ContextPacket) -> str:
    compression_applied = (
        False
        if packet.compression_result is None
        else packet.compression_result.was_applied
    )
    lines = [
        "Packet",
        f"- packet_id: {packet.packet_id}",
        f"- query: {packet.query}",
        f"- selected_candidates: {packet.selected_candidate_count}",
        f"- selected_memory_entries: {packet.selected_memory_count}",
        f"- total_items: {packet.item_count}",
        f"- compression_applied: {_yes_no(compression_applied)}",
        f"- trace_attached: {_yes_no(packet.has_trace)}",
    ]
    return "\n".join(lines)


def _render_budget_section(packet: ContextPacket) -> str:
    if packet.budget is None:
        return "Budget\n- none"

    lines = [
        "Budget",
        f"- total_tokens: {packet.budget.total_tokens}",
        f"- reserved_tokens: {packet.budget.reserved_tokens}",
        f"- remaining_tokens: {packet.budget.remaining_tokens}",
    ]
    if packet.budget.slots:
        lines.append("- slots:")
        for slot in packet.budget.slots:
            lines.append(
                f"  - {slot.slot_name}: limit={slot.token_limit}, mode={slot.mode.value}, priority={slot.priority}"
            )
    else:
        lines.append("- slots: none")
    return "\n".join(lines)


def _render_sources_section(packet: ContextPacket) -> str:
    lines = ["Selected Sources"]
    if not packet.selected_candidates:
        lines.append("- none")
        return "\n".join(lines)

    for candidate in packet.selected_candidates:
        title = candidate.source.title or "(untitled)"
        score = "n/a" if candidate.score is None else f"{candidate.score:.4f}"
        rank = "n/a" if candidate.rank is None else str(candidate.rank)
        lines.append(
            f"- {candidate.source.source_id}: title={title}; class={candidate.source.source_class.value}; authority={candidate.source.authority.value}; rank={rank}; score={score}"
        )
    return "\n".join(lines)


def _render_memory_section(packet: ContextPacket) -> str:
    lines = ["Retained Memory"]
    if not packet.selected_memory_entries:
        lines.append("- none")
        return "\n".join(lines)

    for entry in packet.selected_memory_entries:
        lines.append(
            f"- {entry.entry_id}: source_id={entry.source.source_id}; importance={entry.importance:.3f}; recorded_at={entry.recorded_at_epoch_seconds}"
        )
    return "\n".join(lines)


def _render_compression_section(packet: ContextPacket) -> str:
    lines = ["Compression"]
    if packet.compression_result is None:
        lines.append("- none")
        return "\n".join(lines)

    result = packet.compression_result
    lines.extend(
        [
            f"- strategy: {result.strategy_used.value}",
            f"- was_applied: {_yes_no(result.was_applied)}",
            f"- original_chars: {result.original_chars}",
            f"- compressed_chars: {result.compressed_chars}",
            f"- compression_ratio: {result.compression_ratio}",
            f"- estimated_tokens_saved: {result.estimated_tokens_saved}",
        ]
    )
    if result.source_ids:
        lines.append(f"- source_ids: {', '.join(result.source_ids)}")
    else:
        lines.append("- source_ids: none")
    return "\n".join(lines)


def _yes_no(value: bool) -> str:
    return "yes" if value else "no"


__all__ = ["render_packet_inspection"]
