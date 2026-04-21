"""Compression policy contracts and starter implementations."""

from __future__ import annotations

import math
import re
from typing import Callable
from typing import Iterable, Protocol

from pydantic import Field, field_validator

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


TokenEstimator = Callable[[str], int]


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
    """Starter compression policy."""

    strategy: CompressionStrategy = CompressionStrategy.EXTRACTIVE
    chars_per_token: int = 4
    min_chunk_chars: int = 20
    token_estimator: TokenEstimator | None = Field(
        default=None,
        exclude=True,
        repr=False,
    )
    token_estimator_name: str = "starter_heuristic"

    @field_validator("token_estimator_name")
    @classmethod
    def _validate_token_estimator_name(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("token_estimator_name must not be blank")
        return normalized

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
        token_estimator_name_was_provided = (
            "token_estimator_name" in self.model_fields_set
        )
        if self.token_estimator is None:
            if token_estimator_name_was_provided and (
                self.token_estimator_name != "starter_heuristic"
            ):
                raise ContextAtlasError(
                    code=ErrorCode.INVALID_COMPRESSION_REQUEST,
                    message_args=("token_estimator_name requires token_estimator",),
                )
            return
        if not token_estimator_name_was_provided:
            object.__setattr__(self, "token_estimator_name", "external_binding")

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

        candidate_tuple = tuple(candidates)
        if not candidate_tuple:
            result = CompressionResult(
                text="",
                strategy_used=self.strategy,
                original_chars=0,
                compressed_chars=0,
                estimated_tokens_saved=0,
                was_applied=False,
                source_ids=(),
                metadata={
                    "outcome": "empty_input",
                    "token_estimator": self.token_estimator_name,
                },
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
                    "token_estimator": self.token_estimator_name,
                },
            )
            return CompressionOutcome(compression_result=result, trace=trace)

        source_ids = tuple(candidate.source.source_id for candidate in candidate_tuple)
        chunks = [candidate.source.content for candidate in candidate_tuple]
        original_text = "\n\n".join(chunks)
        original_chars = len(original_text)
        max_chars = _max_chars_for_token_budget(
            original_text,
            max_tokens=max_tokens,
            token_estimator=self._estimate_tokens,
        )

        if self._estimate_tokens(original_text) <= max_tokens:
            result = CompressionResult(
                text=original_text,
                strategy_used=self.strategy,
                original_chars=original_chars,
                compressed_chars=original_chars,
                estimated_tokens_saved=0,
                was_applied=False,
                source_ids=source_ids,
                metadata={
                    "outcome": "fits_budget",
                    "token_estimator": self.token_estimator_name,
                },
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
                    "token_estimator": self.token_estimator_name,
                },
            )
            return CompressionOutcome(compression_result=result, trace=trace)

        compression_input = [
            chunk for chunk in chunks if len(chunk) >= self.min_chunk_chars
        ]
        if not compression_input:
            compressed_text = _truncate_chunks(chunks, max_chars=max_chars)
            fallback_used = (
                None
                if self.strategy is CompressionStrategy.TRUNCATE
                else CompressionStrategy.TRUNCATE
            )
        else:
            compressed_text, fallback_used = self._compress_chunks(
                compression_input,
                query=query,
                max_chars=max_chars,
            )
        compressed_text, budget_trimmed = _fit_text_within_token_budget(
            compressed_text,
            max_tokens=max_tokens,
            token_estimator=self._estimate_tokens,
        )
        if budget_trimmed and fallback_used is None:
            fallback_used = CompressionStrategy.TRUNCATE

        compressed_chars = len(compressed_text)
        estimated_tokens_saved = max(
            0,
            self._estimate_tokens(original_text)
            - self._estimate_tokens(compressed_text),
        )
        metadata = {
            "outcome": "compressed",
            "token_estimator": self.token_estimator_name,
        }
        if fallback_used is not None:
            metadata["fallback_strategy"] = fallback_used.value
        if not compression_input:
            metadata["compression_scope"] = "all_candidates_below_min_chunk_chars"

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
                "token_estimator": self.token_estimator_name,
            },
        )
        return CompressionOutcome(compression_result=result, trace=trace)

    def _estimate_tokens(self, text: str) -> int:
        """Estimate token count through the bound seam or the starter heuristic."""

        if not text:
            return 0
        if self.token_estimator is not None:
            return max(0, int(self.token_estimator(text)))
        return estimate_tokens(text, chars_per_token=self.chars_per_token)

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
    """Estimate token count using a bounded content-shape-aware starter heuristic."""

    if chars_per_token < 1:
        raise ContextAtlasError(
            code=ErrorCode.INVALID_COMPRESSION_REQUEST,
            message_args=(
                ErrorMessage.CHARS_PER_TOKEN_MUST_BE_AT_LEAST_ONE_GOT
                % (chars_per_token,),
            ),
        )
    if not text:
        return 0
    return len(text) // _effective_chars_per_token(
        text,
        baseline_chars_per_token=chars_per_token,
    )


