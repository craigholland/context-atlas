"""Canonical core domain artifacts for Context Atlas."""

from .assembly import (
    ContextAssemblyDecision,
    ContextDecisionAction,
    ContextPacket,
    ContextTrace,
)
from .budget import ContextBudget, ContextBudgetSlot, ContextBudgetSlotMode
from .reason_codes import (
    AuthorityPrecedenceReasonCode,
    BudgetPressureReasonCode,
    ExclusionReasonCode,
    InclusionReasonCode,
)
from .sources import (
    ContextCandidate,
    ContextSource,
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceDurability,
    ContextSourceProvenance,
)
from .transformations import CompressionResult, CompressionStrategy

__all__ = [
    "AuthorityPrecedenceReasonCode",
    "BudgetPressureReasonCode",
    "ContextAssemblyDecision",
    "ContextBudget",
    "ContextBudgetSlot",
    "ContextBudgetSlotMode",
    "ContextCandidate",
    "ContextDecisionAction",
    "ContextPacket",
    "ContextSource",
    "ContextSourceAuthority",
    "ContextSourceClass",
    "ContextSourceDurability",
    "ContextSourceProvenance",
    "ContextTrace",
    "CompressionResult",
    "CompressionStrategy",
    "ExclusionReasonCode",
    "InclusionReasonCode",
]
