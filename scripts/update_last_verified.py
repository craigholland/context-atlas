"""
Update the "Last Verified (CI)" block in affected `__ai__.md` owner files.

This example is designed to be copied into a real repository and adapted there.
It is intentionally generic:

- the repository root is configurable
- the owner filename is configurable
- the base/head refs are configurable
- fallback base refs can be customized to match your branch strategy

What it does:
1. Find changed files in a git diff.
2. Map each changed file to its nearest owning `__ai__.md`.
3. Skip diffs that only touch `__ai__.md` files to avoid self-trigger loops.
4. Rewrite the "Last Verified (CI)" block in the owning files.

What it does not do:
- prove the guidance text is semantically correct
- detect whether a human should have updated the surrounding prose
- commit or push changes; the workflow should decide that
"""

import argparse
import re
import subprocess
from datetime import datetime, timezone
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
    """Run a command and capture stdout/stderr for later reporting."""
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        capture_output=True,
    )


def _git_ref_exists(repo_root: Path, ref: str) -> bool:
    """Return True if the provided ref resolves to a commit."""
    result = _run(["git", "rev-parse", "--verify", f"{ref}^{{commit}}"], cwd=repo_root)
    return result.returncode == 0


def _git_merge_base(repo_root: Path, base_ref: str, head_ref: str) -> str | None:
    """Return merge-base(base_ref, head_ref) or None if it cannot be resolved."""
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
    """
    Resolve a safe base ref for diffing.

    Why this is more complex than `git diff base...head`:
    - CI events sometimes provide an empty or unusable base SHA
    - a branch name may not exist in shallow/local clones
    - rewritten history can remove the originally expected base
    """
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
    """Return changed file paths relative to the repository root."""
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
    """Walk upward from a changed file until a matching owner file is found."""
    current = (repo_root / rel_path).parent

    while True:
        candidate = current / owner_filename
        if candidate.exists():
            return candidate.relative_to(repo_root)

        if current == repo_root:
            return None

        current = current.parent


def _affected_owner_files(
    repo_root: Path,
    changed_paths: list[Path],
    *,
    owner_filename: str,
) -> list[Path]:
    """
    Return the set of owner files that should receive a Last Verified update.

    We update only the nearest owner for non-owner changes.
    If an owner file itself changed, we do not treat that alone as a reason to
    rewrite metadata, because doing so creates noisy self-trigger loops.
    """
    owners: set[Path] = set()

    for rel_path in changed_paths:
        if rel_path.name == owner_filename:
            continue

        nearest = _nearest_owner_file(repo_root, rel_path, owner_filename)
        if nearest is not None:
            owners.add(nearest)

    return sorted(owners)


def _rewrite_last_verified_block(
    text: str,
    *,
    commit: str,
    timestamp_utc: str,
    verified_by: str,
) -> str:
    """
    Replace the existing Last Verified block or insert one at the top.

    The regex intentionally expects the canonical section shape described in the
    Craig Architecture `__ai__.md` template document.
    """
    pattern = re.compile(
        r"## Last Verified \(CI\)\n"
        r"- commit: .*?\n"
        r"- timestamp_utc: .*?\n"
        r"- verified_by: .*?\n"
        r"- notes: .*?(?=\n## |\Z)",
        flags=re.DOTALL,
    )

    replacement = (
        "## Last Verified (CI)\n"
        f"- commit: {commit}\n"
        f"- timestamp_utc: {timestamp_utc}\n"
        f"- verified_by: {verified_by}\n"
        '- notes: Verified means "all commands in Verification Contract passed" '
        "(not a human review)."
    )

    if pattern.search(text):
        return pattern.sub(replacement, text, count=1)

    return replacement + "\n\n" + text


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Update Last Verified (CI) metadata in affected owner files."
    )
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--base", default=None)
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--owner-file", default=DEFAULT_OWNER_FILENAME)
    parser.add_argument("--verified-by", default="ci")
    parser.add_argument(
        "--fallback-base-ref",
        action="append",
        default=[],
        help="Optional fallback refs used when --base is missing or invalid. "
        "May be provided multiple times.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    fallback_base_refs = tuple(args.fallback_base_ref) or DEFAULT_FALLBACK_BASE_REFS

    changed_paths = _git_diff_name_only(
        repo_root,
        base_ref=args.base,
        head_ref=args.head,
        fallback_base_refs=fallback_base_refs,
    )

    if not changed_paths:
        print("[update_last_verified] No changed files detected.")
        return 0

    if all(path.name == args.owner_file for path in changed_paths):
        print(
            "[update_last_verified] Diff contains only owner-file changes; "
            "skipping metadata rewrite."
        )
        return 0

    owners = _affected_owner_files(
        repo_root,
        changed_paths,
        owner_filename=args.owner_file,
    )

    if not owners:
        print("[update_last_verified] No affected owner files found.")
        return 0

    commit = _run(["git", "rev-parse", args.head], cwd=repo_root).stdout.strip()
    timestamp = (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )

    for rel_path in owners:
        abs_path = repo_root / rel_path
        old_text = abs_path.read_text(encoding="utf-8")
        new_text = _rewrite_last_verified_block(
            old_text,
            commit=commit,
            timestamp_utc=timestamp,
            verified_by=args.verified_by,
        )
        if new_text != old_text:
            abs_path.write_text(new_text, encoding="utf-8")
            print(f"[update_last_verified] Updated: {rel_path.as_posix()}")
        else:
            print(f"[update_last_verified] No change needed: {rel_path.as_posix()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
