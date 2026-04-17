"""Stable error identifiers for Context Atlas."""

from enum import StrEnum


class ErrorCode(StrEnum):
    """Stable machine-facing identifiers for Context Atlas errors."""

    UNKNOWN = "unknown"
    DOCUMENT_NO_CONTENT = "document_no_content"
    INVALID_CONFIGURATION = "invalid_configuration"
    MISSING_REQUIRED_SETTING = "missing_required_setting"
    EMPTY_SOURCE_IDENTIFIER = "empty_source_identifier"
    EMPTY_SOURCE_CONTENT = "empty_source_content"
    INVALID_CANDIDATE_STATE = "invalid_candidate_state"
    INVALID_BUDGET_TOTAL = "invalid_budget_total"
    INVALID_BUDGET_SLOT = "invalid_budget_slot"
    DUPLICATE_BUDGET_SLOT_NAME = "duplicate_budget_slot_name"
    INVALID_ASSEMBLY_DECISION = "invalid_assembly_decision"
    INVALID_TRACE_IDENTIFIER = "invalid_trace_identifier"
    INVALID_PACKET_IDENTIFIER = "invalid_packet_identifier"
    EMPTY_PACKET_QUERY = "empty_packet_query"
    DUPLICATE_SOURCE_IDENTIFIER = "duplicate_source_identifier"
    INVALID_RETRIEVAL_REQUEST = "invalid_retrieval_request"
