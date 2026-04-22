"""Tests for deterministic Codex runtime materialization."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

_REPO_ROOT = Path(__file__).resolve().parents[1]
_SCRIPT_PATH = _REPO_ROOT / "scripts" / "materialize_codex_runtime.py"
_MODULE_SPEC = importlib.util.spec_from_file_location(
    "materialize_codex_runtime",
    _SCRIPT_PATH,
)
assert _MODULE_SPEC is not None and _MODULE_SPEC.loader is not None
_MATERIALIZE_MODULE = importlib.util.module_from_spec(_MODULE_SPEC)
sys.modules[_MODULE_SPEC.name] = _MATERIALIZE_MODULE
_MODULE_SPEC.loader.exec_module(_MATERIALIZE_MODULE)


class CodexRuntimeMaterializationTests(unittest.TestCase):
    """Keep the generated Codex runtime surface reproducible and reviewable."""

    def test_manifest_driven_plan_matches_committed_runtime_surface(self) -> None:
        plan = _MATERIALIZE_MODULE.build_materialization_plan(_REPO_ROOT)

        self.assertEqual(len(plan.human_managed), 0)
        self.assertEqual(len(plan.generated), 45)

        for surface in plan.generated:
            surface_path = _REPO_ROOT / surface.relative_path
            self.assertTrue(surface_path.is_file(), surface_path.as_posix())
            self.assertEqual(
                surface_path.read_text(encoding="utf-8"),
                surface.content,
                surface.relative_path.as_posix(),
            )

    def test_cli_check_passes_for_current_runtime_surface(self) -> None:
        result = subprocess.run(
            [sys.executable, str(_SCRIPT_PATH), "--check"],
            cwd=_REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "All selected generated Codex surfaces are in sync.",
            result.stdout,
        )

    def test_cli_surface_filter_can_check_subset(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(_SCRIPT_PATH),
                "--check",
                "--surface",
                "roles",
                "--surface",
                "agents",
            ],
            cwd=_REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "All selected generated Codex surfaces are in sync.",
            result.stdout,
        )

    def test_mixed_maintenance_mode_is_rejected_until_block_markers_exist(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            _MATERIALIZE_MODULE._surface_from_render(
                relative_path=".codex/roles/example.md",
                concept_family="roles",
                maintenance_mode="mixed",
                render=lambda: "content\n",
            )


if __name__ == "__main__":
    unittest.main()
