"""Recommended first-run example for the Context Atlas MVP starter flow."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from context_atlas.api import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetriever,
    build_starter_context_assembly_service,
    load_settings_from_env,
    render_packet_context,
)
from context_atlas.rendering import (
    render_packet_inspection,
    render_trace_inspection,
)

DEFAULT_QUERY = "How should planning docs be treated?"
DEFAULT_LOG_LEVEL = "WARNING"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the recommended Context Atlas getting-started flow.",
    )
    parser.add_argument(
        "docs_root",
        nargs="?",
        default="docs",
        help="Path to the documentation root to ingest. Defaults to ./docs.",
    )
    parser.add_argument(
        "query",
        nargs="?",
        default=DEFAULT_QUERY,
        help="Question or task query to assemble context for.",
    )
    args = parser.parse_args()

    docs_root = Path(args.docs_root)
    if "CONTEXT_ATLAS_LOG_LEVEL" not in os.environ:
        os.environ["CONTEXT_ATLAS_LOG_LEVEL"] = DEFAULT_LOG_LEVEL
    settings = load_settings_from_env()
    sources = FilesystemDocumentSourceAdapter(docs_root).load_sources()
    retriever = LexicalRetriever(InMemorySourceRegistry(sources))
    assembly_service = build_starter_context_assembly_service(
        retriever=retriever,
        settings=settings,
    )

    packet = assembly_service.assemble(query=args.query)

    print(f"Running starter flow against: {docs_root}")
    print(f"Query: {args.query}")
    print()
    print("=== Rendered Context ===")
    print(render_packet_context(packet))
    print()
    print("=== Packet Inspection ===")
    print(render_packet_inspection(packet))
    print()
    print("=== Trace Inspection ===")
    if packet.trace is None:
        print("Trace\n- none")
    else:
        print(render_trace_inspection(packet.trace))


if __name__ == "__main__":
    main()
