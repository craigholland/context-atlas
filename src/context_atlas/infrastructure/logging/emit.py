"""Helpers for emitting structured log messages with stable names."""

from __future__ import annotations

from enum import Enum
import logging
from typing import Any

from ...domain.messages import LogMessage


def log_message(
    logger: logging.Logger,
    level: int,
    message: str,
    *message_args: Any,
    **fields: Any,
) -> None:
    """Emit a log line using a direct `LogMessage` constant."""

    extra = {
        "event": getattr(message, "event_name", "log"),
    }
    extra.update(_normalize_log_fields(fields))
    logger.log(level, message, *message_args, extra=extra)


def log_assembly_stage_message(
    logger: logging.Logger,
    level: int,
    message: str,
    *,
    trace_id: str,
    message_args: tuple[Any, ...] = (),
    **fields: Any,
) -> None:
    """Emit an assembly-stage log message with consistent trace fields."""

    stage_fields = {"trace_id": trace_id}
    stage_fields.update(fields)
    log_message(
        logger,
        level,
        message,
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


__all__ = ["LogMessage", "log_assembly_stage_message", "log_message"]
