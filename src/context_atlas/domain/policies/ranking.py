"""Candidate ranking, deduplication, and decision-trace policies."""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable, Protocol

from ..errors import ContextAtlasError, ErrorCode
from ..models.base import CanonicalDomainModel
from ..models import (
    AuthorityPrecedenceReasonCode,
    ContextAssemblyDecision,
    ContextCandidate,
    ContextDecisionAction,
    ContextSourceAuthority,
    ContextTrace,
    ExclusionReasonCode,
    InclusionReasonCode,
)

_DEFAULT_MINIMUM_SCORE = 0.0
_AUTHORITY_BONUS_BY_LEVEL: dict[ContextSourceAuthority, float] = {
    ContextSourceAuthority.BINDING: 0.12,
    ContextSourceAuthority.PREFERRED: 0.06,
    ContextSourceAuthority.ADVISORY: 0.0,
    ContextSourceAuthority.SPECULATIVE: -0.04,
    ContextSourceAuthority.HISTORICAL: -0.08,
}
_AUTHORITY_ORDER: dict[ContextSourceAuthority, int] = {
    ContextSourceAuthority.BINDING: 5,
    ContextSourceAuthority.PREFERRED: 4,
    ContextSourceAuthority.ADVISORY: 3,
    ContextSourceAuthority.SPECULATIVE: 2,
    ContextSourceAuthority.HISTORICAL: 1,
}
_RANKED_SIGNAL = "ranked_starter_policy"


class CandidateRankingPolicy(Protocol):
    """Contract for deterministic candidate ranking and trace generation."""

    def rank_candidates(
        self,
        candidates: Iterable[ContextCandidate],
        *,
        trace_id: str,
        limit: int | None = None,
    ) -> "CandidateRankingOutcome":
        """Return ranked candidates plus a structured decision trace."""


class CandidateRankingOutcome(CanonicalDomainModel):
    """Structured output of a ranking policy invocation."""

    ranked_candidates: tuple[ContextCandidate, ...]
    trace: ContextTrace

    @property
    def included_count(self) -> int:
        """Return the number of included/ranked candidates."""

        return len(self.ranked_candidates)


class StarterCandidateRankingPolicy(CanonicalDomainModel):
    """Starter ranking policy combining candidate score and authority priority."""

    minimum_score: float = _DEFAULT_MINIMUM_SCORE
    deduplicate_by_content: bool = True

    def model_post_init(self, __context: object) -> None:
        if not math.isfinite(self.minimum_score):
            raise ContextAtlasError(
                code=ErrorCode.INVALID_RANKING_REQUEST,
                message_args=("minimum_score must be finite",),
            )

    def rank_candidates(
        self,
        candidates: Iterable[ContextCandidate],
        *,
        trace_id: str,
        limit: int | None = None,
    ) -> CandidateRankingOutcome:
        """Apply starter ranking, dedupe, and decision recording to candidates."""

        if limit is not None and limit < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_RANKING_REQUEST,
                message_args=(f"limit must be >= 1, got {limit}",),
            )

        ranked_input = sorted(
            (_RankableCandidate.from_candidate(candidate) for candidate in candidates),
            key=lambda item: item.sort_key,
        )

        retained_by_source_id: dict[str, _RankableCandidate] = {}
        retained_by_content_key: dict[str, _RankableCandidate] = {}
        included_candidates: list[ContextCandidate] = []
        decisions: list[ContextAssemblyDecision] = []
        deduplicated_count = 0

        for rankable_candidate in ranked_input:
            duplicate_of = self._find_duplicate(
                rankable_candidate,
                retained_by_source_id=retained_by_source_id,
                retained_by_content_key=retained_by_content_key,
            )
            if duplicate_of is not None:
                deduplicated_count += 1
                decisions.append(
                    self._build_duplicate_decision(
                        rankable_candidate,
                        duplicate_of=duplicate_of,
                    )
                )
                continue

            if rankable_candidate.ranking_score < self.minimum_score:
                decisions.append(
                    ContextAssemblyDecision(
                        source_id=rankable_candidate.source_id,
                        action=ContextDecisionAction.EXCLUDED,
                        reason_codes=(ExclusionReasonCode.BELOW_THRESHOLD,),
                        explanation=(
                            "Candidate score fell below the configured ranking threshold."
                        ),
                        candidate_score=rankable_candidate.ranking_score,
                    )
                )
                continue

            if limit is not None and len(included_candidates) >= limit:
                decisions.append(
                    ContextAssemblyDecision(
                        source_id=rankable_candidate.source_id,
                        action=ContextDecisionAction.EXCLUDED,
                        reason_codes=(ExclusionReasonCode.BELOW_THRESHOLD,),
                        explanation="Candidate ranked below the requested limit.",
                        candidate_score=rankable_candidate.ranking_score,
                    )
                )
                continue

            retained_by_source_id[rankable_candidate.source_id] = rankable_candidate
            retained_by_content_key[rankable_candidate.content_key] = rankable_candidate

            included_candidate = rankable_candidate.to_ranked_candidate(
                rank=len(included_candidates) + 1
            )
            included_candidates.append(included_candidate)
            decisions.append(
                ContextAssemblyDecision(
                    source_id=included_candidate.source.source_id,
                    action=ContextDecisionAction.INCLUDED,
                    reason_codes=rankable_candidate.include_reason_codes,
                    candidate_score=included_candidate.score,
                    position=included_candidate.rank,
                )
            )

        trace = ContextTrace(
            trace_id=trace_id,
            decisions=tuple(decisions),
            metadata={
                "ranking_policy": "starter_candidate_ranking_policy",
                "input_candidate_count": str(len(ranked_input)),
                "included_candidate_count": str(len(included_candidates)),
                "excluded_candidate_count": str(
                    len(decisions) - len(included_candidates)
                ),
                "deduplicated_candidate_count": str(deduplicated_count),
            },
        )
        return CandidateRankingOutcome(
            ranked_candidates=tuple(included_candidates),
            trace=trace,
        )

    def _find_duplicate(
        self,
        candidate: "_RankableCandidate",
        *,
        retained_by_source_id: dict[str, "_RankableCandidate"],
        retained_by_content_key: dict[str, "_RankableCandidate"],
    ) -> "_RankableCandidate | None":
        """Return the retained winner if a duplicate candidate has already been kept."""

        retained = retained_by_source_id.get(candidate.source_id)
        if retained is not None:
            return retained
        if self.deduplicate_by_content:
            return retained_by_content_key.get(candidate.content_key)
        return None

    def _build_duplicate_decision(
        self,
        candidate: "_RankableCandidate",
        *,
        duplicate_of: "_RankableCandidate",
    ) -> ContextAssemblyDecision:
        """Build an exclusion decision for a deduplicated candidate."""

        reason_codes: list[ExclusionReasonCode | AuthorityPrecedenceReasonCode] = [
            ExclusionReasonCode.DUPLICATE
        ]
        if candidate.authority_order < duplicate_of.authority_order:
            reason_codes.append(AuthorityPrecedenceReasonCode.LOWER_AUTHORITY_DEMOTED)
        explanation = (
            f"Duplicate candidate was removed in favor of '{duplicate_of.source_id}'."
        )
        return ContextAssemblyDecision(
            source_id=candidate.source_id,
            action=ContextDecisionAction.EXCLUDED,
            reason_codes=tuple(reason_codes),
            explanation=explanation,
            candidate_score=candidate.ranking_score,
        )


