"""Helpers for emitting structured log events with stable templates."""

from __future__ import annotations

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
    extra.update(fields)
    logger.log(level, get_log_message(event), *message_args, extra=extra)
