"""Human-facing log message templates keyed by stable event identifiers."""

from types import MappingProxyType
from typing import Mapping

from ..events import LogEvent


class LogMessageTemplate:
    """Centralized log message templates for reusable operational events."""

    LOGGER_CONFIGURED = "Logger configured: name=%s, level=%s"
    SETTINGS_LOADED = "Settings loaded: logger_name=%s, log_level=%s"
    COMPONENT_INITIALIZED = "Component initialized: name=%s"
    SOURCE_CLASSIFIED = "Source classified: source_id=%s, source_class=%s"
    PACKET_ASSEMBLED = "Context packet assembled: packet_id=%s, item_count=%d"


_LOG_MESSAGES: Mapping[LogEvent, str] = MappingProxyType(
    {
        LogEvent.LOGGER_CONFIGURED: LogMessageTemplate.LOGGER_CONFIGURED,
        LogEvent.SETTINGS_LOADED: LogMessageTemplate.SETTINGS_LOADED,
        LogEvent.COMPONENT_INITIALIZED: LogMessageTemplate.COMPONENT_INITIALIZED,
        LogEvent.SOURCE_CLASSIFIED: LogMessageTemplate.SOURCE_CLASSIFIED,
        LogEvent.PACKET_ASSEMBLED: LogMessageTemplate.PACKET_ASSEMBLED,
    }
)


def get_log_message(event: LogEvent) -> str:
    """Return the registered message template for a stable log event."""

    return _LOG_MESSAGES[event]
