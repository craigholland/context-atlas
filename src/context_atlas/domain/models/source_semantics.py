"""Canonical source-semantics enums, defaults, and normalization helpers."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from enum import StrEnum

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


def coerce_source_text_sequence(value: object) -> tuple[str, ...]:
    """Coerce a source-facing text sequence input into a normalized tuple."""

    if value is None:
        return ()
    if isinstance(value, str):
        normalized = value.strip()
        return () if not normalized else (normalized,)
    if isinstance(value, Mapping):
        raise ValueError("must not be a mapping")
    if isinstance(value, Iterable):
        normalized_items: list[str] = []
        for item in value:
            if not isinstance(item, str):
                raise ValueError("must contain only strings")
            normalized = item.strip()
            if normalized:
                normalized_items.append(normalized)
        return CanonicalDomainModel.normalize_text_sequence(normalized_items)
    raise ValueError("must be a string or iterable of strings")


def get_default_source_semantics(
    source_class: ContextSourceClass,
) -> ContextSourceSemanticsProfile:
    """Return the canonical default semantics for a source class."""

    return _DEFAULT_SOURCE_SEMANTICS_BY_CLASS[source_class]


def merge_source_text_groups(*groups: Iterable[str]) -> tuple[str, ...]:
    """Merge source-related text groups while preserving first-seen order."""

    return CanonicalDomainModel.merge_unique_text_groups(*groups)


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
        intended_uses=merge_source_text_groups(
            defaults.intended_uses,
            intended_uses,
        ),
    )


__all__ = [
    "ContextSourceAuthority",
    "ContextSourceClass",
    "ContextSourceDurability",
    "ContextSourceFamily",
    "ContextSourceSemanticsProfile",
    "coerce_source_text_sequence",
    "get_default_source_semantics",
    "merge_source_text_groups",
    "resolve_source_semantics",
]
