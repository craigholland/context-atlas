"""Budget-allocation policy contracts and starter implementations."""

from __future__ import annotations

from typing import Iterable, Protocol

from ..errors import ContextAtlasError, ErrorCode
from ..models.base import CanonicalDomainModel
from ..models import (
    BudgetPressureReasonCode,
    ContextAssemblyDecision,
    ContextBudget,
    ContextBudgetSlotMode,
    ContextDecisionAction,
    ContextTrace,
    InclusionReasonCode,
)


class ContextBudgetAllocationPolicy(Protocol):
    """Contract for deterministic budget-slot allocation."""

    def allocate_budget(
        self,
        budget: ContextBudget,
        *,
        requests: Iterable["BudgetRequest"],
        trace_id: str,
    ) -> "BudgetAllocationOutcome":
        """Allocate token requests across fixed and elastic slots."""


class BudgetRequest(CanonicalDomainModel):
    """Requested token demand for a named budget slot."""

    slot_name: str
    requested_tokens: int

    def model_post_init(self, __context: object) -> None:
        normalized_name = self.slot_name.strip()
        if not normalized_name:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_ALLOCATION,
                message_args=("slot_name must not be empty",),
            )
        if self.requested_tokens < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_ALLOCATION,
                message_args=(
                    f"requested_tokens for '{normalized_name}' must be >= 0",
                ),
            )
        object.__setattr__(self, "slot_name", normalized_name)


class BudgetAllocation(CanonicalDomainModel):
    """Actual allocation outcome for a single slot."""

    slot_name: str
    requested_tokens: int
    allocated_tokens: int
    was_reduced: bool
    mode: ContextBudgetSlotMode

    def model_post_init(self, __context: object) -> None:
        normalized_name = self.slot_name.strip()
        if not normalized_name:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_ALLOCATION,
                message_args=("slot_name must not be empty",),
            )
        if self.requested_tokens < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_ALLOCATION,
                message_args=(
                    f"requested_tokens for '{normalized_name}' must be >= 0",
                ),
            )
        if self.allocated_tokens < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_ALLOCATION,
                message_args=(
                    f"allocated_tokens for '{normalized_name}' must be >= 0",
                ),
            )
        if self.allocated_tokens > self.requested_tokens:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_ALLOCATION,
                message_args=(
                    f"allocated_tokens for '{normalized_name}' must be <= requested_tokens",
                ),
            )
        if self.was_reduced != (self.allocated_tokens < self.requested_tokens):
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_ALLOCATION,
                message_args=(
                    f"was_reduced for '{normalized_name}' must match the allocation delta",
                ),
            )

        object.__setattr__(self, "slot_name", normalized_name)


class BudgetAllocationOutcome(CanonicalDomainModel):
    """Structured result of a budget allocation pass."""

    allocations: tuple[BudgetAllocation, ...]
    trace: ContextTrace
    remaining_tokens: int

    def model_post_init(self, __context: object) -> None:
        if self.remaining_tokens < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_ALLOCATION,
                message_args=("remaining_tokens must be >= 0",),
            )

    @property
    def total_allocated_tokens(self) -> int:
        """Return the sum of allocated tokens across all slots."""

        return sum(allocation.allocated_tokens for allocation in self.allocations)


