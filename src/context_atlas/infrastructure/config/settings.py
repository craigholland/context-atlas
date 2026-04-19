"""Pydantic-backed runtime settings models for Context Atlas."""

from __future__ import annotations

import math

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from ...domain.messages import LogMessage
from ...domain.models import CompressionStrategy
from .presets import (
    DEFAULT_LOW_CODE_WORKFLOW_DOCS_ROOT,
    DEFAULT_LOW_CODE_WORKFLOW_INCLUDE_DOCUMENTS,
    DEFAULT_LOW_CODE_WORKFLOW_INCLUDE_RECORDS,
    DEFAULT_LOW_CODE_WORKFLOW_PRESET,
    DEFAULT_LOW_CODE_WORKFLOW_RECORDS_FILE,
)

_VALID_LOG_LEVELS = frozenset(
    {
        "CRITICAL",
        "ERROR",
        "WARNING",
        "INFO",
        "DEBUG",
        "NOTSET",
    }
)


class LoggingSettings(BaseModel):
    """Validated runtime logging settings."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        str_strip_whitespace=True,
    )

    logger_name: str = "context_atlas"
    level: str = "INFO"
    structured_events: bool = True

    @field_validator("logger_name")
    @classmethod
    def _validate_logger_name(cls, value: str) -> str:
        if not value:
            raise ValueError("LOGGER_NAME must not be empty")
        return value

    @field_validator("level")
    @classmethod
    def _normalize_level(cls, value: str) -> str:
        normalized = value.upper()
        if normalized not in _VALID_LOG_LEVELS:
            raise ValueError(f"LOG_LEVEL must be one of {_VALID_LOG_LEVELS}")
        return normalized


class AssemblySettings(BaseModel):
    """Validated runtime defaults for early assembly behavior."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    default_total_budget: int = 2048
    default_retrieval_top_k: int = 5
    default_compression_strategy: CompressionStrategy = CompressionStrategy.EXTRACTIVE
    ranking_minimum_score: float = 0.0
    compression_chars_per_token: int = 4
    compression_min_chunk_chars: int = 20

    @field_validator("default_total_budget")
    @classmethod
    def _validate_total_budget(cls, value: int) -> int:
        if value < 64:
            raise ValueError(f"DEFAULT_TOTAL_BUDGET must be >= 64, got {value}")
        return value

    @field_validator("default_retrieval_top_k")
    @classmethod
    def _validate_top_k(cls, value: int) -> int:
        if value < 1:
            raise ValueError(f"DEFAULT_RETRIEVAL_TOP_K must be >= 1, got {value}")
        return value

    @field_validator("ranking_minimum_score")
    @classmethod
    def _validate_ranking_minimum_score(cls, value: float) -> float:
        if not math.isfinite(value):
            raise ValueError("RANKING_MINIMUM_SCORE must be finite")
        return value

    @field_validator("compression_chars_per_token")
    @classmethod
    def _validate_compression_chars_per_token(cls, value: int) -> int:
        if value < 1:
            raise ValueError(f"COMPRESSION_CHARS_PER_TOKEN must be >= 1, got {value}")
        return value

    @field_validator("compression_min_chunk_chars")
    @classmethod
    def _validate_compression_min_chunk_chars(cls, value: int) -> int:
        if value < 1:
            raise ValueError(f"COMPRESSION_MIN_CHUNK_CHARS must be >= 1, got {value}")
        return value


