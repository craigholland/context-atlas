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
from .source_semantics import (
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceDurability,
    ContextSourceFamily,
    ContextSourceSemanticsProfile,
    coerce_source_text_sequence,
    get_default_source_semantics,
    merge_source_text_groups,
    resolve_source_semantics,
)
from .sources import (
    ContextCandidate,
    ContextSource,
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
    "coerce_source_text_sequence",
    "get_default_source_semantics",
    "merge_source_text_groups",
    "resolve_source_semantics",
]
