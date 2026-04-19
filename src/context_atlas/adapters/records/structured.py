"""Structured-record adapters for translating record payloads into Atlas sources."""

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


class StructuredRecordSourceAdapter:
    """Translate structured record payloads into canonical Atlas sources."""

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
        records: Iterable[StructuredRecordInput | Mapping[str, object]],
    ) -> tuple[ContextSource, ...]:
        """Translate a sequence of structured records into canonical sources."""

        return tuple(self.load_source(record) for record in records)

    def load_source(
        self,
        record: StructuredRecordInput | Mapping[str, object],
    ) -> ContextSource:
        """Translate one structured record into a canonical source."""

        record_input = self._validate_record(record)
        semantics = resolve_source_semantics(
            source_class=record_input.source_class,
            authority=record_input.authority,
            durability=record_input.durability,
            intended_uses=record_input.intended_uses,
        )
        return ContextSource(
            source_id=record_input.record_id,
            content=record_input.content,
            title=record_input.title,
            source_class=record_input.source_class,
            authority=semantics.authority,
            durability=semantics.durability,
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
            intended_uses=semantics.intended_uses,
            metadata=record_input.metadata,
        )

    def _validate_record(
        self,
        record: StructuredRecordInput | Mapping[str, object],
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
    "StructuredRecordSourceAdapter",
]
