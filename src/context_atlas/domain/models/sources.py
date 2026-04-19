"""Canonical source and candidate domain artifacts."""

from __future__ import annotations

import math

from pydantic import Field

from ..errors import ContextAtlasError, ErrorCode
from ..messages import ErrorMessage
from .base import CanonicalDomainModel
from .source_semantics import (
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceDurability,
    ContextSourceFamily,
    ContextSourceSemanticsProfile,
    merge_source_text_groups,
)


class ContextSourceProvenance(CanonicalDomainModel):
    """Describe how a source entered the system."""

    source_family: ContextSourceFamily = ContextSourceFamily.OTHER
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

    @classmethod
    def from_semantics(
        cls,
        *,
        source_id: str,
        content: str,
        semantics: ContextSourceSemanticsProfile,
        title: str | None = None,
        provenance: ContextSourceProvenance | None = None,
        tags: tuple[str, ...] = (),
        metadata: dict[str, str] | None = None,
    ) -> "ContextSource":
        """Build a canonical source from a resolved semantic profile.

        Adapters should shape source-family-specific mechanics outward, then cross
        into the domain through one canonical semantic surface instead of passing
        source-class, authority, durability, and intended-use pieces around
        independently.
        """

        return cls(
            source_id=source_id,
            content=content,
            title=title,
            source_class=semantics.source_class,
            authority=semantics.authority,
            durability=semantics.durability,
            provenance=provenance or ContextSourceProvenance(),
            tags=tags,
            intended_uses=semantics.intended_uses,
            metadata={} if metadata is None else metadata,
        )

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
            merge_source_text_groups(self.tags),
        )
        object.__setattr__(
            self,
            "intended_uses",
            merge_source_text_groups(self.intended_uses),
        )
        object.__setattr__(self, "metadata", self.freeze_metadata(self.metadata))

    @property
    def collector_name(self) -> str | None:
        """Return the outward collector identity that supplied this source."""

        return self.provenance.collector

    @property
    def semantics(self) -> ContextSourceSemanticsProfile:
        """Return the canonical semantic profile expressed by this source."""

        return ContextSourceSemanticsProfile(
            source_class=self.source_class,
            authority=self.authority,
            durability=self.durability,
            intended_uses=self.intended_uses,
        )

    @property
    def source_family(self) -> ContextSourceFamily:
        """Return the canonical ingestion family carried in source provenance."""

        return self.provenance.source_family


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
                message_args=(ErrorMessage.SCORE_MUST_BE_FINITE_WHEN_PROVIDED,),
            )
        if self.rank is not None and self.rank < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_CANDIDATE_STATE,
                message_args=(ErrorMessage.RANK_MUST_BE_AT_LEAST_ONE_WHEN_PROVIDED,),
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
    "ContextSourceFamily",
    "ContextSourceProvenance",
]
