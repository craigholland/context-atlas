"""Verify that the committed Codex runtime surface matches its manifest-driven plan."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from materialize_codex_runtime import SUPPORTED_SURFACES, check_materialization_plan


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check that the committed Codex runtime surface matches the "
            "authoritative materialization manifest and upstream bindings."
        )
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root to validate (default: current directory).",
    )
    parser.add_argument(
        "--surface",
        action="append",
        choices=sorted(SUPPORTED_SURFACES),
        help=(
            "Limit verification to one or more concept families. Defaults to all "
            "supported surfaces when omitted."
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    selected_surfaces = set(args.surface) if args.surface else set(SUPPORTED_SURFACES)

    plan, problems = check_materialization_plan(repo_root, selected_surfaces)
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1

    print(
        "[check_codex_materialization] Verified "
        f"{len(plan.generated)} generated and "
        f"{len(plan.human_managed)} human-managed Codex surface(s) across "
        f"{len(selected_surfaces)} selected family(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
