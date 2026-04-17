"""Human-facing log message templates keyed by stable event identifiers."""

from types import MappingProxyType
from typing import Mapping

from ..events import LogEvent


class LogMessageTemplate:
    """Centralized log message templates for reusable operational events."""

    LOGGER_CONFIGURED = "Logger configured: name=%s, level=%s"
    SETTINGS_LOADED = (
        "Settings loaded: logger_name=%s, log_level=%s, default_total_budget=%d, "
        "default_retrieval_top_k=%d, default_compression_strategy=%s"
    )
    COMPONENT_INITIALIZED = "Component initialized: name=%s"
    CANDIDATES_GATHERED = "Candidates gathered: trace_id=%s, candidate_count=%d"
    CANDIDATES_RANKED = "Candidates ranked: trace_id=%s, candidate_count=%d"
    BUDGET_ALLOCATED = (
        "Budget allocated: trace_id=%s, total_tokens=%d, remaining_tokens=%d"
    )
    COMPRESSION_APPLIED = (
        "Compression applied: trace_id=%s, strategy=%s, original_chars=%d, "
        "compressed_chars=%d"
    )
    MEMORY_SELECTED = "Memory selected: trace_id=%s, memory_entries=%d"
    SOURCE_REGISTERED = "Source registered: source_id=%s, total_sources=%d"
    RETRIEVAL_COMPLETED = "Retrieval completed: mode=%s, query=%s, candidate_count=%d"
    ASSEMBLY_STARTED = "Context assembly started: trace_id=%s, query=%s"
    ASSEMBLY_COMPLETED = (
        "Context assembly completed: trace_id=%s, selected_candidates=%d"
    )
    PACKET_CREATED = "Context packet created: packet_id=%s, selected_candidates=%d"
    SOURCE_CLASSIFIED = "Source classified: source_id=%s, source_class=%s"
    PACKET_ASSEMBLED = "Context packet assembled: packet_id=%s, item_count=%d"


_LOG_MESSAGES: Mapping[LogEvent, str] = MappingProxyType(
    {
        LogEvent.LOGGER_CONFIGURED: LogMessageTemplate.LOGGER_CONFIGURED,
        LogEvent.SETTINGS_LOADED: LogMessageTemplate.SETTINGS_LOADED,
        LogEvent.COMPONENT_INITIALIZED: LogMessageTemplate.COMPONENT_INITIALIZED,
        LogEvent.CANDIDATES_GATHERED: LogMessageTemplate.CANDIDATES_GATHERED,
        LogEvent.CANDIDATES_RANKED: LogMessageTemplate.CANDIDATES_RANKED,
        LogEvent.BUDGET_ALLOCATED: LogMessageTemplate.BUDGET_ALLOCATED,
        LogEvent.COMPRESSION_APPLIED: LogMessageTemplate.COMPRESSION_APPLIED,
        LogEvent.MEMORY_SELECTED: LogMessageTemplate.MEMORY_SELECTED,
        LogEvent.SOURCE_REGISTERED: LogMessageTemplate.SOURCE_REGISTERED,
        LogEvent.RETRIEVAL_COMPLETED: LogMessageTemplate.RETRIEVAL_COMPLETED,
        LogEvent.ASSEMBLY_STARTED: LogMessageTemplate.ASSEMBLY_STARTED,
        LogEvent.ASSEMBLY_COMPLETED: LogMessageTemplate.ASSEMBLY_COMPLETED,
        LogEvent.PACKET_CREATED: LogMessageTemplate.PACKET_CREATED,
        LogEvent.SOURCE_CLASSIFIED: LogMessageTemplate.SOURCE_CLASSIFIED,
        LogEvent.PACKET_ASSEMBLED: LogMessageTemplate.PACKET_ASSEMBLED,
    }
)


def get_log_message(event: LogEvent) -> str:
    """Return the registered message template for a stable log event."""

    return _LOG_MESSAGES[event]
