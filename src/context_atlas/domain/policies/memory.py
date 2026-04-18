"""Memory-entry retention and selection policies."""

from __future__ import annotations

from dataclasses import dataclass
import math
import time
from typing import Iterable, Protocol

from ..errors import ContextAtlasError, ErrorCode
from ..messages import ErrorMessage
from ..models.base import CanonicalDomainModel
from ..models import (
    ContextAssemblyDecision,
    ContextDecisionAction,
    ContextMemoryEntry,
    ContextTrace,
    ExclusionReasonCode,
    InclusionReasonCode,
)

_DEFAULT_MINIMUM_EFFECTIVE_SCORE = 0.1
_DEFAULT_QUERY_BOOST_WEIGHT = 0.35


class MemoryRetentionPolicy(Protocol):
    """Contract for deterministic memory retention and trace generation."""

    def select_memory(
        self,
        entries: Iterable[ContextMemoryEntry],
        *,
        trace_id: str,
        query: str = "",
        now_epoch_seconds: float | None = None,
    ) -> "MemorySelectionOutcome":
        """Return retained memory entries plus a structured decision trace."""


class MemorySelectionOutcome(CanonicalDomainModel):
    """Structured result of a memory-selection policy invocation."""

    selected_entries: tuple[ContextMemoryEntry, ...]
    trace: ContextTrace

    @property
    def selected_count(self) -> int:
        """Return the number of retained memory entries."""

        return len(self.selected_entries)


