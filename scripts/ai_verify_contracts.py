"""
Execute Verification Contract steps from affected owner files.

This example script is intentionally conservative:
- it only reads the nearest affected owner files (for example `__ai__.md`)
- it expects a simple CI-like YAML block under "## Verification Contract"
- it treats the block as executable shell instructions and runs each step in order

This is powerful but blunt tooling. Treat it as a repository-owned contract runner,
not as an untrusted general-purpose workflow engine.
"""

import argparse
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

DEFAULT_OWNER_FILENAME = "__ai__.md"
DEFAULT_FALLBACK_BASE_REFS = (
    "origin/development",
    "development",
    "origin/main",
    "main",
    "origin/master",
    "master",
)


def _run(cmd: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)


def _git_ref_exists(repo_root: Path, ref: str) -> bool:
    result = _run(["git", "rev-parse", "--verify", f"{ref}^{{commit}}"], cwd=repo_root)
    return result.returncode == 0


def _git_merge_base(repo_root: Path, base_ref: str, head_ref: str) -> str | None:
    result = _run(["git", "merge-base", base_ref, head_ref], cwd=repo_root)
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None


def _resolve_diff_base(
    repo_root: Path,
    *,
    base_ref: str | None,
    head_ref: str,
    fallback_base_refs: tuple[str, ...],
) -> str:
    if not _git_ref_exists(repo_root, head_ref):
        raise RuntimeError(f"head ref '{head_ref}' is not a valid commit")

    if base_ref and _git_ref_exists(repo_root, base_ref):
        return base_ref

    for candidate in fallback_base_refs:
        merge_base = _git_merge_base(repo_root, candidate, head_ref)
        if merge_base:
            return merge_base

    parent_ref = f"{head_ref}^"
    if _git_ref_exists(repo_root, parent_ref):
        return parent_ref

    return head_ref


