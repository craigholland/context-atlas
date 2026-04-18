"""Context Atlas package bootstrap.

The package root intentionally remains thin for now.

Current MVP-facing imports should normally come from:

- ``context_atlas.infrastructure`` for the starter assembly entrypoint
- ``context_atlas.infrastructure.config`` for validated settings loading
- ``context_atlas.adapters`` for starter source/retrieval adapters
- ``context_atlas.rendering`` for derived packet rendering

Until a broader curated API surface is introduced, user-facing guides should
prefer those supported subpackage imports rather than deep internal module
paths.
"""

__all__ = ["__version__"]

__version__ = "0.1.0a0"