class StarterMemoryRetentionPolicy(CanonicalDomainModel):
    """Starter retention policy inspired by the context-engine memory prototype."""

    short_term_count: int = 4
    decay_rate: float = 0.001
    dedup_threshold: float = 0.72
    min_effective_score: float = _DEFAULT_MINIMUM_EFFECTIVE_SCORE
    query_boost_weight: float = _DEFAULT_QUERY_BOOST_WEIGHT

    def model_post_init(self, __context: object) -> None:
        if self.short_term_count < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_SELECTION,
                message_args=(ErrorMessage.SHORT_TERM_COUNT_MUST_BE_AT_LEAST_ONE,),
            )
        if not math.isfinite(self.decay_rate) or self.decay_rate < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_SELECTION,
                message_args=(ErrorMessage.DECAY_RATE_MUST_BE_FINITE_AND_NON_NEGATIVE,),
            )
        if not math.isfinite(self.dedup_threshold) or not (
            0.0 <= self.dedup_threshold <= 1.0
        ):
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_SELECTION,
                message_args=(
                    ErrorMessage.DEDUP_THRESHOLD_MUST_BE_WITHIN_UNIT_INTERVAL,
                ),
            )
        if not math.isfinite(self.min_effective_score) or self.min_effective_score < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_SELECTION,
                message_args=(
                    ErrorMessage.MIN_EFFECTIVE_SCORE_MUST_BE_FINITE_AND_NON_NEGATIVE,
                ),
            )
        if not math.isfinite(self.query_boost_weight) or self.query_boost_weight < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_SELECTION,
                message_args=(
                    ErrorMessage.QUERY_BOOST_WEIGHT_MUST_BE_FINITE_AND_NON_NEGATIVE,
                ),
            )

    def select_memory(
        self,
        entries: Iterable[ContextMemoryEntry],
        *,
        trace_id: str,
        query: str = "",
        now_epoch_seconds: float | None = None,
    ) -> MemorySelectionOutcome:
        """Retain short-term entries and score long-term memory deterministically."""

        active_now = time.time() if now_epoch_seconds is None else now_epoch_seconds
        if not math.isfinite(active_now) or active_now < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_MEMORY_SELECTION,
                message_args=(
                    ErrorMessage.NOW_EPOCH_SECONDS_MUST_BE_FINITE_AND_NON_NEGATIVE,
                ),
            )

        ordered_entries = tuple(
            sorted(
                entries,
                key=lambda entry: (
                    entry.recorded_at_epoch_seconds,
                    entry.entry_id,
                ),
            )
        )
        if not ordered_entries:
            return MemorySelectionOutcome(
                selected_entries=(),
                trace=ContextTrace(
                    trace_id=trace_id,
                    metadata={
                        "memory_policy": "starter_memory_retention_policy",
                        "input_entry_count": "0",
                        "selected_entry_count": "0",
                        "recent_entry_count": "0",
                        "deduplicated_entry_count": "0",
                        "rejected_entry_count": "0",
                    },
                ),
            )

        recent_entries = ordered_entries[-self.short_term_count :]
        long_term_entries = ordered_entries[: -len(recent_entries)]

        selected_long_term: list[_ScoredMemoryEntry] = []
        decisions: list[ContextAssemblyDecision] = []
        deduplicated_count = 0
        rejected_count = 0

        for recent_entry in recent_entries:
            decisions.append(
                ContextAssemblyDecision(
                    source_id=recent_entry.entry_id,
                    action=ContextDecisionAction.INCLUDED,
                    reason_codes=(
                        InclusionReasonCode.SHORT_TERM_PRIORITY,
                        InclusionReasonCode.MEMORY_RETAINED,
                    ),
                    explanation=(
                        "Memory entry was retained because it falls within the "
                        "short-term always-include window."
                    ),
                    candidate_score=recent_entry.importance,
                )
            )

        retained_for_dedup = list(recent_entries)
        scored_long_term = sorted(
            (
                _ScoredMemoryEntry.from_entry(
                    entry,
                    now_epoch_seconds=active_now,
                    decay_rate=self.decay_rate,
                    query=query,
                    query_boost_weight=self.query_boost_weight,
                )
                for entry in long_term_entries
            ),
            key=lambda item: (
                -item.effective_score,
                -item.entry.recorded_at_epoch_seconds,
                item.entry.entry_id,
            ),
        )

        for scored_entry in scored_long_term:
            duplicate_of = _find_duplicate_entry(
                scored_entry.entry,
                retained_for_dedup,
                threshold=self.dedup_threshold,
            )
            if duplicate_of is not None:
                deduplicated_count += 1
                rejected_count += 1
                decisions.append(
                    ContextAssemblyDecision(
                        source_id=scored_entry.entry.entry_id,
                        action=ContextDecisionAction.EXCLUDED,
                        reason_codes=(ExclusionReasonCode.DUPLICATE,),
                        explanation=(
                            f"Memory entry duplicated retained entry "
                            f"'{duplicate_of.entry_id}'."
                        ),
                        candidate_score=scored_entry.effective_score,
                    )
                )
                continue

            if scored_entry.effective_score < self.min_effective_score:
                rejected_count += 1
                decisions.append(
                    ContextAssemblyDecision(
                        source_id=scored_entry.entry.entry_id,
                        action=ContextDecisionAction.EXCLUDED,
                        reason_codes=(
                            ExclusionReasonCode.STALE_MEMORY,
                            ExclusionReasonCode.BELOW_THRESHOLD,
                        ),
                        explanation=(
                            f"Effective memory score {scored_entry.effective_score:.4f} "
                            f"fell below the retention threshold "
                            f"{self.min_effective_score:.4f}."
                        ),
                        candidate_score=scored_entry.effective_score,
                    )
                )
                continue

            selected_long_term.append(scored_entry)
            retained_for_dedup.append(scored_entry.entry)
            decisions.append(
                ContextAssemblyDecision(
                    source_id=scored_entry.entry.entry_id,
                    action=ContextDecisionAction.INCLUDED,
                    reason_codes=scored_entry.inclusion_reason_codes,
                    explanation=(
                        "Memory entry survived decay and relevance scoring for "
                        "long-term retention."
                    ),
                    candidate_score=scored_entry.effective_score,
                )
            )

        # The returned order is semantic priority order. The service layer consumes
        # this sequence directly when trimming against the memory-slot budget, so
        # the short-term keep window must remain first.
        selected_entries = tuple(recent_entries) + tuple(
            scored_entry.entry for scored_entry in selected_long_term
        )
        trace = ContextTrace(
            trace_id=trace_id,
            decisions=tuple(decisions),
            metadata={
                "memory_policy": "starter_memory_retention_policy",
                "input_entry_count": str(len(ordered_entries)),
                "selected_entry_count": str(len(selected_entries)),
                "recent_entry_count": str(len(recent_entries)),
                "retained_long_term_count": str(len(selected_long_term)),
                "deduplicated_entry_count": str(deduplicated_count),
                "rejected_entry_count": str(rejected_count),
                "query_present": str(bool(query)).lower(),
            },
        )
        return MemorySelectionOutcome(
            selected_entries=selected_entries,
            trace=trace,
        )


