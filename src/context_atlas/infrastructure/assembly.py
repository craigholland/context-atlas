"""Supported starter composition helpers for Context Atlas.

This module defines the current MVP-facing assembly entrypoint that wires
validated runtime settings and logging into the shared assembly service.
The curated ``context_atlas.api`` surface re-exports this helper for callers
who do not need to learn the deeper package layout yet.

This module owns starter wiring only. It should return configured orchestration
services and leave packet rendering or inspection concerns to
``context_atlas.rendering``.

For repository-oriented or mixed-source workflows such as the flagship Codex
path and the technical-builder docs-plus-database path, the current
composition boundary is intentionally explicit:

- outer workflow code chooses the governed docs or record-backed inputs
- outer workflow code translates those inputs into a `CandidateRetriever`
- this module wires the shared policies, settings, and logger into the
  canonical assembly service

That keeps repository-specific source collection outside the engine while still
making the shared assembly path easy to reuse.

The runnable example under ``examples/codex_repository_workflow/`` is the
current reference implementation of that outer workflow composition.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
import logging

from ..domain.models import ContextBudget, ContextMemoryEntry, ContextPacket
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
    modules when they only need the supported default assembly path.

    For the current Codex repository workflow and the technical-builder
    docs-plus-database workflow, this helper should sit after outer workflow
    code has already resolved docs and/or record-backed inputs into a
    retriever over canonical Atlas sources. It intentionally stops at
    configured orchestration; it does not choose workflow inputs, own row
    mapping conventions, execute database access, render packet context, or
    render inspection views.
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


def assemble_with_starter_context_service(
    *,
    retriever: CandidateRetriever,
    query: str,
    settings: ContextAtlasSettings | None = None,
    logger: logging.Logger | None = None,
    budget: ContextBudget | None = None,
    memory_entries: Iterable[ContextMemoryEntry] = (),
    top_k: int | None = None,
    packet_id: str | None = None,
    trace_id: str | None = None,
    metadata: Mapping[str, str] | None = None,
    now_epoch_seconds: float | None = None,
) -> ContextPacket:
    """Build the supported starter service and assemble one canonical packet.

    This remains a workflow-agnostic outer composition helper. Callers still
    choose retrievers, queries, any record/database access they own, and any
    outer-workflow metadata; the helper just keeps supported starter wiring in
    one place.
    """

    service = build_starter_context_assembly_service(
        retriever=retriever,
        settings=settings,
        logger=logger,
    )
    return service.assemble(
        query=query,
        budget=budget,
        memory_entries=memory_entries,
        top_k=top_k,
        packet_id=packet_id,
        trace_id=trace_id,
        metadata=metadata,
        now_epoch_seconds=now_epoch_seconds,
    )


__all__ = [
    "assemble_with_starter_context_service",
    "build_starter_context_assembly_service",
]
