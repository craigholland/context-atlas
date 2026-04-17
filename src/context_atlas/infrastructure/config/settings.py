"""Runtime settings models for Context Atlas infrastructure concerns."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class LoggingSettings:
    """Configuration for the runtime logging implementation."""

    logger_name: str = "context_atlas"
    level: str = "INFO"
    structured_events: bool = True


@dataclass(slots=True)
class ContextAtlasSettings:
    """Top-level runtime settings assembled by infrastructure loaders."""

    logging: LoggingSettings = field(default_factory=LoggingSettings)
    last_loaded_event: str | None = None
    last_loaded_message: str | None = None
