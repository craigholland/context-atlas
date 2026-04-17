"""Human-facing error message templates keyed by stable error codes."""

from __future__ import annotations

from types import MappingProxyType
from typing import Mapping

from ..errors.codes import ErrorCode


class ErrorMessageTemplate:
    """Centralized error message templates for reusable domain errors."""

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
    INVALID_RETRIEVAL_REQUEST = "Invalid retrieval request: %s"
    INVALID_RANKING_REQUEST = "Invalid ranking request: %s"
    INVALID_BUDGET_ALLOCATION = "Invalid budget allocation: %s"
    INVALID_COMPRESSION_REQUEST = "Invalid compression request: %s"
    INVALID_MEMORY_ENTRY = "Invalid memory entry: %s"
    INVALID_MEMORY_SELECTION = "Invalid memory selection: %s"


_ERROR_MESSAGES: Mapping[ErrorCode, str] = MappingProxyType(
    {
        ErrorCode.UNKNOWN: ErrorMessageTemplate.UNKNOWN,
        ErrorCode.DOCUMENT_NO_CONTENT: ErrorMessageTemplate.DOCUMENT_NO_CONTENT,
        ErrorCode.INVALID_CONFIGURATION: ErrorMessageTemplate.INVALID_CONFIGURATION,
        ErrorCode.MISSING_REQUIRED_SETTING: ErrorMessageTemplate.MISSING_REQUIRED_SETTING,
        ErrorCode.EMPTY_SOURCE_IDENTIFIER: ErrorMessageTemplate.EMPTY_SOURCE_IDENTIFIER,
        ErrorCode.EMPTY_SOURCE_CONTENT: ErrorMessageTemplate.EMPTY_SOURCE_CONTENT,
        ErrorCode.INVALID_CANDIDATE_STATE: ErrorMessageTemplate.INVALID_CANDIDATE_STATE,
        ErrorCode.INVALID_BUDGET_TOTAL: ErrorMessageTemplate.INVALID_BUDGET_TOTAL,
        ErrorCode.INVALID_BUDGET_SLOT: ErrorMessageTemplate.INVALID_BUDGET_SLOT,
        ErrorCode.DUPLICATE_BUDGET_SLOT_NAME: ErrorMessageTemplate.DUPLICATE_BUDGET_SLOT_NAME,
        ErrorCode.INVALID_ASSEMBLY_DECISION: ErrorMessageTemplate.INVALID_ASSEMBLY_DECISION,
        ErrorCode.INVALID_TRACE_IDENTIFIER: ErrorMessageTemplate.INVALID_TRACE_IDENTIFIER,
        ErrorCode.INVALID_PACKET_IDENTIFIER: ErrorMessageTemplate.INVALID_PACKET_IDENTIFIER,
        ErrorCode.EMPTY_PACKET_QUERY: ErrorMessageTemplate.EMPTY_PACKET_QUERY,
        ErrorCode.DUPLICATE_SOURCE_IDENTIFIER: ErrorMessageTemplate.DUPLICATE_SOURCE_IDENTIFIER,
        ErrorCode.INVALID_RETRIEVAL_REQUEST: ErrorMessageTemplate.INVALID_RETRIEVAL_REQUEST,
        ErrorCode.INVALID_RANKING_REQUEST: ErrorMessageTemplate.INVALID_RANKING_REQUEST,
        ErrorCode.INVALID_BUDGET_ALLOCATION: ErrorMessageTemplate.INVALID_BUDGET_ALLOCATION,
        ErrorCode.INVALID_COMPRESSION_REQUEST: ErrorMessageTemplate.INVALID_COMPRESSION_REQUEST,
        ErrorCode.INVALID_MEMORY_ENTRY: ErrorMessageTemplate.INVALID_MEMORY_ENTRY,
        ErrorCode.INVALID_MEMORY_SELECTION: ErrorMessageTemplate.INVALID_MEMORY_SELECTION,
    }
)


def get_error_message(code: ErrorCode) -> str:
    """Return the registered template for a stable error code."""

    return _ERROR_MESSAGES.get(code, ErrorMessageTemplate.UNKNOWN)


def format_error_message(
    code: ErrorCode,
    *message_args: object,
    template: str | None = None,
) -> str:
    """Format a stable error message using the registered template."""

    active_template = template or get_error_message(code)
    if not message_args:
        return active_template

    return active_template % message_args
