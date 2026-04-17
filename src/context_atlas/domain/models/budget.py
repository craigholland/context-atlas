"""Canonical budget artifacts for Context Atlas."""

from __future__ import annotations

from enum import StrEnum

from pydantic import Field

from ..errors import ContextAtlasError, ErrorCode
from .base import CanonicalDomainModel


class ContextBudgetSlotMode(StrEnum):
    """How a budget slot should be interpreted by future policy."""

    FIXED = "fixed"
    ELASTIC = "elastic"


class ContextBudgetSlot(CanonicalDomainModel):
    """A named budget slot inside a context budget."""

    slot_name: str
    token_limit: int
    mode: ContextBudgetSlotMode = ContextBudgetSlotMode.FIXED
    priority: int = 100

    def model_post_init(self, __context: object) -> None:
        normalized_name = self.slot_name.strip()
        if not normalized_name:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_SLOT,
                message_args=("<unnamed>", "slot name must not be empty"),
            )
        if self.token_limit < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_SLOT,
                message_args=(normalized_name, "token limit must be >= 0"),
            )
        if self.priority < 0:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_SLOT,
                message_args=(normalized_name, "priority must be >= 0"),
            )

        object.__setattr__(self, "slot_name", normalized_name)


class ContextBudget(CanonicalDomainModel):
    """Top-level budget artifact for packet assembly."""

    total_tokens: int
    slots: tuple[ContextBudgetSlot, ...] = ()
    metadata: dict[str, str] = Field(default_factory=dict)

    def model_post_init(self, __context: object) -> None:
        if self.total_tokens < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_TOTAL,
                message_args=("total tokens must be >= 1",),
            )

        fixed_reserved_tokens = 0
        seen_slot_names: set[str] = set()

        for slot in self.slots:
            if slot.slot_name in seen_slot_names:
                raise ContextAtlasError(
                    code=ErrorCode.DUPLICATE_BUDGET_SLOT_NAME,
                    message_args=(slot.slot_name,),
                )
            seen_slot_names.add(slot.slot_name)
            if slot.mode is ContextBudgetSlotMode.FIXED:
                fixed_reserved_tokens += slot.token_limit

        if fixed_reserved_tokens > self.total_tokens:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_TOTAL,
                message_args=(
                    f"fixed slot reservations ({fixed_reserved_tokens}) exceed total tokens ({self.total_tokens})",
                ),
            )

        object.__setattr__(self, "metadata", self.freeze_metadata(self.metadata))

    @property
    def reserved_tokens(self) -> int:
        """Total tokens reserved by fixed slots."""

        return sum(
            slot.token_limit
            for slot in self.slots
            if slot.mode is ContextBudgetSlotMode.FIXED
        )

    @property
    def remaining_tokens(self) -> int:
        """Tokens not already reserved by fixed slots."""

        return self.total_tokens - self.reserved_tokens


__all__ = ["ContextBudget", "ContextBudgetSlot", "ContextBudgetSlotMode"]
