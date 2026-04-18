"""Compression policy contracts and starter implementations."""

from __future__ import annotations

import re
from typing import Iterable, Protocol

from ..errors import ContextAtlasError, ErrorCode
from ..messages import ErrorMessage
from ..models.base import CanonicalDomainModel
from ..models import (
    BudgetPressureReasonCode,
    CompressionResult,
    CompressionStrategy,
    ContextAssemblyDecision,
    ContextCandidate,
    ContextDecisionAction,
    ContextTrace,
    InclusionReasonCode,
)


class CompressionPolicy(Protocol):
    """Contract for reducing candidate content under a budget constraint."""

    def compress_candidates(
        self,
        candidates: Iterable[ContextCandidate],
        *,
        trace_id: str,
        max_tokens: int,
        query: str = "",
    ) -> "CompressionOutcome":
        """Compress candidate content into a bounded structured result."""


class CompressionOutcome(CanonicalDomainModel):
    """Structured result of a compression-policy invocation."""

    compression_result: CompressionResult
    trace: ContextTrace


class StarterCompressionPolicy(CanonicalDomainModel):
    """Starter compression policy inspired by the context-engine prototype."""

    strategy: CompressionStrategy = CompressionStrategy.EXTRACTIVE
    chars_per_token: int = 4
    min_chunk_chars: int = 20

    def model_post_init(self, __context: object) -> None:
        if self.chars_per_token < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_COMPRESSION_REQUEST,
                message_args=(ErrorMessage.CHARS_PER_TOKEN_MUST_BE_AT_LEAST_ONE,),
            )
        if self.min_chunk_chars < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_COMPRESSION_REQUEST,
                message_args=(ErrorMessage.MIN_CHUNK_CHARS_MUST_BE_AT_LEAST_ONE,),
            )

    def compress_candidates(
        self,
        candidates: Iterable[ContextCandidate],
        *,
        trace_id: str,
        max_tokens: int,
        query: str = "",
    ) -> CompressionOutcome:
        """Compress ranked candidate content to fit within a token budget."""

        if max_tokens < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_COMPRESSION_REQUEST,
                message_args=(
                    ErrorMessage.MAX_TOKENS_MUST_BE_AT_LEAST_ONE % (max_tokens,),
                ),
            )

        valid_candidates = tuple(
            candidate
            for candidate in candidates
            if len(candidate.source.content) >= self.min_chunk_chars
        )
        source_ids = tuple(candidate.source.source_id for candidate in valid_candidates)
        if not valid_candidates:
            result = CompressionResult(
                text="",
                strategy_used=self.strategy,
                original_chars=0,
                compressed_chars=0,
                estimated_tokens_saved=0,
                was_applied=False,
                source_ids=(),
                metadata={"outcome": "empty_input"},
            )
            trace = ContextTrace(
                trace_id=trace_id,
                decisions=(
                    ContextAssemblyDecision(
                        source_id="compression",
                        action=ContextDecisionAction.DEFERRED,
                        reason_codes=(BudgetPressureReasonCode.COMPRESSION_REQUIRED,),
                        explanation="No candidate content met the minimum compression threshold.",
                    ),
                ),
                metadata={
                    "compression_strategy": self.strategy.value,
                    "source_count": "0",
                },
            )
            return CompressionOutcome(compression_result=result, trace=trace)

        chunks = [candidate.source.content for candidate in valid_candidates]
        original_text = "\n\n".join(chunks)
        original_chars = len(original_text)
        max_chars = max_tokens * self.chars_per_token

        if original_chars <= max_chars:
            result = CompressionResult(
                text=original_text,
                strategy_used=self.strategy,
                original_chars=original_chars,
                compressed_chars=original_chars,
                estimated_tokens_saved=0,
                was_applied=False,
                source_ids=source_ids,
                metadata={"outcome": "fits_budget"},
            )
            trace = ContextTrace(
                trace_id=trace_id,
                decisions=(
                    ContextAssemblyDecision(
                        source_id="compression",
                        action=ContextDecisionAction.INCLUDED,
                        reason_codes=(InclusionReasonCode.BUDGET_AVAILABLE,),
                        candidate_score=float(max_tokens),
                    ),
                ),
                metadata={
                    "compression_strategy": self.strategy.value,
                    "source_count": str(len(source_ids)),
                    "max_tokens": str(max_tokens),
                },
            )
            return CompressionOutcome(compression_result=result, trace=trace)

        compressed_text, fallback_used = self._compress_chunks(
            chunks,
            query=query,
            max_chars=max_chars,
        )
        compressed_chars = len(compressed_text)
        estimated_tokens_saved = max(
            0,
            estimate_tokens(original_text, chars_per_token=self.chars_per_token)
            - estimate_tokens(compressed_text, chars_per_token=self.chars_per_token),
        )
        metadata = {"outcome": "compressed"}
        if fallback_used is not None:
            metadata["fallback_strategy"] = fallback_used.value

        result = CompressionResult(
            text=compressed_text,
            strategy_used=self.strategy,
            original_chars=original_chars,
            compressed_chars=compressed_chars,
            estimated_tokens_saved=estimated_tokens_saved,
            was_applied=True,
            source_ids=source_ids,
            metadata=metadata,
        )
        decisions = [
            ContextAssemblyDecision(
                source_id="compression",
                action=ContextDecisionAction.TRANSFORMED,
                reason_codes=(BudgetPressureReasonCode.COMPRESSION_REQUIRED,),
                explanation=(
                    f"Compression reduced content from {original_chars} to "
                    f"{compressed_chars} characters."
                ),
                candidate_score=float(compressed_chars),
            )
        ]
        if fallback_used is not None:
            decisions.append(
                ContextAssemblyDecision(
                    source_id="compression",
                    action=ContextDecisionAction.TRANSFORMED,
                    reason_codes=(BudgetPressureReasonCode.ELASTIC_SLOT_REDUCED,),
                    explanation=(
                        f"Compression fell back to {fallback_used.value} because the "
                        f"primary strategy could not satisfy the budget cleanly."
                    ),
                )
            )
        trace = ContextTrace(
            trace_id=trace_id,
            decisions=tuple(decisions),
            metadata={
                "compression_strategy": self.strategy.value,
                "source_count": str(len(source_ids)),
                "max_tokens": str(max_tokens),
                "estimated_tokens_saved": str(estimated_tokens_saved),
            },
        )
        return CompressionOutcome(compression_result=result, trace=trace)

    def _compress_chunks(
        self,
        chunks: list[str],
        *,
        query: str,
        max_chars: int,
    ) -> tuple[str, CompressionStrategy | None]:
        """Dispatch to the configured compression strategy."""

        if self.strategy is CompressionStrategy.TRUNCATE:
            return _truncate_chunks(chunks, max_chars=max_chars), None
        if self.strategy is CompressionStrategy.SENTENCE:
            return _sentence_preserving(chunks, max_chars=max_chars), None

        extracted = _extractive_compress(chunks, query=query, max_chars=max_chars)
        if extracted is None:
            return _truncate_chunks(
                chunks, max_chars=max_chars
            ), CompressionStrategy.TRUNCATE
        return extracted, None


