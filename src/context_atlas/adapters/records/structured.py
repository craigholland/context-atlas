"""Structured-record adapters for translating already-fetched record payloads.

These adapters intentionally stop at translation. Outer application code owns
query execution, client lifecycles, and row fetching before Atlas sees any
record-shaped payloads.

When callers need to reshape row field names before translation, that mapping
should happen through adapter-facing helpers such as ``StructuredRecordRowMapper``
rather than by widening this adapter into a query or client surface.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

from ...domain.errors import ContextAtlasError, ErrorCode
from ...domain.messages import ErrorMessage
from ...domain.models import (
    ContextSource,
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceDurability,
    ContextSourceFamily,
    ContextSourceProvenance,
    coerce_source_text_sequence,
    resolve_source_semantics,
)


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
    authority: ContextSourceAuthority | None = None
    durability: ContextSourceDurability | None = None
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
        return coerce_source_text_sequence(value)


type StructuredRecordPayload = StructuredRecordInput | Mapping[str, object]


class StructuredRecordSourceAdapter:
    """Translate record-shaped payloads into canonical Atlas sources.

    Accepted inputs are intentionally narrow:
    - validated ``StructuredRecordInput`` objects
    - mapping-shaped row payloads that outer integration code already fetched

    Richer database, ORM, or vector-store objects should be normalized outside
    Atlas before they cross this adapter boundary.
    """

    def __init__(
        self,
        *,
        collector_name: str = "structured_record_source_adapter",
    ) -> None:
        normalized_collector = collector_name.strip()
        if not normalized_collector:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
                message_args=(ErrorMessage.RECORD_COLLECTOR_NAME_MUST_NOT_BE_EMPTY,),
            )
        self._collector_name = normalized_collector

    @property
    def collector_name(self) -> str:
        """Return the stable collector name used in source provenance."""

        return self._collector_name

    def load_sources(
        self,
        records: Iterable[StructuredRecordPayload],
    ) -> tuple[ContextSource, ...]:
        """Translate a sequence of structured records into canonical sources."""

        return tuple(self.load_source(record) for record in records)

    def load_source(
        self,
        record: StructuredRecordPayload,
    ) -> ContextSource:
        """Translate one record-shaped payload into a canonical source."""

        record_input = self._validate_record(record)
        semantics = resolve_source_semantics(
            source_class=record_input.source_class,
            authority=record_input.authority,
            durability=record_input.durability,
            intended_uses=record_input.intended_uses,
        )
        return ContextSource.from_semantics(
            source_id=record_input.record_id,
            content=record_input.content,
            title=record_input.title,
            semantics=semantics,
            provenance=ContextSourceProvenance(
                source_family=ContextSourceFamily.STRUCTURED_RECORD,
                source_uri=record_input.source_uri,
                collector=self._collector_name,
                metadata={
                    **record_input.provenance_metadata,
                    "record_id": record_input.record_id,
                },
            ),
            tags=record_input.tags,
            metadata=record_input.metadata,
        )

    def _validate_record(
        self,
        record: StructuredRecordPayload,
    ) -> StructuredRecordInput:
        if isinstance(record, StructuredRecordInput):
            return record

        try:
            return StructuredRecordInput.model_validate(record)
        except ValidationError as error:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
                message_args=(ErrorMessage.INVALID_STRUCTURED_RECORD_INPUT % (error,),),
            ) from error


__all__ = [
    "StructuredRecordInput",
    "StructuredRecordPayload",
    "StructuredRecordSourceAdapter",
]
