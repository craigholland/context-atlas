"""Canonical source and candidate domain artifacts."""

from __future__ import annotations

from collections.abc import Iterable
import math
from enum import StrEnum

from pydantic import Field

from ..errors import ContextAtlasError, ErrorCode
from ..messages import ErrorMessage
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


class ContextSourceFamily(StrEnum):
    """High-level ingestion family for a canonical source."""

    DOCUMENT = "document"
    STRUCTURED_RECORD = "structured_record"
    MEMORY = "memory"
    CODE = "code"
    OTHER = "other"


class ContextSourceSemanticsProfile(CanonicalDomainModel):
    """Canonical semantic defaults for a source class."""

    source_class: ContextSourceClass
    authority: ContextSourceAuthority
    durability: ContextSourceDurability
    intended_uses: tuple[str, ...] = ()

    def model_post_init(self, __context: object) -> None:
        object.__setattr__(
            self,
            "intended_uses",
            self.normalize_text_sequence(self.intended_uses),
        )


_DEFAULT_SOURCE_SEMANTICS_BY_CLASS = {
    ContextSourceClass.AUTHORITATIVE: ContextSourceSemanticsProfile(
        source_class=ContextSourceClass.AUTHORITATIVE,
        authority=ContextSourceAuthority.BINDING,
        durability=ContextSourceDurability.DURABLE,
        intended_uses=("implementation", "review", "planning"),
    ),
    ContextSourceClass.PLANNING: ContextSourceSemanticsProfile(
        source_class=ContextSourceClass.PLANNING,
        authority=ContextSourceAuthority.PREFERRED,
        durability=ContextSourceDurability.WORKING,
        intended_uses=("planning", "execution"),
    ),
    ContextSourceClass.REVIEWS: ContextSourceSemanticsProfile(
        source_class=ContextSourceClass.REVIEWS,
        authority=ContextSourceAuthority.ADVISORY,
        durability=ContextSourceDurability.WORKING,
        intended_uses=("review", "evidence"),
    ),
    ContextSourceClass.EXPLORATORY: ContextSourceSemanticsProfile(
        source_class=ContextSourceClass.EXPLORATORY,
        authority=ContextSourceAuthority.SPECULATIVE,
        durability=ContextSourceDurability.WORKING,
        intended_uses=("hypothesis_generation", "exploration"),
    ),
    ContextSourceClass.RELEASES: ContextSourceSemanticsProfile(
        source_class=ContextSourceClass.RELEASES,
        authority=ContextSourceAuthority.HISTORICAL,
        durability=ContextSourceDurability.ARCHIVAL,
        intended_uses=("history", "operations"),
    ),
    ContextSourceClass.CODE: ContextSourceSemanticsProfile(
        source_class=ContextSourceClass.CODE,
        authority=ContextSourceAuthority.PREFERRED,
        durability=ContextSourceDurability.WORKING,
        intended_uses=("implementation", "debugging"),
    ),
    ContextSourceClass.MEMORY: ContextSourceSemanticsProfile(
        source_class=ContextSourceClass.MEMORY,
        authority=ContextSourceAuthority.ADVISORY,
        durability=ContextSourceDurability.SESSION,
        intended_uses=("continuity", "follow_up"),
    ),
    ContextSourceClass.OTHER: ContextSourceSemanticsProfile(
        source_class=ContextSourceClass.OTHER,
        authority=ContextSourceAuthority.ADVISORY,
        durability=ContextSourceDurability.WORKING,
        intended_uses=(),
    ),
}


def get_default_source_semantics(
    source_class: ContextSourceClass,
) -> ContextSourceSemanticsProfile:
    """Return the canonical default semantics for a source class."""

    return _DEFAULT_SOURCE_SEMANTICS_BY_CLASS[source_class]


def resolve_source_semantics(
    *,
    source_class: ContextSourceClass,
    authority: ContextSourceAuthority | None = None,
    durability: ContextSourceDurability | None = None,
    intended_uses: Iterable[str] = (),
) -> ContextSourceSemanticsProfile:
    """Resolve source semantics from canonical class defaults plus overrides."""

    defaults = get_default_source_semantics(source_class)
    return ContextSourceSemanticsProfile(
        source_class=source_class,
        authority=authority or defaults.authority,
        durability=durability or defaults.durability,
        intended_uses=CanonicalDomainModel.merge_unique_text_groups(
            defaults.intended_uses,
            intended_uses,
        ),
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
            self.normalize_text_sequence(self.tags),
        )
        object.__setattr__(
            self,
            "intended_uses",
            self.normalize_text_sequence(self.intended_uses),
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
    "ContextSourceSemanticsProfile",
    "get_default_source_semantics",
    "resolve_source_semantics",
]
