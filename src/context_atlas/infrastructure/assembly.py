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
import json
import logging
from pathlib import Path

from ..adapters import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetriever,
)
from ..domain.models import (
    ContextBudget,
    ContextMemoryEntry,
    ContextPacket,
    ContextSource,
)
from ..domain.policies import (
    StarterBudgetAllocationPolicy,
    StarterCandidateRankingPolicy,
    StarterCompressionPolicy,
    StarterMemoryRetentionPolicy,
    TokenEstimator,
)
from ..services.assembly import CandidateRetriever, ContextAssemblyService
from .config import ContextAtlasSettings, build_low_code_workflow_plan
from .logging import configure_logger


def build_starter_context_assembly_service(
    *,
    retriever: CandidateRetriever,
    settings: ContextAtlasSettings | None = None,
    logger: logging.Logger | None = None,
    token_estimator: TokenEstimator | None = None,
    token_estimator_name: str | None = None,
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
    active_token_estimator_name = token_estimator_name or (
        "external_binding"
        if token_estimator is not None
        else active_settings.assembly.compression_token_estimator_name
    )

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
            token_estimator=token_estimator,
            token_estimator_name=active_token_estimator_name,
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
        default_memory_budget_fraction=(
            active_settings.assembly.default_memory_budget_fraction
        ),
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
    metadata: Mapping[str, object] | None = None,
    now_epoch_seconds: float | None = None,
    token_estimator: TokenEstimator | None = None,
    token_estimator_name: str | None = None,
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
        token_estimator=token_estimator,
        token_estimator_name=token_estimator_name,
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


def assemble_with_starter_sources(
    *,
    sources: Iterable[ContextSource],
    query: str,
    settings: ContextAtlasSettings | None = None,
    logger: logging.Logger | None = None,
    budget: ContextBudget | None = None,
    memory_entries: Iterable[ContextMemoryEntry] = (),
    top_k: int | None = None,
    packet_id: str | None = None,
    trace_id: str | None = None,
    metadata: Mapping[str, object] | None = None,
    now_epoch_seconds: float | None = None,
    token_estimator: TokenEstimator | None = None,
    token_estimator_name: str | None = None,
) -> ContextPacket:
    """Assemble one packet from canonical sources through the shared starter path."""

    source_registry = InMemorySourceRegistry(tuple(sources))
    return assemble_with_starter_context_service(
        retriever=LexicalRetriever(source_registry),
        query=query,
        settings=settings,
        logger=logger,
        budget=budget,
        memory_entries=memory_entries,
        top_k=top_k,
        packet_id=packet_id,
        trace_id=trace_id,
        metadata=metadata,
        now_epoch_seconds=now_epoch_seconds,
        token_estimator=token_estimator,
        token_estimator_name=token_estimator_name,
    )


def assemble_with_low_code_workflow(
    *,
    query: str,
    settings: ContextAtlasSettings | None = None,
    logger: logging.Logger | None = None,
    repo_root: Path | str | None = None,
    top_k: int | None = None,
    packet_id: str | None = None,
    trace_id: str | None = None,
    metadata: Mapping[str, object] | None = None,
    now_epoch_seconds: float | None = None,
    token_estimator: TokenEstimator | None = None,
    token_estimator_name: str | None = None,
) -> ContextPacket:
    """Assemble one packet through the supported low-code wrapper path.

    This helper stays in the outer layer on purpose. It chooses one supported
    preset, translates enabled sources into canonical Atlas inputs, and then
    delegates packet creation to the same starter assembly path used elsewhere.
    """

    active_settings = settings or ContextAtlasSettings()
    active_low_code = active_settings.low_code
    active_repo_root = Path.cwd() if repo_root is None else Path(repo_root)
    active_repo_root = active_repo_root.resolve()
    plan = build_low_code_workflow_plan(
        low_code_settings=active_low_code,
        repo_root=active_repo_root,
    )

    sources: list[ContextSource] = []
    workflow_metadata = plan.build_request_metadata(metadata)

    if plan.docs_root is not None:
        document_sources = FilesystemDocumentSourceAdapter(
            plan.docs_root
        ).load_sources()
        sources.extend(document_sources)
    if plan.records_file is not None:
        payload = json.loads(plan.records_file.read_text(encoding="utf-8"))
        if not isinstance(payload, list):
            raise TypeError(
                "Low-code records payload must be a JSON array of row objects."
            )
        record_rows = tuple(row for row in payload if isinstance(row, Mapping))
        if len(record_rows) != len(payload):
            raise TypeError(
                "Low-code records payload must contain only mapping-shaped rows."
            )
        record_sources = plan.load_record_sources(record_rows)
        sources.extend(record_sources)
        workflow_metadata["record_origin"] = "payload_file"
        workflow_metadata["record_input_count"] = len(record_rows)

    return assemble_with_starter_sources(
        sources=tuple(sources),
        query=query,
        settings=active_settings,
        logger=logger,
        top_k=top_k,
        packet_id=packet_id,
        trace_id=trace_id,
        metadata=workflow_metadata,
        now_epoch_seconds=now_epoch_seconds,
        token_estimator=token_estimator,
        token_estimator_name=token_estimator_name,
    )


def write_standard_proof_artifacts(
    *,
    output_dir: Path,
    packet: ContextPacket,
    rendered_context: str,
) -> Path:
    """Write the standard proof-artifact set for one canonical workflow run.

    This helper stays in infrastructure because it packages the canonical packet
    and trace artifacts emitted by the shared engine without changing their
    meaning. Workflow examples may call it, but they should not each maintain
    their own proof-only artifact writer.
    """

    resolved_output_dir = output_dir.resolve()
    resolved_output_dir.mkdir(parents=True, exist_ok=True)
    (resolved_output_dir / "atlas_rendered_context.txt").write_text(
        rendered_context,
        encoding="utf-8",
    )
    (resolved_output_dir / "atlas_packet.json").write_text(
        json.dumps(packet.model_dump(mode="json"), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (resolved_output_dir / "atlas_trace.json").write_text(
        json.dumps(
            packet.trace.model_dump(mode="json") if packet.trace is not None else None,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return resolved_output_dir


__all__ = [
    "assemble_with_low_code_workflow",
    "assemble_with_starter_sources",
    "assemble_with_starter_context_service",
    "build_starter_context_assembly_service",
    "write_standard_proof_artifacts",
]
