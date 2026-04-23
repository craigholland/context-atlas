"""Unit tests for portable Verification Contract command normalization."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


_REPO_ROOT = Path(__file__).resolve().parents[1]
_SCRIPT_PATH = _REPO_ROOT / "scripts" / "ai_verify_contracts.py"
_MODULE_SPEC = importlib.util.spec_from_file_location(
    "context_atlas_ai_verify_contracts",
    _SCRIPT_PATH,
)
assert _MODULE_SPEC is not None and _MODULE_SPEC.loader is not None
_MODULE = importlib.util.module_from_spec(_MODULE_SPEC)
_MODULE_SPEC.loader.exec_module(_MODULE)


class PortablePythonCommandNormalizationTests(unittest.TestCase):
    """Keep shell-neutral Verification Contract commands runnable everywhere."""

    def test_powershell_normalizes_portable_python_launcher(self) -> None:
        normalized = _MODULE._normalize_portable_python_commands(
            "python -m pytest tests/test_cli.py",
            shell_prefix=["pwsh", "-Command"],
            python_executable=r"C:\Python314\python.exe",
        )

        self.assertEqual(
            normalized,
            '& "C:\\Python314\\python.exe" -m pytest tests/test_cli.py',
        )

    def test_bash_normalizes_portable_python_launcher(self) -> None:
        normalized = _MODULE._normalize_portable_python_commands(
            "python scripts/preflight.py",
            shell_prefix=["bash", "-lc"],
            python_executable="/opt/python 3.14/bin/python3",
        )

        self.assertEqual(
            normalized,
            "'/opt/python 3.14/bin/python3' scripts/preflight.py",
        )

    def test_multiline_contract_only_rewrites_leading_python_commands(self) -> None:
        normalized = _MODULE._normalize_portable_python_commands(
            "\n".join(
                (
                    "# comment stays untouched",
                    "python -m ruff check .",
                    "echo done",
                    "python -m pytest",
                )
            ),
            shell_prefix=["pwsh", "-Command"],
            python_executable=r"C:\Python314\python.exe",
        )

        self.assertEqual(
            normalized,
            "\n".join(
                (
                    "# comment stays untouched",
                    '& "C:\\Python314\\python.exe" -m ruff check .',
                    "echo done",
                    '& "C:\\Python314\\python.exe" -m pytest',
                )
            ),
        )


if __name__ == "__main__":
    unittest.main()
