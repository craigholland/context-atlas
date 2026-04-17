from __future__ import annotations

"""
Validate the structural shape of affected `__ai__.md` files.

This script intentionally focuses on structure, not meaning.
It is useful for catching:

- missing required sections
- empty high-value sections
- malformed Verification Contract blocks

It is not a semantic reviewer and should not be treated as one.
"""

import argparse
import re
import subprocess
from pathlib import Path

DEFAULT_OWNER_FILENAME = "__ai__.md"
DEFAULT_FALLBACK_BASE_REFS = ("origin/main", "main", "origin/master", "master")

# Keep this list aligned with the canonical `__ai__.md` template doc.
REQUIRED_HEADINGS = [
    "## Last Verified (CI)",
    "## Scope",
    "## Purpose",
    "## Architectural Rules",
    "## Allowed Dependencies",
    "## Public API / Key Exports",
    "## File Index",
    "## Known Gaps / Future-State Notes",
    "## Cross-Folder Contracts",
    "## Verification Contract",
]


def _run(cmd: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


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
    result = _run(["git", "diff", "--name-only", f"{diff_base}...{head_ref}"], cwd=repo_root)
    if result.returncode != 0:
        raise RuntimeError(
            "git diff failed\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
    return [Path(line.strip()) for line in result.stdout.splitlines() if line.strip()]


def _nearest_owner_file(repo_root: Path, rel_path: Path, owner_filename: str) -> Path | None:
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


def _validate_headings(text: str, *, owner_rel: Path) -> list[str]:
    errors: list[str] = []
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"{owner_rel.as_posix()}: missing required heading '{heading}'")
    return errors


def _validate_non_empty_section(text: str, heading: str, *, owner_rel: Path) -> list[str]:
    pattern = re.compile(
        rf"^{re.escape(heading)}\n(.*?)(?=^## |\Z)",
        flags=re.DOTALL | re.MULTILINE,
    )
    match = pattern.search(text)
    if not match:
        return []

    if not match.group(1).strip():
        return [f"{owner_rel.as_posix()}: section '{heading}' must not be empty"]

    return []


def _validate_verification_contract(text: str, *, owner_rel: Path) -> list[str]:
    """
    Keep the parser intentionally lightweight.

    The goal here is not to validate arbitrary YAML. It is to enforce the
    canonical section shape expected by the `__ai__.md` template.
    """
    block_match = re.search(
        r"^##\s+Verification Contract(?:[^\n`]*)?\n\s*```ya?ml\s*(.*?)```",
        text,
        flags=re.DOTALL | re.IGNORECASE | re.MULTILINE,
    )
    if not block_match:
        return [f"{owner_rel.as_posix()}: Verification Contract block missing or malformed"]

    block = block_match.group(1)
    if "- name:" not in block or "run: |" not in block:
        return [
            f"{owner_rel.as_posix()}: Verification Contract must contain at least "
            "one '- name:' step with a 'run: |' body"
        ]

    return []


def _validate_owner_file(repo_root: Path, owner_rel: Path) -> list[str]:
    text = (repo_root / owner_rel).read_text(encoding="utf-8")
    errors: list[str] = []
    errors.extend(_validate_headings(text, owner_rel=owner_rel))
    errors.extend(_validate_non_empty_section(text, "## Scope", owner_rel=owner_rel))
    errors.extend(_validate_non_empty_section(text, "## Purpose", owner_rel=owner_rel))
    errors.extend(_validate_non_empty_section(text, "## File Index", owner_rel=owner_rel))
    errors.extend(
        _validate_non_empty_section(
            text,
            "## Cross-Folder Contracts",
            owner_rel=owner_rel,
        )
    )
    errors.extend(_validate_verification_contract(text, owner_rel=owner_rel))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the structure of affected owner files such as __ai__.md."
    )
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--base", default=None)
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--owner-file", default=DEFAULT_OWNER_FILENAME)
    parser.add_argument("--files", nargs="*", default=[])
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
        print("[validate_ai_docs] No affected owner files found.")
        return 0

    all_errors: list[str] = []

    for owner_rel in target_files:
        print(f"[validate_ai_docs] Validating: {owner_rel.as_posix()}")
        all_errors.extend(_validate_owner_file(repo_root, owner_rel))

    if all_errors:
        print("[validate_ai_docs] FAIL:")
        for error in all_errors:
            print(f"  - {error}")
        return 1

    print("[validate_ai_docs] All affected owner files passed structural validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
