"""Starter reason-code enums for structured context assembly decisions."""

from enum import StrEnum


class InclusionReasonCode(StrEnum):
    """Explain why a source or candidate was included."""

    DIRECT_MATCH = "direct_match"
    AUTHORITY_PRIORITY = "authority_priority"
    BUDGET_AVAILABLE = "budget_available"
    MEMORY_RETAINED = "memory_retained"
    SHORT_TERM_PRIORITY = "short_term_priority"
    QUERY_RELEVANCE = "query_relevance"


class ExclusionReasonCode(StrEnum):
    """Explain why a source or candidate was excluded."""

    BELOW_THRESHOLD = "below_threshold"
    DUPLICATE = "duplicate"
    OUT_OF_BUDGET = "out_of_budget"
    LOWER_AUTHORITY = "lower_authority"
    EMPTY_CONTENT = "empty_content"
    STALE_MEMORY = "stale_memory"


class BudgetPressureReasonCode(StrEnum):
    """Explain budget pressure or allocation changes."""

    SLOT_EXHAUSTED = "slot_exhausted"
    TOTAL_BUDGET_EXHAUSTED = "total_budget_exhausted"
    COMPRESSION_REQUIRED = "compression_required"
    ELASTIC_SLOT_REDUCED = "elastic_slot_reduced"


class AuthorityPrecedenceReasonCode(StrEnum):
    """Explain authority-driven ordering or demotion behavior."""

    HIGHER_AUTHORITY_PREFERRED = "higher_authority_preferred"
    LOWER_AUTHORITY_DEMOTED = "lower_authority_demoted"
    NON_BINDING_SOURCE_CANNOT_OVERRIDE = "non_binding_source_cannot_override"
    HISTORICAL_SOURCE_DEFERRED = "historical_source_deferred"


__all__ = [
    "AuthorityPrecedenceReasonCode",
    "BudgetPressureReasonCode",
    "ExclusionReasonCode",
    "InclusionReasonCode",
]
