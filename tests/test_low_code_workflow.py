"""Validation tests for the low-code workflow example."""

from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import textwrap
import tomllib
import unittest

from context_atlas.domain.models import ContextSourceFamily
from context_atlas.infrastructure.config.presets import (
    DEFAULT_LOW_CODE_WORKFLOW_PRESET,
    build_low_code_workflow_config_artifact,
    build_low_code_workflow_preset_artifact,
)

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKFLOW_SCRIPT = _REPO_ROOT / "examples" / "low_code_workflow" / "run.py"
_WORKFLOW_CONFIG_ARTIFACT = (
    _REPO_ROOT / "examples" / "low_code_workflow" / "config.example.toml"
)
_WORKFLOW_PRESET_ARTIFACT = (
    _REPO_ROOT / "examples" / "low_code_workflow" / "presets" / "basic.toml"
)
_MODULE_SPEC = importlib.util.spec_from_file_location(
    "low_code_workflow_run",
    _WORKFLOW_SCRIPT,
)
assert _MODULE_SPEC is not None and _MODULE_SPEC.loader is not None
_WORKFLOW_MODULE = importlib.util.module_from_spec(_MODULE_SPEC)
_MODULE_SPEC.loader.exec_module(_WORKFLOW_MODULE)


class LowCodeWorkflowTests(unittest.TestCase):
    """Keep the low-code wrapper honest as a real Atlas integration path."""

    def test_workflow_packet_mixes_documents_and_structured_records(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_root = repo_root / "docs" / "Guides"
            self._write_doc(
                docs_root / "getting-started.md",
                """
                # Getting Started

                Low-code builders should keep guided docs visible and inspect
                packet plus trace output when validating Atlas behavior.
                """,
            )
            self._write_doc(
                docs_root / "operations.md",
                """
                # Operations

                Support-style rows should remain already-fetched outer inputs
                even when Atlas provides a lower-code wrapper path.
                """,
            )
            records_path = self._write_records_file(repo_root / "records.json")

            with _temporary_environment(CONTEXT_ATLAS_LOG_LEVEL="WARNING"):
                resolved_repo_root, low_code_settings, packet = (
                    _WORKFLOW_MODULE.assemble_low_code_workflow_packet(
                        repo_root_arg=repo_root,
                        query=(
                            "How should a low-code builder validate Atlas packet "
                            "and trace behavior?"
                        ),
                        docs_root="docs/Guides",
                        records_file="records.json",
                    )
                )

            source_families = {
                candidate.source.provenance.source_family
                for candidate in packet.selected_candidates
            }

            self.assertEqual(resolved_repo_root, repo_root.resolve())
            self.assertEqual(low_code_settings.preset, "chatbot_docs_records")
            self.assertEqual(
                source_families,
                {
                    ContextSourceFamily.DOCUMENT,
                    ContextSourceFamily.STRUCTURED_RECORD,
                },
            )
            self.assertIsNotNone(packet.trace)
            assert packet.trace is not None
            self.assertEqual(
                packet.trace.metadata["request_workflow"],
                "low_code_chatbot",
            )
            self.assertEqual(
                packet.trace.metadata["request_low_code_preset"],
                "chatbot_docs_records",
            )
            self.assertEqual(
                packet.trace.metadata["request_docs_root"],
                docs_root.resolve().as_posix(),
            )
            self.assertEqual(
                packet.trace.metadata["request_records_file"],
                records_path.resolve().as_posix(),
            )
            self.assertEqual(
                packet.trace.metadata["request_enabled_source_families"],
                "document,structured_record",
            )

    def test_workflow_can_disable_documents_and_keep_records_only(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            records_path = self._write_records_file(repo_root / "records.json")

            with _temporary_environment(CONTEXT_ATLAS_LOG_LEVEL="WARNING"):
                _, low_code_settings, packet = (
                    _WORKFLOW_MODULE.assemble_low_code_workflow_packet(
                        repo_root_arg=repo_root,
                        query="How should a low-code builder validate record inputs?",
                        records_file="records.json",
                        include_documents=False,
                    )
                )

            self.assertFalse(low_code_settings.include_documents)
            self.assertTrue(low_code_settings.include_records)
            source_families = {
                candidate.source.provenance.source_family
                for candidate in packet.selected_candidates
            }
            self.assertEqual(
                source_families,
                {ContextSourceFamily.STRUCTURED_RECORD},
            )
            self.assertIsNotNone(packet.trace)
            assert packet.trace is not None
            self.assertEqual(
                packet.trace.metadata["request_enabled_source_families"],
                "structured_record",
            )
            self.assertNotIn("request_docs_root", packet.trace.metadata)
            self.assertEqual(
                packet.trace.metadata["request_records_file"],
                records_path.resolve().as_posix(),
            )

    def test_workflow_script_emits_context_and_trace_sections(self) -> None:
        with TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            docs_root = repo_root / "docs" / "Guides"
            self._write_doc(
                docs_root / "guide.md",
                """
                # Guide

                Low-code builders should see packet and trace inspection output
                without needing to wire retrievers or adapters manually.
                """,
            )
            self._write_records_file(repo_root / "records.json")

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
                    "docs/Guides",
                    "--records-file",
                    "records.json",
                    "--query",
                    "How should a low-code builder review Atlas output?",
                ],
                cwd=_REPO_ROOT,
                capture_output=True,
                text=True,
                env=environment,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Preset: chatbot_docs_records", result.stdout)
            self.assertIn("=== Chatbot Context ===", result.stdout)
            self.assertIn("=== Packet Inspection ===", result.stdout)
            self.assertIn("=== Trace Highlights ===", result.stdout)
            self.assertIn("=== Trace Inspection ===", result.stdout)
            self.assertIn(
                "request_low_code_preset: chatbot_docs_records", result.stdout
            )
            self.assertIn(
                "request_enabled_source_families: document,structured_record",
                result.stdout,
            )

    def test_help_mentions_repo_root_resolution_and_presets(self) -> None:
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
            "Relative --docs-root and --records-file values are resolved from",
            result.stdout,
        )
        self.assertIn(
            "chatbot_docs_records",
            result.stdout,
        )
        self.assertIn(
            "--no-documents",
            result.stdout,
        )

    def test_reference_artifacts_match_supported_low_code_surface(self) -> None:
        with _WORKFLOW_CONFIG_ARTIFACT.open("rb") as config_file:
            config_artifact = tomllib.load(config_file)
        with _WORKFLOW_PRESET_ARTIFACT.open("rb") as preset_file:
            preset_artifact = tomllib.load(preset_file)

        self.assertEqual(
            config_artifact,
            build_low_code_workflow_config_artifact(),
        )
        self.assertEqual(
            preset_artifact,
            build_low_code_workflow_preset_artifact(DEFAULT_LOW_CODE_WORKFLOW_PRESET),
        )

    def _write_doc(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")

    def _write_records_file(self, path: Path) -> Path:
        path.write_text(
            json.dumps(
                [
                    {
                        "ticket_id": "support-301",
                        "title": "Inspection guidance",
                        "body": (
                            "Low-code builders should inspect packet and trace "
                            "output when validating Atlas behavior."
                        ),
                        "uri": "records://support/support-301",
                        "uses": ["answering", "support"],
                        "team": "support",
                        "table": "support_tickets",
                        "database": "atlas_app",
                    },
                    {
                        "ticket_id": "support-302",
                        "title": "Preflight note",
                        "body": (
                            "Run py -3 scripts/preflight.py before push and keep "
                            "the relevant __ai__.md owner files updated."
                        ),
                        "uri": "records://support/support-302",
                        "uses": ["support", "troubleshooting"],
                        "team": "developer-experience",
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


class _temporary_environment:
    """Temporarily set and later restore selected environment variables."""

    def __init__(self, **overrides: str) -> None:
        self._overrides = overrides
        self._previous: dict[str, str | None] = {}

    def __enter__(self) -> None:
        for key, value in self._overrides.items():
            self._previous[key] = os.environ.get(key)
            os.environ[key] = value

    def __exit__(self, *_: object) -> None:
        for key, previous in self._previous.items():
            if previous is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = previous


if __name__ == "__main__":
    unittest.main()
