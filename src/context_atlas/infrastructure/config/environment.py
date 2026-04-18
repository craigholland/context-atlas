"""Pydantic-settings environment loader for Context Atlas."""

from __future__ import annotations

from pydantic import ValidationError, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from ...domain.errors import ConfigurationError, ErrorCode
from ...domain.models import CompressionStrategy
from .settings import (
    AssemblySettings,
    ContextAtlasSettings,
    LoggingSettings,
    MemorySettings,
)


class EnvironmentSettings(BaseSettings):
    """Validated flat environment surface for Context Atlas runtime settings."""

    model_config = SettingsConfigDict(
        env_prefix="CONTEXT_ATLAS_",
        extra="ignore",
        frozen=True,
        case_sensitive=False,
    )

    logger_name: str = "context_atlas"
    log_level: str = "INFO"
    log_structured_events: bool = True
    default_total_budget: int = 2048
    default_retrieval_top_k: int = 5
    default_compression_strategy: CompressionStrategy = CompressionStrategy.EXTRACTIVE
    ranking_minimum_score: float = 0.0
    compression_chars_per_token: int = 4
    compression_min_chunk_chars: int = 20
    memory_short_term_count: int = 4
    memory_decay_rate: float = 0.001
    memory_dedup_threshold: float = 0.72
    memory_min_effective_score: float = 0.1
    memory_query_boost_weight: float = 0.35

    @field_validator("logger_name")
    @classmethod
    def _validate_logger_name(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("LOGGER_NAME must not be empty")
        return value.strip()

    @field_validator("log_level")
    @classmethod
    def _normalize_log_level(cls, value: str) -> str:
        return LoggingSettings(level=value).level

    @field_validator("default_total_budget")
    @classmethod
    def _validate_total_budget(cls, value: int) -> int:
        return AssemblySettings(default_total_budget=value).default_total_budget

    @field_validator("default_retrieval_top_k")
    @classmethod
    def _validate_top_k(cls, value: int) -> int:
        return AssemblySettings(default_retrieval_top_k=value).default_retrieval_top_k

    @field_validator("ranking_minimum_score")
    @classmethod
    def _validate_ranking_minimum_score(cls, value: float) -> float:
        return AssemblySettings(ranking_minimum_score=value).ranking_minimum_score

    @field_validator("compression_chars_per_token")
    @classmethod
    def _validate_compression_chars_per_token(cls, value: int) -> int:
        return AssemblySettings(
            compression_chars_per_token=value
        ).compression_chars_per_token

    @field_validator("compression_min_chunk_chars")
    @classmethod
    def _validate_compression_min_chunk_chars(cls, value: int) -> int:
        return AssemblySettings(
            compression_min_chunk_chars=value
        ).compression_min_chunk_chars

    @field_validator("memory_short_term_count")
    @classmethod
    def _validate_short_term_count(cls, value: int) -> int:
        return MemorySettings(short_term_count=value).short_term_count

    @field_validator("memory_decay_rate")
    @classmethod
    def _validate_decay_rate(cls, value: float) -> float:
        return MemorySettings(decay_rate=value).decay_rate

    @field_validator("memory_dedup_threshold")
    @classmethod
    def _validate_dedup_threshold(cls, value: float) -> float:
        return MemorySettings(dedup_threshold=value).dedup_threshold

    @field_validator("memory_min_effective_score")
    @classmethod
    def _validate_min_effective_score(cls, value: float) -> float:
        return MemorySettings(min_effective_score=value).min_effective_score

    @field_validator("memory_query_boost_weight")
    @classmethod
    def _validate_query_boost_weight(cls, value: float) -> float:
        return MemorySettings(query_boost_weight=value).query_boost_weight


def load_settings_from_env(prefix: str = "CONTEXT_ATLAS_") -> ContextAtlasSettings:
    """Load validated runtime settings from environment variables."""

    if not prefix:
        raise ConfigurationError(
            code=ErrorCode.INVALID_CONFIGURATION,
            message_args=("environment prefix must not be empty",),
        )

    try:
        env_settings = EnvironmentSettings(_env_prefix=prefix)  # type: ignore[call-arg]
        logging_settings = LoggingSettings(
            logger_name=env_settings.logger_name,
            level=env_settings.log_level,
            structured_events=env_settings.log_structured_events,
        )
        assembly_settings = AssemblySettings(
            default_total_budget=env_settings.default_total_budget,
            default_retrieval_top_k=env_settings.default_retrieval_top_k,
            default_compression_strategy=env_settings.default_compression_strategy,
            ranking_minimum_score=env_settings.ranking_minimum_score,
            compression_chars_per_token=env_settings.compression_chars_per_token,
            compression_min_chunk_chars=env_settings.compression_min_chunk_chars,
        )
        memory_settings = MemorySettings(
            short_term_count=env_settings.memory_short_term_count,
            decay_rate=env_settings.memory_decay_rate,
            dedup_threshold=env_settings.memory_dedup_threshold,
            min_effective_score=env_settings.memory_min_effective_score,
            query_boost_weight=env_settings.memory_query_boost_weight,
        )
    except ValidationError as error:
        raise ConfigurationError(
            code=ErrorCode.INVALID_CONFIGURATION,
            message_args=(_format_validation_error(error),),
        ) from error

    return ContextAtlasSettings.with_loaded_message(
        logging=logging_settings,
        assembly=assembly_settings,
        memory=memory_settings,
    )


def _format_validation_error(error: ValidationError) -> str:
    """Compress pydantic validation issues into one stable user-facing line."""

    details: list[str] = []
    for issue in error.errors():
        location = ".".join(str(part).upper() for part in issue["loc"])
        details.append(f"{location}: {issue['msg']}")
    return "; ".join(details)
