"""Validation tests for the technical-builder docs-plus-database workflow example."""

from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import textwrap
import unittest

from context_atlas.domain.models import ContextSourceFamily

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKFLOW_SCRIPT = _REPO_ROOT / "examples" / "docs_database_workflow" / "run.py"
_RECORD_FEED_SCRIPT = (
    _REPO_ROOT / "examples" / "docs_database_workflow" / "record_feed.py"
)
_MODULE_SPEC = importlib.util.spec_from_file_location(
    "docs_database_workflow_run",
    _WORKFLOW_SCRIPT,
)
assert _MODULE_SPEC is not None and _MODULE_SPEC.loader is not None
_WORKFLOW_MODULE = importlib.util.module_from_spec(_MODULE_SPEC)
_MODULE_SPEC.loader.exec_module(_WORKFLOW_MODULE)
_RECORD_FEED_SPEC = importlib.util.spec_from_file_location(
    "docs_database_workflow_record_feed",
    _RECORD_FEED_SCRIPT,
)
assert _RECORD_FEED_SPEC is not None and _RECORD_FEED_SPEC.loader is not None
_RECORD_FEED_MODULE = importlib.util.module_from_spec(_RECORD_FEED_SPEC)
_RECORD_FEED_SPEC.loader.exec_module(_RECORD_FEED_MODULE)


