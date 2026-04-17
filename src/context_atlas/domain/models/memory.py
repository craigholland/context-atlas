"""Canonical memory-entry artifacts for Context Atlas."""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Mapping

from ..errors import ContextAtlasError, ErrorCode
from .sources import ContextSource


def _freeze_mapping(raw_mapping: Mapping[str, str]) -> Mapping[str, str]:
    """Return an immutable copy of a string-keyed mapping."""

    return MappingProxyType(dict(raw_mapping))


@dataclass(frozen=True, slots=True)
class ContextMemoryEntry:
    """Canonical retained-memory artifact for future packet assembly."""

    entry_id: str
    source: ContextSource
    recorded_at_epoch_seconds: float
    importance: float = 1.0
    last_accessed_at_epoch_seconds: float | None = None
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        normalized_entry_id = self.entry_id.strip()
        if not normalized_entry_id:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_ENTRY,
                message_args=("entry_id must not be empty",),
            )
        if not math.isfinite(self.recorded_at_epoch_seconds):
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_ENTRY,
                message_args=("recorded_at_epoch_seconds must be finite",),
            )
        if self.recorded_at_epoch_seconds < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_ENTRY,
                message_args=("recorded_at_epoch_seconds must be >= 0",),
            )
        if not math.isfinite(self.importance):
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_ENTRY,
                message_args=("importance must be finite",),
            )
        if self.importance < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_ENTRY,
                message_args=("importance must be >= 0",),
            )
        if self.last_accessed_at_epoch_seconds is not None:
            if not math.isfinite(self.last_accessed_at_epoch_seconds):
                raise ContextAtlasError(
                    code=ErrorCode.INVALID_MEMORY_ENTRY,
                    message_args=("last_accessed_at_epoch_seconds must be finite",),
                )
            if self.last_accessed_at_epoch_seconds < 0:
                raise ContextAtlasError(
                    code=ErrorCode.INVALID_MEMORY_ENTRY,
                    message_args=("last_accessed_at_epoch_seconds must be >= 0",),
                )

        object.__setattr__(self, "entry_id", normalized_entry_id)
        object.__setattr__(self, "metadata", _freeze_mapping(self.metadata))

    def age_seconds(self, *, now_epoch_seconds: float) -> float:
        """Return age at the provided clock instant, flooring negative drift to zero."""

        return max(0.0, now_epoch_seconds - self.recorded_at_epoch_seconds)


__all__ = ["ContextMemoryEntry"]