@dataclass(frozen=True, slots=True)
class _RankableCandidate:
    """Internal helper carrying ranking and dedupe metadata."""

    candidate: ContextCandidate
    base_score: float
    authority_bonus: float
    ranking_score: float
    source_id: str
    content_key: str
    authority_order: int

    @classmethod
    def from_candidate(cls, candidate: ContextCandidate) -> "_RankableCandidate":
        """Construct rankable metadata from a canonical candidate artifact."""

        base_score = candidate.score or 0.0
        authority = candidate.source.authority
        authority_bonus = _AUTHORITY_BONUS_BY_LEVEL[authority]
        ranking_score = round(base_score + authority_bonus, 4)
        return cls(
            candidate=candidate,
            base_score=base_score,
            authority_bonus=authority_bonus,
            ranking_score=ranking_score,
            source_id=candidate.source.source_id,
            content_key=candidate.source.content.casefold(),
            authority_order=_AUTHORITY_ORDER[authority],
        )

    @property
    def sort_key(self) -> tuple[float, int, str]:
        """Stable descending ranking key with deterministic tie-breaking."""

        return (-self.ranking_score, -self.authority_order, self.source_id)

    @property
    def include_reason_codes(
        self,
    ) -> tuple[InclusionReasonCode | AuthorityPrecedenceReasonCode, ...]:
        """Return structured reasons for why this candidate was kept."""

        reason_codes: list[InclusionReasonCode | AuthorityPrecedenceReasonCode] = [
            InclusionReasonCode.DIRECT_MATCH
        ]
        if self.authority_bonus > 0.0:
            reason_codes.append(
                AuthorityPrecedenceReasonCode.HIGHER_AUTHORITY_PREFERRED
            )
            reason_codes.append(InclusionReasonCode.AUTHORITY_PRIORITY)
        return tuple(reason_codes)

    def to_ranked_candidate(self, *, rank: int) -> ContextCandidate:
        """Create a canonical ranked candidate with ranking metadata attached."""

        signals = tuple(dict.fromkeys((*self.candidate.signals, _RANKED_SIGNAL)))
        metadata = dict(self.candidate.metadata)
        metadata.update(
            {
                "base_score": f"{self.base_score:.4f}",
                "authority_bonus": f"{self.authority_bonus:.4f}",
                "ranking_score": f"{self.ranking_score:.4f}",
            }
        )
        return ContextCandidate(
            source=self.candidate.source,
            score=self.ranking_score,
            rank=rank,
            signals=signals,
            metadata=metadata,
        )
