"""Canonical memory-entry artifacts for Context Atlas."""

from __future__ import annotations

import math

from pydantic import Field

from ..errors import ContextAtlasError, ErrorCode
from ..messages import ErrorMessage
from .base import CanonicalDomainModel
from .sources import ContextSource


class ContextMemoryEntry(CanonicalDomainModel):
    """Canonical retained-memory artifact for future packet assembly."""

    entry_id: str
    source: ContextSource
    recorded_at_epoch_seconds: float
    importance: float = 1.0
    last_accessed_at_epoch_seconds: float | None = None
    metadata: dict[str, str] = Field(default_factory=dict)

    def model_post_init(self, __context: object) -> None:
        normalized_entry_id = self.entry_id.strip()
        if not normalized_entry_id:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_ENTRY,
                message_args=(ErrorMessage.ENTRY_ID_MUST_NOT_BE_EMPTY,),
            )
        if not math.isfinite(self.recorded_at_epoch_seconds):
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_ENTRY,
                message_args=(ErrorMessage.RECORDED_AT_EPOCH_SECONDS_MUST_BE_FINITE,),
            )
        if self.recorded_at_epoch_seconds < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_ENTRY,
                message_args=(
                    ErrorMessage.RECORDED_AT_EPOCH_SECONDS_MUST_BE_NON_NEGATIVE,
                ),
            )
        if not math.isfinite(self.importance):
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_ENTRY,
                message_args=(ErrorMessage.IMPORTANCE_MUST_BE_FINITE,),
            )
        if self.importance < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_ENTRY,
                message_args=(ErrorMessage.IMPORTANCE_MUST_BE_NON_NEGATIVE,),
            )
        if self.last_accessed_at_epoch_seconds is not None:
            if not math.isfinite(self.last_accessed_at_epoch_seconds):
                raise ContextAtlasError(
                    code=ErrorCode.INVALID_MEMORY_ENTRY,
                    message_args=(
                        ErrorMessage.LAST_ACCESSED_AT_EPOCH_SECONDS_MUST_BE_FINITE,
                    ),
                )
            if self.last_accessed_at_epoch_seconds < 0:
                raise ContextAtlasError(
                    code=ErrorCode.INVALID_MEMORY_ENTRY,
                    message_args=(
                        ErrorMessage.LAST_ACCESSED_AT_EPOCH_SECONDS_MUST_BE_NON_NEGATIVE,
                    ),
                )

        object.__setattr__(self, "entry_id", normalized_entry_id)
        object.__setattr__(self, "metadata", self.freeze_metadata(self.metadata))

    def age_seconds(self, *, now_epoch_seconds: float) -> float:
        """Return age at the provided clock instant, flooring negative drift to zero."""

        return max(0.0, now_epoch_seconds - self.recorded_at_epoch_seconds)


__all__ = ["ContextMemoryEntry"]
