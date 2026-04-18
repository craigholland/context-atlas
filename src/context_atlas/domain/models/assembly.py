"""Canonical assembly decision, trace, and packet artifacts."""

from __future__ import annotations

import math
from enum import StrEnum

from pydantic import Field

from ..errors import ContextAtlasError, ErrorCode
from ..messages import ErrorMessage
from .base import CanonicalDomainModel
from .budget import ContextBudget
from .memory import ContextMemoryEntry
from .reason_codes import (
    AuthorityPrecedenceReasonCode,
    BudgetPressureReasonCode,
    ExclusionReasonCode,
    InclusionReasonCode,
)
from .sources import ContextCandidate
from .transformations import CompressionResult

ContextReasonCode = (
    InclusionReasonCode
    | ExclusionReasonCode
    | BudgetPressureReasonCode
    | AuthorityPrecedenceReasonCode
)


class ContextDecisionAction(StrEnum):
    """High-level action taken during packet assembly."""

    INCLUDED = "included"
    EXCLUDED = "excluded"
    TRANSFORMED = "transformed"
    DEFERRED = "deferred"


class ContextAssemblyDecision(CanonicalDomainModel):
    """Structured inclusion, exclusion, or transformation decision."""

    source_id: str
    action: ContextDecisionAction
    reason_codes: tuple[ContextReasonCode, ...]
    explanation: str | None = None
    candidate_score: float | None = None
    position: int | None = None

    def model_post_init(self, __context: object) -> None:
        normalized_source_id = self.source_id.strip()
        if not normalized_source_id:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_DECISION,
                message_args=(ErrorMessage.ASSEMBLY_DECISION_SOURCE_ID_REQUIRED,),
            )
        if not self.reason_codes:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_DECISION,
                message_args=(ErrorMessage.ASSEMBLY_DECISION_REASON_CODES_REQUIRED,),
            )
        if self.candidate_score is not None and not math.isfinite(self.candidate_score):
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_DECISION,
                message_args=(
                    ErrorMessage.CANDIDATE_SCORE_MUST_BE_FINITE_WHEN_PROVIDED,
                ),
            )
        if self.position is not None and self.position < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_DECISION,
                message_args=(
                    ErrorMessage.POSITION_MUST_BE_AT_LEAST_ONE_WHEN_PROVIDED,
                ),
            )

        object.__setattr__(self, "source_id", normalized_source_id)
        object.__setattr__(self, "reason_codes", tuple(self.reason_codes))
        if self.explanation is not None:
            object.__setattr__(self, "explanation", self.explanation.strip() or None)


class ContextTrace(CanonicalDomainModel):
    """Canonical trace for a packet assembly attempt."""

    trace_id: str
    decisions: tuple[ContextAssemblyDecision, ...] = ()
    metadata: dict[str, str] = Field(default_factory=dict)

    def model_post_init(self, __context: object) -> None:
        normalized_trace_id = self.trace_id.strip()
        if not normalized_trace_id:
            raise ContextAtlasError(code=ErrorCode.INVALID_TRACE_IDENTIFIER)

        object.__setattr__(self, "trace_id", normalized_trace_id)
        object.__setattr__(self, "metadata", self.freeze_metadata(self.metadata))


class ContextPacket(CanonicalDomainModel):
    """Canonical structured packet artifact produced by assembly."""

    packet_id: str
    query: str
    selected_candidates: tuple[ContextCandidate, ...] = ()
    selected_memory_entries: tuple[ContextMemoryEntry, ...] = ()
    budget: ContextBudget | None = None
    trace: ContextTrace | None = None
    compression_result: CompressionResult | None = None
    metadata: dict[str, str] = Field(default_factory=dict)

    def model_post_init(self, __context: object) -> None:
        normalized_packet_id = self.packet_id.strip()
        if not normalized_packet_id:
            raise ContextAtlasError(code=ErrorCode.INVALID_PACKET_IDENTIFIER)

        normalized_query = self.query.strip()
        if not normalized_query:
            raise ContextAtlasError(code=ErrorCode.EMPTY_PACKET_QUERY)

        object.__setattr__(self, "packet_id", normalized_packet_id)
        object.__setattr__(self, "query", normalized_query)
        object.__setattr__(self, "metadata", self.freeze_metadata(self.metadata))

    @property
    def item_count(self) -> int:
        """Return the number of canonical items included in the packet."""

        return len(self.selected_candidates) + len(self.selected_memory_entries)


__all__ = [
    "ContextAssemblyDecision",
    "ContextDecisionAction",
    "ContextPacket",
    "ContextTrace",
]
