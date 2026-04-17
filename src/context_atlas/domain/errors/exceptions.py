"""Domain exception types built on stable error codes."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..messages import ErrorMessage
from .codes import ErrorCode


@dataclass(eq=False, slots=True)
class ContextAtlasError(Exception):
    """Base exception carrying a stable code and formatted message."""

    code: ErrorCode = ErrorCode.UNKNOWN
    message_args: tuple[Any, ...] = field(default_factory=tuple)
    message_text: str | None = None

    def __post_init__(self) -> None:
        super().__init__(str(self))

    @property
    def message(self) -> str:
        active_message = self.message_text
        if active_message is None:
            active_message = str(
                getattr(
                    ErrorMessage,
                    self.code.name,
                    ErrorMessage.UNKNOWN,
                )
            )
        if not self.message_args:
            return active_message
        return active_message % self.message_args

    def __str__(self) -> str:
        return self.message


class ConfigurationError(ContextAtlasError):
    """Raised when runtime configuration is invalid or incomplete."""
