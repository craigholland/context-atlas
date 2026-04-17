"""Canonical budget artifacts for Context Atlas."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from types import MappingProxyType
from typing import Mapping

from ..errors import ContextAtlasError, ErrorCode


class ContextBudgetSlotMode(StrEnum):
    """How a budget slot should be interpreted by future policy."""

    FIXED = "fixed"
    ELASTIC = "elastic"


def _freeze_mapping(raw_mapping: Mapping[str, str]) -> Mapping[str, str]:
    """Return an immutable copy of a string-keyed mapping."""

    return MappingProxyType(dict(raw_mapping))


@dataclass(frozen=True, slots=True)
class ContextBudgetSlot:
    """A named budget slot inside a context budget."""

    slot_name: str
    token_limit: int
    mode: ContextBudgetSlotMode = ContextBudgetSlotMode.FIXED
    priority: int = 100

    def __post_init__(self) -> None:
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


@dataclass(frozen=True, slots=True)
class ContextBudget:
    """Top-level budget artifact for packet assembly."""

    total_tokens: int
    slots: tuple[ContextBudgetSlot, ...] = ()
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.total_tokens < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_BUDGET_TOTAL,
                message_args=("total tokens must be >= 1",),
            )

        normalized_slots = tuple(self.slots)
        fixed_reserved_tokens = 0
        seen_slot_names: set[str] = set()

        for slot in normalized_slots:
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

        object.__setattr__(self, "slots", normalized_slots)
        object.__setattr__(self, "metadata", _freeze_mapping(self.metadata))

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
