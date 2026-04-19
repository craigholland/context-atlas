"""Example mixed-source registry flow for Context Atlas."""

from __future__ import annotations

from pathlib import Path

from context_atlas.adapters import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetrievalMode,
    LexicalRetriever,
    StructuredRecordInput,
    StructuredRecordSourceAdapter,
)
from context_atlas.infrastructure import build_starter_context_assembly_service
from context_atlas.infrastructure.config import (
    AssemblySettings,
    ContextAtlasSettings,
    LoggingSettings,
    MemorySettings,
)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    docs_root = repo_root / "docs"

    document_sources = FilesystemDocumentSourceAdapter(docs_root).load_sources()
    record_sources = StructuredRecordSourceAdapter().load_sources(
        (
            StructuredRecordInput(
                record_id="product-1",
                content=(
                    "Structured product record describing pricing policy, support "
                    "escalation, and release readiness."
                ),
                title="Product 1",
                source_uri="records://products/1",
                intended_uses=("answering", "comparison"),
                metadata={"table": "products"},
                provenance_metadata={"database": "atlas_app"},
            ),
            StructuredRecordInput(
                record_id="ticket-42",
                content=(
                    "Support ticket record describing packet budgeting concerns "
                    "and escalation ownership."
                ),
                title="Ticket 42",
                source_uri="records://tickets/42",
                intended_uses=("triage",),
                metadata={"table": "tickets"},
                provenance_metadata={"database": "atlas_app"},
            ),
        )
    )

    registry = InMemorySourceRegistry((*document_sources, *record_sources))
    service = build_starter_context_assembly_service(
        retriever=LexicalRetriever(registry, mode=LexicalRetrievalMode.TFIDF),
        settings=ContextAtlasSettings(
            logging=LoggingSettings(
                logger_name="context_atlas.examples.mixed_sources",
                level="WARNING",
            ),
            assembly=AssemblySettings(
                default_total_budget=240,
                default_retrieval_top_k=6,
            ),
            memory=MemorySettings(),
        ),
    )

    packet = service.assemble(query="packet budgeting escalation policy")

    print("Selected sources:")
    for candidate in packet.selected_candidates:
        source = candidate.source
        print(
            "- "
            f"{source.source_id} | family={source.provenance.source_family.value} | "
            f"class={source.source_class.value} | collector={source.provenance.collector}"
        )

    print("\nTrace collectors:")
    print(packet.trace.metadata.get("selected_source_collectors", "<none>"))


if __name__ == "__main__":
    main()