def estimate_tokens(text: str, *, chars_per_token: int = 4) -> int:
    """Estimate token count using a coarse chars-per-token heuristic."""

    if chars_per_token < 1:
        raise ContextAtlasError(
            code=ErrorCode.INVALID_COMPRESSION_REQUEST,
            message_args=(
                ErrorMessage.CHARS_PER_TOKEN_MUST_BE_AT_LEAST_ONE_GOT
                % (chars_per_token,),
            ),
        )
    return len(text) // chars_per_token


def _truncate_chunks(chunks: list[str], *, max_chars: int) -> str:
    """Apply a simple head-truncation strategy across all chunks."""

    budget_per_chunk = max_chars // max(len(chunks), 1)
    joined = "\n\n".join(chunk[:budget_per_chunk] for chunk in chunks)
    return joined[:max_chars].strip()


def _sentence_preserving(chunks: list[str], *, max_chars: int) -> str:
    """Greedily preserve whole sentences in original order within the budget."""

    all_sentences: list[str] = []
    for chunk in chunks:
        all_sentences.extend(_split_sentences(chunk))

    parts: list[str] = []
    used = 0
    for sentence in all_sentences:
        needed = len(sentence) + (1 if parts else 0)
        if used + needed > max_chars:
            break
        parts.append(sentence)
        used += needed
    return " ".join(parts).strip()


def _extractive_compress(
    chunks: list[str],
    *,
    query: str,
    max_chars: int,
) -> str | None:
    """Apply query-aware extractive sentence selection within the budget."""

    indexed: list[tuple[int, int, float, str]] = []
    for chunk_index, chunk in enumerate(chunks):
        for sentence_index, sentence in enumerate(_split_sentences(chunk)):
            indexed.append(
                (
                    chunk_index,
                    sentence_index,
                    _sentence_score(sentence, query),
                    sentence,
                )
            )

    ranked = sorted(indexed, key=lambda item: item[2], reverse=True)
    remaining_chars = max_chars
    selected_keys: list[tuple[int, int]] = []
    separator = "  "

    for chunk_index, sentence_index, _score, sentence in ranked:
        cost = len(sentence) + (len(separator) if selected_keys else 0)
        if cost <= remaining_chars:
            selected_keys.append((chunk_index, sentence_index))
            remaining_chars -= cost
        if remaining_chars <= 10:
            break

    if not selected_keys:
        return None

    selected_set = set(selected_keys)
    ordered_sentences = [
        sentence
        for chunk_index, sentence_index, _score, sentence in indexed
        if (chunk_index, sentence_index) in selected_set
    ]
    return separator.join(ordered_sentences).strip()


def _split_sentences(text: str) -> list[str]:
    """Split a chunk into sentences while preserving closing punctuation."""

    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [part.strip() for part in parts if part.strip()]


def _sentence_score(sentence: str, query: str) -> float:
    """Score a sentence by normalized query-token overlap."""

    query_tokens = set(query.lower().split())
    if not query_tokens:
        return 0.0
    sentence_tokens = set(sentence.lower().split())
    return len(query_tokens & sentence_tokens) / len(query_tokens)
