from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

RUBRIC_DIMENSIONS = [
    "packet_quality",
    "trace_legibility",
    "authority_handling",
    "budget_behavior",
    "workflow_reproducibility",
]

COMPARISON_STEPS = [
    "Read the naive baseline rendered-context artifact first.",
    "Read the Atlas rendered-context artifact for the same scenario.",
    "Inspect the Atlas packet artifact to confirm what was actually selected.",
    "Inspect the Atlas trace artifact to understand why sources were included, excluded, or transformed.",
    "Record notes against each rubric dimension before making an MVP-readiness recommendation.",
]

ATLAS_PACKET_FILENAME = "atlas_packet.json"
ATLAS_RENDERED_CONTEXT_FILENAME = "atlas_rendered_context.txt"
ATLAS_TRACE_FILENAME = "atlas_trace.json"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Capture one reproducible MVP-proof evidence package from already-generated "
            "workflow artifacts."
        ),
    )
    parser.add_argument("--workflow", required=True, help="Stable workflow name.")
    parser.add_argument("--scenario", required=True, help="Stable scenario name.")
    parser.add_argument(
        "--query", required=True, help="Query or task text for the scenario."
    )
    parser.add_argument(
        "--input-summary",
        required=True,
        help="Short summary of the source inputs used for the scenario.",
    )
    parser.add_argument(
        "--baseline-rendered",
        required=True,
        type=Path,
        help="Path to the naive baseline rendered-context artifact.",
    )
    parser.add_argument(
        "--atlas-packet",
        type=Path,
        default=None,
        help="Path to the Atlas packet artifact.",
    )
    parser.add_argument(
        "--atlas-trace",
        type=Path,
        default=None,
        help="Path to the Atlas trace artifact.",
    )
    parser.add_argument(
        "--atlas-rendered",
        type=Path,
        default=None,
        help="Path to the Atlas rendered-context artifact.",
    )
    parser.add_argument(
        "--atlas-artifact-dir",
        type=Path,
        default=None,
        help=(
            "Optional directory containing the standard Atlas workflow artifacts "
            f"({ATLAS_PACKET_FILENAME}, {ATLAS_TRACE_FILENAME}, "
            f"{ATLAS_RENDERED_CONTEXT_FILENAME})."
        ),
    )
    parser.add_argument(
        "--note",
        action="append",
        default=[],
        help="Optional short reviewer note. May be supplied multiple times.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path to the JSON evidence package to write.",
    )
    return parser


def _require_file(path: Path) -> Path:
    resolved = path.resolve()
    if not resolved.is_file():
        raise FileNotFoundError(f"Artifact file does not exist: {resolved}")
    return resolved


def _load_artifact(path: Path) -> dict[str, Any]:
    resolved = _require_file(path)
    if resolved.suffix.lower() == ".json":
        return {
            "kind": "json",
            "path": str(resolved),
            "content": json.loads(resolved.read_text(encoding="utf-8")),
        }

    return {
        "kind": "text",
        "path": str(resolved),
        "content": resolved.read_text(encoding="utf-8"),
    }


def _resolve_atlas_artifact_paths(
    args: argparse.Namespace,
) -> tuple[Path, Path, Path]:
    artifact_dir: Path | None = args.atlas_artifact_dir
    explicit_paths = (args.atlas_packet, args.atlas_trace, args.atlas_rendered)
    explicit_path_count = sum(path is not None for path in explicit_paths)

    if artifact_dir is not None:
        if explicit_path_count:
            raise ValueError(
                "Use either --atlas-artifact-dir or the explicit --atlas-* paths, not both."
            )
        resolved_artifact_dir = artifact_dir.resolve()
        return (
            resolved_artifact_dir / ATLAS_PACKET_FILENAME,
            resolved_artifact_dir / ATLAS_TRACE_FILENAME,
            resolved_artifact_dir / ATLAS_RENDERED_CONTEXT_FILENAME,
        )

    if explicit_path_count != 3:
        raise ValueError(
            "Provide all of --atlas-packet, --atlas-trace, and --atlas-rendered when "
            "--atlas-artifact-dir is not supplied."
        )

    assert args.atlas_packet is not None
    assert args.atlas_trace is not None
    assert args.atlas_rendered is not None
    return args.atlas_packet, args.atlas_trace, args.atlas_rendered


def build_evidence_package(args: argparse.Namespace) -> dict[str, Any]:
    atlas_packet_path, atlas_trace_path, atlas_rendered_path = (
        _resolve_atlas_artifact_paths(args)
    )
    return {
        "captured_at_utc": datetime.now(UTC).isoformat(),
        "workflow": args.workflow,
        "scenario": args.scenario,
        "query": args.query,
        "input_summary": args.input_summary,
        "review_notes": list(args.note),
        "review_path": {
            "rubric_document": "docs/Reviews/MVP/mvp_evaluation_rubric.md",
            "rubric_dimensions": list(RUBRIC_DIMENSIONS),
            "comparison_steps": list(COMPARISON_STEPS),
        },
        "artifacts": {
            "baseline_rendered_context": _load_artifact(args.baseline_rendered),
            "atlas_packet": _load_artifact(atlas_packet_path),
            "atlas_trace": _load_artifact(atlas_trace_path),
            "atlas_rendered_context": _load_artifact(atlas_rendered_path),
        },
    }


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        package = build_evidence_package(args)
    except ValueError as error:
        parser.error(str(error))

    output_path = args.output.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(package, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
