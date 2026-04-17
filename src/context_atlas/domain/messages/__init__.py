"""Centralized message templates for stable errors and log events."""

from .error_messages import (
    ErrorMessageTemplate,
    format_error_message,
    get_error_message,
)
from .log_messages import LogMessageTemplate, get_log_message

__all__ = [
    "ErrorMessageTemplate",
    "LogMessageTemplate",
    "format_error_message",
    "get_error_message",
    "get_log_message",
]
