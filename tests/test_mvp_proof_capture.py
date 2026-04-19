"""Regression tests for MVP proof evidence capture helpers."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest

_REPO_ROOT = Path(__file__).resolve().parents[1]
_CAPTURE_SCRIPT = _REPO_ROOT / "scripts" / "mvp_proof" / "capture_evidence.py"
_MODULE_SPEC = importlib.util.spec_from_file_location(
    "mvp_proof_capture_evidence",
    _CAPTURE_SCRIPT,
)
assert _MODULE_SPEC is not None and _MODULE_SPEC.loader is not None
_CAPTURE_MODULE = importlib.util.module_from_spec(_MODULE_SPEC)
_MODULE_SPEC.loader.exec_module(_CAPTURE_MODULE)


class MvpProofCaptureTests(unittest.TestCase):
    """Keep proof capture idempotent and reviewable."""

    def _write_valid_atlas_artifacts(
        self,
        bundle_dir: Path,
        *,
        workflow: str = "codex_repository",
        packet_metadata: dict[str, str] | None = None,
        trace_metadata: dict[str, str] | None = None,
        decisions: list[dict[str, object]] | None = None,
        selected_candidates: list[dict[str, object]] | None = None,
    ) -> None:
        trace = {
            "trace_id": "trace-proof-1",
            "metadata": {"request_workflow": workflow} | (trace_metadata or {}),
            "decisions": decisions or [],
        }
        packet = {
            "packet_id": "packet-proof-1",
            "selected_candidates": selected_candidates or [],
            "trace": trace,
            "metadata": packet_metadata or {},
        }
        (bundle_dir / "atlas_packet.json").write_text(
            json.dumps(packet) + "\n",
            encoding="utf-8",
        )
        (bundle_dir / "atlas_trace.json").write_text(
            json.dumps(trace) + "\n",
            encoding="utf-8",
        )

    def test_main_allows_regeneration_into_existing_bundle_directory(self) -> None:
        with TemporaryDirectory() as temp_dir:
            bundle_root = Path(temp_dir)
            bundle_dir = bundle_root / "codex_repository" / "repo_governed_docs_update"
            bundle_dir.mkdir(parents=True, exist_ok=True)

            (bundle_dir / "baseline_rendered_context.txt").write_text(
                "baseline content\n",
                encoding="utf-8",
            )
            (bundle_dir / "atlas_rendered_context.txt").write_text(
                "rendered content\n",
                encoding="utf-8",
            )
            self._write_valid_atlas_artifacts(bundle_dir)

            original_argv = sys.argv
            output = io.StringIO()
            try:
                sys.argv = [
                    "capture_evidence.py",
                    "--workflow",
                    "codex_repository",
                    "--scenario",
                    "repo_governed_docs_update",
                    "--query",
                    "How should repository planning docs be updated?",
                    "--input-summary",
                    "docs_root=docs/Guides",
                    "--baseline-rendered",
                    str(bundle_dir / "baseline_rendered_context.txt"),
                    "--atlas-artifact-dir",
                    str(bundle_dir),
                    "--bundle-root",
                    str(bundle_root),
                ]
                with contextlib.redirect_stdout(output):
                    exit_code = _CAPTURE_MODULE.main()
            finally:
                sys.argv = original_argv

            self.assertEqual(exit_code, 0)
            self.assertEqual(output.getvalue().strip(), str(bundle_dir.resolve()))
            package = json.loads(
                (bundle_dir / "evidence_package.json").read_text(encoding="utf-8")
            )
            self.assertEqual(package["workflow"], "codex_repository")
            self.assertEqual(
                package["artifacts"]["atlas_packet"]["path"],
                str((bundle_dir / "atlas_packet.json").resolve()),
            )

    def test_build_evidence_package_rejects_mismatched_workflow_metadata(self) -> None:
        with TemporaryDirectory() as temp_dir:
            bundle_dir = Path(temp_dir)
            (bundle_dir / "baseline_rendered_context.txt").write_text(
                "baseline content\n",
                encoding="utf-8",
            )
            (bundle_dir / "atlas_rendered_context.txt").write_text(
                "rendered content\n",
                encoding="utf-8",
            )
            self._write_valid_atlas_artifacts(
                bundle_dir,
                workflow="docs_database_builder",
            )

            args = _CAPTURE_MODULE.build_parser().parse_args(
                [
                    "--workflow",
                    "codex_repository",
                    "--scenario",
                    "repo_governed_docs_update",
                    "--query",
                    "How should repository planning docs be updated?",
                    "--input-summary",
                    "docs_root=docs/Guides",
                    "--baseline-rendered",
                    str(bundle_dir / "baseline_rendered_context.txt"),
                    "--atlas-artifact-dir",
                    str(bundle_dir),
                    "--output",
                    str(bundle_dir / "evidence_package.json"),
                ]
            )

            with self.assertRaisesRegex(
                ValueError,
                "request_workflow must match the declared workflow",
            ):
                _CAPTURE_MODULE.build_evidence_package(args)

    def test_build_evidence_package_rejects_budget_pressure_bundle_without_signal(
        self,
    ) -> None:
        with TemporaryDirectory() as temp_dir:
            bundle_dir = Path(temp_dir)
            (bundle_dir / "baseline_rendered_context.txt").write_text(
                "baseline content\n",
                encoding="utf-8",
            )
            (bundle_dir / "atlas_rendered_context.txt").write_text(
                "rendered content\n",
                encoding="utf-8",
            )
            self._write_valid_atlas_artifacts(
                bundle_dir,
                trace_metadata={"budget_budget_total_tokens": "64"},
            )

            args = _CAPTURE_MODULE.build_parser().parse_args(
                [
                    "--workflow",
                    "codex_repository",
                    "--scenario",
                    "repo_budget_pressure_tradeoffs",
                    "--query",
                    "What guidance should an engineer follow when updating repository planning docs or architecture guidance?",
                    "--input-summary",
                    "repo_root=.; docs_root=docs/Guides; total_budget=64",
                    "--baseline-rendered",
                    str(bundle_dir / "baseline_rendered_context.txt"),
                    "--atlas-artifact-dir",
                    str(bundle_dir),
                    "--expect-budget-pressure",
                    "--output",
                    str(bundle_dir / "evidence_package.json"),
                ]
            )

            with self.assertRaisesRegex(
                ValueError,
                "Budget-pressure proof artifacts must include visible pressure decisions",
            ):
                _CAPTURE_MODULE.build_evidence_package(args)

    def test_build_evidence_package_accepts_budget_pressure_bundle_with_compression_metadata(
        self,
    ) -> None:
        with TemporaryDirectory() as temp_dir:
            bundle_dir = Path(temp_dir)
            (bundle_dir / "baseline_rendered_context.txt").write_text(
                "baseline content\n",
                encoding="utf-8",
            )
            (bundle_dir / "atlas_rendered_context.txt").write_text(
                "rendered content\n",
                encoding="utf-8",
            )
            self._write_valid_atlas_artifacts(
                bundle_dir,
                packet_metadata={"compression_applied": "true"},
                trace_metadata={"budget_budget_total_tokens": "64"},
            )

            args = _CAPTURE_MODULE.build_parser().parse_args(
                [
                    "--workflow",
                    "codex_repository",
                    "--scenario",
                    "repo_budget_pressure_tradeoffs",
                    "--query",
                    "What guidance should an engineer follow when updating repository planning docs or architecture guidance?",
                    "--input-summary",
                    "repo_root=.; docs_root=docs/Guides; total_budget=64",
                    "--baseline-rendered",
                    str(bundle_dir / "baseline_rendered_context.txt"),
                    "--atlas-artifact-dir",
                    str(bundle_dir),
                    "--expect-budget-pressure",
                    "--output",
                    str(bundle_dir / "evidence_package.json"),
                ]
            )

            package = _CAPTURE_MODULE.build_evidence_package(args)

            self.assertEqual(package["scenario"], "repo_budget_pressure_tradeoffs")
            self.assertTrue(package["review_path"]["budget_pressure_expected"])

    def test_build_evidence_package_rejects_missing_document_authority_contrast(
        self,
    ) -> None:
        with TemporaryDirectory() as temp_dir:
            bundle_dir = Path(temp_dir)
            (bundle_dir / "baseline_rendered_context.txt").write_text(
                "baseline content\n",
                encoding="utf-8",
            )
            (bundle_dir / "atlas_rendered_context.txt").write_text(
                "rendered content\n",
                encoding="utf-8",
            )
            self._write_valid_atlas_artifacts(
                bundle_dir,
                selected_candidates=[
                    {
                        "source": {
                            "source_class": "planning",
                            "authority": "preferred",
                            "provenance": {"source_family": "document"},
                        }
                    }
                ],
            )

            args = _CAPTURE_MODULE.build_parser().parse_args(
                [
                    "--workflow",
                    "codex_repository",
                    "--scenario",
                    "repo_document_authority_precedence",
                    "--query",
                    "Which guidance should an engineer follow when authoritative and planning docs both discuss repository process?",
                    "--input-summary",
                    "repo_root=examples/codex_repository_workflow/sample_repo; docs_root=<repo_root>/docs",
                    "--baseline-rendered",
                    str(bundle_dir / "baseline_rendered_context.txt"),
                    "--atlas-artifact-dir",
                    str(bundle_dir),
                    "--expect-document-authority-contrast",
                    "--output",
                    str(bundle_dir / "evidence_package.json"),
                ]
            )

            with self.assertRaisesRegex(
                ValueError,
                "must include at least one lower-authority document",
            ):
                _CAPTURE_MODULE.build_evidence_package(args)

    def test_build_evidence_package_accepts_document_authority_contrast(
        self,
    ) -> None:
        with TemporaryDirectory() as temp_dir:
            bundle_dir = Path(temp_dir)
            (bundle_dir / "baseline_rendered_context.txt").write_text(
                "baseline content\n",
                encoding="utf-8",
            )
            (bundle_dir / "atlas_rendered_context.txt").write_text(
                "rendered content\n",
                encoding="utf-8",
            )
            self._write_valid_atlas_artifacts(
                bundle_dir,
                selected_candidates=[
                    {
                        "source": {
                            "source_class": "authoritative",
                            "authority": "binding",
                            "provenance": {"source_family": "document"},
                        }
                    },
                    {
                        "source": {
                            "source_class": "planning",
                            "authority": "preferred",
                            "provenance": {"source_family": "document"},
                        }
                    },
                ],
            )

            args = _CAPTURE_MODULE.build_parser().parse_args(
                [
                    "--workflow",
                    "codex_repository",
                    "--scenario",
                    "repo_document_authority_precedence",
                    "--query",
                    "Which guidance should an engineer follow when authoritative and planning docs both discuss repository process?",
                    "--input-summary",
                    "repo_root=examples/codex_repository_workflow/sample_repo; docs_root=<repo_root>/docs",
                    "--baseline-rendered",
                    str(bundle_dir / "baseline_rendered_context.txt"),
                    "--atlas-artifact-dir",
                    str(bundle_dir),
                    "--expect-document-authority-contrast",
                    "--output",
                    str(bundle_dir / "evidence_package.json"),
                ]
            )

            package = _CAPTURE_MODULE.build_evidence_package(args)

            self.assertEqual(package["scenario"], "repo_document_authority_precedence")
            self.assertTrue(package["review_path"]["document_authority_expected"])

    def test_build_evidence_package_uses_authority_not_source_class_for_contrast(
        self,
    ) -> None:
        with TemporaryDirectory() as temp_dir:
            bundle_dir = Path(temp_dir)
            (bundle_dir / "baseline_rendered_context.txt").write_text(
                "baseline content\n",
                encoding="utf-8",
            )
            (bundle_dir / "atlas_rendered_context.txt").write_text(
                "rendered content\n",
                encoding="utf-8",
            )
            self._write_valid_atlas_artifacts(
                bundle_dir,
                selected_candidates=[
                    {
                        "source": {
                            "source_class": "authoritative",
                            "authority": "advisory",
                            "provenance": {"source_family": "document"},
                        }
                    },
                    {
                        "source": {
                            "source_class": "planning",
                            "authority": "binding",
                            "provenance": {"source_family": "document"},
                        }
                    },
                ],
            )

            args = _CAPTURE_MODULE.build_parser().parse_args(
                [
                    "--workflow",
                    "codex_repository",
                    "--scenario",
                    "repo_document_authority_precedence",
                    "--query",
                    "Which guidance should an engineer follow when authoritative and planning docs both discuss repository process?",
                    "--input-summary",
                    "repo_root=examples/codex_repository_workflow/sample_repo; docs_root=<repo_root>/docs",
                    "--baseline-rendered",
                    str(bundle_dir / "baseline_rendered_context.txt"),
                    "--atlas-artifact-dir",
                    str(bundle_dir),
                    "--expect-document-authority-contrast",
                    "--output",
                    str(bundle_dir / "evidence_package.json"),
                ]
            )

            with self.assertRaisesRegex(
                ValueError,
                "must keep higher-authority documents ahead",
            ):
                _CAPTURE_MODULE.build_evidence_package(args)


if __name__ == "__main__":
    unittest.main()
