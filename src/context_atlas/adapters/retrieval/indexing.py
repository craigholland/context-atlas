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
    source_tfidf_vectors: Mapping[str, Mapping[str, float]]
    source_vector_norms: Mapping[str, float]

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
    source_tfidf_vectors = {
        source_id: _build_tfidf_vector(tokens, inverse_document_frequency)
        for source_id, tokens in source_tokens.items()
    }
    source_vector_norms = {
        source_id: _vector_norm(vector)
        for source_id, vector in source_tfidf_vectors.items()
    }

    return LexicalIndexSnapshot(
        registry_revision=registry_revision,
        source_ids=tuple(source_tokens.keys()),
        source_tokens=MappingProxyType(source_tokens),
        document_frequency=MappingProxyType(dict(document_frequency)),
        inverse_document_frequency=MappingProxyType(inverse_document_frequency),
        missing_term_inverse_document_frequency=math.log(1 + source_count) + 1.0,
        source_tfidf_vectors=MappingProxyType(
            {
                source_id: MappingProxyType(vector)
                for source_id, vector in source_tfidf_vectors.items()
            }
        ),
        source_vector_norms=MappingProxyType(source_vector_norms),
    )


def _build_tfidf_vector(
    tokens: tuple[str, ...],
    inverse_document_frequency: Mapping[str, float],
) -> dict[str, float]:
    """Build one sparse TF-IDF vector from cached corpus-wide IDF state."""

    term_frequency = _term_frequency(tokens)
    return {
        term: weight * inverse_document_frequency[term]
        for term, weight in term_frequency.items()
    }


def _term_frequency(tokens: tuple[str, ...]) -> dict[str, float]:
    """Compute sparse term-frequency weights from normalized tokens."""

    if not tokens:
        return {}

    counts = Counter(tokens)
    token_count = len(tokens)
    return {
        term: occurrence_count / token_count
        for term, occurrence_count in counts.items()
    }


def _vector_norm(vector: Mapping[str, float]) -> float:
    """Return the Euclidean norm for one sparse weighted vector."""

    return math.sqrt(sum(weight**2 for weight in vector.values()))
