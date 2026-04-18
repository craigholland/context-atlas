"""Logger configuration utilities for Context Atlas runtime infrastructure."""

from __future__ import annotations

import logging

from ...domain.messages import LogMessage
from .emit import log_message
from ..config.settings import LoggingSettings

DEFAULT_STRUCTURED_LOG_FORMAT = (
    "%(asctime)s %(levelname)s %(name)s [%(event)s] %(message)s"
)
DEFAULT_PLAIN_LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s %(message)s"


class _EventFieldFilter(logging.Filter):
    """Ensure every record exposes an event field for the formatter."""

    def filter(self, record: logging.LogRecord) -> bool:
        if not hasattr(record, "event"):
            record.event = "log"
        return True


def configure_logger(settings: LoggingSettings | None = None) -> logging.Logger:
    """Configure and return the package logger."""

    active_settings = settings or LoggingSettings()
    logger = logging.getLogger(active_settings.logger_name)
    logger.setLevel(_coerce_log_level(active_settings.level))
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.addFilter(_EventFieldFilter())
        handler.setFormatter(
            logging.Formatter(
                DEFAULT_STRUCTURED_LOG_FORMAT
                if active_settings.structured_events
                else DEFAULT_PLAIN_LOG_FORMAT
            )
        )
        logger.addHandler(handler)

    log_message(
        logger,
        logging.INFO,
        LogMessage.LOGGER_CONFIGURED,
        logger.name,
        logging.getLevelName(logger.level),
    )
    return logger


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a configured package logger or a named child logger."""

    base_logger = logging.getLogger(LoggingSettings().logger_name)
    return base_logger if name is None else base_logger.getChild(name)


def _coerce_log_level(level_name: str) -> int:
    """Translate user-facing level strings into stdlib logging levels."""

    level = getattr(logging, level_name.upper(), None)
    if not isinstance(level, int):
        return logging.INFO
    return level
