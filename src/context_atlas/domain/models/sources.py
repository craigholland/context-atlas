"""Canonical source and candidate domain artifacts."""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import StrEnum
from types import MappingProxyType
from typing import Mapping

from ..errors import ContextAtlasError, ErrorCode


class ContextSourceClass(StrEnum):
    """High-level source classes available to Context Atlas."""

    AUTHORITATIVE = "authoritative"
    PLANNING = "planning"
    REVIEWS = "reviews"
    EXPLORATORY = "exploratory"
    RELEASES = "releases"
    CODE = "code"
    MEMORY = "memory"
    OTHER = "other"


class ContextSourceAuthority(StrEnum):
    """Trust/precedence posture of a source."""

    BINDING = "binding"
    PREFERRED = "preferred"
    ADVISORY = "advisory"
    SPECULATIVE = "speculative"
    HISTORICAL = "historical"


class ContextSourceDurability(StrEnum):
    """Expected stability of a source over time."""

    EPHEMERAL = "ephemeral"
    SESSION = "session"
    WORKING = "working"
    DURABLE = "durable"
    ARCHIVAL = "archival"


def _freeze_mapping(raw_mapping: Mapping[str, str]) -> Mapping[str, str]:
    """Return an immutable copy of a string-keyed mapping."""

    return MappingProxyType(dict(raw_mapping))


@dataclass(frozen=True, slots=True)
class ContextSourceProvenance:
    """Describe how a source entered the system."""

    source_uri: str | None = None
    collector: str | None = None
    version: str | None = None
    captured_at_utc: str | None = None
    checksum: str | None = None
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "metadata", _freeze_mapping(self.metadata))


@dataclass(frozen=True, slots=True)
class ContextSource:
    """Canonical source artifact for Context Atlas."""

    source_id: str
    content: str
    title: str | None = None
    source_class: ContextSourceClass = ContextSourceClass.OTHER
    authority: ContextSourceAuthority = ContextSourceAuthority.ADVISORY
    durability: ContextSourceDurability = ContextSourceDurability.WORKING
    provenance: ContextSourceProvenance = field(default_factory=ContextSourceProvenance)
    tags: tuple[str, ...] = ()
    intended_uses: tuple[str, ...] = ()
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        normalized_source_id = self.source_id.strip()
        if not normalized_source_id:
            raise ContextAtlasError(code=ErrorCode.EMPTY_SOURCE_IDENTIFIER)

        normalized_content = self.content.strip()
        if not normalized_content:
            raise ContextAtlasError(
                code=ErrorCode.EMPTY_SOURCE_CONTENT,
                message_args=(normalized_source_id,),
            )

        normalized_title = self.title.strip() if self.title else None
        object.__setattr__(self, "source_id", normalized_source_id)
        object.__setattr__(self, "content", normalized_content)
        object.__setattr__(self, "title", normalized_title or None)
        object.__setattr__(self, "tags", tuple(self.tags))
        object.__setattr__(self, "intended_uses", tuple(self.intended_uses))
        object.__setattr__(self, "metadata", _freeze_mapping(self.metadata))


@dataclass(frozen=True, slots=True)
class ContextCandidate:
    """A candidate source paired with optional scoring metadata."""

    source: ContextSource
    score: float | None = None
    rank: int | None = None
    signals: tuple[str, ...] = ()
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.score is not None and not math.isfinite(self.score):
            raise ContextAtlasError(
                code=ErrorCode.INVALID_CANDIDATE_STATE,
                message_args=("score must be finite when provided",),
            )
        if self.rank is not None and self.rank < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_CANDIDATE_STATE,
                message_args=("rank must be >= 1 when provided",),
            )

        object.__setattr__(self, "signals", tuple(self.signals))
        object.__setattr__(self, "metadata", _freeze_mapping(self.metadata))


__all__ = [
    "ContextCandidate",
    "ContextSource",
    "ContextSourceAuthority",
    "ContextSourceClass",
    "ContextSourceDurability",
    "ContextSourceProvenance",
]
