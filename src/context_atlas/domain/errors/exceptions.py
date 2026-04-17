"""Domain exception types built on stable error codes."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..messages import format_error_message
from .codes import ErrorCode


@dataclass(eq=False, slots=True)
class ContextAtlasError(Exception):
    """Base exception carrying a stable code and formatted message."""

    code: ErrorCode = ErrorCode.UNKNOWN
    message_args: tuple[Any, ...] = field(default_factory=tuple)
    template: str | None = None

    def __post_init__(self) -> None:
        super().__init__(str(self))

    @property
    def message(self) -> str:
        return format_error_message(
            self.code,
            *self.message_args,
            template=self.template,
        )

    def __str__(self) -> str:
        return self.message


class ConfigurationError(ContextAtlasError):
    """Raised when runtime configuration is invalid or incomplete."""
