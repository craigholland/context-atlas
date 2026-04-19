"""Example mixed-source registry flow for Context Atlas."""

from __future__ import annotations

from pathlib import Path

from context_atlas.adapters import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetrievalMode,
    LexicalRetriever,
    StructuredRecordRowMapper,
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
    already_fetched_rows = (
        {
            "external_id": "product-1",
            "body": (
                "Structured product record describing pricing policy, support "
                "escalation, and release readiness."
            ),
            "name": "Product 1",
            "uri": "records://products/1",
            "uses": ("answering", "comparison"),
            "table": "products",
            "database": "atlas_app",
        },
        {
            "external_id": "ticket-42",
            "body": (
                "Support ticket record describing packet budgeting concerns "
                "and escalation ownership."
            ),
            "name": "Ticket 42",
            "uri": "records://tickets/42",
            "uses": ("triage",),
            "table": "tickets",
            "database": "atlas_app",
        },
    )
    record_mapper = StructuredRecordRowMapper(
        record_id_field="external_id",
        content_field="body",
        title_field="name",
        source_uri_field="uri",
        intended_uses_field="uses",
        metadata_fields=("table",),
        provenance_fields=("database",),
    )
    record_sources = StructuredRecordSourceAdapter().load_sources(
        record_mapper.to_record_inputs(already_fetched_rows)
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

    print(
        "\nRecord adapter boundary:"
        " rows were shaped before translation; Atlas did not fetch them."
    )


if __name__ == "__main__":
    main()
