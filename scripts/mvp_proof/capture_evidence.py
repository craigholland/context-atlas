from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


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
        required=True,
        type=Path,
        help="Path to the Atlas packet artifact.",
    )
    parser.add_argument(
        "--atlas-trace",
        required=True,
        type=Path,
        help="Path to the Atlas trace artifact.",
    )
    parser.add_argument(
        "--atlas-rendered",
        required=True,
        type=Path,
        help="Path to the Atlas rendered-context artifact.",
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


def build_evidence_package(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "captured_at_utc": datetime.now(UTC).isoformat(),
        "workflow": args.workflow,
        "scenario": args.scenario,
        "query": args.query,
        "input_summary": args.input_summary,
        "review_notes": list(args.note),
        "artifacts": {
            "baseline_rendered_context": _load_artifact(args.baseline_rendered),
            "atlas_packet": _load_artifact(args.atlas_packet),
            "atlas_trace": _load_artifact(args.atlas_trace),
            "atlas_rendered_context": _load_artifact(args.atlas_rendered),
        },
    }


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    package = build_evidence_package(args)
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
