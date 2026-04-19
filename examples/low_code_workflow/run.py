"""Runnable low-code workflow over the shared Atlas starter engine."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from context_atlas.domain.models import ContextPacket
from context_atlas.infrastructure.assembly import assemble_with_low_code_workflow
from context_atlas.infrastructure.config import (
    LowCodeWorkflowSettings,
    build_low_code_workflow_plan,
    load_settings_from_env,
    list_low_code_workflow_presets,
)
from context_atlas.rendering import (
    render_packet_context,
    render_packet_inspection,
    render_trace_highlights,
    render_trace_inspection,
)

DEFAULT_QUERY = (
    "How should a low-code builder configure Context Atlas and troubleshoot "
    "environment or preflight issues in a chatbot workflow?"
)
DEFAULT_LOG_LEVEL = "WARNING"
CHATBOT_CONTEXT_HEADER = "Low-Code Chatbot Context"
ATLAS_PACKET_FILENAME = "atlas_packet.json"
ATLAS_RENDERED_CONTEXT_FILENAME = "atlas_rendered_context.txt"
ATLAS_TRACE_FILENAME = "atlas_trace.json"


def build_parser() -> argparse.ArgumentParser:
    """Build the supported CLI surface for the low-code workflow example."""

    parser = argparse.ArgumentParser(
        description=(
            "Run the low-code workflow over one supported preset-driven Atlas path."
        ),
        epilog=(
            "Relative --docs-root and --records-file values are resolved from "
            "--repo-root. The default preset uses governed docs plus a tracked "
            "sample records payload. Use --no-documents or --no-records to "
            "inspect one source family in isolation."
        ),
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path("."),
        help="Repository root for resolving relative low-code workflow inputs.",
    )
    parser.add_argument(
        "--query",
        default=DEFAULT_QUERY,
        help="Chatbot question to assemble context for.",
    )
    parser.add_argument(
        "--preset",
        default=None,
        choices=list_low_code_workflow_presets(),
        help="Optional low-code preset override.",
    )
    parser.add_argument(
        "--docs-root",
        default=None,
        help="Optional docs-root override relative to --repo-root.",
    )
    parser.add_argument(
        "--records-file",
        default=None,
        help="Optional records-file override relative to --repo-root.",
    )
    parser.add_argument(
        "--no-documents",
        dest="include_documents",
        action="store_false",
        default=None,
        help="Disable document ingestion for this run.",
    )
    parser.add_argument(
        "--no-records",
        dest="include_records",
        action="store_false",
        default=None,
        help="Disable structured-record ingestion for this run.",
    )
    parser.add_argument(
        "--proof-artifacts-dir",
        type=Path,
        default=None,
        help=(
            "Optional directory for writing standard MVP-proof artifacts "
            "(rendered context, packet JSON, trace JSON)."
        ),
    )
    return parser


def assemble_low_code_workflow_packet(
    *,
    repo_root_arg: Path,
    query: str,
    preset: str | None = None,
    docs_root: str | None = None,
    records_file: str | None = None,
    include_documents: bool | None = None,
    include_records: bool | None = None,
) -> tuple[Path, LowCodeWorkflowSettings, ContextPacket]:
    """Run one supported low-code workflow composition over the shared engine."""

    active_repo_root = repo_root_arg.resolve()
    if "CONTEXT_ATLAS_LOG_LEVEL" not in os.environ:
        os.environ["CONTEXT_ATLAS_LOG_LEVEL"] = DEFAULT_LOG_LEVEL

    settings = load_settings_from_env()
    active_settings = settings.with_low_code_overrides(
        preset=preset,
        docs_root=docs_root,
        records_file=records_file,
        include_documents=include_documents,
        include_records=include_records,
    )
    packet = assemble_with_low_code_workflow(
        query=query,
        settings=active_settings,
        repo_root=active_repo_root,
    )
    return active_repo_root, active_settings.low_code, packet


def main() -> None:
    args = build_parser().parse_args()
    repo_root, low_code_settings, packet = assemble_low_code_workflow_packet(
        repo_root_arg=args.repo_root,
        query=args.query,
        preset=args.preset,
        docs_root=args.docs_root,
        records_file=args.records_file,
        include_documents=args.include_documents,
        include_records=args.include_records,
    )
    plan = build_low_code_workflow_plan(
        low_code_settings=low_code_settings,
        repo_root=repo_root,
    )

    print(f"Repo root: {repo_root}")
    print(f"Preset: {plan.preset_name}")
    print(f"Preset description: {plan.preset_description}")
    print(
        f"Enabled source families: {','.join(plan.enabled_source_families) or 'none'}"
    )
    print(f"Governed docs root: {plan.docs_root or 'disabled'}")
    print(f"Records file: {plan.records_file or 'disabled'}")
    print(f"Query: {args.query}")
    print()
    print("=== Chatbot Context ===")
    rendered_context = render_packet_context(
        packet,
        include_section_headers=True,
        context_header=CHATBOT_CONTEXT_HEADER,
    )
    print(rendered_context)
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
        "Low-code boundary note: presets choose supported source defaults, but "
        "packet assembly and trace generation still run through the shared "
        "starter engine."
    )

    if args.proof_artifacts_dir is not None:
        output_dir = _write_proof_artifacts(
            output_dir=args.proof_artifacts_dir,
            packet=packet,
            rendered_context=rendered_context,
        )
        print()
        print(f"Proof artifacts written to: {output_dir}")


def _write_proof_artifacts(
    *,
    output_dir: Path,
    packet: ContextPacket,
    rendered_context: str,
) -> Path:
    """Write the standard Atlas proof artifacts for one workflow run."""

    resolved_output_dir = output_dir.resolve()
    resolved_output_dir.mkdir(parents=True, exist_ok=True)
    (resolved_output_dir / ATLAS_RENDERED_CONTEXT_FILENAME).write_text(
        rendered_context,
        encoding="utf-8",
    )
    (resolved_output_dir / ATLAS_PACKET_FILENAME).write_text(
        json.dumps(packet.model_dump(mode="json"), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (resolved_output_dir / ATLAS_TRACE_FILENAME).write_text(
        json.dumps(
            packet.trace.model_dump(mode="json") if packet.trace is not None else None,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return resolved_output_dir


if __name__ == "__main__":
    main()
