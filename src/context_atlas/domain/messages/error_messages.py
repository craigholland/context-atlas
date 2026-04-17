"""Centralized human-facing error messages for Context Atlas."""

from __future__ import annotations


class ErrorMessage:
    """Stable human-facing error messages keyed by `ErrorCode.name`."""

    UNKNOWN = "Unknown Context Atlas error."
    DOCUMENT_NO_CONTENT = "Document '%s' has empty content."
    INVALID_CONFIGURATION = "Invalid configuration: %s"
    MISSING_REQUIRED_SETTING = "Required setting '%s' is missing."
    EMPTY_SOURCE_IDENTIFIER = "Context source identifier must not be empty."
    EMPTY_SOURCE_CONTENT = "Context source '%s' has empty content."
    INVALID_CANDIDATE_STATE = "Invalid context candidate state: %s"
    INVALID_BUDGET_TOTAL = "Invalid context budget total: %s"
    INVALID_BUDGET_SLOT = "Invalid context budget slot '%s': %s"
    DUPLICATE_BUDGET_SLOT_NAME = "Context budget slot '%s' is defined more than once."
    INVALID_ASSEMBLY_DECISION = "Invalid context assembly decision: %s"
    INVALID_TRACE_IDENTIFIER = "Context trace identifier must not be empty."
    INVALID_PACKET_IDENTIFIER = "Context packet identifier must not be empty."
    EMPTY_PACKET_QUERY = "Context packet query must not be empty."
    DUPLICATE_SOURCE_IDENTIFIER = "Context source '%s' is already registered."
    INVALID_ASSEMBLY_REQUEST = "Invalid assembly request: %s"
    INVALID_RETRIEVAL_REQUEST = "Invalid retrieval request: %s"
    INVALID_RANKING_REQUEST = "Invalid ranking request: %s"
    INVALID_BUDGET_ALLOCATION = "Invalid budget allocation: %s"
    INVALID_COMPRESSION_REQUEST = "Invalid compression request: %s"
    INVALID_MEMORY_ENTRY = "Invalid memory entry: %s"
    INVALID_MEMORY_SELECTION = "Invalid memory selection: %s"
    INVALID_SOURCE_ADAPTER_INPUT = "Invalid source adapter input: %s"
    UNSUPPORTED_DOCUMENT_CLASS = "Unsupported document class: %s"


__all__ = ["ErrorMessage"]
