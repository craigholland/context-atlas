"""Runtime settings models for Context Atlas infrastructure concerns."""

from __future__ import annotations

from dataclasses import dataclass, field
import math

from ...domain.errors import ConfigurationError, ErrorCode
from ...domain.events import LogEvent
from ...domain.models import CompressionStrategy


@dataclass(frozen=True, slots=True)
class LoggingSettings:
    """Configuration for the runtime logging implementation."""

    logger_name: str = "context_atlas"
    level: str = "INFO"
    structured_events: bool = True


@dataclass(frozen=True, slots=True)
class AssemblySettings:
    """Runtime defaults for early context-assembly behavior."""

    default_total_budget: int = 2048
    default_retrieval_top_k: int = 5
    default_compression_strategy: CompressionStrategy = CompressionStrategy.EXTRACTIVE

    def __post_init__(self) -> None:
        if self.default_total_budget < 64:
            raise ConfigurationError(
                code=ErrorCode.INVALID_CONFIGURATION,
                message_args=(
                    f"default_total_budget must be >= 64, got {self.default_total_budget}",
                ),
            )
        if self.default_retrieval_top_k < 1:
            raise ConfigurationError(
                code=ErrorCode.INVALID_CONFIGURATION,
                message_args=(
                    f"default_retrieval_top_k must be >= 1, got {self.default_retrieval_top_k}",
                ),
            )


@dataclass(frozen=True, slots=True)
class MemorySettings:
    """Runtime defaults for starter memory-retention behavior."""

    short_term_count: int = 4
    decay_rate: float = 0.001
    dedup_threshold: float = 0.72

    def __post_init__(self) -> None:
        if self.short_term_count < 1:
            raise ConfigurationError(
                code=ErrorCode.INVALID_CONFIGURATION,
                message_args=(
                    f"short_term_count must be >= 1, got {self.short_term_count}",
                ),
            )
        if not math.isfinite(self.decay_rate) or self.decay_rate < 0:
            raise ConfigurationError(
                code=ErrorCode.INVALID_CONFIGURATION,
                message_args=(f"decay_rate must be >= 0, got {self.decay_rate}",),
            )
        if not math.isfinite(self.dedup_threshold) or not (
            0.0 <= self.dedup_threshold <= 1.0
        ):
            raise ConfigurationError(
                code=ErrorCode.INVALID_CONFIGURATION,
                message_args=(
                    "dedup_threshold must be in [0.0, 1.0], "
                    f"got {self.dedup_threshold}",
                ),
            )


@dataclass(slots=True)
class ContextAtlasSettings:
    """Top-level runtime settings assembled by infrastructure loaders."""

    logging: LoggingSettings = field(default_factory=LoggingSettings)
    assembly: AssemblySettings = field(default_factory=AssemblySettings)
    memory: MemorySettings = field(default_factory=MemorySettings)
    last_loaded_event: LogEvent | None = None
    last_loaded_message: str | None = None
