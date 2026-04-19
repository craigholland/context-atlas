"""Supported starter composition helpers for Context Atlas.

This module defines the current MVP-facing assembly entrypoint that wires
validated runtime settings and logging into the shared assembly service.
The curated ``context_atlas.api`` surface re-exports this helper for callers
who do not need to learn the deeper package layout yet.

This module owns starter wiring only. It should return configured orchestration
services and leave packet rendering or inspection concerns to
``context_atlas.rendering``.
"""

from __future__ import annotations

import logging

from ..domain.policies import (
    StarterBudgetAllocationPolicy,
    StarterCandidateRankingPolicy,
    StarterCompressionPolicy,
    StarterMemoryRetentionPolicy,
)
from ..services.assembly import CandidateRetriever, ContextAssemblyService
from .config import ContextAtlasSettings
from .logging import configure_logger


def build_starter_context_assembly_service(
    *,
    retriever: CandidateRetriever,
    settings: ContextAtlasSettings | None = None,
    logger: logging.Logger | None = None,
) -> ContextAssemblyService:
    """Build the supported starter assembly service from validated settings.

    This is the preferred composition boundary for the current MVP starter flow.
    Callers should prefer this helper to hand-wiring policies from deeper
    modules when they only need the supported default assembly path. This helper
    intentionally stops at configured orchestration; it does not render packet
    context or inspection views.
    """

    active_settings = settings or ContextAtlasSettings()
    active_logger = logger or configure_logger(active_settings.logging)

    return ContextAssemblyService(
        retriever=retriever,
        ranking_policy=StarterCandidateRankingPolicy(
            minimum_score=active_settings.assembly.ranking_minimum_score,
        ),
        budget_policy=StarterBudgetAllocationPolicy(),
        compression_policy=StarterCompressionPolicy(
            strategy=active_settings.assembly.default_compression_strategy,
            chars_per_token=active_settings.assembly.compression_chars_per_token,
            min_chunk_chars=active_settings.assembly.compression_min_chunk_chars,
        ),
        memory_policy=StarterMemoryRetentionPolicy(
            short_term_count=active_settings.memory.short_term_count,
            decay_rate=active_settings.memory.decay_rate,
            dedup_threshold=active_settings.memory.dedup_threshold,
            min_effective_score=active_settings.memory.min_effective_score,
            query_boost_weight=active_settings.memory.query_boost_weight,
        ),
        logger=active_logger,
        default_top_k=active_settings.assembly.default_retrieval_top_k,
        default_total_budget=active_settings.assembly.default_total_budget,
    )


__all__ = ["build_starter_context_assembly_service"]
