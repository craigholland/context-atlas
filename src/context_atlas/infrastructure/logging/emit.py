"""Helpers for emitting structured log events with stable templates."""

from __future__ import annotations

from enum import Enum
import logging
from typing import Any

from ...domain.events import LogEvent
from ...domain.messages import get_log_message


def log_event(
    logger: logging.Logger,
    level: int,
    event: LogEvent,
    *message_args: Any,
    **fields: Any,
) -> None:
    """Emit a log line using a stable event identifier and template."""

    extra = {"event": event.value}
    extra.update(_normalize_log_fields(fields))
    logger.log(level, get_log_message(event), *message_args, extra=extra)


def log_assembly_stage_event(
    logger: logging.Logger,
    level: int,
    event: LogEvent,
    *,
    trace_id: str,
    message_args: tuple[Any, ...] = (),
    **fields: Any,
) -> None:
    """Emit an assembly-stage event with consistent structured trace fields."""

    stage_fields = {"trace_id": trace_id}
    stage_fields.update(fields)
    log_event(
        logger,
        level,
        event,
        *message_args,
        **stage_fields,
    )


def _normalize_log_fields(fields: dict[str, Any]) -> dict[str, Any]:
    """Drop nulls and coerce enum-like values to logging-friendly primitives."""

    normalized: dict[str, Any] = {}
    for key, value in fields.items():
        if value is None:
            continue
        if isinstance(value, Enum):
            normalized[key] = value.value
            continue
        normalized[key] = value
    return normalized
