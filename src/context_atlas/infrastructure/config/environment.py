"""Environment-backed settings loaders for runtime infrastructure."""

from __future__ import annotations

import os

from ...domain.errors import ConfigurationError, ErrorCode
from ...domain.events import LogEvent
from ...domain.messages import get_log_message
from .settings import ContextAtlasSettings, LoggingSettings


def load_settings_from_env(prefix: str = "CONTEXT_ATLAS_") -> ContextAtlasSettings:
    """Load runtime settings from environment variables.

    Supported variables:

    - ``<prefix>LOGGER_NAME``
    - ``<prefix>LOG_LEVEL``
    - ``<prefix>LOG_STRUCTURED_EVENTS``
    """

    if not prefix:
        raise ConfigurationError(
            code=ErrorCode.INVALID_CONFIGURATION,
            message_args=("environment prefix must not be empty",),
        )

    defaults = LoggingSettings()
    logger_name = os.getenv(f"{prefix}LOGGER_NAME", defaults.logger_name)
    log_level = os.getenv(f"{prefix}LOG_LEVEL", defaults.level)
    structured_events = _read_bool(
        os.getenv(f"{prefix}LOG_STRUCTURED_EVENTS"),
        default=defaults.structured_events,
    )

    settings = ContextAtlasSettings(
        logging=LoggingSettings(
            logger_name=logger_name,
            level=log_level,
            structured_events=structured_events,
        )
    )
    settings.last_loaded_event = LogEvent.SETTINGS_LOADED
    settings.last_loaded_message = get_log_message(LogEvent.SETTINGS_LOADED)
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