class StarterBudgetAllocationPolicy:
    """Starter policy for fixed and elastic slot allocation."""

    def allocate_budget(
        self,
        budget: ContextBudget,
        *,
        requests: Iterable[BudgetRequest],
        trace_id: str,
    ) -> BudgetAllocationOutcome:
        """Allocate requested tokens across budget slots deterministically."""

        request_tuple = tuple(requests)
        request_by_slot = {request.slot_name: request for request in request_tuple}
        if len(request_by_slot) != len(request_tuple):
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_ALLOCATION,
                message_args=(
                    "duplicate budget requests for the same slot are not allowed",
                ),
            )
        slot_by_name = {slot.slot_name: slot for slot in budget.slots}

        unknown_slots = sorted(set(request_by_slot) - set(slot_by_name))
        if unknown_slots:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_ALLOCATION,
                message_args=(f"unknown budget slots: {', '.join(unknown_slots)}",),
            )

        allocations: list[BudgetAllocation] = []
        decisions: list[ContextAssemblyDecision] = []
        fixed_allocated = 0

        for slot in budget.slots:
            request = request_by_slot.get(
                slot.slot_name,
                BudgetRequest(slot_name=slot.slot_name, requested_tokens=0),
            )
            if slot.mode is not ContextBudgetSlotMode.FIXED:
                continue

            allocated_tokens = min(request.requested_tokens, slot.token_limit)
            fixed_allocated += allocated_tokens
            allocation = BudgetAllocation(
                slot_name=slot.slot_name,
                requested_tokens=request.requested_tokens,
                allocated_tokens=allocated_tokens,
                was_reduced=allocated_tokens < request.requested_tokens,
                mode=slot.mode,
            )
            allocations.append(allocation)
            decisions.append(_build_budget_decision(allocation))

        remaining_tokens = max(0, budget.total_tokens - fixed_allocated)

        elastic_slots = sorted(
            (
                slot
                for slot in budget.slots
                if slot.mode is ContextBudgetSlotMode.ELASTIC
            ),
            key=lambda slot: (slot.priority, slot.slot_name),
        )
        for slot in elastic_slots:
            request = request_by_slot.get(
                slot.slot_name,
                BudgetRequest(slot_name=slot.slot_name, requested_tokens=0),
            )
            allocated_tokens = min(
                request.requested_tokens, slot.token_limit, remaining_tokens
            )
            remaining_tokens -= allocated_tokens
            allocation = BudgetAllocation(
                slot_name=slot.slot_name,
                requested_tokens=request.requested_tokens,
                allocated_tokens=allocated_tokens,
                was_reduced=allocated_tokens < request.requested_tokens,
                mode=slot.mode,
            )
            allocations.append(allocation)
            decisions.append(_build_budget_decision(allocation))

        trace = ContextTrace(
            trace_id=trace_id,
            decisions=tuple(decisions),
            metadata={
                "budget_total_tokens": str(budget.total_tokens),
                "allocated_tokens": str(sum(a.allocated_tokens for a in allocations)),
                "remaining_tokens": str(remaining_tokens),
            },
        )
        return BudgetAllocationOutcome(
            allocations=tuple(allocations),
            trace=trace,
            remaining_tokens=remaining_tokens,
        )


def _build_budget_decision(allocation: BudgetAllocation) -> ContextAssemblyDecision:
    """Build a structured budget decision for a slot allocation result."""

    if allocation.requested_tokens == 0:
        return ContextAssemblyDecision(
            source_id=f"budget:{allocation.slot_name}",
            action=ContextDecisionAction.DEFERRED,
            reason_codes=(BudgetPressureReasonCode.SLOT_EXHAUSTED,),
            explanation="No tokens were requested for this slot.",
            candidate_score=float(allocation.allocated_tokens),
        )

    if not allocation.was_reduced:
        return ContextAssemblyDecision(
            source_id=f"budget:{allocation.slot_name}",
            action=ContextDecisionAction.INCLUDED,
            reason_codes=(InclusionReasonCode.BUDGET_AVAILABLE,),
            candidate_score=float(allocation.allocated_tokens),
        )

    reduced_reason = (
        BudgetPressureReasonCode.SLOT_EXHAUSTED
        if allocation.mode is ContextBudgetSlotMode.FIXED
        else BudgetPressureReasonCode.ELASTIC_SLOT_REDUCED
    )
    return ContextAssemblyDecision(
        source_id=f"budget:{allocation.slot_name}",
        action=ContextDecisionAction.TRANSFORMED,
        reason_codes=(reduced_reason,),
        explanation=(
            f"Budget allocation for '{allocation.slot_name}' was reduced from "
            f"{allocation.requested_tokens} to {allocation.allocated_tokens} tokens."
        ),
        candidate_score=float(allocation.allocated_tokens),
    )
