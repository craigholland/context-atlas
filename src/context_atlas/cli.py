"""Installable CLI entrypoints for the current Context Atlas MVP surface."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
import os
from pathlib import Path

from .api import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetriever,
    build_starter_context_assembly_service,
    load_settings_from_env,
    render_packet_context,
)
from .rendering import render_packet_inspection, render_trace_inspection

DEFAULT_QUERY = "How should planning docs be treated?"
DEFAULT_LOG_LEVEL = "WARNING"
DEFAULT_DOCS_ROOT = "examples/codex_repository_workflow/sample_repo/docs"


def build_starter_parser() -> argparse.ArgumentParser:
    """Build the installable starter CLI surface."""

    parser = argparse.ArgumentParser(
        prog="context-atlas-starter",
        description=(
            "Run the Context Atlas starter flow against a documentation directory."
        ),
        epilog=(
            "This command is the installable starter surface for the current MVP. "
            "Point it at governed docs, inspect the rendered context, then use "
            "docs/Guides/ for the fuller workflow guides when you need repository, "
            "mixed-source, or low-code setup."
        ),
    )
    parser.add_argument(
        "docs_root",
        nargs="?",
        default=DEFAULT_DOCS_ROOT,
        help=(
            "Path to the documentation root to ingest. Defaults to the "
            "checked-in sample repository docs so a local repository checkout "
            "can reproduce the starter flow out of the box."
        ),
    )
    parser.add_argument(
        "--query",
        default=DEFAULT_QUERY,
        help="Question or task query to assemble context for.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the installable starter flow once."""

    args = build_starter_parser().parse_args(argv)
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
