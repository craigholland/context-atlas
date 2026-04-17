"""Canonical source and candidate domain artifacts."""

from __future__ import annotations

import math
from enum import StrEnum

from pydantic import Field

from ..errors import ContextAtlasError, ErrorCode
from .base import CanonicalDomainModel


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


class ContextSourceProvenance(CanonicalDomainModel):
    """Describe how a source entered the system."""

    source_uri: str | None = None
    collector: str | None = None
    version: str | None = None
    captured_at_utc: str | None = None
    checksum: str | None = None
    metadata: dict[str, str] = Field(default_factory=dict)

    def model_post_init(self, __context: object) -> None:
        if self.source_uri is not None:
            object.__setattr__(self, "source_uri", self.source_uri.strip() or None)
        if self.collector is not None:
            object.__setattr__(self, "collector", self.collector.strip() or None)
        if self.version is not None:
            object.__setattr__(self, "version", self.version.strip() or None)
        if self.captured_at_utc is not None:
            object.__setattr__(
                self,
                "captured_at_utc",
                self.captured_at_utc.strip() or None,
            )
        if self.checksum is not None:
            object.__setattr__(self, "checksum", self.checksum.strip() or None)
        object.__setattr__(self, "metadata", self.freeze_metadata(self.metadata))


class ContextSource(CanonicalDomainModel):
    """Canonical source artifact for Context Atlas."""

    source_id: str
    content: str
    title: str | None = None
    source_class: ContextSourceClass = ContextSourceClass.OTHER
    authority: ContextSourceAuthority = ContextSourceAuthority.ADVISORY
    durability: ContextSourceDurability = ContextSourceDurability.WORKING
    provenance: ContextSourceProvenance = Field(default_factory=ContextSourceProvenance)
    tags: tuple[str, ...] = ()
    intended_uses: tuple[str, ...] = ()
    metadata: dict[str, str] = Field(default_factory=dict)

    def model_post_init(self, __context: object) -> None:
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
        object.__setattr__(
            self,
            "tags",
            tuple(tag.strip() for tag in self.tags if tag.strip()),
        )
        object.__setattr__(
            self,
            "intended_uses",
            tuple(use.strip() for use in self.intended_uses if use.strip()),
        )
        object.__setattr__(self, "metadata", self.freeze_metadata(self.metadata))


class ContextCandidate(CanonicalDomainModel):
    """A candidate source paired with optional scoring metadata."""

    source: ContextSource
    score: float | None = None
    rank: int | None = None
    signals: tuple[str, ...] = ()
    metadata: dict[str, str] = Field(default_factory=dict)

    def model_post_init(self, __context: object) -> None:
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

        object.__setattr__(
            self,
            "signals",
            tuple(signal.strip() for signal in self.signals if signal.strip()),
        )
        object.__setattr__(self, "metadata", self.freeze_metadata(self.metadata))


__all__ = [
    "ContextCandidate",
    "ContextSource",
    "ContextSourceAuthority",
    "ContextSourceClass",
    "ContextSourceDurability",
    "ContextSourceProvenance",
]