class DocsDatabaseWorkflowTests(unittest.TestCase):
    """Keep the technical-builder mixed-source workflow honest and inspectable."""

    def test_workflow_packet_mixes_documents_and_structured_records(self) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            self._write_doc(
                docs_root / "getting-started.md",
                """
                # Getting Started

                Builders should configure Context Atlas through environment
                variables and inspect packet plus trace output when
                troubleshooting chatbot pipelines.
                """,
            )
            self._write_doc(
                docs_root / "operations.md",
                """
                # Operations

                Preflight should run before push, and troubleshooting guidance
                should stay visible in governed documentation.
                """,
            )

            records_path = self._write_records_file(docs_root / "sample_records.json")
            resolved_docs_root, records_file, record_count, packet = (
                _WORKFLOW_MODULE.assemble_docs_database_workflow_packet(
                    docs_root_arg=docs_root,
                    records_file_arg=records_path,
                    query=(
                        "How should a builder configure Context Atlas and "
                        "troubleshoot preflight or environment-loading issues "
                        "in a chatbot pipeline?"
                    ),
                )
            )

            source_families = {
                candidate.source.provenance.source_family
                for candidate in packet.selected_candidates
            }

            self.assertEqual(resolved_docs_root, docs_root.resolve())
            self.assertEqual(records_file, records_path.resolve())
            self.assertEqual(record_count, 3)
            self.assertEqual(
                source_families,
                {
                    ContextSourceFamily.DOCUMENT,
                    ContextSourceFamily.STRUCTURED_RECORD,
                },
            )
            self.assertEqual(
                packet.trace.metadata["request_workflow"],
                "docs_database_builder",
            )
            self.assertEqual(
                packet.trace.metadata["request_record_origin"],
                "already_fetched_rows",
            )
            self.assertIn(
                "document=",
                packet.trace.metadata["selected_source_family_counts"],
            )
            self.assertIn(
                "structured_record=",
                packet.trace.metadata["selected_source_family_counts"],
            )
            self.assertIn(
                "docs_database_demo_records",
                packet.trace.metadata["selected_source_collectors"],
            )

    def test_workflow_script_emits_chatbot_context_and_mixed_source_trace(
        self,
    ) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            self._write_doc(
                docs_root / "support-guide.md",
                """
                # Support Guide

                Builders should inspect packet and trace output when
                troubleshooting environment loading or preflight issues.
                """,
            )
            records_path = self._write_records_file(docs_root / "sample_records.json")

            environment = os.environ.copy()
            environment["PYTHONPATH"] = str(_REPO_ROOT / "src")
            environment["CONTEXT_ATLAS_LOG_LEVEL"] = "WARNING"

            result = subprocess.run(
                [
                    sys.executable,
                    str(_WORKFLOW_SCRIPT),
                    "--docs-root",
                    str(docs_root),
                    "--records-file",
                    str(records_path),
                    "--query",
                    (
                        "How should a builder configure Context Atlas and "
                        "troubleshoot preflight or environment-loading issues "
                        "in a chatbot pipeline?"
                    ),
                ],
                cwd=_REPO_ROOT,
                capture_output=True,
                text=True,
                env=environment,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("=== Chatbot Context ===", result.stdout)
            self.assertIn("Records file:", result.stdout)
            self.assertIn("=== Packet Inspection ===", result.stdout)
            self.assertIn("=== Trace Highlights ===", result.stdout)
            self.assertIn("=== Trace Inspection ===", result.stdout)
            self.assertIn(
                "selected_source_families: document,structured_record", result.stdout
            )
            self.assertIn("selected_source_family_counts:", result.stdout)
            self.assertIn("request_record_origin: already_fetched_rows", result.stdout)
            self.assertIn("Record boundary note:", result.stdout)

    def test_record_feed_module_loads_tracked_sample_payload(self) -> None:
        records_file = _RECORD_FEED_MODULE.resolve_records_file(None)

        rows = _RECORD_FEED_MODULE.load_record_rows(records_file)

        self.assertEqual(records_file.name, "sample_records.json")
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0]["ticket_id"], "support-101")

    def test_workflow_script_can_write_standard_proof_artifacts(self) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            proof_dir = docs_root / "proof"
            self._write_doc(
                docs_root / "support-guide.md",
                """
                # Support Guide

                Proof workflows should emit reproducible packet, trace, and
                rendered-context artifacts from the supported mixed-source path.
                """,
            )
            records_path = self._write_records_file(docs_root / "sample_records.json")

            environment = os.environ.copy()
            environment["PYTHONPATH"] = str(_REPO_ROOT / "src")
            environment["CONTEXT_ATLAS_LOG_LEVEL"] = "WARNING"

            result = subprocess.run(
                [
                    sys.executable,
                    str(_WORKFLOW_SCRIPT),
                    "--docs-root",
                    str(docs_root),
                    "--records-file",
                    str(records_path),
                    "--query",
                    "How should proof artifacts be generated for the mixed-source workflow?",
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

            self.assertEqual(packet["metadata"]["workflow"], "docs_database_builder")
            self.assertEqual(
                trace["metadata"]["request_workflow"],
                "docs_database_builder",
            )

    def _write_doc(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")

    def _write_records_file(self, path: Path) -> Path:
        path.write_text(
            json.dumps(
                [
                    {
                        "ticket_id": "support-201",
                        "title": "Environment troubleshooting",
                        "body": (
                            "Builders should inspect packet and trace output when "
                            "debugging configuration and preflight issues."
                        ),
                        "uri": "records://support/support-201",
                        "uses": ["answering", "support"],
                        "team": "support",
                        "table": "support_tickets",
                        "database": "atlas_app",
                    },
                    {
                        "ticket_id": "support-202",
                        "title": "Preflight note",
                        "body": (
                            "Run py -3 scripts/preflight.py before push and keep "
                            "the relevant __ai__.md files updated."
                        ),
                        "uri": "records://support/support-202",
                        "uses": ["support", "troubleshooting"],
                        "team": "developer-experience",
                        "table": "support_tickets",
                        "database": "atlas_app",
                    },
                    {
                        "ticket_id": "support-203",
                        "title": "Starter path note",
                        "body": (
                            "Builder-facing guidance should keep the shared runtime "
                            "knob and inspection story visible."
                        ),
                        "uri": "records://support/support-203",
                        "uses": ["answering", "onboarding"],
                        "team": "developer-education",
                        "table": "support_tickets",
                        "database": "atlas_app",
                    },
                ],
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return path


if __name__ == "__main__":
    unittest.main()
