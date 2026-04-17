"""
Small AST-based import-boundary checker for Python projects.

Why this exists:
- architecture docs often say "layer X must not import layer Y"
- those rules are easy to violate accidentally in Python
- a tiny static checker catches many of these mistakes without needing a full linter plugin

This example reads its rules from a TOML file so that the script itself can stay
generic while the repository defines project-specific module boundaries.
"""

import argparse
import ast
import tomllib
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BoundaryRule:
    target_prefix: str
    forbidden_prefixes: tuple[str, ...]


@dataclass(frozen=True)
class BoundaryConfig:
    source_root: Path
    rules: tuple[BoundaryRule, ...]


def _matches_prefix(module_name: str, prefix: str) -> bool:
    return module_name == prefix or module_name.startswith(prefix + ".")


def _module_name_for_file(source_root: Path, path: Path) -> str:
    rel = path.relative_to(source_root).with_suffix("")
    parts = list(rel.parts)
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _package_name_for_file(source_root: Path, path: Path) -> str:
    rel = path.relative_to(source_root).with_suffix("")
    parts = list(rel.parts[:-1])
    return ".".join(parts)


def _resolve_import_from_base(
    source_root: Path, path: Path, node: ast.ImportFrom
) -> str | None:
    if node.level == 0:
        return node.module

    package_name = _package_name_for_file(source_root, path)
    package_parts = package_name.split(".") if package_name else []
    trim = node.level - 1

    if trim > len(package_parts):
        return None

    anchor_parts = package_parts[: len(package_parts) - trim]
    if node.module:
        return ".".join(anchor_parts + node.module.split("."))
    return ".".join(anchor_parts)


def _iter_import_from_targets(
    source_root: Path, path: Path, node: ast.ImportFrom
) -> list[str]:
    base = _resolve_import_from_base(source_root, path, node)
    if not base:
        return []

    targets: list[str] = []
    for alias in node.names:
        targets.append(base if alias.name == "*" else f"{base}.{alias.name}")
    return targets


def _iter_imports(source_root: Path, path: Path) -> list[tuple[int, str]]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    imports: list[tuple[int, str]] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append((node.lineno, alias.name))
        elif isinstance(node, ast.ImportFrom):
            for target in _iter_import_from_targets(source_root, path, node):
                imports.append((node.lineno, target))

    return imports


def _iter_python_files(source_root: Path) -> list[Path]:
    return sorted(
        path for path in source_root.rglob("*.py") if "__pycache__" not in path.parts
    )


def _load_config(repo_root: Path, config_path: Path) -> BoundaryConfig:
    config_abs = (
        (repo_root / config_path).resolve()
        if not config_path.is_absolute()
        else config_path
    )
    data = tomllib.loads(config_abs.read_text(encoding="utf-8"))

    source_root_raw = data.get("source_root")
    if not source_root_raw:
        raise RuntimeError(f"{config_abs}: missing required 'source_root' setting")

    rules_raw = data.get("rule", [])
    if not rules_raw:
        raise RuntimeError(f"{config_abs}: at least one [[rule]] entry is required")

    rules: list[BoundaryRule] = []
    for idx, rule_data in enumerate(rules_raw, start=1):
        target_prefix = rule_data.get("target_prefix")
        forbidden_prefixes = tuple(rule_data.get("forbidden_prefixes", []))
        if not target_prefix or not forbidden_prefixes:
            raise RuntimeError(
                f"{config_abs}: rule #{idx} must define 'target_prefix' and "
                "'forbidden_prefixes'"
            )
        rules.append(
            BoundaryRule(
                target_prefix=target_prefix,
                forbidden_prefixes=forbidden_prefixes,
            )
        )

    source_root = (repo_root / source_root_raw).resolve()
    return BoundaryConfig(source_root=source_root, rules=tuple(rules))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check configured Python import-boundary rules."
    )
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--config",
        required=True,
        help="Path to a TOML file defining source_root and [[rule]] entries.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    config = _load_config(repo_root, Path(args.config))

    violations: list[str] = []

    for path in _iter_python_files(config.source_root):
        module_name = _module_name_for_file(config.source_root, path)
        imports = _iter_imports(config.source_root, path)

        for rule in config.rules:
            if not _matches_prefix(module_name, rule.target_prefix):
                continue

            for lineno, imported in imports:
                for forbidden in rule.forbidden_prefixes:
                    if _matches_prefix(imported, forbidden):
                        rel_path = path.relative_to(repo_root).as_posix()
                        violations.append(
                            f"{rel_path}:{lineno}: {module_name} must not import "
                            f"{imported} (forbidden by rule for {rule.target_prefix})"
                        )

    if violations:
        print("[check_import_boundaries] FAIL:")
        for violation in violations:
            print(f"  - {violation}")
        return 1

    print("[check_import_boundaries] All configured import-boundary checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
