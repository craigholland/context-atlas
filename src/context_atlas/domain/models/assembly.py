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

    @property
    def decision_count(self) -> int:
        """Return the number of recorded assembly decisions."""

        return len(self.decisions)

    @property
    def included_decisions(self) -> tuple[ContextAssemblyDecision, ...]:
        """Return decisions that included content in the packet."""

        return self._decisions_for_action(ContextDecisionAction.INCLUDED)

    @property
    def excluded_decisions(self) -> tuple[ContextAssemblyDecision, ...]:
        """Return decisions that excluded content from the packet."""

        return self._decisions_for_action(ContextDecisionAction.EXCLUDED)

    @property
    def transformed_decisions(self) -> tuple[ContextAssemblyDecision, ...]:
        """Return decisions that transformed content during assembly."""

        return self._decisions_for_action(ContextDecisionAction.TRANSFORMED)

    @property
    def deferred_decisions(self) -> tuple[ContextAssemblyDecision, ...]:
        """Return decisions that deferred content for later handling."""

        return self._decisions_for_action(ContextDecisionAction.DEFERRED)

    def _decisions_for_action(
        self,
        action: ContextDecisionAction,
    ) -> tuple[ContextAssemblyDecision, ...]:
        """Filter decisions by high-level action without mutating trace state."""

        return tuple(
            decision for decision in self.decisions if decision.action == action
        )


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

    @property
    def selected_candidate_count(self) -> int:
        """Return the number of selected source candidates."""

        return len(self.selected_candidates)

    @property
    def selected_memory_count(self) -> int:
        """Return the number of selected retained-memory entries."""

        return len(self.selected_memory_entries)

    @property
    def selected_source_ids(self) -> tuple[str, ...]:
        """Return selected source identifiers in packet order."""

        return tuple(
            candidate.source.source_id for candidate in self.selected_candidates
        )

    @property
    def selected_memory_entry_ids(self) -> tuple[str, ...]:
        """Return selected memory entry identifiers in packet order."""

        return tuple(entry.entry_id for entry in self.selected_memory_entries)

    @property
    def has_compression(self) -> bool:
        """Return whether the packet includes a structured compression result."""

        return self.compression_result is not None

    @property
    def has_budget(self) -> bool:
        """Return whether the packet carries canonical budget state."""

        return self.budget is not None

    @property
    def has_trace(self) -> bool:
        """Return whether the packet carries canonical trace state."""

        return self.trace is not None


__all__ = [
    "ContextAssemblyDecision",
    "ContextDecisionAction",
    "ContextPacket",
    "ContextTrace",
]
