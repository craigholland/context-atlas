"""Canonical core domain artifacts for Context Atlas."""

from .assembly import (
    ContextAssemblyDecision,
    ContextDecisionAction,
    ContextPacket,
    ContextTrace,
)
from .budget import ContextBudget, ContextBudgetSlot, ContextBudgetSlotMode
from .memory import ContextMemoryEntry
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
    ContextSourceFamily,
    ContextSourceProvenance,
    ContextSourceSemanticsProfile,
    get_default_source_semantics,
    resolve_source_semantics,
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
    "ContextMemoryEntry",
    "ContextPacket",
    "ContextSource",
    "ContextSourceAuthority",
    "ContextSourceClass",
    "ContextSourceDurability",
    "ContextSourceFamily",
    "ContextSourceProvenance",
    "ContextSourceSemanticsProfile",
    "ContextTrace",
    "CompressionResult",
    "CompressionStrategy",
    "ExclusionReasonCode",
    "InclusionReasonCode",
    "get_default_source_semantics",
    "resolve_source_semantics",
]
