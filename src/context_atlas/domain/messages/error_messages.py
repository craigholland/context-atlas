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


_ERROR_MESSAGES: Mapping[ErrorCode, str] = MappingProxyType(
    {
        ErrorCode.UNKNOWN: ErrorMessageTemplate.UNKNOWN,
        ErrorCode.DOCUMENT_NO_CONTENT: ErrorMessageTemplate.DOCUMENT_NO_CONTENT,
        ErrorCode.INVALID_CONFIGURATION: ErrorMessageTemplate.INVALID_CONFIGURATION,
        ErrorCode.MISSING_REQUIRED_SETTING: ErrorMessageTemplate.MISSING_REQUIRED_SETTING,
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
