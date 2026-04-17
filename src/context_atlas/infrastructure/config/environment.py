"""Environment-backed settings loaders for runtime infrastructure."""

from __future__ import annotations

import os
import math

from ...domain.errors import ConfigurationError, ErrorCode
from ...domain.events import LogEvent
from ...domain.messages import get_log_message
from ...domain.models import CompressionStrategy
from .settings import (
    AssemblySettings,
    ContextAtlasSettings,
    LoggingSettings,
    MemorySettings,
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


def load_settings_from_env(prefix: str = "CONTEXT_ATLAS_") -> ContextAtlasSettings:
    """Load runtime settings from environment variables.

    Supported variables:

    - ``<prefix>LOGGER_NAME``
    - ``<prefix>LOG_LEVEL``
    - ``<prefix>LOG_STRUCTURED_EVENTS``
    - ``<prefix>DEFAULT_TOTAL_BUDGET``
    - ``<prefix>DEFAULT_RETRIEVAL_TOP_K``
    - ``<prefix>DEFAULT_COMPRESSION_STRATEGY``
    - ``<prefix>MEMORY_SHORT_TERM_COUNT``
    - ``<prefix>MEMORY_DECAY_RATE``
    - ``<prefix>MEMORY_DEDUP_THRESHOLD``
    """

    if not prefix:
        raise ConfigurationError(
            code=ErrorCode.INVALID_CONFIGURATION,
            message_args=("environment prefix must not be empty",),
        )

    defaults = LoggingSettings()
    assembly_defaults = AssemblySettings()
    memory_defaults = MemorySettings()
    logger_name = os.getenv(f"{prefix}LOGGER_NAME", defaults.logger_name)
    log_level = _read_log_level(
        os.getenv(f"{prefix}LOG_LEVEL"),
        default=defaults.level,
    )
    structured_events = _read_bool(
        os.getenv(f"{prefix}LOG_STRUCTURED_EVENTS"),
        default=defaults.structured_events,
    )
    default_total_budget = _read_int(
        os.getenv(f"{prefix}DEFAULT_TOTAL_BUDGET"),
        default=assembly_defaults.default_total_budget,
        minimum=64,
        setting_name=f"{prefix}DEFAULT_TOTAL_BUDGET",
    )
    default_retrieval_top_k = _read_int(
        os.getenv(f"{prefix}DEFAULT_RETRIEVAL_TOP_K"),
        default=assembly_defaults.default_retrieval_top_k,
        minimum=1,
        setting_name=f"{prefix}DEFAULT_RETRIEVAL_TOP_K",
    )
    default_compression_strategy = _read_compression_strategy(
        os.getenv(f"{prefix}DEFAULT_COMPRESSION_STRATEGY"),
        default=assembly_defaults.default_compression_strategy,
        setting_name=f"{prefix}DEFAULT_COMPRESSION_STRATEGY",
    )
    memory_short_term_count = _read_int(
        os.getenv(f"{prefix}MEMORY_SHORT_TERM_COUNT"),
        default=memory_defaults.short_term_count,
        minimum=1,
        setting_name=f"{prefix}MEMORY_SHORT_TERM_COUNT",
    )
    memory_decay_rate = _read_float(
        os.getenv(f"{prefix}MEMORY_DECAY_RATE"),
        default=memory_defaults.decay_rate,
        minimum=0.0,
        maximum=None,
        setting_name=f"{prefix}MEMORY_DECAY_RATE",
    )
    memory_dedup_threshold = _read_float(
        os.getenv(f"{prefix}MEMORY_DEDUP_THRESHOLD"),
        default=memory_defaults.dedup_threshold,
        minimum=0.0,
        maximum=1.0,
        setting_name=f"{prefix}MEMORY_DEDUP_THRESHOLD",
    )

    settings = ContextAtlasSettings(
        logging=LoggingSettings(
            logger_name=logger_name,
            level=log_level,
            structured_events=structured_events,
        ),
        assembly=AssemblySettings(
            default_total_budget=default_total_budget,
            default_retrieval_top_k=default_retrieval_top_k,
            default_compression_strategy=default_compression_strategy,
        ),
        memory=MemorySettings(
            short_term_count=memory_short_term_count,
            decay_rate=memory_decay_rate,
            dedup_threshold=memory_dedup_threshold,
        ),
    )
    settings.last_loaded_event = LogEvent.SETTINGS_LOADED
    settings.last_loaded_message = get_log_message(LogEvent.SETTINGS_LOADED) % (
        logger_name,
        log_level,
        default_total_budget,
        default_retrieval_top_k,
        default_compression_strategy.value,
        memory_short_term_count,
        memory_decay_rate,
        memory_dedup_threshold,
    )
    return settings


def _read_bool(raw_value: str | None, *, default: bool) -> bool:
    """Interpret common truthy and falsy environment values."""

    if raw_value is None:
        return default

    normalized = raw_value.strip().lower()
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False

    raise ConfigurationError(
        code=ErrorCode.INVALID_CONFIGURATION,
        message_args=(f"invalid boolean value '{raw_value}'",),
    )


def _read_int(
    raw_value: str | None,
    *,
    default: int,
    minimum: int,
    setting_name: str,
) -> int:
    """Read a positive integer setting with a minimum floor."""

    if raw_value is None:
        return default

    try:
        value = int(raw_value.strip())
    except ValueError as error:
        raise ConfigurationError(
            code=ErrorCode.INVALID_CONFIGURATION,
            message_args=(f"{setting_name} must be an integer, got '{raw_value}'",),
        ) from error

    if value < minimum:
        raise ConfigurationError(
            code=ErrorCode.INVALID_CONFIGURATION,
            message_args=(f"{setting_name} must be >= {minimum}, got {value}",),
        )
    return value


def _read_float(
    raw_value: str | None,
    *,
    default: float,
    minimum: float,
    maximum: float | None,
    setting_name: str,
) -> float:
    """Read a bounded float setting while keeping user-facing errors explicit."""

    if raw_value is None:
        return default

    try:
        value = float(raw_value.strip())
    except ValueError as error:
        raise ConfigurationError(
            code=ErrorCode.INVALID_CONFIGURATION,
            message_args=(f"{setting_name} must be a float, got '{raw_value}'",),
        ) from error

    if not math.isfinite(value):
        raise ConfigurationError(
            code=ErrorCode.INVALID_CONFIGURATION,
            message_args=(f"{setting_name} must be finite, got {raw_value}",),
        )
    if value < minimum:
        raise ConfigurationError(
            code=ErrorCode.INVALID_CONFIGURATION,
            message_args=(f"{setting_name} must be >= {minimum}, got {value}",),
        )
    if maximum is not None and value > maximum:
        raise ConfigurationError(
            code=ErrorCode.INVALID_CONFIGURATION,
            message_args=(f"{setting_name} must be <= {maximum}, got {value}",),
        )
    return value


def _read_log_level(raw_value: str | None, *, default: str) -> str:
    """Validate user-facing logging levels instead of silently coercing them."""

    if raw_value is None:
        return default

    normalized = raw_value.strip().upper()
    if normalized in _VALID_LOG_LEVELS:
        return normalized

    raise ConfigurationError(
        code=ErrorCode.INVALID_CONFIGURATION,
        message_args=(f"invalid log level '{raw_value}'",),
    )


def _read_compression_strategy(
    raw_value: str | None,
    *,
    default: CompressionStrategy,
    setting_name: str,
) -> CompressionStrategy:
    """Validate starter compression strategy names from the environment."""

    if raw_value is None:
        return default

    normalized = raw_value.strip().lower()
    try:
        return CompressionStrategy(normalized)
    except ValueError as error:
        allowed = ", ".join(strategy.value for strategy in CompressionStrategy)
        raise ConfigurationError(
            code=ErrorCode.INVALID_CONFIGURATION,
            message_args=(
                f"{setting_name} must be one of [{allowed}], got '{raw_value}'",
            ),
        ) from error
