"""Lexical retrieval adapters for Atlas-native in-memory source selection."""

from __future__ import annotations

from collections import Counter
from collections.abc import Mapping
from enum import Enum, StrEnum
import logging
import math
import re

from ...domain.errors import ContextAtlasError, ErrorCode
from ...domain.messages import ErrorMessage, LogMessage
from ...domain.models import ContextCandidate, ContextSource
from .indexing import LexicalIndexSnapshot, build_lexical_index_snapshot
from .registry import InMemorySourceRegistry

logger = logging.getLogger(__name__)

_SIGNAL_KEYWORD_OVERLAP = "keyword_overlap"
_SIGNAL_TFIDF_COSINE = "tfidf_cosine_similarity"

_STOPWORDS = frozenset(
    {
        "a",
        "an",
        "the",
        "is",
        "it",
        "in",
        "on",
        "at",
        "to",
        "for",
        "of",
        "and",
        "or",
        "but",
        "not",
        "with",
        "this",
        "that",
        "are",
        "was",
        "be",
        "by",
        "from",
        "as",
        "has",
        "have",
        "had",
        "its",
        "they",
        "them",
        "their",
        "we",
        "you",
        "he",
        "she",
        "i",
        "my",
        "your",
        "our",
        "how",
        "what",
        "which",
        "who",
        "when",
        "where",
        "do",
        "does",
        "did",
        "will",
        "would",
        "can",
        "could",
        "should",
        "may",
        "might",
        "also",
        "so",
        "if",
        "about",
        "into",
        "than",
        "more",
        "such",
        "both",
        "each",
        "all",
        "no",
        "any",
        "there",
    }
)


class LexicalRetrievalMode(StrEnum):
    """Supported lexical retrieval implementations for the starter adapter."""

    KEYWORD = "keyword"
    TFIDF = "tfidf"


class LexicalRetriever:
    """Build Atlas-native candidates from lexical keyword or TF-IDF matching."""

    def __init__(
        self,
        registry: InMemorySourceRegistry,
        mode: LexicalRetrievalMode = LexicalRetrievalMode.TFIDF,
    ) -> None:
        self._registry = registry
        self.mode = mode
        self._tfidf_index_snapshot: LexicalIndexSnapshot | None = None

    def retrieve(self, query: str, *, top_k: int = 5) -> tuple[ContextCandidate, ...]:
        """Return ranked candidates for a query using the configured lexical mode."""

        if top_k < 1:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_RETRIEVAL_REQUEST,
                message_args=(ErrorMessage.TOP_K_MUST_BE_AT_LEAST_ONE % (top_k,),),
            )

        query_tokens = _tokenize(query)
        if not query_tokens:
            return ()

        sources = self._registry.list_sources()
        index_snapshot_state = "not_applicable"

        if self.mode is LexicalRetrievalMode.KEYWORD:
            candidates = self._keyword_retrieve(
                query_tokens, sources=sources, top_k=top_k
            )
        else:
            candidates, index_snapshot_state = self._tfidf_retrieve(
                query_tokens, sources=sources, top_k=top_k
            )

        _emit_log_message(
            LogMessage.RETRIEVAL_COMPLETED,
            self.mode.value,
            query,
            len(candidates),
            mode=self.mode,
            query=query,
            candidate_count=len(candidates),
            query_token_count=len(query_tokens),
            source_count=len(sources),
            registry_revision=self._registry.revision,
            index_snapshot_state=index_snapshot_state,
        )
        return candidates

    def _keyword_retrieve(
        self,
        query_tokens: list[str],
        *,
        sources: tuple[ContextSource, ...],
        top_k: int,
    ) -> tuple[ContextCandidate, ...]:
        """Rank sources by query-token overlap."""

        query_token_set = set(query_tokens)
        scored: list[tuple[float, ContextSource]] = []
        for source in sources:
            source_token_set = set(_tokenize(source.content))
            overlap = query_token_set & source_token_set
            if not overlap:
                continue
            score = len(overlap) / len(query_token_set)
            scored.append((score, source))
        return _to_candidates(scored, signal=_SIGNAL_KEYWORD_OVERLAP, top_k=top_k)

    def _tfidf_retrieve(
        self,
        query_tokens: list[str],
        *,
        sources: tuple[ContextSource, ...],
        top_k: int,
    ) -> tuple[tuple[ContextCandidate, ...], str]:
        """Rank sources by sparse TF-IDF cosine similarity."""

        query_tf = _term_frequency(query_tokens)
        index_snapshot, index_snapshot_state = self._get_tfidf_index_snapshot(sources)
        inverse_document_frequency = index_snapshot.inverse_document_frequency
        missing_term_inverse_document_frequency = (
            index_snapshot.missing_term_inverse_document_frequency
        )
        query_vector = {
            term: term_frequency
            * inverse_document_frequency.get(
                term,
                missing_term_inverse_document_frequency,
            )
            for term, term_frequency in query_tf.items()
        }

        scored: list[tuple[float, ContextSource]] = []
        for source in sources:
            source_vector = index_snapshot.source_tfidf_vectors[source.source_id]
            source_vector_norm = index_snapshot.source_vector_norms[source.source_id]
            if source_vector_norm == 0.0:
                continue
            score = _cosine_similarity(
                query_vector,
                source_vector,
                right_norm=source_vector_norm,
            )
            if score <= 0.0:
                continue
            scored.append((score, source))

        return (
            _to_candidates(scored, signal=_SIGNAL_TFIDF_COSINE, top_k=top_k),
            index_snapshot_state,
        )

    def _get_tfidf_index_snapshot(
        self,
        sources: tuple[ContextSource, ...],
    ) -> tuple[LexicalIndexSnapshot, str]:
        """Return a registry-revision-aligned index snapshot for TF-IDF work."""

        if (
            self._tfidf_index_snapshot is None
            or self._tfidf_index_snapshot.registry_revision != self._registry.revision
        ):
            self._tfidf_index_snapshot = build_lexical_index_snapshot(
                sources,
                registry_revision=self._registry.revision,
                tokenize=_tokenize,
            )
            return self._tfidf_index_snapshot, "rebuilt"
        return self._tfidf_index_snapshot, "warm"


