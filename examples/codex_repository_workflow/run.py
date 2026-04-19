"""Runnable Codex repository workflow example built on the shared Atlas engine."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from context_atlas.api import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetriever,
    load_settings_from_env,
    render_packet_context,
)
from context_atlas.domain.models import ContextPacket
from context_atlas.infrastructure.assembly import assemble_with_starter_context_service
from context_atlas.rendering import (
    render_packet_inspection,
    render_trace_inspection,
)

DEFAULT_QUERY = (
    "What guidance should an engineer follow when updating repository planning "
    "docs or architecture guidance?"
)
DEFAULT_LOG_LEVEL = "WARNING"
REPOSITORY_CONTEXT_HEADER = "Repository Context"


def build_parser(*, description: str) -> argparse.ArgumentParser:
    """Build the shared CLI surface for supported repository workflow scripts."""

    parser = argparse.ArgumentParser(
        description=description,
        epilog=(
            "See examples/codex_repository_workflow/sample_repo/README.md for "
            "the minimal supported repository shape. Relative --docs-root "
            "values are resolved from --repo-root."
        ),
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path("."),
        help="Path to the repository root. Defaults to the current directory.",
    )
    parser.add_argument(
        "--docs-root",
        type=Path,
        default=None,
        help="Optional explicit docs root. Defaults to <repo-root>/docs.",
    )
    parser.add_argument(
        "--query",
        default=DEFAULT_QUERY,
        help="Engineering question or task query to assemble context for.",
    )
    return parser


def assemble_repository_workflow_packet(
    *,
    repo_root_arg: Path,
    docs_root_arg: Path | None,
    query: str,
) -> tuple[Path, Path, ContextPacket]:
    """Run the shared repository-workflow composition path once."""

    repo_root = repo_root_arg.resolve()
    docs_root = _resolve_docs_root(repo_root=repo_root, docs_root_arg=docs_root_arg)

    if "CONTEXT_ATLAS_LOG_LEVEL" not in os.environ:
        os.environ["CONTEXT_ATLAS_LOG_LEVEL"] = DEFAULT_LOG_LEVEL

    settings = load_settings_from_env()
    sources = FilesystemDocumentSourceAdapter(docs_root).load_sources()
    retriever = LexicalRetriever(InMemorySourceRegistry(sources))
    packet = assemble_with_starter_context_service(
        retriever=retriever,
        query=query,
        settings=settings,
        metadata={
            "workflow": "codex_repository",
            "repo_root": repo_root.as_posix(),
            "docs_root": docs_root.as_posix(),
        },
    )
    return repo_root, docs_root, packet


def main() -> None:
    parser = build_parser(
        description="Run the flagship Codex repository workflow over governed docs."
    )
    args = parser.parse_args()
    repo_root, docs_root, packet = assemble_repository_workflow_packet(
        repo_root_arg=args.repo_root,
        docs_root_arg=args.docs_root,
        query=args.query,
    )

    print(f"Repository root: {repo_root}")
    print(f"Governed docs root: {docs_root}")
    print(f"Query: {args.query}")
    print()
    print("=== Codex Context ===")
    print(
        render_packet_context(
            packet,
            include_section_headers=True,
            context_header=REPOSITORY_CONTEXT_HEADER,
        )
    )
    print()
    print("=== Packet Inspection ===")
    print(render_packet_inspection(packet))
    print()
    print("=== Trace Inspection ===")
    if packet.trace is None:
        print("Trace\n- none")
    else:
        print(render_trace_inspection(packet.trace))


def _resolve_docs_root(*, repo_root: Path, docs_root_arg: Path | None) -> Path:
    """Resolve docs-root arguments against the selected repository root."""

    if docs_root_arg is None:
        return (repo_root / "docs").resolve()
    if docs_root_arg.is_absolute():
        return docs_root_arg.resolve()
    return (repo_root / docs_root_arg).resolve()


if __name__ == "__main__":
    main()
