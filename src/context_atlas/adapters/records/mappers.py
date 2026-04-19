"""Helpers for shaping already-fetched record rows into adapter inputs."""

from __future__ import annotations

from collections.abc import Iterable, Mapping

from pydantic import (
    BaseModel,
    ConfigDict,
    ValidationError,
    ValidationInfo,
    field_validator,
)

from ...domain.errors import ContextAtlasError, ErrorCode
from ...domain.messages import ErrorMessage
from ...domain.models import (
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceDurability,
    coerce_source_text_sequence,
    merge_source_text_groups,
)
from .structured import StructuredRecordInput


class StructuredRecordRowMapper(BaseModel):
    """Maps already-fetched row payloads into validated record inputs."""

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
        str_strip_whitespace=True,
    )

    record_id_field: str = "id"
    content_field: str = "content"
    title_field: str | None = None
    source_uri_field: str | None = None
    tags_field: str | None = None
    intended_uses_field: str | None = None
    metadata_fields: tuple[str, ...] = ()
    provenance_fields: tuple[str, ...] = ()
    source_class: ContextSourceClass = ContextSourceClass.OTHER
    authority: ContextSourceAuthority | None = None
    durability: ContextSourceDurability | None = None
    fixed_tags: tuple[str, ...] = ()
    fixed_intended_uses: tuple[str, ...] = ()

    @field_validator(
        "record_id_field",
        "content_field",
        "title_field",
        "source_uri_field",
        "tags_field",
        "intended_uses_field",
    )
    @classmethod
    def _require_field_name_when_provided(
        cls,
        value: str | None,
        info: ValidationInfo,
    ) -> str | None:
        if value == "":
            field_name = info.field_name or "field"
            raise ValueError(
                ErrorMessage.FIELD_MUST_NOT_BE_BLANK_WHEN_PROVIDED % (field_name,)
            )
        return value

    @field_validator(
        "metadata_fields",
        "provenance_fields",
        "fixed_tags",
        "fixed_intended_uses",
        mode="before",
    )
    @classmethod
    def _normalize_text_fields(cls, value: object) -> tuple[str, ...]:
        return coerce_source_text_sequence(value)

    def to_record_input(self, row: Mapping[str, object]) -> StructuredRecordInput:
        """Translate a single row mapping into a validated record input."""

        try:
            row_tags = self._sequence_value(row, self.tags_field)
            row_intended_uses = self._sequence_value(row, self.intended_uses_field)
            return StructuredRecordInput.model_validate(
                {
                    "record_id": self._required_value(row, self.record_id_field),
                    "content": self._required_value(row, self.content_field),
                    "title": self._optional_value(row, self.title_field),
                    "source_uri": self._optional_value(row, self.source_uri_field),
                    "source_class": self.source_class,
                    "authority": self.authority,
                    "durability": self.durability,
                    "tags": merge_source_text_groups(self.fixed_tags, row_tags),
                    "intended_uses": merge_source_text_groups(
                        self.fixed_intended_uses,
                        row_intended_uses,
                    ),
                    "metadata": self._string_field_map(row, self.metadata_fields),
                    "provenance_metadata": self._string_field_map(
                        row,
                        self.provenance_fields,
                    ),
                }
            )
        except (KeyError, TypeError, ValidationError, ValueError) as error:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
                message_args=(ErrorMessage.INVALID_STRUCTURED_RECORD_INPUT % (error,),),
            ) from error

    def to_record_inputs(
        self,
        rows: Iterable[Mapping[str, object]],
    ) -> tuple[StructuredRecordInput, ...]:
        """Translate multiple row mappings into validated record inputs."""

        return tuple(self.to_record_input(row) for row in rows)

    def _required_value(self, row: Mapping[str, object], field_name: str) -> object:
        return row[field_name]

    def _optional_value(
        self,
        row: Mapping[str, object],
        field_name: str | None,
    ) -> object | None:
        if field_name is None:
            return None
        return row[field_name]

    def _sequence_value(
        self,
        row: Mapping[str, object],
        field_name: str | None,
    ) -> tuple[str, ...]:
        if field_name is None:
            return ()
        return coerce_source_text_sequence(row[field_name])

    def _string_field_map(
        self,
        row: Mapping[str, object],
        field_names: tuple[str, ...],
    ) -> dict[str, str]:
        mapped_fields: dict[str, str] = {}
        for field_name in field_names:
            value = row[field_name]
            if value is None:
                continue
            mapped_fields[field_name] = str(value)
        return mapped_fields


__all__ = ["StructuredRecordRowMapper"]
