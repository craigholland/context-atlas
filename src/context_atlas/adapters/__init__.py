"""Adapter layer for external systems and provider-facing translations."""

from .docs import FilesystemDocumentSourceAdapter
from .retrieval import InMemorySourceRegistry, LexicalRetrievalMode, LexicalRetriever

__all__ = [
    "FilesystemDocumentSourceAdapter",
    "InMemorySourceRegistry",
    "LexicalRetrievalMode",
    "LexicalRetriever",
]