class MemorySettings(BaseModel):
    """Validated runtime defaults for starter memory retention behavior."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    short_term_count: int = 4
    decay_rate: float = 0.001
    dedup_threshold: float = 0.72
    min_effective_score: float = 0.1
    query_boost_weight: float = 0.35

    @field_validator("short_term_count")
    @classmethod
    def _validate_short_term_count(cls, value: int) -> int:
        if value < 1:
            raise ValueError(f"MEMORY_SHORT_TERM_COUNT must be >= 1, got {value}")
        return value

    @field_validator("decay_rate")
    @classmethod
    def _validate_decay_rate(cls, value: float) -> float:
        if value < 0:
            raise ValueError(f"MEMORY_DECAY_RATE must be >= 0, got {value}")
        return value

    @field_validator("dedup_threshold")
    @classmethod
    def _validate_dedup_threshold(cls, value: float) -> float:
        if not 0.0 <= value <= 1.0:
            raise ValueError(
                f"MEMORY_DEDUP_THRESHOLD must be in [0.0, 1.0], got {value}"
            )
        return value

    @field_validator("min_effective_score")
    @classmethod
    def _validate_min_effective_score(cls, value: float) -> float:
        if not math.isfinite(value) or value < 0:
            raise ValueError(
                f"MEMORY_MIN_EFFECTIVE_SCORE must be finite and >= 0, got {value}"
            )
        return value

    @field_validator("query_boost_weight")
    @classmethod
    def _validate_query_boost_weight(cls, value: float) -> float:
        if not math.isfinite(value) or value < 0:
            raise ValueError(
                f"MEMORY_QUERY_BOOST_WEIGHT must be finite and >= 0, got {value}"
            )
        return value


class LowCodeWorkflowSettings(BaseModel):
    """Validated low-code workflow settings for the MVP wrapper path."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        str_strip_whitespace=True,
    )

    preset: str = DEFAULT_LOW_CODE_WORKFLOW_PRESET
    docs_root: str = DEFAULT_LOW_CODE_WORKFLOW_DOCS_ROOT
    records_file: str = DEFAULT_LOW_CODE_WORKFLOW_RECORDS_FILE
    include_documents: bool = DEFAULT_LOW_CODE_WORKFLOW_INCLUDE_DOCUMENTS
    include_records: bool = DEFAULT_LOW_CODE_WORKFLOW_INCLUDE_RECORDS

    @field_validator("preset", "docs_root", "records_file")
    @classmethod
    def _require_non_blank_strings(cls, value: str) -> str:
        if not value:
            raise ValueError("LOW_CODE settings must not be blank")
        return value

    @field_validator("preset")
    @classmethod
    def _validate_supported_preset(cls, value: str) -> str:
        from .presets import (
            is_supported_low_code_preset,
            list_low_code_workflow_presets,
        )

        if not is_supported_low_code_preset(value):
            raise ValueError(
                "LOW_CODE_PRESET must be one of "
                f"{list_low_code_workflow_presets()}, got {value}"
            )
        return value

    @model_validator(mode="after")
    def _require_at_least_one_source(self) -> "LowCodeWorkflowSettings":
        if not (self.include_documents or self.include_records):
            raise ValueError("At least one low-code source family must be enabled.")
        return self

    def with_overrides(
        self,
        *,
        preset: str | None = None,
        docs_root: str | None = None,
        records_file: str | None = None,
        include_documents: bool | None = None,
        include_records: bool | None = None,
    ) -> "LowCodeWorkflowSettings":
        """Return a validated copy with explicit low-code overrides applied."""

        overrides: dict[str, object] = {}
        if preset is not None:
            overrides["preset"] = preset
        if docs_root is not None:
            overrides["docs_root"] = docs_root
        if records_file is not None:
            overrides["records_file"] = records_file
        if include_documents is not None:
            overrides["include_documents"] = include_documents
        if include_records is not None:
            overrides["include_records"] = include_records
        return self.__class__.model_validate(
            self.model_dump(mode="python") | overrides,
        )


class ContextAtlasSettings(BaseModel):
    """Validated top-level runtime settings assembled from environment input."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    logging: LoggingSettings = Field(default_factory=LoggingSettings)
    assembly: AssemblySettings = Field(default_factory=AssemblySettings)
    memory: MemorySettings = Field(default_factory=MemorySettings)
    low_code: LowCodeWorkflowSettings = Field(default_factory=LowCodeWorkflowSettings)
    last_loaded_message_name: str | None = None
    last_loaded_message: str | None = None

    @field_validator("last_loaded_message_name")
    @classmethod
    def _validate_last_loaded_message_name(cls, value: str | None) -> str | None:
        if value is None:
            return value
        if not value.strip():
            raise ValueError("last_loaded_message_name must not be empty when set")
        return value

    @classmethod
    def with_loaded_message(
        cls,
        *,
        logging: LoggingSettings,
        assembly: AssemblySettings,
        memory: MemorySettings,
        low_code: LowCodeWorkflowSettings,
    ) -> "ContextAtlasSettings":
        """Build a settings object with a formatted load-summary message attached."""

        return cls(
            logging=logging,
            assembly=assembly,
            memory=memory,
            low_code=low_code,
            last_loaded_message_name=LogMessage.SETTINGS_LOADED.name,
            last_loaded_message=str(LogMessage.SETTINGS_LOADED)
            % (
                logging.logger_name,
                logging.level,
                assembly.default_total_budget,
                assembly.default_retrieval_top_k,
                assembly.default_compression_strategy.value,
                assembly.ranking_minimum_score,
                assembly.compression_chars_per_token,
                assembly.compression_min_chunk_chars,
                memory.short_term_count,
                memory.decay_rate,
                memory.dedup_threshold,
                memory.min_effective_score,
                memory.query_boost_weight,
            ),
        )

    def with_low_code_overrides(
        self,
        *,
        preset: str | None = None,
        docs_root: str | None = None,
        records_file: str | None = None,
        include_documents: bool | None = None,
        include_records: bool | None = None,
    ) -> "ContextAtlasSettings":
        """Return settings with validated low-code overrides applied."""

        return self.model_copy(
            update={
                "low_code": self.low_code.with_overrides(
                    preset=preset,
                    docs_root=docs_root,
                    records_file=records_file,
                    include_documents=include_documents,
                    include_records=include_records,
                )
            }
        )
