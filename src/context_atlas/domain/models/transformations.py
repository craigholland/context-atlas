"""Canonical transformation artifacts for Context Atlas."""

from __future__ import annotations

from enum import StrEnum

from pydantic import Field

from ..errors import ContextAtlasError, ErrorCode
from .base import CanonicalDomainModel


class CompressionStrategy(StrEnum):
    """Supported starter compression strategies."""

    TRUNCATE = "truncate"
    SENTENCE = "sentence"
    EXTRACTIVE = "extractive"


class CompressionResult(CanonicalDomainModel):
    """Structured compression artifact retained as canonical packet metadata."""

    text: str
    strategy_used: CompressionStrategy
    original_chars: int
    compressed_chars: int
    estimated_tokens_saved: int
    was_applied: bool = True
    source_ids: tuple[str, ...] = ()
    metadata: dict[str, str] = Field(default_factory=dict)

    def model_post_init(self, __context: object) -> None:
        if self.original_chars < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_COMPRESSION_REQUEST,
                message_args=("original_chars must be >= 0",),
            )
        if self.compressed_chars < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_COMPRESSION_REQUEST,
                message_args=("compressed_chars must be >= 0",),
            )
        if self.compressed_chars > self.original_chars:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_COMPRESSION_REQUEST,
                message_args=(
                    "compressed_chars must be <= original_chars for canonical compression results",
                ),
            )
        if self.estimated_tokens_saved < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_COMPRESSION_REQUEST,
                message_args=("estimated_tokens_saved must be >= 0",),
            )

        object.__setattr__(self, "source_ids", tuple(self.source_ids))
        object.__setattr__(self, "metadata", self.freeze_metadata(self.metadata))

    @property
    def compression_ratio(self) -> float:
        """Return the retained fraction of the original content size."""

        if self.original_chars == 0:
            return 1.0
        return round(self.compressed_chars / self.original_chars, 3)


__all__ = ["CompressionResult", "CompressionStrategy"]
