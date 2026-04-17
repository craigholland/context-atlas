"""Stable event identifiers for operational logging and tracing."""

from enum import StrEnum


class LogEvent(StrEnum):
    """Stable machine-facing identifiers for meaningful log events."""

    LOGGER_CONFIGURED = "logger_configured"
    SETTINGS_LOADED = "settings_loaded"
    COMPONENT_INITIALIZED = "component_initialized"
    SOURCE_CLASSIFIED = "source_classified"
    PACKET_ASSEMBLED = "packet_assembled"
