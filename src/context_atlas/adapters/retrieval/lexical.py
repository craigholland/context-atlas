"""Lexical retrieval adapters for Atlas-native in-memory source selection."""

from __future__ import annotations

from collections import Counter
from enum import Enum, StrEnum
import logging
import math
import re
from typing import Iterable

from ...domain.errors import ContextAtlasError, ErrorCode
from ...domain.messages import ErrorMessage, LogMessage
from ...domain.models import ContextCandidate, ContextSource

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


class InMemorySourceRegistry:
    """A small in-memory registry for canonical context sources."""

    def __init__(self, sources: Iterable[ContextSource] = ()) -> None:
        self._sources: dict[str, ContextSource] = {}
        self.add_sources(sources)

    def add_source(self, source: ContextSource) -> None:
        """Register a canonical source by its stable identifier."""

        if source.source_id in self._sources:
            raise ContextAtlasError(
                code=ErrorCode.DUPLICATE_SOURCE_IDENTIFIER,
                message_args=(source.source_id,),
            )

        self._sources[source.source_id] = source
        _emit_log_message(
            LogMessage.SOURCE_REGISTERED,
            source.source_id,
            len(self._sources),
            source_id=source.source_id,
            total_sources=len(self._sources),
        )

    def add_sources(self, sources: Iterable[ContextSource]) -> None:
        """Bulk-register canonical sources in insertion order."""

        for source in sources:
            self.add_source(source)

    def list_sources(self) -> tuple[ContextSource, ...]:
        """Return registered sources in insertion order."""

        return tuple(self._sources.values())

    def __len__(self) -> int:
        return len(self._sources)


class LexicalRetriever:
    """Build Atlas-native candidates from lexical keyword or TF-IDF matching."""

    def __init__(
        self,
        registry: InMemorySourceRegistry,
        mode: LexicalRetrievalMode = LexicalRetrievalMode.TFIDF,
    ) -> None:
        self._registry = registry
        self.mode = mode

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

        if self.mode is LexicalRetrievalMode.KEYWORD:
            candidates = self._keyword_retrieve(query_tokens, top_k=top_k)
        else:
            candidates = self._tfidf_retrieve(query_tokens, top_k=top_k)

        _emit_log_message(
            LogMessage.RETRIEVAL_COMPLETED,
            self.mode.value,
            query,
            len(candidates),
            mode=self.mode,
            query=query,
            candidate_count=len(candidates),
        )
        return candidates

    def _keyword_retrieve(
        self,
        query_tokens: list[str],
        *,
        top_k: int,
    ) -> tuple[ContextCandidate, ...]:
        """Rank sources by query-token overlap."""

        query_token_set = set(query_tokens)
        scored: list[tuple[float, ContextSource]] = []
        for source in self._registry.list_sources():
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
        top_k: int,
    ) -> tuple[ContextCandidate, ...]:
        """Rank sources by sparse TF-IDF cosine similarity."""

        query_tf = _term_frequency(query_tokens)
        sources = self._registry.list_sources()
        source_tokens = {
            source.source_id: _tokenize(source.content) for source in sources
        }
        document_frequency = _document_frequency(source_tokens.values())
        source_count = len(sources)
        query_vector = {
            term: term_frequency
            * _inverse_document_frequency(
                term,
                document_frequency=document_frequency,
                source_count=source_count,
            )
            for term, term_frequency in query_tf.items()
        }

        scored: list[tuple[float, ContextSource]] = []
        for source in sources:
            tokens = source_tokens[source.source_id]
            if not tokens:
                continue
            source_tf = _term_frequency(tokens)
            source_vector = {
                term: term_frequency
                * _inverse_document_frequency(
                    term,
                    document_frequency=document_frequency,
                    source_count=source_count,
                )
                for term, term_frequency in source_tf.items()
            }
            score = _cosine_similarity(query_vector, source_vector)
            if score <= 0.0:
                continue
            scored.append((score, source))

        return _to_candidates(scored, signal=_SIGNAL_TFIDF_COSINE, top_k=top_k)


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


def _document_frequency(source_tokens: Iterable[list[str]]) -> Counter[str]:
    """Count how many sources contain each normalized token."""

    frequency: Counter[str] = Counter()
    for tokens in source_tokens:
        frequency.update(set(tokens))
    return frequency


def _inverse_document_frequency(
    term: str,
    *,
    document_frequency: Counter[str],
    source_count: int,
) -> float:
    """Compute a smoothed inverse-document-frequency score."""

    return math.log((1 + source_count) / (1 + document_frequency.get(term, 0))) + 1.0


def _cosine_similarity(
    left_vector: dict[str, float],
    right_vector: dict[str, float],
) -> float:
    """Compute cosine similarity between two sparse weighted vectors."""

    dot_product = sum(
        left_vector.get(term, 0.0) * right_vector.get(term, 0.0) for term in left_vector
    )
    left_norm = math.sqrt(sum(weight**2 for weight in left_vector.values()))
    right_norm = math.sqrt(sum(weight**2 for weight in right_vector.values()))
    if left_norm == 0.0 or right_norm == 0.0:
        return 0.0
    return dot_product / (left_norm * right_norm)