def _effective_chars_per_token(
    text: str,
    *,
    baseline_chars_per_token: int,
) -> int:
    """Return a bounded starter chars-per-token estimate for obvious content shapes."""

    effective = baseline_chars_per_token
    if _looks_like_structured_text(text):
        effective = min(effective, max(1, baseline_chars_per_token - 1))
    if _looks_non_latin_heavy(text):
        effective = min(effective, max(1, math.ceil(baseline_chars_per_token / 2)))
    return effective


def _looks_like_structured_text(text: str) -> bool:
    """Detect code- or markup-heavy text without introducing provider assumptions."""

    stripped = text.strip()
    if not stripped:
        return False

    line_count = stripped.count("\n") + 1
    markdown_marker_count = sum(
        1
        for line in stripped.splitlines()
        if re.match(r"^\s{0,3}(#{1,6}\s|[-*+]\s|>\s|\d+[.)]\s|```|~~~)", line)
    )
    code_signal_count = len(re.findall(r"```|~~~|::|->|=>|[{}[\]();<>]", stripped))
    structural_char_count = sum(1 for char in stripped if char in "#*_`[](){}<>-|\\/")
    structural_ratio = structural_char_count / len(stripped)

    return (
        markdown_marker_count >= 2
        or (line_count >= 3 and markdown_marker_count >= 1)
        or code_signal_count >= 8
        or (line_count >= 3 and code_signal_count >= 4)
        or structural_ratio >= 0.10
    )


def _looks_non_latin_heavy(text: str) -> bool:
    """Detect text where alphabetic content is dominated by non-ASCII characters."""

    alphabetic_chars = [char for char in text if char.isalpha()]
    if not alphabetic_chars:
        return False
    non_ascii_alpha = sum(1 for char in alphabetic_chars if ord(char) > 127)
    return (non_ascii_alpha / len(alphabetic_chars)) >= 0.35


def _truncate_chunks(chunks: list[str], *, max_chars: int) -> str:
    """Apply a simple head-truncation strategy across all chunks."""

    budget_per_chunk = max_chars // max(len(chunks), 1)
    joined = "\n\n".join(chunk[:budget_per_chunk] for chunk in chunks)
    return joined[:max_chars].strip()


def _fit_text_within_token_budget(
    text: str,
    *,
    max_tokens: int,
    token_estimator: TokenEstimator,
) -> tuple[str, bool]:
    """Trim text until its estimated token count fits the requested budget."""

    if token_estimator(text) <= max_tokens:
        return text, False

    low = 0
    high = len(text)
    best = ""
    while low <= high:
        midpoint = (low + high) // 2
        candidate = text[:midpoint].strip()
        if token_estimator(candidate) <= max_tokens:
            best = candidate
            low = midpoint + 1
        else:
            high = midpoint - 1
    return best, True


def _max_chars_for_token_budget(
    text: str,
    *,
    max_tokens: int,
    token_estimator: TokenEstimator,
) -> int:
    """Return the longest prefix length whose estimated tokens fit the budget."""

    if not text or max_tokens < 1:
        return 0
    if token_estimator(text) <= max_tokens:
        return len(text)

    low = 0
    high = len(text)
    best = 0
    while low <= high:
        midpoint = (low + high) // 2
        if token_estimator(text[:midpoint]) <= max_tokens:
            best = midpoint
            low = midpoint + 1
        else:
            high = midpoint - 1
    return best


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
