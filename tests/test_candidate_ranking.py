"""Tests for deterministic ranking, deduplication, and decision tracing."""

from __future__ import annotations

import io
import logging
import unittest

from context_atlas.domain.errors import ContextAtlasError, ErrorCode
from context_atlas.domain.messages import LogMessage
from context_atlas.domain.models import (
    AuthorityPrecedenceReasonCode,
    ContextDecisionAction,
    ContextSource,
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceFamily,
    ContextSourceProvenance,
    ExclusionReasonCode,
)
from context_atlas.domain.policies import StarterCandidateRankingPolicy
from context_atlas.infrastructure.logging import log_assembly_stage_message
from context_atlas.adapters import (
    InMemorySourceRegistry,
    LexicalRetrievalMode,
    LexicalRetriever,
)


class CandidateRankingTests(unittest.TestCase):
    """Verify the PR 4 ranking and decision-trace slice."""

    def setUp(self) -> None:
        self.registry = InMemorySourceRegistry(
            (
                ContextSource(
                    source_id="authoritative-architecture",
                    title="Architecture",
                    content=(
                        "Architecture authority ranking and packet governance should "
                        "prefer durable authoritative guidance."
                    ),
                    source_class=ContextSourceClass.AUTHORITATIVE,
                    authority=ContextSourceAuthority.BINDING,
                ),
                ContextSource(
                    source_id="planning-architecture",
                    title="Planning Notes",
                    content=(
                        "Architecture authority ranking and packet governance should "
                        "prefer durable authoritative guidance."
                    ),
                    source_class=ContextSourceClass.PLANNING,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
                ContextSource(
                    source_id="advisory-overview",
                    title="Overview",
                    content=(
                        "Overview context notes mention architecture and ranking but "
                        "carry less authority."
                    ),
                    source_class=ContextSourceClass.REVIEWS,
                    authority=ContextSourceAuthority.ADVISORY,
                ),
            )
        )

    def test_ranking_prefers_higher_authority_and_records_deduplication(self) -> None:
        retriever = LexicalRetriever(self.registry, mode=LexicalRetrievalMode.KEYWORD)
        candidates = retriever.retrieve(
            "architecture authority ranking governance", top_k=3
        )

        outcome = StarterCandidateRankingPolicy().rank_candidates(
            candidates,
            trace_id="trace-ranking-1",
        )

        self.assertEqual(len(outcome.ranked_candidates), 2)
        self.assertEqual(
            outcome.ranked_candidates[0].source.source_id,
            "authoritative-architecture",
        )
        self.assertEqual(outcome.ranked_candidates[0].rank, 1)
        self.assertEqual(
            outcome.trace.metadata["deduplicated_candidate_count"],
            "1",
        )

        duplicate_decisions = [
            decision
            for decision in outcome.trace.decisions
            if decision.action is ContextDecisionAction.EXCLUDED
        ]
        self.assertEqual(len(duplicate_decisions), 1)
        self.assertIn(
            ExclusionReasonCode.DUPLICATE, duplicate_decisions[0].reason_codes
        )
        self.assertIn(
            AuthorityPrecedenceReasonCode.LOWER_AUTHORITY_DEMOTED,
            duplicate_decisions[0].reason_codes,
        )

    def test_ranking_uses_deterministic_source_id_tiebreaker(self) -> None:
        tie_registry = InMemorySourceRegistry(
            (
                ContextSource(
                    source_id="alpha-source",
                    content="retrieval ranking policy tie breaker alpha",
                    authority=ContextSourceAuthority.ADVISORY,
                ),
                ContextSource(
                    source_id="beta-source",
                    content="retrieval ranking policy tie breaker beta",
                    authority=ContextSourceAuthority.ADVISORY,
                ),
            )
        )
        retriever = LexicalRetriever(tie_registry, mode=LexicalRetrievalMode.KEYWORD)
        candidates = retriever.retrieve("retrieval ranking policy tie breaker", top_k=2)

        outcome = StarterCandidateRankingPolicy().rank_candidates(
            candidates,
            trace_id="trace-ranking-2",
        )

        self.assertEqual(
            [candidate.source.source_id for candidate in outcome.ranked_candidates],
            ["alpha-source", "beta-source"],
        )

    def test_ranking_deduplicates_case_and_whitespace_variants(self) -> None:
        registry = InMemorySourceRegistry(
            (
                ContextSource(
                    source_id="authoritative-shape",
                    content=(
                        "Atlas duplicate handling should prefer bounded lexical "
                        "normalization."
                    ),
                    source_class=ContextSourceClass.AUTHORITATIVE,
                    authority=ContextSourceAuthority.BINDING,
                ),
                ContextSource(
                    source_id="planning-shape",
                    content=(
                        "  atlas   duplicate handling should prefer bounded lexical "
                        "normalization.  "
                    ),
                    source_class=ContextSourceClass.PLANNING,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
            )
        )
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.KEYWORD)
        candidates = retriever.retrieve(
            "duplicate handling lexical normalization",
            top_k=2,
        )

        outcome = StarterCandidateRankingPolicy().rank_candidates(
            candidates,
            trace_id="trace-ranking-2b",
        )

        self.assertEqual(
            tuple(
                candidate.source.source_id for candidate in outcome.ranked_candidates
            ),
            ("authoritative-shape",),
        )
        self.assertEqual(
            outcome.trace.metadata["deduplicated_candidate_count"],
            "1",
        )

    def test_ranking_deduplicates_matching_bodies_despite_front_matter(self) -> None:
        registry = InMemorySourceRegistry(
            (
                ContextSource(
                    source_id="authoritative-front-matter",
                    content=(
                        "---\n"
                        "title: Atlas Canon\n"
                        "owners: [core]\n"
                        "---\n"
                        "Atlas duplicate handling should stay traceable after "
                        "front matter normalization."
                    ),
                    source_class=ContextSourceClass.AUTHORITATIVE,
                    authority=ContextSourceAuthority.BINDING,
                ),
                ContextSource(
                    source_id="planning-front-matter",
                    content=(
                        "---\n"
                        "title: Working Notes\n"
                        "owners: [planning]\n"
                        "---\n"
                        "Atlas duplicate handling should stay traceable after "
                        "front matter normalization."
                    ),
                    source_class=ContextSourceClass.PLANNING,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
            )
        )
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.KEYWORD)
        candidates = retriever.retrieve(
            "duplicate handling traceable front matter normalization",
            top_k=2,
        )

        outcome = StarterCandidateRankingPolicy().rank_candidates(
            candidates,
            trace_id="trace-ranking-2c",
        )

        self.assertEqual(
            tuple(
                candidate.source.source_id for candidate in outcome.ranked_candidates
            ),
            ("authoritative-front-matter",),
        )
        self.assertEqual(outcome.trace.metadata["deduplicated_candidate_count"], "1")

    def test_ranking_keeps_distinct_metadata_only_sources(self) -> None:
        registry = InMemorySourceRegistry(
            (
                ContextSource(
                    source_id="metadata-only-authoritative",
                    content=(
                        "---\n"
                        "title: Atlas Canon\n"
                        "owners: [core]\n"
                        "status: approved\n"
                        "---\n"
                    ),
                    source_class=ContextSourceClass.AUTHORITATIVE,
                    authority=ContextSourceAuthority.BINDING,
                ),
                ContextSource(
                    source_id="metadata-only-planning",
                    content=(
                        "---\n"
                        "title: Atlas Working Notes\n"
                        "owners: [planning]\n"
                        "status: draft\n"
                        "---\n"
                    ),
                    source_class=ContextSourceClass.PLANNING,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
            )
        )
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.KEYWORD)
        candidates = retriever.retrieve("atlas title status owners", top_k=2)

        outcome = StarterCandidateRankingPolicy().rank_candidates(
            candidates,
            trace_id="trace-ranking-2d",
        )

        self.assertEqual(
            tuple(
                candidate.source.source_id for candidate in outcome.ranked_candidates
            ),
            ("metadata-only-authoritative", "metadata-only-planning"),
        )
        self.assertEqual(outcome.trace.metadata["deduplicated_candidate_count"], "0")

    def test_ranking_deduplicates_reordered_token_variants(self) -> None:
        registry = InMemorySourceRegistry(
            (
                ContextSource(
                    source_id="authoritative-token-overlap",
                    content=(
                        "Atlas retains durable planning context when the ranking "
                        "policy keeps duplicate governance deterministic."
                    ),
                    source_class=ContextSourceClass.AUTHORITATIVE,
                    authority=ContextSourceAuthority.BINDING,
                ),
                ContextSource(
                    source_id="planning-token-overlap",
                    content=(
                        "Ranking policy keeps duplicate governance deterministic "
                        "when Atlas retains durable planning context."
                    ),
                    source_class=ContextSourceClass.PLANNING,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
            )
        )
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.KEYWORD)
        candidates = retriever.retrieve(
            "atlas ranking duplicate governance durable planning context",
            top_k=2,
        )

        outcome = StarterCandidateRankingPolicy(
            dedup_threshold=0.72,
        ).rank_candidates(
            candidates,
            trace_id="trace-ranking-2e",
        )

        self.assertEqual(
            tuple(
                candidate.source.source_id for candidate in outcome.ranked_candidates
            ),
            ("authoritative-token-overlap",),
        )
        self.assertEqual(outcome.trace.metadata["deduplicated_candidate_count"], "1")
        duplicate_decision = next(
            decision
            for decision in outcome.trace.decisions
            if decision.source_id == "planning-token-overlap"
        )
        self.assertEqual(duplicate_decision.action, ContextDecisionAction.EXCLUDED)
        self.assertIn("token_overlap", duplicate_decision.explanation or "")

    def test_ranking_keeps_matching_content_across_source_families(self) -> None:
        registry = InMemorySourceRegistry(
            (
                ContextSource(
                    source_id="document-review",
                    content=(
                        "Shared review evidence should stay canonical across "
                        "source families."
                    ),
                    source_class=ContextSourceClass.REVIEWS,
                    authority=ContextSourceAuthority.ADVISORY,
                    provenance=ContextSourceProvenance(
                        source_family=ContextSourceFamily.DOCUMENT,
                    ),
                ),
                ContextSource(
                    source_id="record-review",
                    content=(
                        "Shared review evidence should stay canonical across "
                        "source families."
                    ),
                    source_class=ContextSourceClass.REVIEWS,
                    authority=ContextSourceAuthority.ADVISORY,
                    provenance=ContextSourceProvenance(
                        source_family=ContextSourceFamily.STRUCTURED_RECORD,
                    ),
                ),
            )
        )
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.KEYWORD)
        candidates = retriever.retrieve(
            "shared review evidence canonical source families",
            top_k=2,
        )

        outcome = StarterCandidateRankingPolicy().rank_candidates(
            candidates,
            trace_id="trace-ranking-2f",
        )

        self.assertEqual(
            tuple(
                candidate.source.source_id for candidate in outcome.ranked_candidates
            ),
            ("document-review", "record-review"),
        )
        self.assertEqual(outcome.trace.metadata["deduplicated_candidate_count"], "0")

    def test_ranking_keeps_shared_header_entries_with_distinct_bodies(self) -> None:
        shared_prefix = (
            "---\n"
            "doc_class: guide\n"
            "owners: [core]\n"
            "---\n"
            "# Context Atlas Hardening\n"
            "Audience: Internal\n"
            "Workflow: Hardening\n"
        )
        registry = InMemorySourceRegistry(
            (
                ContextSource(
                    source_id="authoritative-shared-header",
                    content=shared_prefix
                    + (
                        "\n"
                        "Duplicate normalization should strip front matter before "
                        "comparison.\n"
                        "This note focuses on repeated header handling in governed "
                        "docs."
                    ),
                    source_class=ContextSourceClass.AUTHORITATIVE,
                    authority=ContextSourceAuthority.BINDING,
                ),
                ContextSource(
                    source_id="planning-shared-header",
                    content=shared_prefix
                    + (
                        "\n"
                        "Token estimation should stay provider-agnostic and query "
                        "aware.\n"
                        "This note focuses on tokenizer seams rather than duplicate "
                        "handling."
                    ),
                    source_class=ContextSourceClass.PLANNING,
                    authority=ContextSourceAuthority.PREFERRED,
                ),
            )
        )
        retriever = LexicalRetriever(registry, mode=LexicalRetrievalMode.KEYWORD)
        candidates = retriever.retrieve(
            "context atlas hardening workflow duplicate token estimation",
            top_k=2,
        )

        outcome = StarterCandidateRankingPolicy(dedup_threshold=0.72).rank_candidates(
            candidates,
            trace_id="trace-ranking-2g",
        )

        self.assertCountEqual(
            tuple(
                candidate.source.source_id for candidate in outcome.ranked_candidates
            ),
            ("authoritative-shared-header", "planning-shared-header"),
        )
        self.assertEqual(outcome.trace.metadata["deduplicated_candidate_count"], "0")

    def test_ranking_limit_records_excluded_candidates(self) -> None:
        retriever = LexicalRetriever(self.registry, mode=LexicalRetrievalMode.TFIDF)
        candidates = retriever.retrieve(
            "architecture authority ranking overview", top_k=3
        )

        outcome = StarterCandidateRankingPolicy().rank_candidates(
            candidates,
            trace_id="trace-ranking-3",
            limit=1,
        )

        self.assertEqual(len(outcome.ranked_candidates), 1)
        excluded_decisions = [
            decision
            for decision in outcome.trace.decisions
            if decision.action is ContextDecisionAction.EXCLUDED
        ]
        self.assertEqual(len(excluded_decisions), 2)
        self.assertEqual(outcome.trace.metadata["included_candidate_count"], "1")

    def test_ranking_policy_validates_configuration_inputs(self) -> None:
        with self.assertRaises(ContextAtlasError) as invalid_dedup_threshold:
            StarterCandidateRankingPolicy(dedup_threshold=1.1)

        self.assertEqual(
            invalid_dedup_threshold.exception.code,
            ErrorCode.INVALID_RANKING_REQUEST,
        )

        with self.assertRaises(ContextAtlasError) as invalid_score:
            StarterCandidateRankingPolicy(minimum_score=float("nan"))

        self.assertEqual(
            invalid_score.exception.code,
            ErrorCode.INVALID_RANKING_REQUEST,
        )

    def test_ranking_stage_events_have_stable_templates_and_fields(self) -> None:
        logger = logging.getLogger("context_atlas.tests.ranking")
        logger.handlers.clear()
        stream = io.StringIO()
        handler = logging.StreamHandler(stream)
        handler.setFormatter(
            logging.Formatter("%(event)s|%(trace_id)s|%(decision_count)s|%(message)s")
        )
        logger.handlers = [handler]
        logger.setLevel(logging.INFO)
        logger.propagate = False

        log_assembly_stage_message(
            logger,
            logging.INFO,
            LogMessage.DECISIONS_RECORDED,
            trace_id="trace-ranking-4",
            message_args=("trace-ranking-4", 3),
            decision_count=3,
        )

        self.assertEqual(
            stream.getvalue().strip(),
            "decisions_recorded|trace-ranking-4|3|"
            "Decisions recorded: trace_id=trace-ranking-4, decision_count=3",
        )
        self.assertEqual(
            LogMessage.CANDIDATES_DEDUPED,
            "Candidates deduped: trace_id=%s, removed_candidates=%d",
        )


if __name__ == "__main__":
    unittest.main()
