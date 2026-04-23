"""Tests for deterministic Codex runtime materialization."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

_REPO_ROOT = Path(__file__).resolve().parents[1]
_SCRIPT_PATH = _REPO_ROOT / "scripts" / "materialize_codex_runtime.py"
_CHECK_SCRIPT_PATH = _REPO_ROOT / "scripts" / "check_codex_materialization.py"
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
                str(_CHECK_SCRIPT_PATH),
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
            "Verified",
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

    def test_read_text_cache_is_scoped_by_repo_root_and_file_state(self) -> None:
        relative_path = Path("docs/cache-fixture.md")

        with TemporaryDirectory() as first_dir, TemporaryDirectory() as second_dir:
            first_root = Path(first_dir)
            second_root = Path(second_dir)
            first_path = first_root / relative_path
            second_path = second_root / relative_path
            first_path.parent.mkdir(parents=True, exist_ok=True)
            second_path.parent.mkdir(parents=True, exist_ok=True)
            first_path.write_text("first root\n", encoding="utf-8")
            second_path.write_text("second root\n", encoding="utf-8")

            self.assertEqual(
                _MATERIALIZE_MODULE._read_text(first_root, relative_path),
                "first root\n",
            )
            self.assertEqual(
                _MATERIALIZE_MODULE._read_text(second_root, relative_path),
                "second root\n",
            )

            second_path.write_text(
                "second root updated with more text\n",
                encoding="utf-8",
            )

            self.assertEqual(
                _MATERIALIZE_MODULE._read_text(second_root, relative_path),
                "second root updated with more text\n",
            )

    def test_manifest_runtime_roots_drive_paths_and_runtime_references(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_copy = Path(temp_dir) / "repo"
            shutil.copytree(
                _REPO_ROOT,
                repo_copy,
                ignore=shutil.ignore_patterns(
                    ".git",
                    ".pytest_cache",
                    ".mypy_cache",
                    ".ruff_cache",
                    "__pycache__",
                    "*.pyc",
                ),
            )

            manifest_path = (
                repo_copy
                / "docs"
                / "Authoritative"
                / "Identity"
                / "AgenticDevelopment"
                / "materialization_manifest.yaml"
            )
            manifest_text = manifest_path.read_text(encoding="utf-8")
            manifest_text = manifest_text.replace(
                "runtime_root: .codex",
                "runtime_root: .codex-alt",
            )
            manifest_text = manifest_text.replace(
                "skills_root: .agents/skills",
                "skills_root: .agents-alt/skills",
            )
            manifest_text = manifest_text.replace(
                "path: .codex/AGENTS.md",
                "path: .codex-alt/AGENTS.md",
            )
            manifest_text = manifest_text.replace(
                "path: .codex/config.toml",
                "path: .codex-alt/config.toml",
            )
            manifest_path.write_text(manifest_text, encoding="utf-8")

            plan = _MATERIALIZE_MODULE.build_materialization_plan(repo_copy)
            generated = {
                surface.relative_path.as_posix(): surface for surface in plan.generated
            }

            self.assertIn(".codex-alt/AGENTS.md", generated)
            self.assertIn(".codex-alt/config.toml", generated)
            self.assertIn(".codex-alt/roles/backend.md", generated)
            self.assertIn(".codex-alt/agents/parent-backend.toml", generated)
            self.assertIn(".codex-alt/modes/planning.md", generated)
            self.assertIn(".codex-alt/protocols/review.md", generated)
            self.assertIn(
                ".agents-alt/skills/context-atlas-python-authoring/SKILL.md",
                generated,
            )
            self.assertNotIn(".codex/roles/backend.md", generated)
            self.assertNotIn(
                ".agents/skills/context-atlas-python-authoring/SKILL.md",
                generated,
            )

            orientation_surface = generated[".codex-alt/AGENTS.md"]
            self.assertIn(
                "`.codex-alt/roles/`",
                orientation_surface.content,
            )
            self.assertIn(
                "`.codex-alt/agents/`",
                orientation_surface.content,
            )
            self.assertIn(
                "`.agents-alt/skills/`",
                orientation_surface.content,
            )
            self.assertIn(
                "`.codex-alt/config.toml`",
                orientation_surface.content,
            )

            config_surface = generated[".codex-alt/config.toml"]
            self.assertIn('roles_root = ".codex-alt/roles"', config_surface.content)
            self.assertIn('agents_root = ".codex-alt/agents"', config_surface.content)
            self.assertIn('modes_root = ".codex-alt/modes"', config_surface.content)
            self.assertIn(
                'protocols_root = ".codex-alt/protocols"',
                config_surface.content,
            )
            self.assertIn(
                'skills_root = ".agents-alt/skills"',
                config_surface.content,
            )

            backend_role_surface = generated[".codex-alt/roles/backend.md"]
            self.assertIn(
                "`.codex-alt/agents/parent-backend.toml`",
                backend_role_surface.content,
            )

    def test_mode_transition_data_stops_at_next_higher_heading(self) -> None:
        transitions = _MATERIALIZE_MODULE._mode_transition_data(
            _REPO_ROOT,
            "Operational Delivery",
        )

        self.assertEqual(
            transitions["exit"],
            [
                "when an operational outcome contract is emitted",
                "when an operational artifact is handed to review",
                "when the operational path becomes blocked badly enough to require recovery",
            ],
        )

    def test_materialization_check_script_passes_for_current_repo(self) -> None:
        result = subprocess.run(
            [sys.executable, str(_CHECK_SCRIPT_PATH)],
            cwd=_REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("[check_codex_materialization] Verified", result.stdout)

    def test_materialization_check_script_fails_when_generated_surface_drifts(
        self,
    ) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_copy = Path(temp_dir) / "repo"
            shutil.copytree(
                _REPO_ROOT,
                repo_copy,
                ignore=shutil.ignore_patterns(
                    ".git",
                    ".pytest_cache",
                    ".mypy_cache",
                    ".ruff_cache",
                    "__pycache__",
                    "*.pyc",
                ),
            )
            orientation_path = repo_copy / ".codex" / "AGENTS.md"
            orientation_path.write_text(
                orientation_path.read_text(encoding="utf-8")
                + "\n<!-- local drift -->\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(_CHECK_SCRIPT_PATH),
                    "--repo-root",
                    str(repo_copy),
                ],
                cwd=_REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 1)
            self.assertIn(".codex/AGENTS.md", result.stderr)


if __name__ == "__main__":
    unittest.main()
