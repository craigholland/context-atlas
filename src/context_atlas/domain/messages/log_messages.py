"""Centralized log messages for Context Atlas."""

from __future__ import annotations


class _NamedLogMessage(str):
    """String message constant that also carries a stable event name."""

    __slots__ = ("name", "event_name")

    name: str
    event_name: str

    def __new__(cls, name: str, text: str) -> "_NamedLogMessage":
        instance = str.__new__(cls, text)
        instance.name = name
        instance.event_name = name.lower()
        return instance


class LogMessage:
    """Stable human-facing log messages keyed directly by class variable name."""

    LOGGER_CONFIGURED = _NamedLogMessage(
        "LOGGER_CONFIGURED",
        "Logger configured: name=%s, level=%s",
    )
    SETTINGS_LOADED = _NamedLogMessage(
        "SETTINGS_LOADED",
        "Settings loaded: logger_name=%s, log_level=%s, default_total_budget=%d, "
        "default_memory_budget_fraction=%.4f, default_retrieval_top_k=%d, "
        "default_compression_strategy=%s, ranking_minimum_score=%.4f, "
        "compression_chars_per_token=%d, compression_min_chunk_chars=%d, "
        "memory_short_term_count=%d, memory_decay_rate=%.4f, "
        "memory_dedup_threshold=%.2f, memory_min_effective_score=%.4f, "
        "memory_query_boost_weight=%.4f",
    )
    COMPONENT_INITIALIZED = _NamedLogMessage(
        "COMPONENT_INITIALIZED",
        "Component initialized: name=%s",
    )
    CANDIDATES_GATHERED = _NamedLogMessage(
        "CANDIDATES_GATHERED",
        "Candidates gathered: trace_id=%s, candidate_count=%d",
    )
    CANDIDATES_RANKED = _NamedLogMessage(
        "CANDIDATES_RANKED",
        "Candidates ranked: trace_id=%s, candidate_count=%d",
    )
    BUDGET_ALLOCATED = _NamedLogMessage(
        "BUDGET_ALLOCATED",
        "Budget allocated: trace_id=%s, total_tokens=%d, remaining_tokens=%d",
    )
    COMPRESSION_APPLIED = _NamedLogMessage(
        "COMPRESSION_APPLIED",
        "Compression applied: trace_id=%s, strategy=%s, original_chars=%d, "
        "compressed_chars=%d",
    )
    MEMORY_SELECTED = _NamedLogMessage(
        "MEMORY_SELECTED",
        "Memory selected: trace_id=%s, memory_entries=%d",
    )
    MEMORY_REJECTED = _NamedLogMessage(
        "MEMORY_REJECTED",
        "Memory rejected: trace_id=%s, source_id=%s, reason=%s",
    )
    SOURCE_REGISTERED = _NamedLogMessage(
        "SOURCE_REGISTERED",
        "Source registered: source_id=%s, total_sources=%d",
    )
    RETRIEVAL_COMPLETED = _NamedLogMessage(
        "RETRIEVAL_COMPLETED",
        "Retrieval completed: mode=%s, query=%s, candidate_count=%d",
    )
    CANDIDATES_DEDUPED = _NamedLogMessage(
        "CANDIDATES_DEDUPED",
        "Candidates deduped: trace_id=%s, removed_candidates=%d",
    )
    DECISIONS_RECORDED = _NamedLogMessage(
        "DECISIONS_RECORDED",
        "Decisions recorded: trace_id=%s, decision_count=%d",
    )
    ASSEMBLY_STARTED = _NamedLogMessage(
        "ASSEMBLY_STARTED",
        "Context assembly started: trace_id=%s, query=%s",
    )
    ASSEMBLY_COMPLETED = _NamedLogMessage(
        "ASSEMBLY_COMPLETED",
        "Context assembly completed: trace_id=%s, selected_candidates=%d",
    )
    ASSEMBLY_FAILED = _NamedLogMessage(
        "ASSEMBLY_FAILED",
        "Context assembly failed: trace_id=%s, error=%s",
    )
    PACKET_CREATED = _NamedLogMessage(
        "PACKET_CREATED",
        "Context packet created: packet_id=%s, selected_candidates=%d",
    )
    SOURCE_CLASSIFIED = _NamedLogMessage(
        "SOURCE_CLASSIFIED",
        "Source classified: source_id=%s, source_class=%s",
    )
    PACKET_ASSEMBLED = _NamedLogMessage(
        "PACKET_ASSEMBLED",
        "Context packet assembled: packet_id=%s, item_count=%d",
    )


__all__ = ["LogMessage"]
