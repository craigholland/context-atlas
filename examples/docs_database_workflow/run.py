"""Runnable docs-plus-database workflow over the shared Atlas engine.

This example is intentionally an outer workflow composition path:

- the workflow chooses governed docs and already-fetched record rows
- Atlas adapters translate those inputs into canonical sources
- the shared assembly service builds one packet and one trace

It should demonstrate a mixed-source pipeline without turning Atlas into a
database access framework.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any

from context_atlas.adapters import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetriever,
    StructuredRecordRowMapper,
    StructuredRecordSourceAdapter,
)
from context_atlas.domain.models import ContextPacket
from context_atlas.infrastructure.assembly import assemble_with_starter_context_service
from context_atlas.infrastructure.config import load_settings_from_env
from context_atlas.rendering import (
    render_packet_context,
    render_packet_inspection,
    render_trace_highlights,
    render_trace_inspection,
)

try:
    from examples.docs_database_workflow.record_feed import (
        load_record_rows,
        resolve_records_file,
    )
except ModuleNotFoundError:
    from record_feed import load_record_rows, resolve_records_file

DEFAULT_QUERY = (
    "How should a builder configure Context Atlas and troubleshoot preflight "
    "or environment-loading issues in a chatbot pipeline?"
)
DEFAULT_LOG_LEVEL = "WARNING"
CHATBOT_CONTEXT_HEADER = "Chatbot Context"
RECORD_BATCH_NAME = "demo_support_rows"


def build_parser() -> argparse.ArgumentParser:
    """Build the supported CLI surface for the docs-plus-database workflow."""

    parser = argparse.ArgumentParser(
        description=(
            "Run the technical-builder docs-plus-database workflow over governed "
            "docs and already-fetched record payloads."
        ),
        epilog=(
            "This example keeps database access outside Atlas. The script uses "
            "repo guide docs plus in-memory support-style rows as a demo "
            "stand-in for already-fetched records."
        ),
    )
    parser.add_argument(
        "--docs-root",
        type=Path,
        default=None,
        help="Optional docs root. Defaults to this repository's docs/Guides directory.",
    )
    parser.add_argument(
        "--query",
        default=DEFAULT_QUERY,
        help="Chatbot question to assemble context for.",
    )
    parser.add_argument(
        "--records-file",
        type=Path,
        default=None,
        help=(
            "Optional JSON file containing already-fetched record rows. Defaults "
            "to this example's sample_records.json file."
        ),
    )
    return parser


def assemble_docs_database_workflow_packet(
    *,
    docs_root_arg: Path | None,
    records_file_arg: Path | None,
    query: str,
) -> tuple[Path, Path, int, ContextPacket]:
    """Run one mixed-source workflow composition over the shared engine path."""

    docs_root = _resolve_docs_root(docs_root_arg)
    records_file = resolve_records_file(records_file_arg)
    record_rows = load_record_rows(records_file)
    record_inputs = _build_record_inputs(record_rows)

    if "CONTEXT_ATLAS_LOG_LEVEL" not in os.environ:
        os.environ["CONTEXT_ATLAS_LOG_LEVEL"] = DEFAULT_LOG_LEVEL

    settings = load_settings_from_env()
    document_sources = FilesystemDocumentSourceAdapter(docs_root).load_sources()
    record_sources = StructuredRecordSourceAdapter(
        collector_name="docs_database_demo_records"
    ).load_sources(record_inputs)
    packet = assemble_with_starter_context_service(
        retriever=LexicalRetriever(
            InMemorySourceRegistry((*document_sources, *record_sources)),
        ),
        query=query,
        settings=settings,
        top_k=8,
        metadata={
            "workflow": "docs_database_builder",
            "docs_root": docs_root.as_posix(),
            "record_batch": RECORD_BATCH_NAME,
            "records_file": records_file.as_posix(),
            "record_input_count": str(len(record_inputs)),
            "record_origin": "already_fetched_rows",
        },
    )
    return docs_root, records_file, len(record_inputs), packet


def main() -> None:
    args = build_parser().parse_args()
    docs_root, records_file, record_count, packet = (
        assemble_docs_database_workflow_packet(
            docs_root_arg=args.docs_root,
            records_file_arg=args.records_file,
            query=args.query,
        )
    )

    print(f"Governed docs root: {docs_root}")
    print(f"Records file: {records_file}")
    print(f"Record batch: {RECORD_BATCH_NAME} ({record_count} already-fetched rows)")
    print(f"Query: {args.query}")
    print()
    print("=== Chatbot Context ===")
    print(
        render_packet_context(
            packet,
            include_section_headers=True,
            context_header=CHATBOT_CONTEXT_HEADER,
        )
    )
    print()
    print("=== Packet Inspection ===")
    print(render_packet_inspection(packet))
    print()
    print("=== Trace Highlights ===")
    if packet.trace is None:
        print("Trace Highlights\n- none")
    else:
        print(render_trace_highlights(packet.trace))
    print()
    print("=== Trace Inspection ===")
    if packet.trace is None:
        print("Trace\n- none")
    else:
        print(render_trace_inspection(packet.trace))
    print()
    print(
        "Record boundary note: outer application code fetched and shaped the "
        "record rows before Atlas translated them into canonical sources."
    )


def _resolve_docs_root(docs_root_arg: Path | None) -> Path:
    """Resolve the governed docs root for the runnable demo."""

    if docs_root_arg is not None:
        return docs_root_arg.resolve()
    return (Path(__file__).resolve().parents[2] / "docs" / "Guides").resolve()


def _build_record_inputs(
    rows: tuple[dict[str, Any], ...],
):
    """Shape already-fetched rows at the outer workflow boundary."""

    mapper = StructuredRecordRowMapper(
        record_id_field="ticket_id",
        content_field="body",
        title_field="title",
        source_uri_field="uri",
        intended_uses_field="uses",
        metadata_fields=("team", "table"),
        provenance_fields=("database",),
        source_class="reviews",
        authority="preferred",
    )
    return mapper.to_record_inputs(rows)


if __name__ == "__main__":
    main()
