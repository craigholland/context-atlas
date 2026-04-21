"""Tests for the starter in-memory registry and lexical retrieval adapters."""

from __future__ import annotations

import io
import logging
import math
from unittest.mock import patch
import unittest

from context_atlas.adapters import (
    InMemorySourceRegistry,
    LexicalRetrievalMode,
    LexicalRetriever,
)
from context_atlas.adapters.retrieval import lexical as lexical_module
from context_atlas.adapters.retrieval.indexing import build_lexical_index_snapshot
from context_atlas.domain.errors import ContextAtlasError, ErrorCode
from context_atlas.domain.messages import LogMessage
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

    def _candidate_signature(
        self, results: tuple
    ) -> tuple[tuple[str, float, int, tuple[str, ...]], ...]:
        return tuple(
            (
                candidate.source.source_id,
                candidate.score,
                candidate.rank,
                candidate.signals,
            )
            for candidate in results
        )

    def _collect_repeated_query_proof_bundle(
        self, retriever: LexicalRetriever
    ) -> dict[str, int]:
        with (
            patch.object(
                retriever._registry,
                "list_sources",
                wraps=retriever._registry.list_sources,
            ) as list_sources,
            patch(
                "context_atlas.adapters.retrieval.lexical.build_lexical_index_snapshot",
                wraps=build_lexical_index_snapshot,
            ) as builder,
            patch(
                "context_atlas.adapters.retrieval.lexical._term_frequency",
                wraps=lexical_module._term_frequency,
            ) as term_frequency,
        ):
            retriever.retrieve("document ranking context", top_k=2)

        return {
            "registry_source_listings": list_sources.call_count,
            "snapshot_rebuilds": builder.call_count,
            "query_term_frequency_recomputations": term_frequency.call_count,
        }

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

    def test_registry_revision_increments_as_sources_are_registered(self) -> None:
        registry = InMemorySourceRegistry()

        self.assertEqual(registry.revision, 0)

        registry.add_source(self.sources[0])
        registry.add_source(self.sources[1])

        self.assertEqual(registry.revision, 2)

    def test_tfidf_index_snapshot_is_reused_for_repeated_queries(self) -> None:
        registry = InMemorySourceRegistry(self.sources)
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.TFIDF)

        with patch(
            "context_atlas.adapters.retrieval.lexical.build_lexical_index_snapshot",
            wraps=build_lexical_index_snapshot,
        ) as builder:
            retriever.retrieve("tf idf retrieval", top_k=2)
            retriever.retrieve("document ranking context", top_k=2)

        self.assertEqual(builder.call_count, 1)

    def test_tfidf_index_snapshot_caches_corpus_wide_idf_state(self) -> None:
        registry = InMemorySourceRegistry(self.sources)
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.TFIDF)

        retriever.retrieve("tf idf retrieval", top_k=2)

        snapshot = retriever._tfidf_index_snapshot
        assert snapshot is not None

        self.assertIn("retrieval", snapshot.inverse_document_frequency)
        self.assertAlmostEqual(
            snapshot.inverse_document_frequency["retrieval"],
            math.log((1 + snapshot.source_count) / 3) + 1.0,
        )
        self.assertAlmostEqual(
            snapshot.missing_term_inverse_document_frequency,
            math.log(1 + snapshot.source_count) + 1.0,
        )
        self.assertIn("retrieval-study", snapshot.source_tfidf_vectors)
        self.assertGreater(snapshot.source_vector_norms["retrieval-study"], 0.0)

    def test_tfidf_retrieval_reuses_source_side_vector_state(self) -> None:
        registry = InMemorySourceRegistry(self.sources)
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.TFIDF)

        retriever.retrieve("tf idf retrieval", top_k=2)

        with patch(
            "context_atlas.adapters.retrieval.lexical._term_frequency",
            wraps=lexical_module._term_frequency,
        ) as term_frequency:
            retriever.retrieve("document ranking context", top_k=2)

        self.assertEqual(term_frequency.call_count, 1)

    def test_tfidf_repeated_queries_reuse_both_snapshot_layers(self) -> None:
        registry = InMemorySourceRegistry(self.sources)
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.TFIDF)

        retriever.retrieve("tf idf retrieval", top_k=2)

        with (
            patch(
                "context_atlas.adapters.retrieval.lexical.build_lexical_index_snapshot",
                wraps=build_lexical_index_snapshot,
            ) as builder,
            patch(
                "context_atlas.adapters.retrieval.lexical._term_frequency",
                wraps=lexical_module._term_frequency,
            ) as term_frequency,
        ):
            retriever.retrieve("document ranking context", top_k=2)

        self.assertEqual(builder.call_count, 0)
        self.assertEqual(term_frequency.call_count, 1)

    def test_tfidf_repeated_queries_stay_on_shared_registry_path(self) -> None:
        registry = InMemorySourceRegistry(self.sources)
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.TFIDF)

        with (
            patch.object(
                registry, "list_sources", wraps=registry.list_sources
            ) as list_sources,
            patch(
                "context_atlas.adapters.retrieval.lexical.build_lexical_index_snapshot",
                wraps=build_lexical_index_snapshot,
            ) as builder,
        ):
            retriever.retrieve("tf idf retrieval", top_k=2)
            retriever.retrieve("document ranking context", top_k=2)

        self.assertEqual(list_sources.call_count, 2)
        self.assertEqual(builder.call_count, 1)

    def test_tfidf_repeated_query_semantics_stay_deterministic(self) -> None:
        registry = InMemorySourceRegistry(self.sources)
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.TFIDF)

        initial_results = retriever.retrieve(
            "tf idf retrieval document ranking", top_k=3
        )
        interleaved_results = retriever.retrieve(
            "context governance architecture", top_k=3
        )
        repeated_results = retriever.retrieve(
            "tf idf retrieval document ranking", top_k=3
        )

        self.assertNotEqual(
            self._candidate_signature(initial_results),
            self._candidate_signature(interleaved_results),
        )
        self.assertEqual(
            self._candidate_signature(initial_results),
            self._candidate_signature(repeated_results),
        )

    def test_tfidf_repeated_query_proof_bundle_is_reviewable(self) -> None:
        registry = InMemorySourceRegistry(self.sources)
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.TFIDF)

        retriever.retrieve("tf idf retrieval", top_k=2)

        self.assertEqual(
            self._collect_repeated_query_proof_bundle(retriever),
            {
                "registry_source_listings": 1,
                "snapshot_rebuilds": 0,
                "query_term_frequency_recomputations": 1,
            },
        )

    def test_tfidf_retrieval_logs_bounded_snapshot_reuse_signal(self) -> None:
        registry = InMemorySourceRegistry(self.sources)
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.TFIDF)
        stream = io.StringIO()
        handler = logging.StreamHandler(stream)
        handler.setFormatter(
            logging.Formatter(
                "%(event)s|%(index_snapshot_state)s|%(registry_revision)s|"
                "%(source_count)s|%(query_token_count)s|%(message)s"
            )
        )
        logger = logging.getLogger("context_atlas.adapters.retrieval.lexical")
        previous_handlers = logger.handlers[:]
        previous_level = logger.level
        previous_propagate = logger.propagate
        self.addCleanup(
            self._restore_logger,
            logger,
            previous_handlers,
            previous_level,
            previous_propagate,
        )
        logger.handlers = [handler]
        logger.setLevel(logging.INFO)
        logger.propagate = False

        retriever.retrieve("tf idf retrieval", top_k=2)
        retriever.retrieve("document ranking context", top_k=2)

        self.assertEqual(
            stream.getvalue().strip().splitlines(),
            [
                "retrieval_completed|rebuilt|3|3|3|"
                "Retrieval completed: mode=tfidf, query=tf idf retrieval, "
                "candidate_count=2",
                "retrieval_completed|warm|3|3|3|"
                "Retrieval completed: mode=tfidf, query=document ranking context, "
                "candidate_count=2",
            ],
        )

    def test_tfidf_index_snapshot_rebuilds_after_registry_revision_changes(
        self,
    ) -> None:
        registry = InMemorySourceRegistry(self.sources[:2])
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.TFIDF)

        with patch(
            "context_atlas.adapters.retrieval.lexical.build_lexical_index_snapshot",
            wraps=build_lexical_index_snapshot,
        ) as builder:
            retriever.retrieve("context governance", top_k=2)
            registry.add_source(self.sources[2])
            retriever.retrieve("tf idf retrieval", top_k=2)

        self.assertEqual(builder.call_count, 2)

    def test_retrieval_events_and_templates_are_registered(self) -> None:
        self.assertEqual(
            LogMessage.SOURCE_REGISTERED,
            "Source registered: source_id=%s, total_sources=%d",
        )
        self.assertEqual(
            LogMessage.RETRIEVAL_COMPLETED,
            "Retrieval completed: mode=%s, query=%s, candidate_count=%d",
        )

    @staticmethod
    def _restore_logger(
        logger: logging.Logger,
        handlers: list[logging.Handler],
        level: int,
        propagate: bool,
    ) -> None:
        logger.handlers = handlers
        logger.setLevel(level)
        logger.propagate = propagate


if __name__ == "__main__":
    unittest.main()
