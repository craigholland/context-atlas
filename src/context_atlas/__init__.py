"""Context Atlas package bootstrap.

The package root intentionally remains thin while the product surface hardens.

Current MVP-facing imports should normally come from:

- ``context_atlas.api`` for the supported starter flow
- stable subpackage imports when docs intentionally need to show layer seams

User-facing guides should prefer the curated API over deep internal module
paths unless they are explicitly teaching the architecture.
"""

from . import api

__all__ = ["__version__", "api"]

__version__ = "0.1.0a0"
