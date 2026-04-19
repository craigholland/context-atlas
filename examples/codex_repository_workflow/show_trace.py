"""Demonstration script for showing rendered context plus trace-focused output."""

from __future__ import annotations

from context_atlas.api import render_packet_context
from context_atlas.rendering import render_trace_highlights, render_trace_inspection

if __package__:
    from .run import (
        REPOSITORY_CONTEXT_HEADER,
        assemble_repository_workflow_packet,
        build_parser,
    )
else:
    from run import (
        REPOSITORY_CONTEXT_HEADER,
        assemble_repository_workflow_packet,
        build_parser,
    )


def main() -> None:
    parser = build_parser(
        description=(
            "Show the Codex repository workflow as rendered context plus "
            "trace-focused output."
        )
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


if __name__ == "__main__":
    main()
