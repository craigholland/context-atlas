"""Tests for the installable Context Atlas starter CLI surface."""

from __future__ import annotations

import contextlib
import io
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from context_atlas import __version__
from context_atlas.cli import main


class StarterCliTests(unittest.TestCase):
    """Keep the installable starter CLI aligned with the MVP docs surface."""

    def test_starter_cli_runs_against_a_docs_directory(self) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            (docs_root / "Guide.md").write_text(
                "# Guide\n\nPlanning docs should stay reviewable.\n",
                encoding="utf-8",
            )

            output = io.StringIO()
            with _temporary_environment(CONTEXT_ATLAS_LOG_LEVEL="WARNING"):
                with contextlib.redirect_stdout(output):
                    exit_code = main(
                        [
                            str(docs_root),
                            "--query",
                            "How should planning docs be treated?",
                        ]
                    )

        rendered = output.getvalue()
        self.assertEqual(exit_code, 0)
        self.assertIn("=== Rendered Context ===", rendered)
        self.assertIn("=== Packet Inspection ===", rendered)
        self.assertIn("=== Trace Inspection ===", rendered)

    def test_package_version_reflects_the_current_mvp_release(self) -> None:
        self.assertEqual(__version__, "0.1.2")


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
