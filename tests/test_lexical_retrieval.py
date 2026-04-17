"""Tests for the starter in-memory registry and lexical retrieval adapters."""

from __future__ import annotations

import unittest

from context_atlas.adapters import (
    InMemorySourceRegistry,
    LexicalRetrievalMode,
    LexicalRetriever,
)
from context_atlas.domain.errors import ContextAtlasError, ErrorCode
from context_atlas.domain.events import LogEvent
from context_atlas.domain.messages import get_log_message
from context_atlas.domain.models import (
    ContextSource,
    ContextSourceAuthority,
    ContextSourceClass,
)


class LexicalRetrievalTests(unittest.TestCase):
    """Verify the first Atlas-native lexical retrieval adapter slice."""

    def setUp(self) -> None:
        self.sources = (
            ContextSource(
                source_id="authoritative-charter",
                title="Context Atlas Charter",
                content=(
                    "Authoritative context governance defines how architecture, "
                    "authority, and packet assembly should work."
                ),
                source_class=ContextSourceClass.AUTHORITATIVE,
                authority=ContextSourceAuthority.BINDING,
            ),
            ContextSource(
                source_id="planning-roadmap",
                title="Roadmap",
                content=(
                    "Planning notes describe future retrieval, budgeting, and "
                    "memory work for Context Atlas."
                ),
                source_class=ContextSourceClass.PLANNING,
                authority=ContextSourceAuthority.PREFERRED,
            ),
            ContextSource(
                source_id="retrieval-study",
                title="Retrieval Study",
                content=(
                    "TF IDF retrieval improves document ranking when lexical "
                    "overlap alone is too shallow for relevant context."
                ),
                source_class=ContextSourceClass.EXPLORATORY,
                authority=ContextSourceAuthority.ADVISORY,
            ),
        )

    def test_registry_rejects_duplicate_source_identifiers(self) -> None:
        registry = InMemorySourceRegistry(self.sources[:1])

        with self.assertRaises(ContextAtlasError) as context:
            registry.add_source(self.sources[0])

        self.assertEqual(context.exception.code, ErrorCode.DUPLICATE_SOURCE_IDENTIFIER)

    def test_keyword_retrieval_returns_ranked_candidates(self) -> None:
        registry = InMemorySourceRegistry(self.sources)
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.KEYWORD)

        results = retriever.retrieve("context governance architecture", top_k=2)

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].source.source_id, "authoritative-charter")
        self.assertEqual(results[0].rank, 1)
        self.assertEqual(results[0].signals, ("keyword_overlap",))
        self.assertGreaterEqual(results[0].score, results[1].score)

    def test_tfidf_retrieval_returns_relevant_document_first(self) -> None:
        registry = InMemorySourceRegistry(self.sources)
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.TFIDF)

        results = retriever.retrieve("tf idf retrieval document ranking", top_k=2)

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].source.source_id, "retrieval-study")
        self.assertEqual(results[0].rank, 1)
        self.assertEqual(results[0].signals, ("tfidf_cosine_similarity",))
        self.assertGreater(results[0].score, 0.0)

    def test_empty_query_returns_no_candidates(self) -> None:
        registry = InMemorySourceRegistry(self.sources)
        retriever = LexicalRetriever(registry)

        self.assertEqual(retriever.retrieve("   ", top_k=3), ())

    def test_invalid_top_k_raises_context_error(self) -> None:
        registry = InMemorySourceRegistry(self.sources)
        retriever = LexicalRetriever(registry)

        with self.assertRaises(ContextAtlasError) as context:
            retriever.retrieve("context atlas", top_k=0)

        self.assertEqual(context.exception.code, ErrorCode.INVALID_RETRIEVAL_REQUEST)

    def test_retrieval_events_and_templates_are_registered(self) -> None:
        self.assertEqual(
            get_log_message(LogEvent.SOURCE_REGISTERED),
            "Source registered: source_id=%s, total_sources=%d",
        )
        self.assertEqual(
            get_log_message(LogEvent.RETRIEVAL_COMPLETED),
            "Retrieval completed: mode=%s, query=%s, candidate_count=%d",
        )


if __name__ == "__main__":
    unittest.main()
