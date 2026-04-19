"""Supported low-code preset catalog for the MVP workflow wrapper."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from pydantic import BaseModel, ConfigDict, field_validator

from ...adapters.records import StructuredRecordRowMapper, StructuredRecordSourceAdapter
from ...domain.models import ContextSource, ContextSourceAuthority, ContextSourceClass


class LowCodeWorkflowPreset(BaseModel):
    """Outer-layer preset describing one supported low-code workflow shape."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        str_strip_whitespace=True,
    )

    name: str
    description: str
    record_collector_name: str
    record_row_mapper: StructuredRecordRowMapper | None = None

    @field_validator("name", "description", "record_collector_name")
    @classmethod
    def _require_non_blank_strings(cls, value: str) -> str:
        if not value:
            raise ValueError("preset fields must not be blank")
        return value

    def resolve_configured_path(
        self,
        *,
        repo_root: Path,
        configured_path: str,
    ) -> Path:
        """Resolve one configured path relative to the selected repo root."""

        candidate = Path(configured_path)
        if not candidate.is_absolute():
            candidate = repo_root / candidate
        return candidate.resolve()

    def load_record_sources(
        self,
        rows: tuple[Mapping[str, object], ...],
    ) -> tuple[ContextSource, ...]:
        """Translate already-fetched low-code record rows into canonical sources."""

        if self.record_row_mapper is None:
            return ()

        return StructuredRecordSourceAdapter(
            collector_name=self.record_collector_name,
        ).load_mapped_sources(
            rows,
            row_mapper=self.record_row_mapper,
        )


_LOW_CODE_PRESETS = {
    "chatbot_docs_records": LowCodeWorkflowPreset(
        name="chatbot_docs_records",
        description=(
            "Use governed guide docs plus already-fetched support-style records "
            "to assemble one chatbot-oriented packet."
        ),
        record_collector_name="low_code_support_records",
        record_row_mapper=StructuredRecordRowMapper(
            record_id_field="ticket_id",
            content_field="body",
            title_field="title",
            source_uri_field="uri",
            intended_uses_field="uses",
            metadata_fields=("team", "table"),
            provenance_fields=("database",),
            source_class=ContextSourceClass.REVIEWS,
            authority=ContextSourceAuthority.PREFERRED,
        ),
    ),
}


def get_low_code_workflow_preset(name: str) -> LowCodeWorkflowPreset:
    """Return one supported low-code preset by name."""

    return _LOW_CODE_PRESETS[name]


def is_supported_low_code_preset(name: str) -> bool:
    """Return whether a preset name is supported by the current MVP catalog."""

    return name in _LOW_CODE_PRESETS


def list_low_code_workflow_presets() -> tuple[str, ...]:
    """Return the supported preset names in stable order."""

    return tuple(_LOW_CODE_PRESETS)


__all__ = [
    "LowCodeWorkflowPreset",
    "get_low_code_workflow_preset",
    "is_supported_low_code_preset",
    "list_low_code_workflow_presets",
]
