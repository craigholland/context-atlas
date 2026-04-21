"""Index-shape helpers for lexical retrieval adapters."""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
import math
from types import MappingProxyType

from ...domain.models import ContextSource


@dataclass(frozen=True, slots=True)
class LexicalIndexSnapshot:
    """Baseline immutable index state for one registry revision."""

    registry_revision: int
    source_ids: tuple[str, ...]
    source_tokens: Mapping[str, tuple[str, ...]]
    document_frequency: Mapping[str, int]
    inverse_document_frequency: Mapping[str, float]
    missing_term_inverse_document_frequency: float

    @property
    def source_count(self) -> int:
        """Return the number of indexed sources."""

        return len(self.source_ids)


def build_lexical_index_snapshot(
    sources: Iterable[ContextSource],
    *,
    registry_revision: int,
    tokenize: Callable[[str], list[str]],
) -> LexicalIndexSnapshot:
    """Build the minimal lexical index shape needed for later reuse work."""

    source_tokens: dict[str, tuple[str, ...]] = {}
    document_frequency: Counter[str] = Counter()

    for source in sources:
        tokens = tuple(tokenize(source.content))
        source_tokens[source.source_id] = tokens
        document_frequency.update(set(tokens))

    source_count = len(source_tokens)
    inverse_document_frequency = {
        term: math.log((1 + source_count) / (1 + frequency)) + 1.0
        for term, frequency in document_frequency.items()
    }

    return LexicalIndexSnapshot(
        registry_revision=registry_revision,
        source_ids=tuple(source_tokens.keys()),
        source_tokens=MappingProxyType(source_tokens),
        document_frequency=MappingProxyType(dict(document_frequency)),
        inverse_document_frequency=MappingProxyType(inverse_document_frequency),
        missing_term_inverse_document_frequency=math.log(1 + source_count) + 1.0,
    )
