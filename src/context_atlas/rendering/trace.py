"""Trace inspection renderers for canonical Context Atlas traces."""

from __future__ import annotations

from ..domain.models import ContextAssemblyDecision, ContextTrace


def render_trace_inspection(trace: ContextTrace) -> str:
    """Render a human-readable inspection view of a canonical trace."""

    sections = [
        _render_trace_summary(trace),
        _render_decision_group(
            "Included Decisions",
            trace.included_decisions,
        ),
        _render_decision_group(
            "Excluded Decisions",
            trace.excluded_decisions,
        ),
        _render_decision_group(
            "Transformed Decisions",
            trace.transformed_decisions,
        ),
        _render_decision_group(
            "Deferred Decisions",
            trace.deferred_decisions,
        ),
        _render_trace_metadata(trace),
    ]
    return "\n\n".join(section for section in sections if section)


def _render_trace_summary(trace: ContextTrace) -> str:
    lines = [
        "Trace",
        f"- trace_id: {trace.trace_id}",
        f"- decision_count: {trace.decision_count}",
        f"- included_count: {len(trace.included_decisions)}",
        f"- excluded_count: {len(trace.excluded_decisions)}",
        f"- transformed_count: {len(trace.transformed_decisions)}",
        f"- deferred_count: {len(trace.deferred_decisions)}",
    ]
    return "\n".join(lines)


def _render_decision_group(
    title: str,
    decisions: tuple[ContextAssemblyDecision, ...],
) -> str:
    lines = [title]
    if not decisions:
        lines.append("- none")
        return "\n".join(lines)

    for decision in decisions:
        lines.append(_render_decision(decision))
    return "\n".join(lines)


def _render_decision(decision: ContextAssemblyDecision) -> str:
    reason_codes = ",".join(reason.value for reason in decision.reason_codes)
    parts = [
        f"- [{_position_text(decision)}] {decision.source_id}",
        f"action={decision.action.value}",
        f"reasons={reason_codes}",
    ]
    if decision.candidate_score is not None:
        parts.append(f"score={decision.candidate_score:.4f}")
    if decision.explanation:
        parts.append(f"why={decision.explanation}")
    return "; ".join(parts)


def _render_trace_metadata(trace: ContextTrace) -> str:
    lines = ["Trace Metadata"]
    if not trace.metadata:
        lines.append("- none")
        return "\n".join(lines)

    for key, value in sorted(trace.metadata.items()):
        lines.append(f"- {key}: {value}")
    return "\n".join(lines)


def _position_text(decision: ContextAssemblyDecision) -> str:
    if decision.position is None:
        return "n/a"
    return str(decision.position)


__all__ = ["render_trace_inspection"]
