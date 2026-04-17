"""
Heuristic freshness checker for `__ai__.md` owner files.

This script is intentionally opinionated:
- governed code roots are provided explicitly
- it checks whether changed governed files have a nearest owner file
- it checks whether the nearest owner file changed in the same diff
- it flags owner-file edits that only changed the Last Verified metadata block

This is a staleness heuristic, not a truth detector.
It can tell you that local guidance was probably not reviewed when it should
have been. It cannot tell you whether the prose is actually correct.
"""

import argparse
import subprocess
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
LAST_VERIFIED_HEADING = "## Last Verified (CI)"
SECTION_HEADING_PREFIX = "## "


def _run_git(repo_root: Path, args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(args)} failed (rc={result.returncode}).\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}\n"
        )
    return result.stdout


def _git_ref_exists(repo_root: Path, ref: str) -> bool:
    result = subprocess.run(
        ["git", "rev-parse", "--verify", f"{ref}^{{commit}}"],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def _git_merge_base(repo_root: Path, base_ref: str, head_ref: str) -> str | None:
    result = subprocess.run(
        ["git", "merge-base", base_ref, head_ref],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None


def _resolve_diff_endpoints(
    repo_root: Path,
    base: str | None,
    head: str | None,
    fallback_base_refs: tuple[str, ...],
) -> tuple[str, str] | None:
    """
    Resolve diff endpoints for the staleness check.

    Returning None means "no sensible diff range could be found", which we treat
    as a no-op instead of failing noisy in unusual bootstrap situations.
    """
    head_ref = head or "HEAD"
    if not _git_ref_exists(repo_root, head_ref):
        return None

    if base and _git_ref_exists(repo_root, base):
        return (base, head_ref)

    for candidate in fallback_base_refs:
        merge_base = _git_merge_base(repo_root, candidate, head_ref)
        if merge_base:
            return (merge_base, head_ref)

    if _git_ref_exists(repo_root, "HEAD^"):
        return ("HEAD^", head_ref)

    return None


def _changed_files(
    repo_root: Path,
    *,
    base: str | None,
    head: str | None,
    fallback_base_refs: tuple[str, ...],
) -> list[str]:
    diff_endpoints = _resolve_diff_endpoints(repo_root, base, head, fallback_base_refs)
    if diff_endpoints is None:
        return []

    diff_base, diff_head = diff_endpoints
    out = _run_git(repo_root, ["diff", "--name-only", f"{diff_base}...{diff_head}"])
    return [line.strip() for line in out.splitlines() if line.strip()]


def _nearest_owner_file(
    repo_root: Path, path: Path, owner_filename: str
) -> Path | None:
    current = (repo_root / path).parent

    while True:
        candidate = current / owner_filename
        if candidate.exists():
            return candidate.relative_to(repo_root)

        if current == repo_root:
            return None

        current = current.parent


def _is_governed_file(
    path: Path, governed_roots: tuple[Path, ...], suffixes: tuple[str, ...]
) -> bool:
    if path.suffix not in suffixes:
        return False
    if "__pycache__" in path.parts:
        return False

    path_posix = path.as_posix()
    for root in governed_roots:
        root_posix = root.as_posix()
        if path_posix == root_posix or path_posix.startswith(root_posix + "/"):
            return True
    return False


def _collect_required_owner_files(
    repo_root: Path,
    changed_paths: list[Path],
    *,
    owner_filename: str,
    governed_roots: tuple[Path, ...],
    suffixes: tuple[str, ...],
    debug: bool = False,
) -> tuple[set[str], list[str]]:
    required_owner_files: set[str] = set()
    ownerless_files: list[str] = []

    for rel_path in changed_paths:
        if rel_path.name == owner_filename:
            continue

        nearest = _nearest_owner_file(repo_root, rel_path, owner_filename)
        if nearest is None:
            if _is_governed_file(rel_path, governed_roots, suffixes):
                ownerless_files.append(rel_path.as_posix())
            continue

        required_owner_files.add(nearest.as_posix())

        if debug:
            print(
                f"[check_ai_docs] {rel_path.as_posix()} -> nearest owner file: "
                f"{nearest.as_posix()}"
            )

    return required_owner_files, sorted(ownerless_files)


def _git_show_text(repo_root: Path, rev: str, rel_path: str) -> str | None:
    result = subprocess.run(
        ["git", "show", f"{rev}:{rel_path}"],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return result.stdout


def _normalize_last_verified_block(text: str) -> str:
    """
    Normalize away the Last Verified section so we can detect metadata-only edits.

    This is the key difference between:
    - "the owner file was reviewed and meaningfully changed"
    - "the owner file was touched only because CI rewrote the verification stamp"
    """
    lines = text.splitlines()
    normalized: list[str] = []
    in_last_verified = False

    for line in lines:
        if line == LAST_VERIFIED_HEADING:
            normalized.append(line)
            normalized.append("<normalized-last-verified>")
            in_last_verified = True
            continue

        if in_last_verified and line.startswith(SECTION_HEADING_PREFIX):
            in_last_verified = False

        if not in_last_verified:
            normalized.append(line)

    normalized_text = "\n".join(normalized).strip()
    return normalized_text + "\n"


def _has_meaningful_owner_change(
    repo_root: Path,
    *,
    base_rev: str,
    head_rev: str,
    rel_path: str,
) -> bool:
    old_text = _git_show_text(repo_root, base_rev, rel_path)
    new_text = _git_show_text(repo_root, head_rev, rel_path)

    if old_text is None or new_text is None:
        return True

    return _normalize_last_verified_block(old_text) != _normalize_last_verified_block(
        new_text
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check owner-file freshness using nearest-ancestor ownership."
    )
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--base", default=None)
    parser.add_argument("--head", default=None)
    parser.add_argument("--owner-file", default=DEFAULT_OWNER_FILENAME)
    parser.add_argument(
        "--governed-root",
        action="append",
        default=[],
        help="Repeat for each governed code root, e.g. apps/example_app/src",
    )
    parser.add_argument(
        "--suffix",
        action="append",
        default=[".py"],
        help="File suffixes considered governed code. May be repeated.",
    )
    parser.add_argument(
        "--fallback-base-ref",
        action="append",
        default=[],
        help="Optional fallback refs used when --base is missing or invalid.",
    )
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    fallback_base_refs = tuple(args.fallback_base_ref) or DEFAULT_FALLBACK_BASE_REFS

    if not args.governed_root:
        print(
            "[check_ai_docs] FAIL: at least one --governed-root is required. "
            "This script is intentionally explicit about the code it governs."
        )
        return 1

    governed_roots = tuple(Path(root) for root in args.governed_root)
    suffixes = tuple(args.suffix)

    changed = _changed_files(
        repo_root,
        base=args.base,
        head=args.head,
        fallback_base_refs=fallback_base_refs,
    )
    if not changed:
        print("[check_ai_docs] No changes detected; nothing to check.")
        return 0

    diff_endpoints = _resolve_diff_endpoints(
        repo_root,
        args.base,
        args.head,
        fallback_base_refs,
    )
    changed_rel = {Path(p).as_posix() for p in changed}
    changed_paths = [Path(p) for p in changed]

    required_owner_files, ownerless_files = _collect_required_owner_files(
        repo_root,
        changed_paths,
        owner_filename=args.owner_file,
        governed_roots=governed_roots,
        suffixes=suffixes,
        debug=args.debug,
    )

    missing_updates = sorted(
        owner_file
        for owner_file in required_owner_files
        if owner_file not in changed_rel
    )

    metadata_only_updates: list[str] = []
    if diff_endpoints is not None:
        diff_base, diff_head = diff_endpoints
        for owner_file in sorted(required_owner_files):
            if owner_file not in changed_rel:
                continue
            if not _has_meaningful_owner_change(
                repo_root,
                base_rev=diff_base,
                head_rev=diff_head,
                rel_path=owner_file,
            ):
                metadata_only_updates.append(owner_file)

    has_failures = False

    if ownerless_files:
        has_failures = True
        print("[check_ai_docs] FAIL: governed files do not have a nearest owner file:")
        for path in ownerless_files:
            print(f"  - {path}")

    if missing_updates:
        has_failures = True
        print("[check_ai_docs] FAIL: nearest owner files were not updated:")
        for path in missing_updates:
            print(f"  - {path}")

    if metadata_only_updates:
        has_failures = True
        print(
            "[check_ai_docs] FAIL: owner files were updated only in Last Verified (CI):"
        )
        for path in metadata_only_updates:
            print(f"  - {path}")

    if has_failures:
        return 1

    print("[check_ai_docs] OK: owner-file freshness checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
