"""Stable event identifiers for operational logging and tracing."""

from enum import StrEnum


class LogEvent(StrEnum):
    """Stable machine-facing identifiers for meaningful log events."""

    LOGGER_CONFIGURED = "logger_configured"
    SETTINGS_LOADED = "settings_loaded"
    COMPONENT_INITIALIZED = "component_initialized"
    ASSEMBLY_STARTED = "assembly_started"
    ASSEMBLY_COMPLETED = "assembly_completed"
    PACKET_CREATED = "packet_created"
    SOURCE_CLASSIFIED = "source_classified"
    PACKET_ASSEMBLED = "packet_assembled"