def _git_diff_name_only(
    repo_root: Path,
    *,
    base_ref: str | None,
    head_ref: str,
    fallback_base_refs: tuple[str, ...],
) -> list[Path]:
    diff_base = _resolve_diff_base(
        repo_root,
        base_ref=base_ref,
        head_ref=head_ref,
        fallback_base_refs=fallback_base_refs,
    )
    result = _run(
        ["git", "diff", "--name-only", f"{diff_base}...{head_ref}"], cwd=repo_root
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"git diff failed\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return [Path(line.strip()) for line in result.stdout.splitlines() if line.strip()]


def _nearest_owner_file(
    repo_root: Path, rel_path: Path, owner_filename: str
) -> Path | None:
    current = (repo_root / rel_path).parent

    while True:
        candidate = current / owner_filename
        if candidate.exists():
            return candidate.relative_to(repo_root)

        if current == repo_root:
            return None

        current = current.parent


def _changed_owner_files(
    repo_root: Path,
    changed_paths: list[Path],
    *,
    owner_filename: str,
) -> list[Path]:
    required: set[Path] = set()

    for rel_path in changed_paths:
        if rel_path.name == owner_filename:
            required.add(rel_path)
            continue

        nearest = _nearest_owner_file(repo_root, rel_path, owner_filename)
        if nearest is not None:
            required.add(nearest)

    return sorted(required)


def _extract_verification_steps(owner_abs: Path) -> list[tuple[str, str]]:
    """
    Parse a small YAML-like block without requiring a YAML dependency.

    This assumes the canonical template shape:

    ## Verification Contract
    ```yaml
    steps:
      - name: lint
        run: |
          python -m ruff check ...
    ```
    """
    text = owner_abs.read_text(encoding="utf-8")

    block_match = re.search(
        r"^##\s+Verification Contract(?:[^\n`]*)?\n\s*```ya?ml\s*(.*?)```",
        text,
        flags=re.DOTALL | re.IGNORECASE | re.MULTILINE,
    )
    if not block_match:
        return []

    block = block_match.group(1)

    step_pattern = re.compile(
        r"- name:\s*(.*?)\n\s*run:\s*\|\n((?:\s{6,}.*\n?)*)",
        flags=re.MULTILINE,
    )

    steps: list[tuple[str, str]] = []
    for name, run_block in step_pattern.findall(block):
        lines: list[str] = []
        for line in run_block.splitlines():
            lines.append(line[6:] if line.startswith("      ") else line.lstrip())
        steps.append((name.strip(), "\n".join(lines).strip()))

    return steps


def _shell_command_prefix() -> list[str]:
    """
    Choose a shell runner.

    Context Atlas owner files now prefer portable `python ...` command shapes in
    their executable Verification Contract steps. Prefer PowerShell on Windows
    so local contract execution stays consistent with desktop use, and prefer
    bash on non-Windows platforms.
    """
    if os.name == "nt":
        if shutil.which("pwsh"):
            return ["pwsh", "-Command"]
        if shutil.which("powershell"):
            return ["powershell", "-Command"]

    if shutil.which("bash"):
        return ["bash", "-lc"]

    if shutil.which("pwsh"):
        return ["pwsh", "-Command"]
    if shutil.which("powershell"):
        return ["powershell", "-Command"]

    raise RuntimeError(
        "No supported shell executable found (expected bash or PowerShell)."
    )


def _shell_kind(shell_prefix: list[str]) -> str:
    if shell_prefix and shell_prefix[0] == "bash":
        return "bash"
    return "powershell"


def _quote_executable_for_shell(executable: str, shell_kind: str) -> str:
    if shell_kind == "bash":
        return shlex.quote(executable)
    escaped = executable.replace("`", "``").replace('"', '`"')
    return f'"{escaped}"'


def _normalize_portable_python_commands(
    shell_cmd: str,
    *,
    shell_prefix: list[str],
    python_executable: str | None = None,
) -> str:
    """
    Rewrite leading `python ...` lines to the current interpreter path.

    This keeps owner-file contracts shell-neutral while still allowing local
    PowerShell execution on Windows machines where `python` is not a guaranteed
    launcher on PATH.
    """

    shell_kind = _shell_kind(shell_prefix)
    executable = _quote_executable_for_shell(
        python_executable or sys.executable,
        shell_kind,
    )
    launcher = f"& {executable}" if shell_kind == "powershell" else executable

    return re.sub(
        r"(?m)^(?P<indent>\s*)python(?P<rest>(?:\s|$).*)$",
        lambda match: f"{match.group('indent')}{launcher}{match.group('rest')}",
        shell_cmd,
    )


def _verify_owner_file(repo_root: Path, owner_rel: Path) -> list[tuple[str, int]]:
    owner_abs = repo_root / owner_rel
    steps = _extract_verification_steps(owner_abs)

    print(f"[ai_verify_contracts] Verifying: {owner_rel.as_posix()}")

    if not steps:
        print("[ai_verify_contracts] No Verification Contract found; skipping.")
        return []

    failures: list[tuple[str, int]] = []
    shell_prefix = _shell_command_prefix()

    for step_name, shell_cmd in steps:
        print(f"\n=== [ai_verify_contracts] step: {step_name} ===\n")
        normalized_shell_cmd = _normalize_portable_python_commands(
            shell_cmd,
            shell_prefix=shell_prefix,
        )
        result = _run(shell_prefix + [normalized_shell_cmd], cwd=repo_root)
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="")
        if result.returncode != 0:
            failures.append((step_name, result.returncode))

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Execute Verification Contract steps from affected owner files."
    )
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--base", default=None)
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--owner-file", default=DEFAULT_OWNER_FILENAME)
    parser.add_argument(
        "--files",
        nargs="*",
        default=[],
        help="Optional explicit owner files to verify directly.",
    )
    parser.add_argument(
        "--fallback-base-ref",
        action="append",
        default=[],
        help="Optional fallback refs used when --base is missing or invalid.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    fallback_base_refs = tuple(args.fallback_base_ref) or DEFAULT_FALLBACK_BASE_REFS

    if args.files:
        target_files = sorted({Path(path) for path in args.files})
    else:
        changed_paths = _git_diff_name_only(
            repo_root,
            base_ref=args.base,
            head_ref=args.head,
            fallback_base_refs=fallback_base_refs,
        )
        target_files = _changed_owner_files(
            repo_root,
            changed_paths,
            owner_filename=args.owner_file,
        )

    if not target_files:
        print("[ai_verify_contracts] No affected owner files found.")
        return 0

    all_failures: list[tuple[Path, str, int]] = []

    for owner_rel in target_files:
        failures = _verify_owner_file(repo_root, owner_rel)
        for step_name, rc in failures:
            all_failures.append((owner_rel, step_name, rc))

    if all_failures:
        print("\n[ai_verify_contracts] FAILURES:")
        for owner_rel, step_name, rc in all_failures:
            print(f"  - {owner_rel.as_posix()} :: {step_name} (rc={rc})")
        return 1

    print("\n[ai_verify_contracts] All contract verifications passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
