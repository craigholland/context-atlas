"""Domain exception types built on stable error codes."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..messages import ErrorMessage
from .codes import ErrorCode


class ContextAtlasError(Exception):
    """Base exception carrying a stable code and a validated payload."""

    def __init__(
        self,
        *,
        code: ErrorCode = ErrorCode.UNKNOWN,
        message_args: tuple[Any, ...] | list[Any] = (),
    ) -> None:
        self._payload = _ContextAtlasErrorPayload(
            code=code,
            message_args=tuple(message_args),
        )
        super().__init__(self.message)

    @property
    def code(self) -> ErrorCode:
        return self._payload.code

    @property
    def message_args(self) -> tuple[Any, ...]:
        return self._payload.message_args

    @property
    def message(self) -> str:
        return self._payload.render_message()

    @property
    def payload(self) -> "_ContextAtlasErrorPayload":
        return self._payload

    def model_dump(self) -> dict[str, Any]:
        """Expose the validated payload for testing and inspection."""

        return self._payload.model_dump()

    def __str__(self) -> str:
        return self.message


class ConfigurationError(ContextAtlasError):
    """Raised when runtime configuration is invalid or incomplete."""


class _ContextAtlasErrorPayload(BaseModel):
    """Validated payload backing the public exception types."""

    model_config = ConfigDict(
        frozen=True,
        arbitrary_types_allowed=True,
    )

    code: ErrorCode = ErrorCode.UNKNOWN
    message_args: tuple[Any, ...] = Field(default_factory=tuple)

    @field_validator("message_args", mode="before")
    @classmethod
    def _coerce_message_args(cls, value: object) -> tuple[Any, ...]:
        if value is None:
            return ()
        if isinstance(value, tuple):
            return value
        if isinstance(value, list):
            return tuple(value)
        return (value,)

    def render_message(self) -> str:
        template = str(
            getattr(
                ErrorMessage,
                self.code.name,
                ErrorMessage.UNKNOWN,
            )
        )
        if not self.message_args:
            return template
        return template % self.message_args
