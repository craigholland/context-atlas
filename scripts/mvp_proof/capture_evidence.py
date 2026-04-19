from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
import shutil
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
BASELINE_RENDERED_CONTEXT_FILENAME = "baseline_rendered_context.txt"
EVIDENCE_PACKAGE_FILENAME = "evidence_package.json"


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
        "--expect-budget-pressure",
        action="store_true",
        help=(
            "Require the Atlas packet/trace artifacts to show visible budget-pressure "
            "signals such as compression, out-of-budget exclusion, or budget-pressure "
            "reason codes."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Path to the JSON evidence package to write.",
    )
    parser.add_argument(
        "--bundle-root",
        type=Path,
        default=None,
        help=(
            "Optional root directory for writing a reviewable evidence bundle at "
            "<bundle-root>/<workflow>/<scenario>/."
        ),
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


def _require_mapping(*, value: object, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be a JSON object.")
    return value


def _require_sequence(*, value: object, name: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be a JSON array.")
    return value


def _validate_atlas_artifacts(
    *,
    workflow: str,
    packet_artifact: dict[str, Any],
    trace_artifact: dict[str, Any],
) -> None:
    packet_content = _require_mapping(
        value=packet_artifact["content"],
        name="Atlas packet artifact",
    )
    trace_content = _require_mapping(
        value=trace_artifact["content"],
        name="Atlas trace artifact",
    )

    packet_trace = _require_mapping(
        value=packet_content.get("trace"),
        name="Atlas packet trace",
    )
    packet_id = packet_content.get("packet_id")
    if not isinstance(packet_id, str) or not packet_id.strip():
        raise ValueError("Atlas packet artifact must include a non-empty packet_id.")
    _require_sequence(
        value=packet_content.get("selected_candidates"),
        name="Atlas packet selected_candidates",
    )

    trace_id = trace_content.get("trace_id")
    if not isinstance(trace_id, str) or not trace_id.strip():
        raise ValueError("Atlas trace artifact must include a non-empty trace_id.")
    if packet_trace.get("trace_id") != trace_id:
        raise ValueError(
            "Atlas packet trace_id must match the standalone Atlas trace artifact."
        )

    trace_metadata = _require_mapping(
        value=trace_content.get("metadata"),
        name="Atlas trace metadata",
    )
    _require_sequence(
        value=trace_content.get("decisions"),
        name="Atlas trace decisions",
    )
    if trace_metadata.get("request_workflow") != workflow:
        raise ValueError(
            "Atlas trace metadata request_workflow must match the declared workflow."
        )


def _validate_budget_pressure_artifacts(
    *,
    packet_artifact: dict[str, Any],
    trace_artifact: dict[str, Any],
) -> None:
    packet_content = _require_mapping(
        value=packet_artifact["content"],
        name="Atlas packet artifact",
    )
    trace_content = _require_mapping(
        value=trace_artifact["content"],
        name="Atlas trace artifact",
    )
    packet_metadata = _require_mapping(
        value=packet_content.get("metadata"),
        name="Atlas packet metadata",
    )
    trace_metadata = _require_mapping(
        value=trace_content.get("metadata"),
        name="Atlas trace metadata",
    )
    decisions = _require_sequence(
        value=trace_content.get("decisions"),
        name="Atlas trace decisions",
    )

    if "budget_budget_total_tokens" not in trace_metadata:
        raise ValueError(
            "Budget-pressure proof artifacts must include budget trace metadata."
        )

    pressure_reason_codes = {
        "compression_required",
        "elastic_slot_reduced",
        "out_of_budget",
        "slot_exhausted",
        "total_budget_exhausted",
    }
    pressure_visible = packet_metadata.get("compression_applied") == "true"

    for decision in decisions:
        decision_mapping = _require_mapping(
            value=decision,
            name="Atlas trace decision",
        )
        reason_codes = {
            str(code)
            for code in _require_sequence(
                value=decision_mapping.get("reason_codes", []),
                name="Atlas trace decision reason_codes",
            )
        }
        if reason_codes & pressure_reason_codes:
            pressure_visible = True
            break

    if not pressure_visible:
        raise ValueError(
            "Budget-pressure proof artifacts must include visible pressure decisions "
            "or packet-level compression metadata."
        )


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


def _resolve_output_paths(
    args: argparse.Namespace,
) -> tuple[Path, Path | None]:
    has_output = args.output is not None
    has_bundle_root = args.bundle_root is not None

    if has_output == has_bundle_root:
        raise ValueError("Provide exactly one of --output or --bundle-root.")

    if args.output is not None:
        return args.output.resolve(), None

    assert args.bundle_root is not None
    bundle_dir = args.bundle_root.resolve() / args.workflow / args.scenario
    return bundle_dir / EVIDENCE_PACKAGE_FILENAME, bundle_dir


def build_evidence_package(args: argparse.Namespace) -> dict[str, Any]:
    atlas_packet_path, atlas_trace_path, atlas_rendered_path = (
        _resolve_atlas_artifact_paths(args)
    )
    baseline_rendered_context = _load_artifact(args.baseline_rendered)
    atlas_packet = _load_artifact(atlas_packet_path)
    atlas_trace = _load_artifact(atlas_trace_path)
    atlas_rendered_context = _load_artifact(atlas_rendered_path)
    _validate_atlas_artifacts(
        workflow=args.workflow,
        packet_artifact=atlas_packet,
        trace_artifact=atlas_trace,
    )
    if args.expect_budget_pressure:
        _validate_budget_pressure_artifacts(
            packet_artifact=atlas_packet,
            trace_artifact=atlas_trace,
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
            "budget_pressure_expected": args.expect_budget_pressure,
        },
        "artifacts": {
            "baseline_rendered_context": baseline_rendered_context,
            "atlas_packet": atlas_packet,
            "atlas_trace": atlas_trace,
            "atlas_rendered_context": atlas_rendered_context,
        },
    }


def _copy_artifact_if_needed(*, source_path: Path, target_path: Path) -> None:
    resolved_source = source_path.resolve()
    resolved_target = target_path.resolve()
    if resolved_source == resolved_target:
        return
    shutil.copyfile(resolved_source, resolved_target)


def _write_evidence_bundle(
    *,
    bundle_dir: Path,
    baseline_rendered_path: Path,
    atlas_packet_path: Path,
    atlas_trace_path: Path,
    atlas_rendered_path: Path,
    package: dict[str, Any],
) -> None:
    bundle_dir.mkdir(parents=True, exist_ok=True)
    _copy_artifact_if_needed(
        source_path=baseline_rendered_path,
        target_path=bundle_dir / BASELINE_RENDERED_CONTEXT_FILENAME,
    )
    _copy_artifact_if_needed(
        source_path=atlas_packet_path,
        target_path=bundle_dir / ATLAS_PACKET_FILENAME,
    )
    _copy_artifact_if_needed(
        source_path=atlas_trace_path,
        target_path=bundle_dir / ATLAS_TRACE_FILENAME,
    )
    _copy_artifact_if_needed(
        source_path=atlas_rendered_path,
        target_path=bundle_dir / ATLAS_RENDERED_CONTEXT_FILENAME,
    )
    (bundle_dir / EVIDENCE_PACKAGE_FILENAME).write_text(
        json.dumps(package, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        package = build_evidence_package(args)
        output_path, bundle_dir = _resolve_output_paths(args)
    except ValueError as error:
        parser.error(str(error))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(package, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if bundle_dir is not None:
        atlas_packet_path, atlas_trace_path, atlas_rendered_path = (
            _resolve_atlas_artifact_paths(args)
        )
        _write_evidence_bundle(
            bundle_dir=bundle_dir,
            baseline_rendered_path=args.baseline_rendered.resolve(),
            atlas_packet_path=atlas_packet_path.resolve(),
            atlas_trace_path=atlas_trace_path.resolve(),
            atlas_rendered_path=atlas_rendered_path.resolve(),
            package=package,
        )
        print(bundle_dir)
        return 0

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
