"""Stable error identifiers for Context Atlas."""

from enum import StrEnum


class ErrorCode(StrEnum):
    """Stable machine-facing identifiers for Context Atlas errors."""

    UNKNOWN = "unknown"
    DOCUMENT_NO_CONTENT = "document_no_content"
    INVALID_CONFIGURATION = "invalid_configuration"
    MISSING_REQUIRED_SETTING = "missing_required_setting"