def _emit_log_message(
    message: str,
    *message_args: object,
    **fields: object,
) -> None:
    """Emit a stable retrieval log line without inventing inline message text."""

    logger.info(
        message,
        *message_args,
        extra={
            "event": getattr(message, "event_name", "log"),
            **_normalize_log_fields(fields),
        },
    )


def _to_candidates(
    scored_sources: list[tuple[float, ContextSource]],
    *,
    signal: str,
    top_k: int,
) -> tuple[ContextCandidate, ...]:
    """Convert scored sources into stable candidate artifacts."""

    scored_sources.sort(key=lambda item: (-item[0], item[1].source_id))
    candidates = []
    for rank, (score, source) in enumerate(scored_sources[:top_k], start=1):
        candidates.append(
            ContextCandidate(
                source=source,
                score=round(score, 4),
                rank=rank,
                signals=(signal,),
                metadata={"retrieval_mode_signal": signal},
            )
        )
    return tuple(candidates)


def _tokenize(text: str) -> list[str]:
    """Lowercase, normalize punctuation, and remove stopwords."""

    normalized = re.sub(r"[^a-z0-9\s]", " ", text.lower())
    return [
        token
        for token in normalized.split()
        if len(token) > 1 and token not in _STOPWORDS
    ]


def _normalize_log_fields(fields: dict[str, object]) -> dict[str, object]:
    """Coerce enum-like field values into logging-friendly primitives."""

    normalized: dict[str, object] = {}
    for key, value in fields.items():
        if isinstance(value, Enum):
            normalized[key] = value.value
            continue
        normalized[key] = value
    return normalized


def _term_frequency(tokens: list[str]) -> dict[str, float]:
    """Compute sparse term-frequency weights from normalized tokens."""

    if not tokens:
        return {}

    counts = Counter(tokens)
    token_count = len(tokens)
    return {
        term: occurrence_count / token_count
        for term, occurrence_count in counts.items()
    }


def _cosine_similarity(
    left_vector: Mapping[str, float],
    right_vector: Mapping[str, float],
    *,
    right_norm: float | None = None,
) -> float:
    """Compute cosine similarity between two sparse weighted vectors."""

    dot_product = sum(
        left_vector.get(term, 0.0) * right_vector.get(term, 0.0) for term in left_vector
    )
    left_norm = math.sqrt(sum(weight**2 for weight in left_vector.values()))
    effective_right_norm = (
        right_norm
        if right_norm is not None
        else math.sqrt(sum(weight**2 for weight in right_vector.values()))
    )
    if left_norm == 0.0 or effective_right_norm == 0.0:
        return 0.0
    return dot_product / (left_norm * effective_right_norm)
