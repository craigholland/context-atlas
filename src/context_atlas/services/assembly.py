"""Service-layer orchestration for end-to-end context assembly."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
import math
import logging
from typing import Protocol
from uuid import uuid4

from ..domain.errors import ContextAtlasError, ErrorCode
from ..domain.messages import ErrorMessage, LogMessage
from ..domain.models import (
    BudgetPressureReasonCode,
    CompressionResult,
    CompressionStrategy,
    ContextAssemblyDecision,
    ContextBudget,
    ContextBudgetSlot,
    ContextBudgetSlotMode,
    ContextCandidate,
    ContextDecisionAction,
    ContextMemoryEntry,
    ContextPacket,
    ContextTrace,
    ExclusionReasonCode,
)
from ..domain.policies import (
    BudgetAllocationOutcome,
    BudgetRequest,
    CandidateRankingOutcome,
    CandidateRankingPolicy,
    CompressionOutcome,
    CompressionPolicy,
    ContextBudgetAllocationPolicy,
    MemoryRetentionPolicy,
    MemorySelectionOutcome,
)
from ..domain.policies.compression import estimate_tokens

_DOCUMENT_SLOT_NAME = "documents"
_MEMORY_SLOT_NAME = "memory"


class CandidateRetriever(Protocol):
    """Inward-safe contract for producing raw candidates from a query."""

    def retrieve(self, query: str, *, top_k: int = 5) -> tuple[ContextCandidate, ...]:
        """Return candidate sources for a query."""


class ContextAssemblyService:
    """Compose retrieval, ranking, budgeting, memory, and compression into a packet.

    Outer workflows should share this service path rather than re-implementing
    stage sequencing in example scripts or provider-specific adapters.
    """

    def __init__(
        self,
        *,
        retriever: CandidateRetriever,
        ranking_policy: CandidateRankingPolicy,
        budget_policy: ContextBudgetAllocationPolicy,
        compression_policy: CompressionPolicy,
        memory_policy: MemoryRetentionPolicy | None = None,
        logger: logging.Logger | None = None,
        default_top_k: int = 5,
        default_total_budget: int = 2048,
        default_memory_budget_fraction: float = 0.25,
    ) -> None:
        if default_top_k < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_REQUEST,
                message_args=(ErrorMessage.DEFAULT_TOP_K_MUST_BE_AT_LEAST_ONE,),
            )
        if default_total_budget < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_REQUEST,
                message_args=(ErrorMessage.DEFAULT_TOTAL_BUDGET_MUST_BE_AT_LEAST_ONE,),
            )
        if not math.isfinite(default_memory_budget_fraction) or not (
            0.0 < default_memory_budget_fraction < 1.0
        ):
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_REQUEST,
                message_args=(
                    ErrorMessage.DEFAULT_MEMORY_BUDGET_FRACTION_MUST_BE_IN_UNIT_INTERVAL,
                ),
            )

        self._retriever = retriever
        self._ranking_policy = ranking_policy
        self._budget_policy = budget_policy
        self._compression_policy = compression_policy
        self._memory_policy = memory_policy
        self._logger = logger or logging.getLogger(__name__)
        self._default_top_k = default_top_k
        self._default_total_budget = default_total_budget
        self._default_memory_budget_fraction = default_memory_budget_fraction

    def assemble(
        self,
        *,
        query: str,
        budget: ContextBudget | None = None,
        memory_entries: Iterable[ContextMemoryEntry] = (),
        top_k: int | None = None,
        packet_id: str | None = None,
        trace_id: str | None = None,
        metadata: Mapping[str, object] | None = None,
        now_epoch_seconds: float | None = None,
    ) -> ContextPacket:
        """Build a canonical packet from candidates, memory, budget, and trace state.

        ``metadata`` is preserved as opaque outer-workflow context for packet
        and trace inspection. The service does not interpret those keys as
        ranking, budgeting, memory, or compression policy input. That is
        especially important for mixed-source workflows: the service consumes
        canonical candidates and sources, not database, vector-store, or
        repository-specific semantics.
        """

        normalized_query = query.strip()
        if not normalized_query:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_REQUEST,
                message_args=(ErrorMessage.QUERY_MUST_NOT_BE_EMPTY,),
            )

        active_top_k = self._default_top_k if top_k is None else top_k
        if active_top_k < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_REQUEST,
                message_args=(
                    ErrorMessage.TOP_K_MUST_BE_AT_LEAST_ONE % (active_top_k,),
                ),
            )

        active_trace_id = (
            self._normalize_optional_identifier(
                trace_id,
                field_name="trace_id",
            )
            or f"trace_{uuid4().hex}"
        )
        active_packet_id = (
            self._normalize_optional_identifier(
                packet_id,
                field_name="packet_id",
            )
            or f"packet_{uuid4().hex}"
        )

        selected_memory_input = tuple(memory_entries)
        active_budget = self._resolve_budget(
            budget,
            include_memory=bool(selected_memory_input),
        )
        request_metadata = self._copy_request_metadata(metadata)
        packet_metadata = dict(request_metadata)

        self._emit_log_message(
            LogMessage.ASSEMBLY_STARTED,
            active_trace_id,
            normalized_query,
            trace_id=active_trace_id,
            query=normalized_query,
            top_k=active_top_k,
        )

        try:
            gathered_candidates = self._retriever.retrieve(
                normalized_query,
                top_k=active_top_k,
            )
            self._emit_log_message(
                LogMessage.CANDIDATES_GATHERED,
                active_trace_id,
                len(gathered_candidates),
                trace_id=active_trace_id,
                candidate_count=len(gathered_candidates),
            )

            ranking_outcome = self._ranking_policy.rank_candidates(
                gathered_candidates,
                trace_id=active_trace_id,
                limit=active_top_k,
            )
            self._emit_log_message(
                LogMessage.CANDIDATES_RANKED,
                active_trace_id,
                ranking_outcome.included_count,
                trace_id=active_trace_id,
                candidate_count=ranking_outcome.included_count,
            )

            memory_outcome = self._select_memory(
                selected_memory_input,
                trace_id=active_trace_id,
                query=normalized_query,
                now_epoch_seconds=now_epoch_seconds,
            )
            self._emit_log_message(
                LogMessage.MEMORY_SELECTED,
                active_trace_id,
                memory_outcome.selected_count,
                trace_id=active_trace_id,
                memory_entries=memory_outcome.selected_count,
            )

            budget_outcome = self._budget_policy.allocate_budget(
                active_budget,
                requests=self._build_budget_requests(
                    budget=active_budget,
                    ranked_candidates=ranking_outcome.ranked_candidates,
                    memory_entries=memory_outcome.selected_entries,
                ),
                trace_id=active_trace_id,
            )
            self._emit_log_message(
                LogMessage.BUDGET_ALLOCATED,
                active_trace_id,
                active_budget.total_tokens,
                budget_outcome.remaining_tokens,
                trace_id=active_trace_id,
                total_tokens=active_budget.total_tokens,
                remaining_tokens=budget_outcome.remaining_tokens,
            )

            memory_budget_tokens = self._allocated_tokens(
                budget_outcome,
                slot_name=_MEMORY_SLOT_NAME,
            )
            selected_memory_entries, memory_budget_decisions = (
                self._select_memory_within_budget(
                    memory_outcome.selected_entries,
                    max_tokens=memory_budget_tokens,
                )
            )
            for decision in memory_budget_decisions:
                self._emit_log_message(
                    LogMessage.MEMORY_REJECTED,
                    active_trace_id,
                    decision.source_id,
                    ",".join(reason.value for reason in decision.reason_codes),
                    trace_id=active_trace_id,
                    source_id=decision.source_id,
                    reason_codes=",".join(
                        reason.value for reason in decision.reason_codes
                    ),
                )

            document_budget_tokens = self._allocated_tokens(
                budget_outcome,
                slot_name=_DOCUMENT_SLOT_NAME,
            )
            compression_outcome = self._compress_candidates(
                ranking_outcome.ranked_candidates,
                trace_id=active_trace_id,
                max_tokens=document_budget_tokens,
                query=normalized_query,
            )
            if compression_outcome is not None:
                self._emit_log_message(
                    LogMessage.COMPRESSION_APPLIED,
                    active_trace_id,
                    compression_outcome.compression_result.strategy_used.value,
                    compression_outcome.compression_result.original_chars,
                    compression_outcome.compression_result.compressed_chars,
                    trace_id=active_trace_id,
                    strategy=compression_outcome.compression_result.strategy_used,
                    original_chars=compression_outcome.compression_result.original_chars,
                    compressed_chars=compression_outcome.compression_result.compressed_chars,
                )

            compression_applied = (
                compression_outcome is not None
                and compression_outcome.compression_result.was_applied
            )

            trace = ContextTrace(
                trace_id=active_trace_id,
                decisions=self._with_decision_positions(
                    ranking_outcome.trace.decisions
                    + memory_outcome.trace.decisions
                    + budget_outcome.trace.decisions
                    + tuple(memory_budget_decisions)
                    + (
                        ()
                        if compression_outcome is None
                        else compression_outcome.trace.decisions
                    )
                ),
                metadata=self._build_trace_metadata(
                    request_metadata=request_metadata,
                    retrieved_candidate_count=len(gathered_candidates),
                    ranked_candidate_count=ranking_outcome.included_count,
                    selected_memory_count=len(selected_memory_entries),
                    selected_candidates=ranking_outcome.ranked_candidates,
                    selected_memory_entries=selected_memory_entries,
                    budget=active_budget,
                    ranking_outcome=ranking_outcome,
                    memory_outcome=memory_outcome,
                    budget_outcome=budget_outcome,
                    compression_outcome=compression_outcome,
                    compression_applied=compression_applied,
                ),
            )

            packet_metadata.update(
                {
                    "retrieved_candidate_count": str(len(gathered_candidates)),
                    "ranked_candidate_count": str(ranking_outcome.included_count),
                    "selected_memory_count": str(len(selected_memory_entries)),
                    "document_budget_tokens": str(document_budget_tokens),
                    "memory_budget_tokens": str(memory_budget_tokens),
                    "compression_applied": str(compression_applied).lower(),
                }
            )

            packet = ContextPacket(
                packet_id=active_packet_id,
                query=normalized_query,
                selected_candidates=ranking_outcome.ranked_candidates,
                selected_memory_entries=selected_memory_entries,
                budget=active_budget,
                trace=trace,
                compression_result=(
                    None
                    if compression_outcome is None
                    else compression_outcome.compression_result
                ),
                metadata=packet_metadata,
            )

            self._emit_log_message(
                LogMessage.DECISIONS_RECORDED,
                active_trace_id,
                len(trace.decisions),
                trace_id=active_trace_id,
                decision_count=len(trace.decisions),
            )
            self._emit_log_message(
                LogMessage.PACKET_CREATED,
                packet.packet_id,
                len(packet.selected_candidates),
                packet_id=packet.packet_id,
                selected_candidates=len(packet.selected_candidates),
            )
            self._emit_log_message(
                LogMessage.PACKET_ASSEMBLED,
                packet.packet_id,
                packet.item_count,
                packet_id=packet.packet_id,
                item_count=packet.item_count,
            )
            self._emit_log_message(
                LogMessage.ASSEMBLY_COMPLETED,
                active_trace_id,
                len(packet.selected_candidates),
                trace_id=active_trace_id,
                selected_candidates=len(packet.selected_candidates),
                selected_memory_entries=len(packet.selected_memory_entries),
            )
            return packet
        except Exception as error:
            self._emit_log_message(
                LogMessage.ASSEMBLY_FAILED,
                active_trace_id,
                str(error),
                trace_id=active_trace_id,
                error_type=type(error).__name__,
            )
            raise

    def _resolve_budget(
        self,
        budget: ContextBudget | None,
        *,
        include_memory: bool,
    ) -> ContextBudget:
        """Return a budget that contains the slots expected by the starter service."""

        if budget is None or not budget.slots:
            total_tokens = (
                self._default_total_budget if budget is None else budget.total_tokens
            )
            return self._build_default_budget(total_tokens=total_tokens)

        slot_names = {slot.slot_name for slot in budget.slots}
        if _DOCUMENT_SLOT_NAME not in slot_names:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_REQUEST,
                message_args=(ErrorMessage.CUSTOM_BUDGET_REQUIRES_DOCUMENTS_SLOT,),
            )
        if include_memory and _MEMORY_SLOT_NAME not in slot_names:
            return ContextBudget(
                total_tokens=budget.total_tokens,
                slots=budget.slots
                + (
                    ContextBudgetSlot(
                        slot_name=_MEMORY_SLOT_NAME,
                        token_limit=self._memory_budget_tokens(
                            total_tokens=budget.total_tokens
                        ),
                        mode=ContextBudgetSlotMode.FIXED,
                        priority=0,
                    ),
                ),
                metadata=dict(budget.metadata) | {"budget_augmented": "true"},
            )
        return budget

    def _build_default_budget(self, *, total_tokens: int) -> ContextBudget:
        """Create the starter service budget when callers do not provide one."""

        memory_tokens = self._memory_budget_tokens(total_tokens=total_tokens)
        return ContextBudget(
            total_tokens=total_tokens,
            slots=(
                ContextBudgetSlot(
                    slot_name=_MEMORY_SLOT_NAME,
                    token_limit=memory_tokens,
                    mode=ContextBudgetSlotMode.FIXED,
                    priority=0,
                ),
                ContextBudgetSlot(
                    slot_name=_DOCUMENT_SLOT_NAME,
                    token_limit=total_tokens,
                    mode=ContextBudgetSlotMode.ELASTIC,
                    priority=10,
                ),
            ),
            metadata={"budget_profile": "starter_context_assembly_service"},
        )

    def _memory_budget_tokens(self, *, total_tokens: int) -> int:
        """Return starter memory-slot tokens from the configured budget split."""

        return min(
            total_tokens,
            max(1, int(total_tokens * self._default_memory_budget_fraction)),
        )

    def _select_memory(
        self,
        memory_entries: tuple[ContextMemoryEntry, ...],
        *,
        trace_id: str,
        query: str,
        now_epoch_seconds: float | None,
    ) -> MemorySelectionOutcome:
        """Run memory selection only when both entries and a memory policy exist."""

        if not memory_entries or self._memory_policy is None:
            return MemorySelectionOutcome(
                selected_entries=(),
                trace=ContextTrace(
                    trace_id=trace_id,
                    metadata={
                        "memory_policy": (
                            "disabled"
                            if self._memory_policy is None
                            else "starter_memory_retention_policy"
                        ),
                        "input_entry_count": str(len(memory_entries)),
                        "selected_entry_count": "0",
                    },
                ),
            )

        return self._memory_policy.select_memory(
            memory_entries,
            trace_id=trace_id,
            query=query,
            now_epoch_seconds=now_epoch_seconds,
        )

    def _build_budget_requests(
        self,
        *,
        budget: ContextBudget,
        ranked_candidates: tuple[ContextCandidate, ...],
        memory_entries: tuple[ContextMemoryEntry, ...],
    ) -> tuple[BudgetRequest, ...]:
        """Translate ranked content and retained memory into slot token requests."""

        slot_names = {slot.slot_name for slot in budget.slots}
        requests: list[BudgetRequest] = []

        if _DOCUMENT_SLOT_NAME in slot_names:
            document_text = "\n\n".join(
                candidate.source.content for candidate in ranked_candidates
            )
            requests.append(
                BudgetRequest(
                    slot_name=_DOCUMENT_SLOT_NAME,
                    requested_tokens=estimate_tokens(document_text),
                )
            )

        if _MEMORY_SLOT_NAME in slot_names:
            memory_text = "\n\n".join(entry.source.content for entry in memory_entries)
            requests.append(
                BudgetRequest(
                    slot_name=_MEMORY_SLOT_NAME,
                    requested_tokens=estimate_tokens(memory_text),
                )
            )

        return tuple(requests)

    def _select_memory_within_budget(
        self,
        selected_entries: tuple[ContextMemoryEntry, ...],
        *,
        max_tokens: int,
    ) -> tuple[tuple[ContextMemoryEntry, ...], tuple[ContextAssemblyDecision, ...]]:
        """Trim retained memory entries to the available memory-slot budget.

        The incoming order is significant: domain memory-selection policies return
        retained entries in priority order, so this pass should preserve that order
        rather than re-ranking memory locally.
        """

        if not selected_entries:
            return (), ()

        kept_entries: list[ContextMemoryEntry] = []
        decisions: list[ContextAssemblyDecision] = []
        used_tokens = 0

        for entry in selected_entries:
            entry_tokens = estimate_tokens(entry.source.content)
            if entry_tokens == 0:
                kept_entries.append(entry)
                continue

            if used_tokens + entry_tokens <= max_tokens:
                kept_entries.append(entry)
                used_tokens += entry_tokens
                continue

            decisions.append(
                ContextAssemblyDecision(
                    source_id=entry.entry_id,
                    action=ContextDecisionAction.EXCLUDED,
                    reason_codes=(ExclusionReasonCode.OUT_OF_BUDGET,),
                    explanation=(
                        "Memory entry was selected by the retention policy but did not "
                        "fit in the memory-slot budget."
                    ),
                    candidate_score=entry.importance,
                )
            )

        return tuple(kept_entries), tuple(decisions)

    def _compress_candidates(
        self,
        candidates: tuple[ContextCandidate, ...],
        *,
        trace_id: str,
        max_tokens: int,
        query: str,
    ) -> CompressionOutcome | None:
        """Compress ranked candidate content when there is candidate content to include."""

        if not candidates:
            return None

        if max_tokens < 1:
            original_text = "\n\n".join(
                candidate.source.content for candidate in candidates
            )
            return CompressionOutcome(
                compression_result=CompressionResult(
                    text="",
                    strategy_used=getattr(
                        self._compression_policy,
                        "strategy",
                        CompressionStrategy.TRUNCATE,
                    ),
                    original_chars=len(original_text),
                    compressed_chars=0,
                    estimated_tokens_saved=estimate_tokens(original_text),
                    was_applied=True,
                    source_ids=tuple(
                        candidate.source.source_id for candidate in candidates
                    ),
                    metadata={"outcome": "zero_document_budget"},
                ),
                trace=ContextTrace(
                    trace_id=trace_id,
                    decisions=(
                        ContextAssemblyDecision(
                            source_id="compression",
                            action=ContextDecisionAction.TRANSFORMED,
                            reason_codes=(
                                BudgetPressureReasonCode.SLOT_EXHAUSTED,
                                BudgetPressureReasonCode.COMPRESSION_REQUIRED,
                            ),
                            explanation=(
                                "Document content could not be included because the "
                                "document slot budget fell to zero."
                            ),
                            candidate_score=0.0,
                        ),
                    ),
                    metadata={
                        "compression_strategy": getattr(
                            getattr(self._compression_policy, "strategy", None),
                            "value",
                            CompressionStrategy.TRUNCATE.value,
                        ),
                        "max_tokens": str(max_tokens),
                        "source_count": str(len(candidates)),
                    },
                ),
            )

        return self._compression_policy.compress_candidates(
            candidates,
            trace_id=trace_id,
            max_tokens=max_tokens,
            query=query,
        )

    def _build_trace_metadata(
        self,
        *,
        request_metadata: Mapping[str, str],
        retrieved_candidate_count: int,
        ranked_candidate_count: int,
        selected_memory_count: int,
        selected_candidates: tuple[ContextCandidate, ...],
        selected_memory_entries: tuple[ContextMemoryEntry, ...],
        budget: ContextBudget,
        ranking_outcome: CandidateRankingOutcome,
        memory_outcome: MemorySelectionOutcome,
        budget_outcome: BudgetAllocationOutcome,
        compression_outcome: CompressionOutcome | None,
        compression_applied: bool,
    ) -> dict[str, str]:
        """Assemble service-level and stage-prefixed trace metadata."""

        metadata: dict[str, str] = {
            "service": "context_assembly_service",
            "retrieved_candidate_count": str(retrieved_candidate_count),
            "ranked_candidate_count": str(ranked_candidate_count),
            "selected_memory_count": str(selected_memory_count),
            "budget_total_tokens": str(budget.total_tokens),
            "budget_slot_count": str(len(budget.slots)),
            "compression_present": str(compression_outcome is not None).lower(),
            "compression_applied": str(compression_applied).lower(),
            "selected_source_classes": ",".join(
                self._ordered_unique(
                    candidate.source.source_class.value
                    for candidate in selected_candidates
                )
            ),
            "selected_source_families": ",".join(
                self._ordered_unique(
                    candidate.source.source_family_name
                    for candidate in selected_candidates
                )
            ),
            "selected_source_collectors": ",".join(
                self._ordered_unique(
                    candidate.source.collector_name or ""
                    for candidate in selected_candidates
                )
            ),
            "selected_source_family_counts": self._count_summary(
                candidate.source.source_family_name for candidate in selected_candidates
            ),
            "selected_source_collector_counts": self._count_summary(
                candidate.source.collector_name or ""
                for candidate in selected_candidates
            ),
            "selected_memory_source_classes": ",".join(
                self._ordered_unique(
                    entry.source.source_class.value for entry in selected_memory_entries
                )
            ),
            "selected_memory_source_families": ",".join(
                self._ordered_unique(
                    entry.source.source_family_name for entry in selected_memory_entries
                )
            ),
            "selected_memory_collectors": ",".join(
                self._ordered_unique(
                    entry.source.collector_name or ""
                    for entry in selected_memory_entries
                )
            ),
        }
        metadata.update(self._prefix_metadata("request", request_metadata))
        metadata.update(
            self._prefix_metadata("ranking", ranking_outcome.trace.metadata)
        )
        metadata.update(self._prefix_metadata("memory", memory_outcome.trace.metadata))
        metadata.update(self._prefix_metadata("budget", budget_outcome.trace.metadata))
        if compression_outcome is not None:
            metadata.update(
                self._prefix_metadata("compression", compression_outcome.trace.metadata)
            )
        return metadata

    def _allocated_tokens(
        self,
        budget_outcome: BudgetAllocationOutcome,
        *,
        slot_name: str,
    ) -> int:
        """Return allocated tokens for a named slot, defaulting to zero."""

        for allocation in budget_outcome.allocations:
            if allocation.slot_name == slot_name:
                return allocation.allocated_tokens
        return 0

    def _emit_log_message(
        self,
        message: str,
        *message_args: object,
        **fields: object,
    ) -> None:
        """Emit service logs using stable domain-owned message constants."""

        self._logger.info(
            message,
            *message_args,
            extra={
                "event": getattr(message, "event_name", "log"),
                **fields,
            },
        )

    def _normalize_optional_identifier(
        self,
        value: str | None,
        *,
        field_name: str,
    ) -> str | None:
        """Normalize optional packet/trace ids while preserving caller-generated ids."""

        if value is None:
            return None
        normalized = value.strip()
        if not normalized:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_ASSEMBLY_REQUEST,
                message_args=(
                    ErrorMessage.FIELD_MUST_NOT_BE_BLANK_WHEN_PROVIDED % (field_name,),
                ),
            )
        return normalized

    @staticmethod
    def _copy_request_metadata(
        metadata: Mapping[str, object] | None,
    ) -> dict[str, str]:
        """Copy outer-workflow metadata without treating it as service policy."""

        normalized_metadata: dict[str, str] = {}
        for key, value in (metadata or {}).items():
            normalized_key = str(key)
            if not normalized_key:
                continue
            if value is None:
                continue
            normalized_metadata[normalized_key] = str(value)
        return normalized_metadata

    def _prefix_metadata(
        self,
        prefix: str,
        metadata: Mapping[str, str],
    ) -> dict[str, str]:
        """Prefix trace-metadata keys so stage-level values remain unambiguous."""

        return {f"{prefix}_{key}": value for key, value in metadata.items()}

    def _with_decision_positions(
        self,
        decisions: tuple[ContextAssemblyDecision, ...],
    ) -> tuple[ContextAssemblyDecision, ...]:
        """Attach stable 1-based positions to trace decisions for inspection."""

        return tuple(
            decision.model_copy(update={"position": index})
            for index, decision in enumerate(decisions, start=1)
        )

    def _ordered_unique(self, values: Iterable[str]) -> tuple[str, ...]:
        """Return non-empty values once in first-seen order."""

        ordered: list[str] = []
        seen: set[str] = set()
        for value in values:
            normalized = value.strip()
            if not normalized or normalized in seen:
                continue
            ordered.append(normalized)
            seen.add(normalized)
        return tuple(ordered)

    def _count_summary(self, values: Iterable[str]) -> str:
        """Return first-seen value counts as a stable comma-separated summary."""

        counts: dict[str, int] = {}
        for value in values:
            normalized = value.strip()
            if not normalized:
                continue
            counts[normalized] = counts.get(normalized, 0) + 1
        return ",".join(f"{value}={count}" for value, count in counts.items())


__all__ = ["CandidateRetriever", "ContextAssemblyService"]
