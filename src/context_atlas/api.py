"""Curated starter API surface for Context Atlas MVP users.

This module exposes the supported starter flow without requiring callers to
learn deeper package paths before the broader product surface has hardened.
It is intentionally small: widening this surface should be driven by real
golden-path usage, not convenience re-exporting.
"""

from .adapters import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetrievalMode,
    LexicalRetriever,
)
from .infrastructure import build_starter_context_assembly_service
from .infrastructure.config import ContextAtlasSettings, load_settings_from_env
from .rendering import render_packet_context

__all__ = [
    "FilesystemDocumentSourceAdapter",
    "InMemorySourceRegistry",
    "LexicalRetrievalMode",
    "LexicalRetriever",
    "build_starter_context_assembly_service",
    "ContextAtlasSettings",
    "load_settings_from_env",
    "render_packet_context",
]
