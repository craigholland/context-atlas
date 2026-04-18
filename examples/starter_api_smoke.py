"""Small starter-flow smoke example using the curated Context Atlas API."""

from __future__ import annotations

import argparse
from pathlib import Path

from context_atlas.api import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetriever,
    build_starter_context_assembly_service,
    load_settings_from_env,
    render_packet_context,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Assemble a starter Context Atlas packet from a docs directory.",
    )
    parser.add_argument(
        "docs_root",
        type=Path,
        help="Path to the documentation root to ingest.",
    )
    parser.add_argument(
        "query",
        help="The question or task query to assemble context for.",
    )
    args = parser.parse_args()

    settings = load_settings_from_env()
    sources = FilesystemDocumentSourceAdapter(args.docs_root).load_sources()
    retriever = LexicalRetriever(InMemorySourceRegistry(sources))
    assembly_service = build_starter_context_assembly_service(
        retriever=retriever,
        settings=settings,
    )

    packet = assembly_service.assemble(query=args.query)

    print("=== Rendered Context ===")
    print(render_packet_context(packet))
    print()
    print("=== Trace Metadata ===")
    for key, value in sorted(packet.trace.metadata.items()):
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
