"""Run the repo-wide preflight checks that should pass before push or merge."""

import argparse
import subprocess
import sys
from pathlib import Path


def _run_step(name: str, command: list[str], *, cwd: Path) -> None:
    print(f"[preflight] step: {name}")
    result = subprocess.run(command, cwd=cwd, text=True)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def _discover_owner_files(repo_root: Path) -> list[str]:
    owner_files = {
        path.relative_to(repo_root).as_posix()
        for path in repo_root.rglob("__ai__.md")
        if "__pycache__" not in path.parts
    }
    return sorted(owner_files)


def _python_module_available(module_name: str) -> bool:
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            (
                "import importlib.util; "
                f"raise SystemExit(0 if importlib.util.find_spec('{module_name}') else 1)"
            ),
        ],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def _ensure_tooling() -> None:
    missing = [
        name
        for name in ("ruff", "mypy", "pytest")
        if not _python_module_available(name)
    ]
    if not missing:
        return

    joined = ", ".join(missing)
    raise SystemExit(
        "[preflight] Missing required dev tools: "
        f"{joined}. Install them with `python -m pip install -e .[dev]` "
        "(or `py -3 -m pip install -e .[dev]` on Windows)."
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the full local preflight before push or merge."
    )
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    owner_files = _discover_owner_files(repo_root)

    _ensure_tooling()

    _run_step(
        "compileall",
        [sys.executable, "-m", "compileall", "src", "tests", "scripts"],
        cwd=repo_root,
    )
    _run_step(
        "check-codex-materialization",
        [sys.executable, "scripts/check_codex_materialization.py", "--repo-root", "."],
        cwd=repo_root,
    )
    _run_step("ruff-check", [sys.executable, "-m", "ruff", "check", "."], cwd=repo_root)
    _run_step(
        "ruff-format-check",
        [sys.executable, "-m", "ruff", "format", "--check", "."],
        cwd=repo_root,
    )
    _run_step("mypy", [sys.executable, "-m", "mypy", "src"], cwd=repo_root)
    _run_step("pytest", [sys.executable, "-m", "pytest"], cwd=repo_root)
    _run_step(
        "import-boundaries",
        [
            sys.executable,
            "scripts/check_import_boundaries.py",
            "--repo-root",
            ".",
            "--config",
            "scripts/import_boundary_rules.toml",
        ],
        cwd=repo_root,
    )
    _run_step(
        "validate-ai-docs",
        [
            sys.executable,
            "scripts/validate_ai_docs.py",
            "--repo-root",
            ".",
            "--files",
            *owner_files,
        ],
        cwd=repo_root,
    )
    _run_step(
        "check-ai-docs-freshness",
        [
            sys.executable,
            "scripts/check_ai_docs.py",
            "--repo-root",
            ".",
            "--owner-file",
            "__ai__.md",
            "--governed-root",
            "src/context_atlas",
            "--governed-root",
            "tests",
            "--governed-root",
            "scripts",
            "--governed-root",
            ".github/workflows",
            "--suffix",
            ".py",
            "--suffix",
            ".toml",
            "--suffix",
            ".yml",
        ],
        cwd=repo_root,
    )
    _run_step(
        "verify-ai-contracts",
        [
            sys.executable,
            "scripts/ai_verify_contracts.py",
            "--repo-root",
            ".",
            "--files",
            *owner_files,
        ],
        cwd=repo_root,
    )

    print("[preflight] All checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