@dataclass(frozen=True, slots=True)
class _ScoredMemoryEntry:
    """Internal helper for starter long-term memory scoring."""

    entry: ContextMemoryEntry
    age_seconds: float
    decay_factor: float
    query_boost: float
    effective_score: float

    @classmethod
    def from_entry(
        cls,
        entry: ContextMemoryEntry,
        *,
        now_epoch_seconds: float,
        decay_rate: float,
        query: str,
        query_boost_weight: float,
    ) -> "_ScoredMemoryEntry":
        """Derive starter retention scoring metadata from a memory entry."""

        age_seconds = entry.age_seconds(now_epoch_seconds=now_epoch_seconds)
        decay_factor = math.exp(-decay_rate * age_seconds)
        query_boost = _relevance_boost(
            query,
            entry.source.content,
            weight=query_boost_weight,
        )
        effective_score = round((entry.importance * decay_factor) + query_boost, 4)
        return cls(
            entry=entry,
            age_seconds=age_seconds,
            decay_factor=decay_factor,
            query_boost=query_boost,
            effective_score=effective_score,
        )

    @property
    def inclusion_reason_codes(self) -> tuple[InclusionReasonCode, ...]:
        """Return structured inclusion reasons for a retained memory entry."""

        reason_codes: list[InclusionReasonCode] = [InclusionReasonCode.MEMORY_RETAINED]
        if self.query_boost > 0:
            reason_codes.append(InclusionReasonCode.QUERY_RELEVANCE)
        return tuple(reason_codes)


def _find_duplicate_entry(
    candidate: ContextMemoryEntry,
    retained_entries: Iterable[ContextMemoryEntry],
    *,
    threshold: float,
) -> ContextMemoryEntry | None:
    """Return the retained winner if the candidate duplicates prior memory."""

    candidate_content = candidate.source.content
    if not candidate_content:
        return None

    for retained_entry in retained_entries:
        if _is_duplicate_content(
            candidate_content,
            retained_entry.source.content,
            threshold=threshold,
        ):
            return retained_entry
    return None


def _is_duplicate_content(content_a: str, content_b: str, *, threshold: float) -> bool:
    """Apply starter duplicate detection inspired by context-engine memory."""

    normalized_a = content_a.strip().lower()
    normalized_b = content_b.strip().lower()
    if not normalized_a or not normalized_b:
        return False
    if normalized_a in normalized_b or normalized_b in normalized_a:
        return True

    half = len(normalized_a) // 2
    if len(normalized_a) > 10 and len(normalized_b) >= half and half > 0:
        if normalized_a[:half] == normalized_b[:half]:
            return True

    tokens_a = set(normalized_a.split())
    tokens_b = set(normalized_b.split())
    union_size = len(tokens_a | tokens_b)
    if union_size == 0:
        return False
    jaccard = len(tokens_a & tokens_b) / union_size
    return jaccard >= threshold


def _relevance_boost(query: str, content: str, *, weight: float) -> float:
    """Return a small query-overlap boost for long-term memory retention."""

    query_tokens = set(query.lower().split())
    content_tokens = set(content.lower().split())
    if not query_tokens or not content_tokens:
        return 0.0
    return (len(query_tokens & content_tokens) / len(query_tokens)) * weight


__all__ = [
    "MemoryRetentionPolicy",
    "MemorySelectionOutcome",
    "StarterMemoryRetentionPolicy",
]
