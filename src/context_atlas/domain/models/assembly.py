"""Canonical assembly decision, trace, and packet artifacts."""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import StrEnum
from types import MappingProxyType
from typing import Mapping

from ..errors import ContextAtlasError, ErrorCode
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


def _freeze_mapping(raw_mapping: Mapping[str, str]) -> Mapping[str, str]:
    """Return an immutable copy of a string-keyed mapping."""

    return MappingProxyType(dict(raw_mapping))


@dataclass(frozen=True, slots=True)
class ContextAssemblyDecision:
    """Structured inclusion, exclusion, or transformation decision."""

    source_id: str
    action: ContextDecisionAction
    reason_codes: tuple[ContextReasonCode, ...]
    explanation: str | None = None
    candidate_score: float | None = None
    position: int | None = None

    def __post_init__(self) -> None:
        normalized_source_id = self.source_id.strip()
        if not normalized_source_id:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_DECISION,
                message_args=("source_id must not be empty",),
            )
        if not self.reason_codes:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_DECISION,
                message_args=("at least one reason code is required",),
            )
        if self.candidate_score is not None and not math.isfinite(self.candidate_score):
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_DECISION,
                message_args=("candidate_score must be finite when provided",),
            )
        if self.position is not None and self.position < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_DECISION,
                message_args=("position must be >= 1 when provided",),
            )

        object.__setattr__(self, "source_id", normalized_source_id)
        object.__setattr__(self, "reason_codes", tuple(self.reason_codes))
        if self.explanation is not None:
            object.__setattr__(self, "explanation", self.explanation.strip() or None)


@dataclass(frozen=True, slots=True)
class ContextTrace:
    """Canonical trace for a packet assembly attempt."""

    trace_id: str
    decisions: tuple[ContextAssemblyDecision, ...] = ()
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        normalized_trace_id = self.trace_id.strip()
        if not normalized_trace_id:
            raise ContextAtlasError(code=ErrorCode.INVALID_TRACE_IDENTIFIER)

        object.__setattr__(self, "trace_id", normalized_trace_id)
        object.__setattr__(self, "decisions", tuple(self.decisions))
        object.__setattr__(self, "metadata", _freeze_mapping(self.metadata))


@dataclass(frozen=True, slots=True)
class ContextPacket:
    """Canonical structured packet artifact produced by assembly."""

    packet_id: str
    query: str
    selected_candidates: tuple[ContextCandidate, ...] = ()
    selected_memory_entries: tuple[ContextMemoryEntry, ...] = ()
    budget: ContextBudget | None = None
    trace: ContextTrace | None = None
    compression_result: CompressionResult | None = None
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        normalized_packet_id = self.packet_id.strip()
        if not normalized_packet_id:
            raise ContextAtlasError(code=ErrorCode.INVALID_PACKET_IDENTIFIER)

        normalized_query = self.query.strip()
        if not normalized_query:
            raise ContextAtlasError(code=ErrorCode.EMPTY_PACKET_QUERY)

        object.__setattr__(self, "packet_id", normalized_packet_id)
        object.__setattr__(self, "query", normalized_query)
        object.__setattr__(self, "selected_candidates", tuple(self.selected_candidates))
        object.__setattr__(
            self,
            "selected_memory_entries",
            tuple(self.selected_memory_entries),
        )
        object.__setattr__(self, "metadata", _freeze_mapping(self.metadata))

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
