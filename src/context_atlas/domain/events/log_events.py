"""Stable event identifiers for operational logging and tracing."""

from enum import StrEnum


class LogEvent(StrEnum):
    """Stable machine-facing identifiers for meaningful log events."""

    LOGGER_CONFIGURED = "logger_configured"
    SETTINGS_LOADED = "settings_loaded"
    COMPONENT_INITIALIZED = "component_initialized"
    CANDIDATES_GATHERED = "candidates_gathered"
    CANDIDATES_RANKED = "candidates_ranked"
    BUDGET_ALLOCATED = "budget_allocated"
    COMPRESSION_APPLIED = "compression_applied"
    MEMORY_SELECTED = "memory_selected"
    MEMORY_REJECTED = "memory_rejected"
    SOURCE_REGISTERED = "source_registered"
    RETRIEVAL_COMPLETED = "retrieval_completed"
    CANDIDATES_DEDUPED = "candidates_deduped"
    DECISIONS_RECORDED = "decisions_recorded"
    ASSEMBLY_STARTED = "assembly_started"
    ASSEMBLY_COMPLETED = "assembly_completed"
    PACKET_CREATED = "packet_created"
    SOURCE_CLASSIFIED = "source_classified"
    PACKET_ASSEMBLED = "packet_assembled"
