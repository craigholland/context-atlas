"""Outer-layer assembly helpers that wire services to runtime settings."""

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
    """Build the starter assembly service from validated runtime settings."""

    active_settings = settings or ContextAtlasSettings()
    active_logger = logger or configure_logger(active_settings.logging)

    return ContextAssemblyService(
        retriever=retriever,
        ranking_policy=StarterCandidateRankingPolicy(),
        budget_policy=StarterBudgetAllocationPolicy(),
        compression_policy=StarterCompressionPolicy(
            strategy=active_settings.assembly.default_compression_strategy
        ),
        memory_policy=StarterMemoryRetentionPolicy(
            short_term_count=active_settings.memory.short_term_count,
            decay_rate=active_settings.memory.decay_rate,
            dedup_threshold=active_settings.memory.dedup_threshold,
        ),
        logger=active_logger,
        default_top_k=active_settings.assembly.default_retrieval_top_k,
        default_total_budget=active_settings.assembly.default_total_budget,
    )


__all__ = ["build_starter_context_assembly_service"]
