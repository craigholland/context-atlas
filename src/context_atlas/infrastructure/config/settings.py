"""Pydantic-backed runtime settings models for Context Atlas."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, field_validator

from ...domain.messages import LogMessage
from ...domain.models import CompressionStrategy

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


class MemorySettings(BaseModel):
    """Validated runtime defaults for starter memory retention behavior."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    short_term_count: int = 4
    decay_rate: float = 0.001
    dedup_threshold: float = 0.72

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


class ContextAtlasSettings(BaseModel):
    """Validated top-level runtime settings assembled from environment input."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    logging: LoggingSettings = Field(default_factory=LoggingSettings)
    assembly: AssemblySettings = Field(default_factory=AssemblySettings)
    memory: MemorySettings = Field(default_factory=MemorySettings)
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
    ) -> "ContextAtlasSettings":
        """Build a settings object with a formatted load-summary message attached."""

        return cls(
            logging=logging,
            assembly=assembly,
            memory=memory,
            last_loaded_message_name=LogMessage.SETTINGS_LOADED.name,
            last_loaded_message=str(LogMessage.SETTINGS_LOADED)
            % (
                logging.logger_name,
                logging.level,
                assembly.default_total_budget,
                assembly.default_retrieval_top_k,
                assembly.default_compression_strategy.value,
                memory.short_term_count,
                memory.decay_rate,
                memory.dedup_threshold,
            ),
        )
