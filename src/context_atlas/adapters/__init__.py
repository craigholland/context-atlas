"""Supported starter adapter exports for Context Atlas."""

from __future__ import annotations

from collections.abc import Iterable

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ..domain.models import (
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceDurability,
)
from .docs import FilesystemDocumentSourceAdapter
from .retrieval import InMemorySourceRegistry, LexicalRetrievalMode, LexicalRetriever


class StructuredRecordInput(BaseModel):
    """Minimal validated record shape adapters can translate into canonical sources."""

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
        str_strip_whitespace=True,
    )

    record_id: str
    content: str
    title: str | None = None
    source_uri: str | None = None
    source_class: ContextSourceClass = ContextSourceClass.OTHER
    authority: ContextSourceAuthority = ContextSourceAuthority.ADVISORY
    durability: ContextSourceDurability = ContextSourceDurability.WORKING
    tags: tuple[str, ...] = ()
    intended_uses: tuple[str, ...] = ()
    metadata: dict[str, str] = Field(default_factory=dict)
    provenance_metadata: dict[str, str] = Field(default_factory=dict)

    @field_validator("record_id", "content")
    @classmethod
    def _require_non_blank(cls, value: str) -> str:
        if not value:
            raise ValueError("must not be blank")
        return value

    @field_validator("tags", "intended_uses", mode="before")
    @classmethod
    def _normalize_text_sequence(
        cls,
        value: object,
    ) -> tuple[str, ...]:
        if value is None:
            return ()
        if isinstance(value, str):
            normalized = value.strip()
            return () if not normalized else (normalized,)
        if isinstance(value, Iterable):
            normalized_items = [
                normalized
                for item in value
                if isinstance(item, str) and (normalized := item.strip())
            ]
            return tuple(normalized_items)
        return ()


__all__ = [
    "FilesystemDocumentSourceAdapter",
    "InMemorySourceRegistry",
    "LexicalRetrievalMode",
    "LexicalRetriever",
    "StructuredRecordInput",
]
