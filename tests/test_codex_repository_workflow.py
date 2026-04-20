"""Validation tests for the flagship Codex repository workflow example."""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import json
import subprocess
import sys
from tempfile import TemporaryDirectory
import textwrap
import unittest

from pydantic import ValidationError

from context_atlas.adapters import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetrievalMode,
    LexicalRetriever,
)
from context_atlas.infrastructure.assembly import build_starter_context_assembly_service
from context_atlas.infrastructure.config import (
    AssemblySettings,
    ContextAtlasSettings,
    LoggingSettings,
    MemorySettings,
)

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKFLOW_SCRIPT = _REPO_ROOT / "examples" / "codex_repository_workflow" / "run.py"
_SHOW_TRACE_SCRIPT = (
    _REPO_ROOT / "examples" / "codex_repository_workflow" / "show_trace.py"
)
_MODULE_SPEC = importlib.util.spec_from_file_location(
    "codex_repository_workflow_run",
    _WORKFLOW_SCRIPT,
)
assert _MODULE_SPEC is not None and _MODULE_SPEC.loader is not None
_WORKFLOW_MODULE = importlib.util.module_from_spec(_MODULE_SPEC)
_MODULE_SPEC.loader.exec_module(_WORKFLOW_MODULE)


class CodexRepositoryWorkflowTests(unittest.TestCase):
    """Keep the flagship repository workflow honest and inspectable."""

    def test_service_trace_preserves_request_workflow_metadata(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_root = repo_root / "docs"
            self._write_doc(
                docs_root / "Authoritative" / "Canon" / "Architecture" / "Guidance.md",
                """
                # Guidance

                Engineers should keep architecture guidance aligned with active
                planning documents and update local owner files in the same slice.
                """,
            )

            sources = FilesystemDocumentSourceAdapter(docs_root).load_sources()
            service = build_starter_context_assembly_service(
                retriever=LexicalRetriever(
                    InMemorySourceRegistry(sources),
                    mode=LexicalRetrievalMode.KEYWORD,
                ),
                settings=ContextAtlasSettings(
                    logging=LoggingSettings(
                        logger_name="context_atlas.tests.codex_repository"
                    ),
                    assembly=AssemblySettings(
                        default_total_budget=512,
                        default_retrieval_top_k=3,
                    ),
                    memory=MemorySettings(),
                ),
            )

            packet = service.assemble(
                query="How should engineers update architecture guidance?",
                metadata={
                    "workflow": "codex_repository",
                    "repo_root": repo_root.as_posix(),
                    "docs_root": docs_root.as_posix(),
                },
            )

            self.assertIsNotNone(packet.trace)
            self.assertEqual(
                packet.trace.metadata["request_workflow"],
                "codex_repository",
            )
            self.assertEqual(
                packet.trace.metadata["request_repo_root"],
                repo_root.as_posix(),
            )
            self.assertEqual(
                packet.trace.metadata["request_docs_root"],
                docs_root.as_posix(),
            )

    def test_workflow_script_emits_context_packet_and_trace_sections(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_root = repo_root / "docs"
            self._write_doc(
                docs_root / "Authoritative" / "Canon" / "Architecture" / "Guidance.md",
                """
                # Architecture Guidance

                Engineers should update architecture guidance and planning docs
                together when the supported workflow changes.
                """,
            )
            self._write_doc(
                docs_root / "Planning" / "Workflow.md",
                """
                # Workflow Plan

                Planning notes should describe how contributors review feature
                branches and task-level pull requests.
                """,
            )

            environment = os.environ.copy()
            environment["PYTHONPATH"] = str(_REPO_ROOT / "src")
            environment["CONTEXT_ATLAS_LOG_LEVEL"] = "WARNING"

            result = subprocess.run(
                [
                    sys.executable,
                    str(_WORKFLOW_SCRIPT),
                    "--repo-root",
                    str(repo_root),
                    "--query",
                    "What guidance should an engineer follow when updating "
                    "architecture guidance and planning docs?",
                ],
                cwd=_REPO_ROOT,
                capture_output=True,
                text=True,
                env=environment,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("=== Codex Context ===", result.stdout)
            self.assertIn("[Repository Context]", result.stdout)
            self.assertIn("=== Packet Inspection ===", result.stdout)
            self.assertIn("=== Trace Inspection ===", result.stdout)
            self.assertIn(
                "Authoritative/Canon/Architecture/Guidance.md",
                result.stdout,
            )
            self.assertIn("selected_source_families: document", result.stdout)
            self.assertIn("request_workflow: codex_repository", result.stdout)
            self.assertIn("request_docs_root:", result.stdout)

    def test_relative_docs_root_is_resolved_from_repo_root(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "sample-repo"
            docs_root = repo_root / "docs"
            self._write_doc(
                docs_root / "Authoritative" / "Canon" / "Architecture" / "Guidance.md",
                """
                # Guidance

                Relative docs-root arguments should resolve from the chosen
                repository root, not from the caller's current working directory.
                """,
            )

            outside_cwd = Path(temp_dir) / "outside"
            outside_cwd.mkdir(parents=True, exist_ok=True)

            environment = os.environ.copy()
            environment["PYTHONPATH"] = str(_REPO_ROOT / "src")
            environment["CONTEXT_ATLAS_LOG_LEVEL"] = "WARNING"

            result = subprocess.run(
                [
                    sys.executable,
                    str(_WORKFLOW_SCRIPT),
                    "--repo-root",
                    str(repo_root),
                    "--docs-root",
                    "docs",
                    "--query",
                    "How should docs-root be resolved?",
                ],
                cwd=outside_cwd,
                capture_output=True,
                text=True,
                env=environment,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(
                f"Governed docs root: {docs_root.resolve()}",
                result.stdout,
            )
            self.assertIn(
                "Authoritative/Canon/Architecture/Guidance.md",
                result.stdout,
            )

    def test_workflow_script_can_write_standard_proof_artifacts(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir) / "sample-repo"
            docs_root = repo_root / "docs"
            proof_dir = Path(temp_dir) / "proof"
            self._write_doc(
                docs_root / "Authoritative" / "Canon" / "Architecture" / "Guidance.md",
                """
                # Guidance

                Proof workflows should emit reproducible packet, trace, and
                rendered-context artifacts from the supported runnable path.
                """,
            )

            environment = os.environ.copy()
            environment["PYTHONPATH"] = str(_REPO_ROOT / "src")
            environment["CONTEXT_ATLAS_LOG_LEVEL"] = "WARNING"

            result = subprocess.run(
                [
                    sys.executable,
                    str(_WORKFLOW_SCRIPT),
                    "--repo-root",
                    str(repo_root),
                    "--query",
                    "How should proof artifacts be generated for the repository workflow?",
                    "--proof-artifacts-dir",
                    str(proof_dir),
                ],
                cwd=_REPO_ROOT,
                capture_output=True,
                text=True,
                env=environment,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((proof_dir / "atlas_rendered_context.txt").is_file())
            self.assertTrue((proof_dir / "atlas_packet.json").is_file())
            self.assertTrue((proof_dir / "atlas_trace.json").is_file())
            self.assertIn("Proof artifacts written to:", result.stdout)

            packet = json.loads(
                (proof_dir / "atlas_packet.json").read_text(encoding="utf-8")
            )
            trace = json.loads(
                (proof_dir / "atlas_trace.json").read_text(encoding="utf-8")
            )

            self.assertEqual(packet["metadata"]["workflow"], "codex_repository")
            self.assertEqual(trace["metadata"]["request_workflow"], "codex_repository")

    def test_budget_constrained_repository_workflow_surfaces_pressure_signals(
        self,
    ) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_root = repo_root / "docs" / "Guides"
            repeated_guidance = " ".join(
                [
                    (
                        "Engineers should update planning docs and architecture "
                        "guidance together, keep owner files aligned, and inspect "
                        "packet plus trace output when budget tradeoffs appear."
                    )
                ]
                * 8
            )
            self._write_doc(
                docs_root / "Authoritative" / "Canon" / "Architecture" / "Guidance.md",
                f"# Guidance\n\n{repeated_guidance}\n",
            )
            self._write_doc(
                docs_root / "Planning" / "Workflow.md",
                f"# Workflow\n\n{repeated_guidance}\n",
            )
            self._write_doc(
                docs_root / "Reviews" / "Findings.md",
                f"# Findings\n\n{repeated_guidance}\n",
            )

            resolved_repo_root, resolved_docs_root, packet = (
                _WORKFLOW_MODULE.assemble_repository_workflow_packet(
                    repo_root_arg=repo_root,
                    docs_root_arg=Path("docs/Guides"),
                    query=(
                        "What guidance should an engineer follow when updating "
                        "repository planning docs or architecture guidance?"
                    ),
                    total_budget=64,
                )
            )

            reason_codes = {
                reason.value
                for decision in packet.trace.decisions
                for reason in decision.reason_codes
            }

            self.assertEqual(resolved_repo_root, repo_root.resolve())
            self.assertEqual(resolved_docs_root, docs_root.resolve())
            self.assertEqual(packet.budget.total_tokens, 64)
            self.assertEqual(
                packet.trace.metadata["request_requested_total_budget"], "64"
            )
            self.assertEqual(packet.trace.metadata["budget_budget_total_tokens"], "64")
            self.assertTrue(packet.compression_was_applied)
            self.assertEqual(packet.metadata["compression_applied"], "true")
            self.assertIn("elastic_slot_reduced", reason_codes)
            self.assertIn("compression_required", reason_codes)

    def test_budget_override_is_validated_before_repository_workflow_runs(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_root = repo_root / "docs" / "Guides"
            self._write_doc(
                docs_root / "Authoritative" / "Canon" / "Architecture" / "Guidance.md",
                """
                # Guidance

                Repository proof runs should reject unsupported total budgets
                before assembling packet or trace artifacts.
                """,
            )

            with self.assertRaises(ValidationError):
                _WORKFLOW_MODULE.assemble_repository_workflow_packet(
                    repo_root_arg=repo_root,
                    docs_root_arg=Path("docs/Guides"),
                    query="How should unsupported proof budgets be handled?",
                    total_budget=32,
                )

    def test_sample_repo_authority_scenario_keeps_authoritative_docs_first(
        self,
    ) -> None:
        sample_repo_root = (
            _REPO_ROOT / "examples" / "codex_repository_workflow" / "sample_repo"
        )

        resolved_repo_root, resolved_docs_root, packet = (
            _WORKFLOW_MODULE.assemble_repository_workflow_packet(
                repo_root_arg=sample_repo_root,
                docs_root_arg=None,
                query=(
                    "When authoritative architecture guidance and planning docs "
                    "both discuss repository process, which guidance should an "
                    "engineer follow and how should planning docs be updated?"
                ),
            )
        )

        selected_document_ids = [
            candidate.source.source_id for candidate in packet.selected_candidates
        ]
        selected_document_classes = [
            candidate.source.source_class.value
            for candidate in packet.selected_candidates
        ]
        reason_codes_by_source = {
            decision.source_id: {reason.value for reason in decision.reason_codes}
            for decision in packet.trace.decisions
            if decision.source_id
        }

        self.assertEqual(resolved_repo_root, sample_repo_root.resolve())
        self.assertEqual(resolved_docs_root, (sample_repo_root / "docs").resolve())
        self.assertEqual(
            selected_document_ids,
            [
                "Authoritative/Canon/Architecture/Repo-Guidance.md",
                "Planning/Current-Work.md",
                "Reviews/Review-Notes.md",
            ],
        )
        self.assertEqual(
            selected_document_classes,
            ["authoritative", "planning", "reviews"],
        )
        self.assertIn(
            "authority_priority",
            reason_codes_by_source["Authoritative/Canon/Architecture/Repo-Guidance.md"],
        )
        self.assertEqual(
            packet.trace.metadata["selected_source_classes"],
            "authoritative,planning,reviews",
        )

    def test_help_mentions_sample_repo_reference(self) -> None:
        result = subprocess.run(
            [sys.executable, str(_WORKFLOW_SCRIPT), "--help"],
            cwd=_REPO_ROOT,
            capture_output=True,
            text=True,
            env=os.environ.copy(),
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "examples/codex_repository_workflow/sample_repo/README.md",
            result.stdout,
        )
        self.assertIn(
            "Relative --docs-root values are resolved from",
            result.stdout,
        )
        self.assertIn(
            "--repo-root.",
            result.stdout,
        )

    def test_show_trace_script_emits_highlights_and_trace_output(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_root = repo_root / "docs"
            self._write_doc(
                docs_root / "Authoritative" / "Canon" / "Architecture" / "Guidance.md",
                """
                # Guidance

                Trace output should stay inspectable when repository workflow
                demonstrations are used for internal review.
                """,
            )

            environment = os.environ.copy()
            environment["PYTHONPATH"] = str(_REPO_ROOT / "src")
            environment["CONTEXT_ATLAS_LOG_LEVEL"] = "WARNING"

            result = subprocess.run(
                [
                    sys.executable,
                    str(_SHOW_TRACE_SCRIPT),
                    "--repo-root",
                    str(repo_root),
                    "--query",
                    "How should trace demonstrations be reviewed?",
                ],
                cwd=_REPO_ROOT,
                capture_output=True,
                text=True,
                env=environment,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("=== Codex Context ===", result.stdout)
            self.assertIn("=== Trace Highlights ===", result.stdout)
            self.assertIn("=== Trace Inspection ===", result.stdout)
            self.assertIn("- workflow: codex_repository", result.stdout)

    def test_show_trace_help_reuses_shared_repository_workflow_cli_surface(
        self,
    ) -> None:
        result = subprocess.run(
            [sys.executable, str(_SHOW_TRACE_SCRIPT), "--help"],
            cwd=_REPO_ROOT,
            capture_output=True,
            text=True,
            env=os.environ.copy(),
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "examples/codex_repository_workflow/sample_repo/README.md",
            result.stdout,
        )
        self.assertIn(
            "Relative --docs-root values are resolved from",
            result.stdout,
        )

    def test_show_trace_module_invocation_uses_package_safe_imports(self) -> None:
        environment = os.environ.copy()
        environment["PYTHONPATH"] = str(_REPO_ROOT / "src")

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "examples.codex_repository_workflow.show_trace",
                "--help",
            ],
            cwd=_REPO_ROOT,
            capture_output=True,
            text=True,
            env=environment,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "examples/codex_repository_workflow/sample_repo/README.md",
            result.stdout,
        )

    def _write_doc(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
