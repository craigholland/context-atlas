"""Materialize the Context Atlas Codex runtime surface from authoritative docs."""

from __future__ import annotations

import argparse
import difflib
import re
import sys
import textwrap
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

_MANIFEST_PATH = Path(
    "docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml"
)
_CAPACITY_PATH = Path(
    "docs/Authoritative/Identity/AgenticDevelopment/runtime_capacity.yaml"
)
_CODEX_BINDING_ROOT = Path(
    "docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex"
)
_ROLE_MODEL_PATH = Path(
    "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Model.md"
)
_ROLE_ACCOUNTABILITY_PATH = Path(
    "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Accountability-Matrix.md"
)
_ROLE_AUTHORITY_PATH = Path(
    "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Authority-Matrix.md"
)
_MODE_MODEL_PATH = Path(
    "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Modes/Mode-Model.md"
)
_MODE_TRANSITIONS_PATH = Path(
    "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Modes/Mode-Transition-Rules.md"
)
_MODE_MUTATION_PATH = Path(
    "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Modes/Mode-Mutation-Matrix.md"
)
_PROTOCOL_ROLE_BINDINGS_PATH = Path(
    "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md"
)
_PROTOCOL_MODE_BINDINGS_PATH = Path(
    "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Mode-Bindings.md"
)
_GATE_REVIEW_PASS_PATH = Path(
    "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Gate-Review-Pass-Matrix.md"
)
_PROJECT_PROFILE_PATH = Path(
    "docs/Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md"
)
_MATERIALIZATION_TASK_PATH = Path(
    "docs/Planning/task_codex_runtime_materialization_enforcement.md"
)

_SUPPORTED_SURFACES = {
    "orientation",
    "config",
    "roles",
    "agents",
    "modes",
    "protocols",
    "skills",
}
_SUPPORTED_MAINTENANCE_MODES = {"generated", "human", "mixed"}
_DOC_TEXT_CACHE: dict[tuple[Path, int, int], str] = {}
SUPPORTED_SURFACES = frozenset(_SUPPORTED_SURFACES)

_ROLE_PURPOSE_OVERRIDES: dict[str, str] = {
    "planner-decomp": (
        "Materialize the Context Atlas `Planner/Decomp` role as a Codex-facing "
        "accountability surface for decomposition quality, sequencing "
        "coherence, and planning-layer integrity across Epics, Stories, "
        "Tasks, and PR slices."
    ),
    "backend": (
        "Materialize the Context Atlas `Backend` role as the accountable "
        "surface for engine, domain, service, adapter, infrastructure, "
        "rendering, and backend test work that defines how Context Atlas "
        "behaves as a system."
    ),
    "documentation-uat": (
        "Materialize the Context Atlas `Documentation/UAT` role as the "
        "accountable surface for user-facing guides, runnable examples, "
        "evaluator workflows, and documentation/UAT-owned rework."
    ),
    "qa": (
        "Materialize the Context Atlas `QA` role as the accountable surface "
        "for governed review, findings quality, acceptance analysis, and "
        "structured rework feedback."
    ),
    "devops": (
        "Materialize the Context Atlas `DevOps` role as the accountable "
        "surface for merge, release, workflow, versioning, and other "
        "operational-delivery actions that should remain distinct from "
        "ordinary implementation."
    ),
}

_PARENT_AGENT_SUMMARIES: dict[str, str] = {
    "parent-planner-decomp": (
        "Materialized parent agent for Context Atlas planning ownership, "
        "decomposition quality, and planning-artifact rework."
    ),
    "parent-backend": (
        "Materialized parent agent for Context Atlas backend implementation, "
        "bounded backend decomposition, and backend-owned rework."
    ),
    "parent-documentation-uat": (
        "Materialized parent agent for Context Atlas user-facing guides, "
        "examples, evaluator workflows, and documentation/UAT rework."
    ),
    "parent-qa": (
        "Materialized parent agent for Context Atlas governed review, "
        "findings analysis, review-pass execution, and readiness framing."
    ),
    "parent-devops": (
        "Materialized parent agent for Context Atlas operational delivery, "
        "repository workflow handling, and delivery-facing recovery."
    ),
}

_PARENT_AUTHORITY_SCOPES: dict[str, str] = {
    "parent-planner-decomp": (
        "Owns planning, decomposition, sequencing, and planning-artifact "
        "rework; may delegate bounded planning analysis but retains "
        "accountability."
    ),
    "parent-backend": (
        "Owns backend implementation and backend rework, may decompose an "
        "already-assigned task into PR-sized slices, and may emit structured "
        "completion handoffs without self-accepting or merging."
    ),
    "parent-documentation-uat": (
        "Owns documentation, example, and evaluator-facing implementation "
        "slices and their returned rework, then emits structured completion "
        "handoffs for downstream review."
    ),
    "parent-qa": (
        "Owns governed review, requested review-pass execution, findings "
        "publication, and readiness framing, but does not merge, release, or "
        "silently absorb implementation ownership."
    ),
    "parent-devops": (
        "Owns merge, release, workflow, versioning, and delivery-facing "
        "operational actions, consuming explicit upstream review and handoff "
        "state before acting."
    ),
}

_PARENT_NOTES: dict[str, dict[str, list[str]]] = {
    "parent-planner-decomp": {
        "constraints": [
            (
                "Publishes planning-facing GitHub work through the planner "
                "principal when GitHub is the active repo surface."
            ),
            (
                "Does not gain backend, QA, or release authority merely "
                "because planning touches those surfaces."
            ),
        ],
        "non_goals": [
            "Own ordinary backend implementation.",
            "Self-approve merge or release actions.",
        ],
    },
    "parent-backend": {
        "constraints": [
            (
                "Publishes backend GitHub work through the backend principal "
                "when GitHub is the active repo surface."
            ),
            "May not dismiss blocking QA findings or bypass DevOps merge authority.",
        ],
        "non_goals": [
            "Assume final QA acceptance.",
            "Mutate workflow or release surfaces as ordinary backend work.",
        ],
    },
    "parent-documentation-uat": {
        "constraints": [
            (
                "Publishes documentation and evaluator-facing GitHub work "
                "through the documentation/UAT principal when GitHub is active."
            ),
            (
                "Uses the PR surface as a handoff and response channel but "
                "does not gain merge authority from it."
            ),
        ],
        "non_goals": [
            "Self-accept user-facing work as final QA readiness.",
            "Absorb backend or release ownership by default.",
        ],
    },
    "parent-qa": {
        "constraints": [
            (
                "Publishes GitHub review findings through the QA principal "
                "when GitHub is the active review surface."
            ),
            (
                "Executes the gate-bound review-pass map: code at Task -> "
                "Story, architecture and security at Story -> Epic, product "
                "at Epic -> development."
            ),
        ],
        "non_goals": [
            "Approve merges or releases.",
            "Rewrite primary product surfaces as a substitute for returning findings.",
        ],
    },
    "parent-devops": {
        "constraints": [
            (
                "Uses branch-target-scoped merge principals rather than one "
                "global merge identity."
            ),
            (
                "Consumes explicit upstream review and readiness state instead "
                "of bypassing planning, implementation, or QA gates."
            ),
        ],
        "non_goals": [
            "Act as a generic implementation role.",
            "Treat workflow ownership as authority over all repository content.",
        ],
    },
}

_SPECIALIST_SUMMARIES: dict[str, str] = {
    "specialist-planning-change": (
        "Bounded delegated specialist for planning analysis, decomposition "
        "refinement, recomposition notes, and change-framing support."
    ),
    "specialist-python-implementation": (
        "Bounded delegated specialist for Python implementation, debugging, "
        "test-facing evidence, and focused backend remediation."
    ),
    "specialist-review-readiness": (
        "Bounded delegated specialist for evidence review, findings analysis, "
        "technical readiness framing, and PR-surface review support."
    ),
    "specialist-delivery-recovery": (
        "Bounded delegated specialist for repository workflow handling, "
        "pipeline interpretation, readiness support, and delivery-facing "
        "recovery triage."
    ),
}

_SPECIALIST_AUTHORITY_SCOPES: dict[str, str] = {
    "specialist-planning-change": (
        "Participates under parent-owned planning accountability; returns "
        "structured planning outputs and change framing without becoming the "
        "top-level workflow owner."
    ),
    "specialist-python-implementation": (
        "Participates under Backend-owned accountability for bounded Python "
        "execution, debugging, testing, and remediation; does not gain "
        "independent review, merge, or release authority."
    ),
    "specialist-review-readiness": (
        "Participates under QA-owned accountability for delegated review, "
        "findings framing, and readiness analysis; returns explicit findings "
        "or readiness judgments instead of vague impressions."
    ),
    "specialist-delivery-recovery": (
        "Participates under DevOps-owned accountability for bounded delivery "
        "preparation, pipeline handling, and recovery triage; keeps "
        "operational actions traceable and bounded."
    ),
}

_SPECIALIST_NOTES: dict[str, dict[str, list[str]]] = {
    "specialist-planning-change": {
        "constraints": [
            "Returns explicit planning outputs to the invoking parent agent.",
            "Does not replace architecture, release, or top-level planning authority.",
        ],
        "non_goals": [
            "Become a shadow role roster.",
            "Own cross-role approval decisions.",
        ],
    },
    "specialist-python-implementation": {
        "constraints": [
            "Should stay bounded to explicit delegated Python surfaces.",
            (
                "May collaborate with QA-style actors through findings and "
                "rework loops without absorbing QA ownership."
            ),
        ],
        "non_goals": [
            "Own broad architecture decisions by itself.",
            "Act as an unbounded product owner.",
        ],
    },
    "specialist-review-readiness": {
        "constraints": [
            (
                "Keeps findings and readiness judgments explicit, actionable, "
                "and review-surface aware."
            ),
            "Does not become the primary implementation owner or release authority.",
        ],
        "non_goals": [
            "Merge or release work.",
            "Rewrite product implementation as a substitute for review findings.",
        ],
    },
    "specialist-delivery-recovery": {
        "constraints": [
            "Keeps operational actions traceable and tied to explicit gate state.",
            (
                "Collaborates with QA and implementation actors when readiness "
                "or recovery depends on their evidence."
            ),
        ],
        "non_goals": [
            "Automatically become release authority.",
            "Absorb application-level implementation ownership.",
        ],
    },
}

_MODE_PURPOSE_OVERRIDES: dict[str, str] = {
    "planning": (
        "Materialize the Context Atlas `planning` mode as the Codex-facing "
        "execution state for decomposition, sequencing, and planning-shape "
        "clarification."
    ),
    "implementation": (
        "Materialize the Context Atlas `implementation` mode as the "
        "Codex-facing execution state for role-owned deliverable creation and "
        "bounded first-pass work on owned surfaces."
    ),
    "review": (
        "Materialize the Context Atlas `review` mode as the Codex-facing "
        "execution state for governed assessment, findings production, and "
        "acceptance analysis."
    ),
    "rework": (
        "Materialize the Context Atlas `rework` mode as the Codex-facing "
        "execution state for returned work that is being corrected or clarified "
        "under an explicit review or recovery outcome."
    ),
    "recovery": (
        "Materialize the Context Atlas `recovery` mode as the Codex-facing "
        "execution state for restoring a safe workflow path when ownership, "
        "contracts, or state are broken or ambiguous."
    ),
    "operational-delivery": (
        "Materialize the Context Atlas `operational_delivery` mode as the "
        "Codex-facing execution state for merge, release, workflow, versioning, "
        "and similar delivery-oriented operational actions."
    ),
}

_SKILL_ATTACHMENT_LABEL_OVERRIDES: dict[tuple[str, str], str] = {
    (
        "planning-decomposition",
        "parent-backend",
    ): ("`parent-backend` when breaking an already-assigned task into PR-sized slices"),
}


@dataclass(frozen=True)
class MaterializedSurface:
    """One materialized runtime surface and its overwrite policy."""

    relative_path: Path
    concept_family: str
    maintenance_mode: str
    content: str | None


@dataclass(frozen=True)
class MaterializationPlan:
    """All generated and declared-human surfaces for the current run."""

    generated: tuple[MaterializedSurface, ...]
    human_managed: tuple[MaterializedSurface, ...]


@dataclass(frozen=True)
class _RuntimeLayout:
    """Materialized runtime roots derived from the manifest."""

    runtime_root: Path
    skills_root: Path
    orientation_surface: Path
    config_surface: Path

    @property
    def roles_root(self) -> Path:
        return self.runtime_root / "roles"

    @property
    def agents_root(self) -> Path:
        return self.runtime_root / "agents"

    @property
    def modes_root(self) -> Path:
        return self.runtime_root / "modes"

    @property
    def protocols_root(self) -> Path:
        return self.runtime_root / "protocols"

    def role_path(self, role_id: str) -> Path:
        return self.roles_root / f"{role_id}.md"

    def agent_path(self, agent_id: str) -> Path:
        return self.agents_root / f"{agent_id}.toml"

    def mode_path(self, mode_id: str) -> Path:
        return self.modes_root / f"{mode_id}.md"

    def protocol_path(self, protocol_id: str) -> Path:
        return self.protocols_root / f"{protocol_id}.md"

    def skill_path(self, skill_id: str) -> Path:
        return self.skills_root / f"context-atlas-{skill_id}" / "SKILL.md"


@dataclass(frozen=True)
class _YamlLine:
    indent: int
    text: str


def _read_text(repo_root: Path, relative_path: Path) -> str:
    absolute_path = (repo_root / relative_path).resolve()
    stat_result = absolute_path.stat()
    cache_key = (absolute_path, stat_result.st_mtime_ns, stat_result.st_size)
    cached = _DOC_TEXT_CACHE.get(cache_key)
    if cached is not None:
        return cached

    text = absolute_path.read_text(encoding="utf-8")
    _DOC_TEXT_CACHE[cache_key] = text
    return text


def _strip_inline_comment(line: str) -> str:
    result: list[str] = []
    in_single = False
    in_double = False

    for character in line:
        if character == "'" and not in_double:
            in_single = not in_single
        elif character == '"' and not in_single:
            in_double = not in_double
        elif character == "#" and not in_single and not in_double:
            break
        result.append(character)

    return "".join(result).rstrip()


def _parse_yaml_scalar(text: str) -> object:
    if text == "[]":
        return []
    if text == "{}":
        return {}
    if text == "true":
        return True
    if text == "false":
        return False
    if re.fullmatch(r"-?\d+", text):
        return int(text)
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {'"', "'"}:
        return text[1:-1]
    return text


def _looks_like_mapping_entry(text: str) -> bool:
    return bool(re.match(r"^[A-Za-z0-9_.\-/]+:\s*.*$", text))


def _split_mapping_entry(text: str) -> tuple[str, str]:
    key, remainder = text.split(":", 1)
    return key.strip(), remainder.strip()


def _parse_yaml_tokens(
    tokens: list[_YamlLine], start_index: int, indent: int
) -> tuple[object, int]:
    if start_index >= len(tokens):
        return {}, start_index
    if tokens[start_index].text.startswith("- "):
        return _parse_yaml_list(tokens, start_index, indent)
    return _parse_yaml_mapping(tokens, start_index, indent)


def _parse_yaml_mapping(
    tokens: list[_YamlLine], start_index: int, indent: int
) -> tuple[dict[str, object], int]:
    mapping: dict[str, object] = {}
    index = start_index

    while index < len(tokens):
        token = tokens[index]
        if token.indent < indent:
            break
        if token.indent != indent or token.text.startswith("- "):
            break

        key, remainder = _split_mapping_entry(token.text)
        index += 1

        if remainder:
            mapping[key] = _parse_yaml_scalar(remainder)
            continue

        if index < len(tokens) and tokens[index].indent > token.indent:
            nested, index = _parse_yaml_tokens(tokens, index, token.indent + 2)
            mapping[key] = nested
            continue

        mapping[key] = {}

    return mapping, index


def _parse_yaml_inline_mapping_item(
    tokens: list[_YamlLine], item_text: str, start_index: int, indent: int
) -> tuple[dict[str, object], int]:
    key, remainder = _split_mapping_entry(item_text)
    mapping: dict[str, object] = {}
    index = start_index

    if remainder:
        mapping[key] = _parse_yaml_scalar(remainder)
    elif index < len(tokens) and tokens[index].indent > indent:
        nested, index = _parse_yaml_tokens(tokens, index, indent + 2)
        mapping[key] = nested
    else:
        mapping[key] = {}

    while index < len(tokens):
        token = tokens[index]
        if token.indent < indent + 2:
            break
        if token.indent == indent and token.text.startswith("- "):
            break
        if token.indent != indent + 2 or token.text.startswith("- "):
            break

        key, remainder = _split_mapping_entry(token.text)
        index += 1

        if remainder:
            mapping[key] = _parse_yaml_scalar(remainder)
            continue

        if index < len(tokens) and tokens[index].indent > token.indent:
            nested, index = _parse_yaml_tokens(tokens, index, token.indent + 2)
            mapping[key] = nested
        else:
            mapping[key] = {}

    return mapping, index


def _parse_yaml_list(
    tokens: list[_YamlLine], start_index: int, indent: int
) -> tuple[list[object], int]:
    values: list[object] = []
    index = start_index

    while index < len(tokens):
        token = tokens[index]
        if token.indent < indent:
            break
        if token.indent != indent or not token.text.startswith("- "):
            break

        item_text = token.text[2:].strip()
        index += 1

        if not item_text:
            nested, index = _parse_yaml_tokens(tokens, index, indent + 2)
            values.append(nested)
            continue

        if _looks_like_mapping_entry(item_text):
            item, index = _parse_yaml_inline_mapping_item(
                tokens, item_text, index, indent
            )
            values.append(item)
            continue

        values.append(_parse_yaml_scalar(item_text))

    return values, index


def _load_simple_yaml(repo_root: Path, relative_path: Path) -> dict[str, object]:
    text = _read_text(repo_root, relative_path)
    tokens: list[_YamlLine] = []

    for raw_line in text.splitlines():
        line = _strip_inline_comment(raw_line)
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        tokens.append(_YamlLine(indent=indent, text=line.strip()))

    parsed, _ = _parse_yaml_tokens(tokens, 0, 0)
    if not isinstance(parsed, dict):
        raise ValueError(
            f"{relative_path.as_posix()} did not parse into a mapping as expected"
        )
    return parsed


def _strip_front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return text

    marker = "\n---\n"
    end_index = text.find(marker, 4)
    if end_index == -1:
        return text
    return text[end_index + len(marker) :]


def _normalize_label(value: str) -> str:
    normalized = value.replace("`", "")
    normalized = re.sub(r"^\d+\.\s*", "", normalized)
    normalized = normalized.replace("/", " ")
    normalized = normalized.replace("_", " ")
    normalized = normalized.replace("-", " ")
    normalized = re.sub(r"[^a-z0-9 ]+", " ", normalized.lower())
    return re.sub(r"\s+", " ", normalized).strip()


def _heading_blocks(text: str, level: int) -> list[tuple[str, str]]:
    body = _strip_front_matter(text)
    pattern = re.compile(rf"^{re.escape('#' * level)}\s+(.+?)\s*$", re.MULTILINE)
    matches = list(pattern.finditer(body))
    blocks: list[tuple[str, str]] = []

    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        blocks.append((match.group(1).strip(), body[start:end].strip()))

    return blocks


def _find_heading_block(text: str, level: int, label: str) -> str:
    target = _normalize_label(label)
    for heading, block in _heading_blocks(text, level):
        if _normalize_label(heading) == target:
            return block
    raise KeyError(f"Unable to find heading '{label}' at level {level}")


def _section_text(text: str, heading: str) -> str:
    return _find_heading_block(text, 2, heading)


def _first_paragraph(text: str) -> str:
    for paragraph in re.split(r"\n\s*\n", text.strip()):
        cleaned = " ".join(line.strip() for line in paragraph.splitlines())
        if cleaned:
            return cleaned
    return ""


def _bullet_lines(text: str) -> list[str]:
    bullets: list[str] = []
    current: str | None = None

    for line in text.splitlines():
        bullet_match = re.match(r"^\s*-\s+(.*)$", line)
        if bullet_match:
            if current is not None:
                bullets.append(current.strip())
            current = bullet_match.group(1).strip()
            continue

        if current is not None and not line.strip():
            bullets.append(current.strip())
            current = None
            continue

        if current is not None and line.strip() and not re.match(r"^\s*#+\s", line):
            current = f"{current} {line.strip()}"
            continue

    if current is not None:
        bullets.append(current.strip())

    return bullets


def _numbered_markdown(items: list[str]) -> list[str]:
    lines: list[str] = []
    for index, item in enumerate(items, start=1):
        lines.append(f"{index}. {item}")
    return lines


def _title_from_body(text: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", _strip_front_matter(text), re.MULTILINE)
    if not match:
        raise ValueError("Markdown document is missing a level-1 title")
    return match.group(1).strip()


def _wrap(text: str, *, width: int = 78, indent: str = "", subsequent: str = "") -> str:
    return textwrap.fill(
        " ".join(text.split()),
        width=width,
        initial_indent=indent,
        subsequent_indent=subsequent or indent,
        break_long_words=False,
        break_on_hyphens=False,
    )


def _markdown_bullets(items: list[str], *, indent: str = "") -> list[str]:
    lines: list[str] = []
    for item in items:
        lines.append(_wrap(item, indent=f"{indent}- ", subsequent=f"{indent}  "))
    return lines


def _markdown_subsection(title: str, lines: list[str]) -> list[str]:
    section = [f"## {title}", ""]
    section.extend(lines)
    return section


def _markdown_notice_lines() -> list[str]:
    return [
        "> Generated surface notice",
        "> This file is generated or regenerated from the authoritative Canon and Identity docs.",
        (
            "> Local edits may be overwritten by later regeneration. Durable "
            "semantic changes belong upstream in `docs/Authoritative/Canon/` "
            "or `docs/Authoritative/Identity/`."
        ),
    ]


def _format_markdown(lines: list[str]) -> str:
    return "\n".join(lines).rstrip() + "\n"


def _toml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _toml_string(value: str) -> str:
    return f'"{_toml_escape(value)}"'


def _toml_array(values: list[str]) -> str:
    if not values:
        return "[]"
    return "[" + ", ".join(_toml_string(value) for value in values) + "]"


def _toml_multiline_array(values: list[str]) -> list[str]:
    if not values:
        return ["[]"]
    lines = ["["]
    for value in values:
        lines.append(f"  {_toml_string(value)},")
    lines.append("]")
    return lines


def _quoted_paths(paths: list[str]) -> list[str]:
    return [f"`{path}`" for path in paths]


def _write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def _compare_expected(path: Path, expected: str) -> list[str]:
    if not path.exists():
        return [
            f"[materialize_codex_runtime] Missing generated surface: {path.as_posix()}"
        ]
    current = path.read_text(encoding="utf-8")
    if current == expected:
        return []
    diff = "".join(
        difflib.unified_diff(
            current.splitlines(keepends=True),
            expected.splitlines(keepends=True),
            fromfile=path.as_posix(),
            tofile=f"{path.as_posix()} (expected)",
        )
    ).rstrip()
    return [
        f"[materialize_codex_runtime] Drift detected for {path.as_posix()}:\n{diff}"
    ]


def _require_mapping(value: object, context: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise TypeError(f"{context} must be a mapping")
    return value


def _require_list(value: object, context: str) -> list[object]:
    if not isinstance(value, list):
        raise TypeError(f"{context} must be a list")
    return value


def _require_string(value: object, context: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{context} must be a string")
    return value


def _mode_title(mode_id: str) -> str:
    return mode_id.replace("-", " ").title()


def _protocol_doc_path(protocol_source_name: str) -> Path:
    slug = protocol_source_name.replace("_", "-")
    title = "-".join(part.title() for part in slug.split("-"))
    return Path(
        f"docs/Authoritative/Canon/AgenticDevelopment/Protocols/{title}-Protocol.md"
    )


def _role_accountability_data(
    repo_root: Path, role_display_name: str
) -> dict[str, object]:
    block = _find_heading_block(
        _read_text(repo_root, _ROLE_ACCOUNTABILITY_PATH), 3, role_display_name
    )
    return {
        "primary_accountability": _first_paragraph(
            _find_heading_block(block, 4, "Primary Accountability")
        ),
        "direct_artifact_ownership": _bullet_lines(
            _find_heading_block(block, 4, "Direct Artifact Ownership")
        ),
        "direct_decision_ownership": _bullet_lines(
            _find_heading_block(block, 4, "Direct Decision Ownership")
        ),
    }


def _role_authority_data(repo_root: Path, role_display_name: str) -> dict[str, object]:
    block = _find_heading_block(
        _read_text(repo_root, _ROLE_AUTHORITY_PATH), 3, role_display_name
    )
    return {
        "may": _bullet_lines(_find_heading_block(block, 4, "May")),
        "may_not": _bullet_lines(_find_heading_block(block, 4, "May Not")),
    }


def _mode_transition_data(repo_root: Path, mode_title: str) -> dict[str, object]:
    block = _find_heading_block(
        _read_text(repo_root, _MODE_TRANSITIONS_PATH), 3, mode_title
    )
    return {
        "enter": _bullet_lines(_find_heading_block(block, 4, "Enter")),
        "exit": _bullet_lines(_find_heading_block(block, 4, "Exit")),
    }


def _mode_mutation_row(repo_root: Path, mode_id: str) -> dict[str, str]:
    text = _strip_front_matter(_read_text(repo_root, _MODE_MUTATION_PATH))
    pattern = re.compile(
        rf"^\|\s*`{re.escape(mode_id.replace('-', '_'))}`\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$",
        re.MULTILINE,
    )
    match = pattern.search(text)
    if match is None:
        pattern = re.compile(
            rf"^\|\s*`{re.escape(mode_id)}`\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$",
            re.MULTILINE,
        )
        match = pattern.search(text)
    if match is None:
        raise KeyError(f"Unable to find mutation row for mode '{mode_id}'")
    return {
        "allowed": match.group(1).strip(),
        "not_allowed": match.group(2).strip(),
    }


def _protocol_primary_mode_map(repo_root: Path) -> dict[str, str]:
    text = _strip_front_matter(_read_text(repo_root, _PROTOCOL_MODE_BINDINGS_PATH))
    mapping: dict[str, str] = {}
    for heading, block in _heading_blocks(text, 3):
        normalized = _normalize_label(heading)
        mode_match = re.search(r"`([^`]+)`", block)
        if mode_match is None:
            continue
        mode_id = mode_match.group(1).replace("_", "-")
        if "planning protocol" in normalized:
            mapping["planning"] = mode_id
        elif "execution slice protocol" in normalized:
            mapping["execution-slice"] = mode_id
        elif "review protocol" in normalized:
            mapping["review"] = mode_id
        elif "rework protocol" in normalized:
            mapping["rework"] = mode_id
        elif "recovery protocol" in normalized:
            mapping["recovery"] = mode_id
    return mapping


def _protocol_doc_sections(repo_root: Path, source_name: str) -> dict[str, object]:
    text = _read_text(repo_root, _protocol_doc_path(source_name))
    return {
        "purpose": _first_paragraph(_section_text(text, "Purpose")),
        "trigger": _bullet_lines(_section_text(text, "Trigger / Entry Conditions")),
        "required_inputs": _bullet_lines(_section_text(text, "Required Inputs")),
        "required_outputs": _bullet_lines(_section_text(text, "Required Outputs")),
        "exit_criteria": _bullet_lines(_section_text(text, "Exit Criteria")),
        "review_outcomes": _bullet_lines(_section_text(text, "Review Outcome States"))
        if source_name == "review"
        else [],
    }


def _skill_doc_sections(repo_root: Path, canon_ref: Path) -> dict[str, object]:
    text = _read_text(repo_root, canon_ref)
    return {
        "title": _title_from_body(text),
        "purpose": _first_paragraph(_section_text(text, "Purpose")),
        "execution_pattern": _bullet_lines(_section_text(text, "Execution Pattern")),
        "expected_outputs": _bullet_lines(_section_text(text, "Expected Outputs")),
        "escalation": _bullet_lines(_section_text(text, "Escalation Conditions")),
        "guardrails": _bullet_lines(_section_text(text, "Guardrails")),
    }


def _specialist_doc_sections(repo_root: Path, canon_ref: Path) -> dict[str, object]:
    text = _read_text(repo_root, canon_ref)
    return {
        "title": _title_from_body(text),
        "purpose": _first_paragraph(_section_text(text, "Purpose")),
        "boundaries": _bullet_lines(_section_text(text, "Common Boundaries")),
        "collaboration": _bullet_lines(
            _section_text(text, "Common Collaboration Pattern")
        ),
    }


def _role_sources(role_id: str) -> list[str]:
    sources = [
        "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Model.md",
        "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Accountability-Matrix.md",
        "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Authority-Matrix.md",
        "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Agent-Binding-Model.md",
        "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Mode-Matrix.md",
        "docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml",
    ]
    if role_id in {"planner-decomp", "backend", "documentation-uat", "qa", "devops"}:
        sources.insert(
            5,
            "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md",
        )
    return sources


def _mode_sources() -> list[str]:
    return [
        "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Modes/Mode-Model.md",
        "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Modes/Mode-Transition-Rules.md",
        "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Modes/Mode-Mutation-Matrix.md",
        "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Mode-Matrix.md",
        "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Mode-Bindings.md",
    ]


def _protocol_sources(protocol: dict[str, object]) -> list[str]:
    source_name = _require_string(protocol["source_name"], "protocol source_name")
    sources = [
        _protocol_doc_path(source_name).as_posix(),
        "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md",
        "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Mode-Bindings.md",
    ]
    if source_name == "review":
        sources.append(
            "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Gate-Review-Pass-Matrix.md"
        )
    return sources


def _role_display_map(manifest: dict[str, object]) -> dict[str, str]:
    return {
        _require_string(role["id"], "role id"): _require_string(
            role["source_name"], "role source_name"
        )
        for role in _require_list(manifest["roles"], "roles")
        for role in [_require_mapping(role, "role entry")]
    }


def _parent_for_specialist(
    manifest: dict[str, object], specialist_id: str
) -> dict[str, object]:
    for parent in _require_list(manifest["parent_agents"], "parent_agents"):
        parent_mapping = _require_mapping(parent, "parent agent entry")
        delegated = [
            _require_string(item, "delegated specialist id")
            for item in _require_list(
                parent_mapping["delegated_specialists"], "delegated_specialists"
            )
        ]
        if specialist_id in delegated:
            return parent_mapping
    raise KeyError(f"No parent agent delegates to specialist '{specialist_id}'")


def _role_entry_by_id(manifest: dict[str, object], role_id: str) -> dict[str, object]:
    for role in _require_list(manifest["roles"], "roles"):
        role_mapping = _require_mapping(role, "role entry")
        if _require_string(role_mapping["id"], "role id") == role_id:
            return role_mapping
    raise KeyError(f"Unknown role '{role_id}'")


def _mode_participants(
    manifest: dict[str, object], mode_id: str, role_display_names: dict[str, str]
) -> dict[str, list[str]]:
    primary_roles: list[str] = []
    conditional_roles: list[str] = []

    for parent in _require_list(manifest["parent_agents"], "parent_agents"):
        parent_mapping = _require_mapping(parent, "parent agent entry")
        role_id = _require_string(parent_mapping["role_id"], "parent role_id")
        role_display = role_display_names[role_id]
        participation = _require_mapping(
            parent_mapping["mode_participation"], "mode_participation"
        )

        if mode_id in _require_list(participation["primary"], "primary mode list"):
            primary_roles.append(role_display)
        if mode_id in _require_list(
            participation["conditional"], "conditional mode list"
        ):
            conditional_roles.append(role_display)

    return {"primary": primary_roles, "conditional": conditional_roles}


def _protocol_participants(
    manifest: dict[str, object], protocol_id: str, role_display_names: dict[str, str]
) -> dict[str, list[str]]:
    owning_roles: list[str] = []
    participating_roles: list[str] = []

    for parent in _require_list(manifest["parent_agents"], "parent_agents"):
        parent_mapping = _require_mapping(parent, "parent agent entry")
        role_id = _require_string(parent_mapping["role_id"], "parent role_id")
        role_display = role_display_names[role_id]
        protocol_participation = _require_mapping(
            parent_mapping["protocol_participation"], "protocol_participation"
        )
        owns = [
            _require_string(item, "owned protocol id")
            for item in _require_list(protocol_participation["owns"], "owns list")
        ]
        participates_in = [
            _require_string(item, "participating protocol id")
            for item in _require_list(
                protocol_participation["participates_in"], "participates_in list"
            )
        ]
        if protocol_id in owns:
            owning_roles.append(role_display)
        if protocol_id in participates_in:
            participating_roles.append(role_display)

    return {"owns": owning_roles, "participates_in": participating_roles}


def _maintenance_mode_for_entry(
    codex_materialization: dict[str, object],
    family: str,
    entry: dict[str, object] | None,
) -> str:
    if entry is not None and "maintenance_mode" in entry:
        mode = _require_string(entry["maintenance_mode"], "entry maintenance_mode")
    else:
        defaults = _require_mapping(
            codex_materialization["surface_maintenance_defaults"],
            "surface_maintenance_defaults",
        )
        mode = _require_string(defaults[family], f"{family} maintenance_mode")

    if mode not in _SUPPORTED_MAINTENANCE_MODES:
        raise ValueError(f"Unsupported maintenance_mode '{mode}' for family '{family}'")
    return mode


def _surface_from_render(
    *,
    relative_path: str,
    concept_family: str,
    maintenance_mode: str,
    render: Callable[[], str],
) -> MaterializedSurface:
    if maintenance_mode == "mixed":
        raise ValueError(
            "maintenance_mode='mixed' is reserved until an explicit manual-block "
            "format is defined and validated"
        )
    if maintenance_mode == "human":
        return MaterializedSurface(
            relative_path=Path(relative_path),
            concept_family=concept_family,
            maintenance_mode=maintenance_mode,
            content=None,
        )
    return MaterializedSurface(
        relative_path=Path(relative_path),
        concept_family=concept_family,
        maintenance_mode=maintenance_mode,
        content=render(),
    )


def _runtime_layout(codex_materialization: dict[str, object]) -> _RuntimeLayout:
    orientation_surface = _require_mapping(
        codex_materialization["orientation_surface"], "orientation_surface"
    )
    config_surface = _require_mapping(
        codex_materialization["config_surface"], "config_surface"
    )
    return _RuntimeLayout(
        runtime_root=Path(
            _require_string(codex_materialization["runtime_root"], "runtime_root")
        ),
        skills_root=Path(
            _require_string(codex_materialization["skills_root"], "skills_root")
        ),
        orientation_surface=Path(
            _require_string(orientation_surface["path"], "orientation path")
        ),
        config_surface=Path(_require_string(config_surface["path"], "config path")),
    )


def _render_agents_md(
    manifest: dict[str, object],
    codex_materialization: dict[str, object],
    runtime_layout: _RuntimeLayout,
) -> str:
    role_entries = [
        _require_mapping(role, "role entry")
        for role in _require_list(manifest["roles"], "roles")
    ]
    parent_entries = [
        _require_mapping(parent, "parent agent entry")
        for parent in _require_list(manifest["parent_agents"], "parent_agents")
    ]
    specialist_entries = [
        _require_mapping(item, "specialist entry")
        for item in _require_list(manifest["specialists"], "specialists")
    ]
    mode_entries = [
        _require_mapping(mode, "mode entry")
        for mode in _require_list(manifest["modes"], "modes")
    ]
    protocol_entries = [
        _require_mapping(protocol, "protocol entry")
        for protocol in _require_list(manifest["protocols"], "protocols")
    ]

    lines = ["# Context Atlas Codex Runtime Orientation", ""]
    lines.extend(_markdown_notice_lines())
    lines.extend(
        [
            "",
            "## Purpose",
            "",
            "This is the runtime-facing orientation surface for the Context Atlas Codex materialization. It is downstream of the portable AgenticDevelopment canon, the Context Atlas Identity bindings, and the Codex materialization rules.",
            "",
            "Use this file to orient to the local runtime surface, then move quickly into the more specific role, agent, mode, protocol, and skill files instead of treating this file as the only definition source.",
            "",
            "## Read Order",
            "",
            "1. Read this file for the current runtime surface and concept boundaries.",
            f"2. Read the relevant role projection under `{runtime_layout.roles_root.as_posix()}/`.",
            f"3. Read the parent-agent descriptor in `{runtime_layout.agents_root.as_posix()}/` for the accountable actor bound to that role.",
            f"4. If work is delegated, read the relevant specialist descriptor in `{runtime_layout.agents_root.as_posix()}/`.",
            f"5. Read the active mode under `{runtime_layout.modes_root.as_posix()}/` and the governing workflow under `{runtime_layout.protocols_root.as_posix()}/`.",
            f"6. Read only the attached skills needed for the current bounded work under `{runtime_layout.skills_root.as_posix()}/`.",
            f"7. Use `{runtime_layout.config_surface.as_posix()}` for runtime roots, manifest traceability, and planning-capacity defaults.",
            "",
            "## Runtime Surface Index",
            "",
            "- Roles:",
        ]
    )
    lines.extend(
        _markdown_bullets(
            [
                runtime_layout.role_path(
                    _require_string(role["id"], "role id")
                ).as_posix()
                for role in role_entries
            ],
            indent="  ",
        )
    )
    lines.append("- Agents:")
    lines.extend(
        _markdown_bullets(
            [
                runtime_layout.agent_path(
                    _require_string(agent["id"], "agent id")
                ).as_posix()
                for agent in [*parent_entries, *specialist_entries]
            ],
            indent="  ",
        )
    )
    lines.append("- Modes:")
    lines.extend(
        _markdown_bullets(
            [
                runtime_layout.mode_path(
                    _require_string(mode["id"], "mode id")
                ).as_posix()
                for mode in mode_entries
            ],
            indent="  ",
        )
    )
    lines.append("- Protocols:")
    lines.extend(
        _markdown_bullets(
            [
                runtime_layout.protocol_path(
                    _require_string(protocol["id"], "protocol id")
                ).as_posix()
                for protocol in protocol_entries
            ],
            indent="  ",
        )
    )
    lines.extend(
        [
            "- Skills:",
            f"  - `{runtime_layout.skills_root.as_posix()}/context-atlas-*/SKILL.md`",
            "- Runtime config:",
            f"  - `{runtime_layout.config_surface.as_posix()}`",
            "",
            "## Boundary Notes",
            "",
        ]
    )
    lines.extend(
        _markdown_bullets(
            [
                "Roles are accountability surfaces.",
                "Parent agents are the materialized accountable actors for those roles.",
                "Specialists are bounded delegates beneath parent-owned accountability.",
                "Skills are atomic reusable capabilities attached to parents or specialists.",
                "Modes are execution states, not alternate roles.",
                "Protocols are workflow paths, not new role or mode families.",
                "GitHub authority remains downstream of RepoManagement bindings rather than being redefined by these runtime files.",
            ]
        )
    )
    lines.extend(
        [
            "",
            "## Traceability Notes",
            "",
            "- Maintenance mode: `generated`",
            "- Primary upstream sources:",
        ]
    )
    lines.extend(
        _markdown_bullets(
            _quoted_paths(
                [
                    "docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml",
                    "docs/Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md",
                    "docs/Authoritative/Identity/AgenticDevelopment/Bindings/",
                    "docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/",
                ]
            ),
            indent="  ",
        )
    )
    lines.extend(
        [
            "- Copied content:",
            "  - stable role, mode, protocol, parent-agent, specialist, and skill ids",
            "- Adapted content:",
            "  - short Codex-facing summaries and read-order guidance",
            "- Derived content:",
            "  - file layout, runtime index, and local cross-surface links",
        ]
    )
    return _format_markdown(lines)


def _render_config_toml(
    manifest: dict[str, object],
    capacity: dict[str, object],
    codex_materialization: dict[str, object],
    runtime_layout: _RuntimeLayout,
) -> str:
    planning_capacity = _require_mapping(
        capacity["planning_capacity"], "planning_capacity"
    )
    decomposition_policy = _require_mapping(
        capacity["decomposition_policy"], "decomposition_policy"
    )
    materialization_entry = codex_materialization
    config_surface = _require_mapping(
        materialization_entry["config_surface"], "config_surface"
    )

    lines = [
        "# Context Atlas Codex runtime configuration",
        "# This file is generated or regenerated from the authoritative Canon and",
        "# Identity docs rather than treated as the lasting source of truth.",
        "# Local edits may be overwritten by later regeneration.",
        "# Durable semantic changes belong upstream in:",
        "# - docs/Authoritative/Canon/ for reusable or global meaning",
        "# - docs/Authoritative/Identity/ for Context Atlas-specific meaning",
        "",
        f"project_id = {_toml_string('context-atlas')}",
        f"platform = {_toml_string(_require_string(materialization_entry['platform'], 'platform'))}",
        f"maintenance_mode = {_toml_string(_require_string(config_surface['maintenance_mode'], 'config maintenance_mode'))}",
        f"orientation_surface = {_toml_string(runtime_layout.orientation_surface.as_posix())}",
        "",
        "[traceability]",
        f"materialization_manifest = {_toml_string(_MANIFEST_PATH.as_posix())}",
        f"project_profile = {_toml_string(_PROJECT_PROFILE_PATH.as_posix())}",
        f"runtime_capacity = {_toml_string(_CAPACITY_PATH.as_posix())}",
        f"codex_binding_root = {_toml_string(_CODEX_BINDING_ROOT.as_posix() + '/')}",
        "",
        "[layout]",
        f"roles_root = {_toml_string(runtime_layout.roles_root.as_posix())}",
        f"agents_root = {_toml_string(runtime_layout.agents_root.as_posix())}",
        f"modes_root = {_toml_string(runtime_layout.modes_root.as_posix())}",
        f"protocols_root = {_toml_string(runtime_layout.protocols_root.as_posix())}",
        f"skills_root = {_toml_string(runtime_layout.skills_root.as_posix())}",
        "",
        "[capacity]",
        f"total_runtimes = {planning_capacity['total_runtimes']}",
        f"usable_runtimes = {planning_capacity['usable_runtimes']}",
        f"max_parallel_story_lanes = {decomposition_policy['max_parallel_story_lanes']}",
        f"max_parallel_task_lanes = {decomposition_policy['max_parallel_task_lanes']}",
        f"require_base_work_first = {'true' if decomposition_policy['require_base_work_first'] else 'false'}",
        "",
        "[materialization]",
        f"roles = {len(_require_list(manifest['roles'], 'roles'))}",
        f"parent_agents = {len(_require_list(manifest['parent_agents'], 'parent_agents'))}",
        f"specialists = {len(_require_list(manifest['specialists'], 'specialists'))}",
        f"modes = {len(_require_list(manifest['modes'], 'modes'))}",
        f"protocols = {len(_require_list(manifest['protocols'], 'protocols'))}",
        f"skills = {len(_require_list(manifest['skills'], 'skills'))}",
    ]
    return "\n".join(lines) + "\n"


def _sentence_case(text: str) -> str:
    cleaned = text.strip()
    if not cleaned:
        return cleaned
    return cleaned[0].upper() + cleaned[1:]


def _runtime_skill_purpose(text: str) -> str:
    for prefix in (
        "Define the portable skill for ",
        "Define the portable skill to ",
    ):
        if text.startswith(prefix):
            return "Use this skill for " + text[len(prefix) :]
    return text


def _runtime_protocol_purpose(text: str) -> str:
    prefixes = (
        "Define the portable workflow used when ",
        "Define the portable workflow and structured contract shape used when ",
    )
    cleaned = text
    for prefix in prefixes:
        if cleaned.startswith(prefix):
            cleaned = cleaned[len(prefix) :]
            break
    return "Materialize the workflow path used when " + cleaned


def _title_from_id(value: str) -> str:
    return value.replace("-", " ").replace("_", " ").title()


def _comma_list(text: str) -> list[str]:
    return [item.strip() for item in text.split(",") if item.strip()]


def _format_code_list(values: list[str]) -> list[str]:
    return [f"`{value}`" for value in values]


def _find_manifest_entry(
    entries: list[object], entry_id: str, context: str
) -> dict[str, object]:
    for entry in entries:
        entry_mapping = _require_mapping(entry, context)
        if _require_string(entry_mapping["id"], f"{context} id") == entry_id:
            return entry_mapping
    raise KeyError(f"Unable to find {context} '{entry_id}'")


def _gate_review_rows(repo_root: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    text = _strip_front_matter(_read_text(repo_root, _GATE_REVIEW_PASS_PATH))

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("| `"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) != 4:
            continue
        rows.append(
            {
                "workflow_gate": cells[0],
                "required_review_passes": re.findall(r"`([^`]+)`", cells[1]),
                "typical_intake_contract": cells[2],
                "default_qa_outcome_target": cells[3],
            }
        )

    return rows


def _canonical_protocol_sources(protocol_id: str) -> list[str]:
    if protocol_id in {"delegation", "handoff", "escalation"}:
        return [
            _protocol_doc_path(protocol_id.replace("-", "_")).as_posix(),
            "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md",
            "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Mode-Bindings.md",
        ]
    return _protocol_sources({"source_name": protocol_id.replace("-", "_")})


def _role_protocol_note(role_id: str) -> str | None:
    if role_id == "devops":
        return "Consumes structured review state before merge or release action"
    return None


def _parent_binding_line(parent_id: str, runtime_layout: _RuntimeLayout) -> str:
    return f"Materialized by `{runtime_layout.agent_path(parent_id).as_posix()}`"


def _delegated_specialist_line(
    role_id: str, specialist_id: str, runtime_layout: _RuntimeLayout
) -> str:
    label = "Delegated specialist support may return through"
    if role_id == "planner-decomp":
        label = "Delegated planning support may return through"
    elif role_id == "devops":
        label = "Delegated delivery and recovery support may return through"
    return f"{label} `{runtime_layout.agent_path(specialist_id).as_posix()}`"


def _render_role_projection(
    repo_root: Path,
    manifest: dict[str, object],
    role: dict[str, object],
    parent_agent: dict[str, object],
    runtime_layout: _RuntimeLayout,
) -> str:
    role_id = _require_string(role["id"], "role id")
    role_display_name = _require_string(role["source_name"], "role source_name")
    accountability = _role_accountability_data(repo_root, role_display_name)

    ownership_lines = list(accountability["direct_artifact_ownership"])
    if role_id == "planner-decomp":
        ownership_lines.append(
            "decisions about work breakdown, dependency shape, and sequencing clarity"
        )
    elif role_id == "devops":
        ownership_lines = [
            "CI and workflow definitions under `.github/workflows/`",
            "release-process documentation and release summaries",
            "versioning, tagging, merge, and operational delivery artifacts",
            "operational scripts whose primary purpose is repository delivery",
        ]

    delegated_specialists = [
        _require_string(item, "delegated specialist id")
        for item in _require_list(
            parent_agent["delegated_specialists"], "delegated_specialists"
        )
    ]
    mode_participation = _require_mapping(
        parent_agent["mode_participation"], "mode_participation"
    )
    protocol_participation = _require_mapping(
        parent_agent["protocol_participation"], "protocol_participation"
    )
    owns = [
        _require_string(item, "owned protocol id")
        for item in _require_list(protocol_participation["owns"], "owns")
    ]
    participates_in = [
        _require_string(item, "participating protocol id")
        for item in _require_list(
            protocol_participation["participates_in"], "participates_in"
        )
    ]

    lines = [f"# {role_display_name} Role Projection", ""]
    lines.extend(_markdown_notice_lines())
    lines.extend(
        [
            "",
            "## Purpose",
            "",
            _ROLE_PURPOSE_OVERRIDES.get(
                role_id,
                (
                    f"Materialize the Context Atlas `{role_display_name}` role "
                    f"as the accountable surface for "
                    f"{str(accountability['primary_accountability']).lower()}."
                ),
            ),
            "",
            "## Direct Ownership",
            "",
        ]
    )
    lines.extend(_markdown_bullets(ownership_lines))
    lines.extend(["", "## Parent-Agent Binding", ""])
    binding_lines = [
        _parent_binding_line(
            _require_string(parent_agent["id"], "parent agent id"), runtime_layout
        )
    ]
    binding_lines.extend(
        _delegated_specialist_line(role_id, specialist_id, runtime_layout)
        for specialist_id in delegated_specialists
    )
    lines.extend(_markdown_bullets(binding_lines))
    lines.extend(["", "## Mode Participation", "", "- Primary:"])
    lines.extend(
        _markdown_bullets(
            _format_code_list(
                [
                    _require_string(item, "primary mode id")
                    for item in _require_list(mode_participation["primary"], "primary")
                ]
            ),
            indent="  ",
        )
    )
    lines.append("- Conditional:")
    lines.extend(
        _markdown_bullets(
            _format_code_list(
                [
                    _require_string(item, "conditional mode id")
                    for item in _require_list(
                        mode_participation["conditional"], "conditional"
                    )
                ]
            ),
            indent="  ",
        )
    )
    lines.extend(["", "## Protocol Participation", "", "- Owns:"])
    if owns:
        owns_lines = _format_code_list(owns)
        if role_id == "planner-decomp" and "rework" in owns:
            owns_lines = ["`planning`", "`rework` when planning artifacts are returned"]
        lines.extend(_markdown_bullets(owns_lines, indent="  "))
    else:
        lines.extend(
            _markdown_bullets(
                ["none in the initial shared protocol family"], indent="  "
            )
        )
    lines.append("- Participates in:")
    lines.extend(_markdown_bullets(_format_code_list(participates_in), indent="  "))
    protocol_note = _role_protocol_note(role_id)
    if protocol_note:
        lines.extend(_markdown_bullets([protocol_note]))
    lines.extend(
        [
            "",
            "## Traceability",
            "",
            "- Maintenance mode: `generated`",
            "- Upstream sources:",
        ]
    )
    lines.extend(_markdown_bullets(_quoted_paths(_role_sources(role_id)), indent="  "))
    return _format_markdown(lines)


def _render_agent_descriptor(
    repo_root: Path,
    manifest: dict[str, object],
    agent: dict[str, object],
    *,
    agent_kind: str,
) -> str:
    if agent_kind not in {"parent", "specialist"}:
        raise ValueError(f"Unsupported agent_kind '{agent_kind}'")

    agent_id = _require_string(agent["id"], "agent id")
    role_id: str
    title: str
    summary: str
    authority_scope: str
    notes: dict[str, list[str]]
    binding_sources: list[str]

    if agent_kind == "parent":
        role_id = _require_string(agent["role_id"], "parent role_id")
        role_entry = _role_entry_by_id(manifest, role_id)
        role_display_name = _require_string(
            role_entry["source_name"], "role source_name"
        )
        title = f"{role_display_name} Parent Agent"
        summary = _PARENT_AGENT_SUMMARIES[agent_id]
        authority_scope = _PARENT_AUTHORITY_SCOPES[agent_id]
        notes = _PARENT_NOTES[agent_id]
        binding_sources = [
            _MANIFEST_PATH.as_posix(),
            "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Model.md",
            "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Agent-Binding-Model.md",
            "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Authority-Matrix.md",
        ]
        if role_id == "qa":
            binding_sources.append(
                "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Gate-Review-Pass-Matrix.md"
            )
        elif role_id == "devops":
            binding_sources.append(
                "docs/Authoritative/Identity/RepoManagement/GitHub/Principal-Binding-Model.md"
            )
        else:
            binding_sources.append(
                "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md"
            )
    else:
        parent_agent = _parent_for_specialist(manifest, agent_id)
        role_id = _require_string(parent_agent["role_id"], "specialist role_id")
        title = _specialist_doc_sections(
            repo_root, Path(_require_string(agent["canon_ref"], "canon_ref"))
        )["title"]
        summary = _SPECIALIST_SUMMARIES[agent_id]
        authority_scope = _SPECIALIST_AUTHORITY_SCOPES[agent_id]
        notes = _SPECIALIST_NOTES[agent_id]
        binding_sources = [
            _MANIFEST_PATH.as_posix(),
            _require_string(agent["canon_ref"], "canon_ref"),
        ]

    skill_attachment = (
        _require_mapping(agent["attached_skills"], "attached_skills")
        if agent_kind == "specialist"
        else _require_mapping(agent["direct_skills"], "direct_skills")
    )
    mode_participation = _require_mapping(
        agent["mode_participation"], "mode_participation"
    )
    protocol_participation = _require_mapping(
        agent["protocol_participation"], "protocol_participation"
    )
    owns = []
    if "owns" in protocol_participation:
        owns = [
            _require_string(item, "owned protocol id")
            for item in _require_list(protocol_participation["owns"], "owns")
        ]
    participates_in = [
        _require_string(item, "participating protocol id")
        for item in _require_list(
            protocol_participation["participates_in"], "participates_in"
        )
    ]
    delegated_specialists = []
    returns_to = agent_id
    if agent_kind == "parent":
        delegated_specialists = [
            _require_string(item, "delegated specialist id")
            for item in _require_list(
                agent["delegated_specialists"], "delegated_specialists"
            )
        ]
        returns_to = agent_id
    else:
        returns_to = _require_string(
            _parent_for_specialist(manifest, agent_id)["id"], "parent agent id"
        )

    lines = [
        "# This file is generated or regenerated from the authoritative Canon and",
        "# Identity docs rather than treated as the lasting source of truth.",
        "# Local edits may be overwritten by later regeneration.",
        "# Durable semantic changes belong upstream in:",
        "# - docs/Authoritative/Canon/ for reusable or global meaning",
        "# - docs/Authoritative/Identity/ for Context Atlas-specific meaning",
        "",
        f"id = {_toml_string(agent_id)}",
        f"title = {_toml_string(title)}",
        f"summary = {_toml_string(summary)}",
        f"agent_kind = {_toml_string(agent_kind)}",
        f"maintenance_mode = {_toml_string('generated')}",
        "",
        "[traceability]",
        f"project_profile = {_toml_string(_PROJECT_PROFILE_PATH.as_posix())}",
    ]
    lines.append("binding_sources = [")
    for source in binding_sources:
        lines.append(f"  {_toml_string(source)},")
    lines.extend(
        [
            "]",
            f"template_source = {_toml_string((_CODEX_BINDING_ROOT / 'agent.template.toml').as_posix())}",
            "",
            "[role_binding]",
            f"role_id = {_toml_string(role_id)}",
            f"authority_scope = {_toml_string(authority_scope)}",
            "",
            "[skill_attachment]",
            f"baseline = {_toml_array([_require_string(item, 'baseline skill id') for item in _require_list(skill_attachment['baseline'], 'baseline skills')])}",
            f"conditional = {_toml_array([_require_string(item, 'conditional skill id') for item in _require_list(skill_attachment['conditional'], 'conditional skills')])}",
            "",
            "[mode_participation]",
            f"primary = {_toml_array([_require_string(item, 'primary mode id') for item in _require_list(mode_participation['primary'], 'primary modes')])}",
            f"conditional = {_toml_array([_require_string(item, 'conditional mode id') for item in _require_list(mode_participation['conditional'], 'conditional modes')])}",
            "",
            "[protocol_participation]",
            f"owns = {_toml_array(owns)}",
            f"participates_in = {_toml_array(participates_in)}",
            "",
            "[delegation]",
            f"delegates_to = {_toml_array(delegated_specialists)}",
            f"returns_to = {_toml_string(returns_to)}",
            "",
            "[notes]",
        ]
    )
    lines.append("constraints = [")
    for constraint in notes["constraints"]:
        lines.append(f"  {_toml_string(constraint)},")
    lines.append("]")
    lines.append("non_goals = [")
    for non_goal in notes["non_goals"]:
        lines.append(f"  {_toml_string(non_goal)},")
    lines.append("]")
    return "\n".join(lines).rstrip() + "\n"


def _render_mode_surface(
    repo_root: Path,
    manifest: dict[str, object],
    mode: dict[str, object],
    role_display_names: dict[str, str],
) -> str:
    mode_id = _require_string(mode["id"], "mode id")
    source_name = _require_string(mode["source_name"], "mode source_name")
    mode_title = _mode_title(mode_id)
    transitions = _mode_transition_data(repo_root, mode_title)
    mutation_row = _mode_mutation_row(repo_root, source_name)
    participants = _mode_participants(manifest, mode_id, role_display_names)
    protocol_primary_modes = _protocol_primary_mode_map(repo_root)

    primary_protocol = None
    for protocol_id, mapped_mode_id in protocol_primary_modes.items():
        if mapped_mode_id == source_name:
            primary_protocol = protocol_id
            break

    lines = [f"# {mode_title} Mode", ""]
    lines.extend(_markdown_notice_lines())
    lines.extend(
        [
            "",
            "## Purpose",
            "",
            _MODE_PURPOSE_OVERRIDES.get(
                mode_id,
                (
                    f"Materialize the Context Atlas `{source_name}` mode as the "
                    f"Codex-facing execution state for {source_name.replace('_', ' ')} work."
                ),
            ),
            "",
            "## Entry Conditions",
            "",
        ]
    )
    lines.extend(_markdown_bullets(list(transitions["enter"])))
    lines.extend(["", "## Exit Conditions", ""])
    lines.extend(_markdown_bullets(list(transitions["exit"])))
    lines.extend(["", "## Allowed Mutations", ""])
    lines.extend(_markdown_bullets(_comma_list(mutation_row["allowed"])))
    lines.extend(["", "Not allowed by default:", ""])
    lines.extend(_markdown_bullets(_comma_list(mutation_row["not_allowed"])))
    lines.extend(["", "## Role And Protocol Participation", ""])
    if participants["primary"]:
        label = (
            "Primary role:" if len(participants["primary"]) == 1 else "Primary roles:"
        )
        lines.append(f"- {label}")
        lines.extend(
            _markdown_bullets(
                _format_code_list(participants["primary"]),
                indent="  ",
            )
        )
    if participants["conditional"]:
        label = (
            "Conditional role:"
            if len(participants["conditional"]) == 1
            else "Conditional roles:"
        )
        lines.append(f"- {label}")
        lines.extend(
            _markdown_bullets(
                _format_code_list(participants["conditional"]),
                indent="  ",
            )
        )
    if primary_protocol is None and mode_id == "operational-delivery":
        lines.extend(
            _markdown_bullets(
                [
                    "There is no dedicated initial shared operational-delivery protocol in the current protocol family",
                    "Common cross-cutting contracts:",
                ]
            )
        )
        lines.extend(
            _markdown_bullets(
                _format_code_list(["handoff", "escalation"]),
                indent="  ",
            )
        )
    elif primary_protocol is not None:
        lines.append("- Primary protocol:")
        lines.extend(_markdown_bullets([f"`{primary_protocol}`"], indent="  "))
        if mode_id == "review":
            lines.extend(
                _markdown_bullets(
                    [
                        "Multiple required review passes may occur within one `review` span without creating extra mode nodes",
                        "Cross-cutting contract protocols may appear at the edges:",
                    ]
                )
            )
            lines.extend(
                _markdown_bullets(
                    _format_code_list(["handoff", "escalation"]),
                    indent="  ",
                )
            )
        else:
            lines.extend(
                _markdown_bullets(
                    ["Cross-cutting contract protocols may appear at the edges:"]
                )
            )
            lines.extend(
                _markdown_bullets(
                    _format_code_list(["delegation", "handoff", "escalation"]),
                    indent="  ",
                )
            )
    lines.extend(
        [
            "",
            "## Traceability",
            "",
            "- Maintenance mode: `generated`",
            "- Upstream sources:",
        ]
    )
    mode_sources = _mode_sources()
    if mode_id == "review":
        mode_sources.append(
            "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Gate-Review-Pass-Matrix.md"
        )
    lines.extend(_markdown_bullets(_quoted_paths(mode_sources), indent="  "))
    return _format_markdown(lines)


def _render_protocol_surface(
    repo_root: Path,
    manifest: dict[str, object],
    protocol: dict[str, object],
    role_display_names: dict[str, str],
) -> str:
    protocol_id = _require_string(protocol["id"], "protocol id")
    source_name = _require_string(protocol["source_name"], "protocol source_name")
    sections = _protocol_doc_sections(repo_root, source_name)
    participants = _protocol_participants(manifest, protocol_id, role_display_names)
    gate_rows = (
        _gate_review_rows(repo_root) if protocol_id in {"review", "handoff"} else []
    )

    lines = [f"# {_title_from_id(protocol_id)} Protocol", ""]
    lines.extend(_markdown_notice_lines())
    lines.extend(
        [
            "",
            "## Purpose",
            "",
            _runtime_protocol_purpose(
                _require_string(sections["purpose"], "protocol purpose")
            )
            if sections["purpose"]
            else "",
            "",
            "## Trigger / Enter Conditions",
            "",
        ]
    )
    lines.extend(_markdown_bullets(list(sections["trigger"])))
    lines.extend(["", "## Participating Roles And Modes", ""])

    if protocol_id in {"delegation", "handoff", "escalation"}:
        cross_cutting_lines = {
            "delegation": [
                "no permanent owning top-level role",
                "used by the currently accountable role while work remains in its ownership",
                "mode-spanning contract protocol:",
                "usually occurs within the current mode or at its edges",
            ],
            "handoff": [
                "no permanent owning top-level role",
                "used by whichever accountable boundary is handing work forward",
                "mode-spanning contract protocol:",
                "often occurs at the edge of leaving one mode and entering the next",
            ],
            "escalation": [
                "no permanent owning top-level role",
                "used by the currently accountable boundary when authority or safe next action must move upward",
                "mode-spanning contract protocol:",
                "commonly appears at blocked edges of planning, execution, review, rework, or recovery",
            ],
        }
        lines.append(f"- {cross_cutting_lines[protocol_id][0]}")
        lines.append(f"- {cross_cutting_lines[protocol_id][1]}")
        lines.append(f"- {cross_cutting_lines[protocol_id][2]}")
        lines.append(f"  - {cross_cutting_lines[protocol_id][3]}")
    elif protocol_id == "planning":
        lines.append("- Owning role:")
        lines.extend(_markdown_bullets(["`Planner/Decomp`"], indent="  "))
        lines.append("- Conditional participants:")
        lines.extend(
            _markdown_bullets(
                _format_code_list(["Backend", "Documentation/UAT"]),
                indent="  ",
            )
        )
        lines.append("- Primary mode:")
        lines.extend(_markdown_bullets(["`planning`"], indent="  "))
    elif protocol_id == "execution-slice":
        lines.append("- Owning roles:")
        lines.extend(
            _markdown_bullets(
                _format_code_list(participants["owns"]),
                indent="  ",
            )
        )
        lines.append("- Common delegated participant:")
        lines.extend(
            _markdown_bullets(
                ["backend-oriented implementation specialists"], indent="  "
            )
        )
        lines.append("- Primary mode:")
        lines.extend(_markdown_bullets(["`implementation`"], indent="  "))
    elif protocol_id == "review":
        lines.append("- Owning role:")
        lines.extend(_markdown_bullets(["`QA`"], indent="  "))
        lines.append("- Producing participants:")
        lines.extend(
            _markdown_bullets(
                [
                    "`Backend`",
                    "`Documentation/UAT`",
                    "other roles when their owned work is under review",
                ],
                indent="  ",
            )
        )
        lines.append("- Primary mode:")
        lines.extend(_markdown_bullets(["`review`"], indent="  "))
    elif protocol_id == "rework":
        lines.append("- Owning roles depend on the returned surface:")
        lines.extend(
            _markdown_bullets(
                [
                    "`Planner/Decomp` for planning rework",
                    "`Backend` for backend rework",
                    "`Documentation/UAT` for documentation/UAT rework",
                    "`DevOps` for operational rework",
                    "`QA` only for QA-owned validation artifacts",
                ],
                indent="  ",
            )
        )
        lines.append("- Primary mode:")
        lines.extend(_markdown_bullets(["`rework`"], indent="  "))
    elif protocol_id == "recovery":
        lines.extend(
            _markdown_bullets(
                [
                    "ownership is context-dependent and stays with the role closest to the broken workflow state unless escalation changes that",
                    "any role may participate when its workflow state is implicated",
                ]
            )
        )
        lines.append("- Primary mode:")
        lines.extend(_markdown_bullets(["`recovery`"], indent="  "))
    else:
        if participants["owns"]:
            label = (
                "Owning role:" if len(participants["owns"]) == 1 else "Owning roles:"
            )
            lines.append(f"- {label}")
            lines.extend(
                _markdown_bullets(
                    _format_code_list(participants["owns"]),
                    indent="  ",
                )
            )
        if participants["participates_in"]:
            label = (
                "Participating role:"
                if len(participants["participates_in"]) == 1
                else "Participating roles:"
            )
            lines.append(f"- {label}")
            lines.extend(
                _markdown_bullets(
                    _format_code_list(participants["participates_in"]),
                    indent="  ",
                )
            )

    lines.extend(["", "## Structured Contract Expectations", ""])
    if protocol_id == "review":
        lines.extend(
            _markdown_bullets(
                [
                    "normally consumes `implementation_complete`",
                    "carries gate scope through `scope_level` instead of ad hoc contract types",
                    "requested review passes stay explicit:",
                ]
            )
        )
        for row in gate_rows:
            passes = ", ".join(f"`{item}`" for item in row["required_review_passes"])
            workflow_gate = _require_string(row["workflow_gate"], "workflow_gate")
            lines.append(f"  - {workflow_gate}: {passes}")
        lines.extend(_markdown_bullets(["emits structured review outcomes such as:"]))
        lines.extend(
            _markdown_bullets(
                [str(item) for item in sections["review_outcomes"]],
                indent="  ",
            )
        )
    elif protocol_id == "delegation":
        lines.extend(
            _markdown_bullets(
                [
                    "delegation scope must stay explicit and bounded",
                    "the contract should identify:",
                ]
            )
        )
        lines.extend(
            _markdown_bullets(
                [
                    "applicable constraints",
                    "expected outputs",
                    "return conditions",
                    "escalation conditions",
                ],
                indent="  ",
            )
        )
        lines.extend(
            _markdown_bullets(
                [
                    "parent accountability remains explicit even when specialists are involved"
                ]
            )
        )
    elif protocol_id == "handoff":
        lines.extend(
            _markdown_bullets(
                [
                    "handoff contracts should stay structured and machine-readable",
                ]
            )
        )
        lines.append("- normal completion handoff type:")
        lines.extend(_markdown_bullets(["`implementation_complete`"], indent="  "))
        lines.append("- scope is carried through:")
        scope_levels = []
        for row in gate_rows:
            if "task" in _require_string(row["workflow_gate"], "workflow_gate").lower():
                scope_levels.append("`scope_level: task`")
            elif (
                "story"
                in _require_string(row["workflow_gate"], "workflow_gate").lower()
            ):
                scope_levels.append("`scope_level: story`")
            elif (
                "epic" in _require_string(row["workflow_gate"], "workflow_gate").lower()
            ):
                scope_levels.append("`scope_level: epic`")
        lines.extend(_markdown_bullets(scope_levels, indent="  "))
        lines.extend(
            _markdown_bullets(
                [
                    "downstream target, next action, changed surfaces, verification, and open risks should remain explicit"
                ]
            )
        )
    elif protocol_id == "execution-slice":
        lines.extend(
            _markdown_bullets(
                [
                    "consumes a structured planning or upstream handoff contract",
                    "may use `delegation` for bounded specialist work",
                    "emits a structured `implementation_complete` handoff when review is next",
                    "should include changed surfaces, verification summary, and open risks",
                ]
            )
        )
    elif protocol_id == "planning":
        lines.extend(
            _markdown_bullets(
                [
                    "consumes a planning-intake contract or other structured statement of scope",
                    "may use `delegation` for bounded planning analysis",
                    "should emit a structured planning-output handoff when downstream work is ready",
                    "should use `escalation` when ownership or safe next-step shape remains unclear",
                ]
            )
        )
    elif protocol_id == "rework":
        lines.extend(
            _markdown_bullets(
                [
                    "consumes structured review outcomes or recovery outputs",
                    "should keep traceability back to the returned finding or request",
                    "emits a renewed completion handoff or a structured escalation when the return cannot be satisfied safely",
                ]
            )
        )
    elif protocol_id == "recovery":
        lines.extend(
            _markdown_bullets(
                [
                    "consumes the broken or ambiguous workflow state plus available prior contracts or evidence",
                    "emits a structured recovery outcome naming clarified ownership and the recommended next protocol",
                    "may escalate when the recovering boundary cannot restore workable state",
                ]
            )
        )
    elif protocol_id == "escalation":
        lines.extend(_markdown_bullets(["escalation contracts should preserve:"]))
        lines.extend(
            _markdown_bullets(
                [
                    "escalation reason",
                    "completed scope so far",
                    "unresolved items",
                    "broader target boundary",
                    "recommended next action",
                ],
                indent="  ",
            )
        )
        lines.extend(
            _markdown_bullets(
                [
                    "escalation stays distinct from ordinary completion handoff and ordinary review findings"
                ]
            )
        )
    else:
        lines.extend(
            _markdown_bullets([str(item) for item in sections["required_outputs"]])
        )

    lines.extend(["", "## Exit Criteria", ""])
    lines.extend(_markdown_bullets(list(sections["exit_criteria"])))
    lines.extend(
        [
            "",
            "## Traceability",
            "",
            "- Maintenance mode: `generated`",
            "- Upstream sources:",
        ]
    )
    trace_sources = _canonical_protocol_sources(protocol_id)
    if protocol_id == "handoff":
        trace_sources.append(
            "docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Gate-Review-Pass-Matrix.md"
        )
    if protocol_id in {"delegation", "execution-slice"}:
        trace_sources.append(_MANIFEST_PATH.as_posix())
    lines.extend(_markdown_bullets(_quoted_paths(trace_sources), indent="  "))
    return _format_markdown(lines)


def _skill_attachments(
    manifest: dict[str, object], skill_id: str
) -> dict[str, list[str]]:
    baseline: list[str] = []
    conditional: list[str] = []

    for parent in _require_list(manifest["parent_agents"], "parent_agents"):
        parent_mapping = _require_mapping(parent, "parent agent entry")
        direct_skills = _require_mapping(
            parent_mapping["direct_skills"], "direct_skills"
        )
        parent_id = _require_string(parent_mapping["id"], "parent agent id")
        for item in _require_list(direct_skills["baseline"], "baseline skills"):
            if _require_string(item, "skill id") == skill_id:
                baseline.append(parent_id)
        for item in _require_list(direct_skills["conditional"], "conditional skills"):
            if _require_string(item, "skill id") == skill_id:
                conditional.append(parent_id)

    for specialist in _require_list(manifest["specialists"], "specialists"):
        specialist_mapping = _require_mapping(specialist, "specialist entry")
        attached_skills = _require_mapping(
            specialist_mapping["attached_skills"], "attached_skills"
        )
        specialist_id = _require_string(specialist_mapping["id"], "specialist id")
        for item in _require_list(attached_skills["baseline"], "baseline skills"):
            if _require_string(item, "skill id") == skill_id:
                baseline.append(specialist_id)
        for item in _require_list(attached_skills["conditional"], "conditional skills"):
            if _require_string(item, "skill id") == skill_id:
                conditional.append(specialist_id)

    return {"baseline": baseline, "conditional": conditional}


def _display_attachment_label(skill_id: str, agent_id: str) -> str:
    override = _SKILL_ATTACHMENT_LABEL_OVERRIDES.get((skill_id, agent_id))
    if override is not None:
        return override
    return f"`{agent_id}`"


def _render_skill_surface(
    repo_root: Path,
    manifest: dict[str, object],
    skill: dict[str, object],
) -> str:
    skill_id = _require_string(skill["id"], "skill id")
    canon_ref = Path(_require_string(skill["canon_ref"], "canon_ref"))
    sections = _skill_doc_sections(repo_root, canon_ref)
    attachments = _skill_attachments(manifest, skill_id)

    lines = [f"# Context Atlas Skill: {sections['title']}", ""]
    lines.extend(_markdown_notice_lines())
    lines.extend(
        [
            "",
            "## Purpose",
            "",
            _runtime_skill_purpose(
                _require_string(sections["purpose"], "skill purpose")
            ),
            "",
            "## Parent Boundary",
            "",
        ]
    )
    if attachments["baseline"]:
        lines.append("- Baseline for:")
        lines.extend(
            _markdown_bullets(
                [
                    _display_attachment_label(skill_id, agent_id)
                    for agent_id in attachments["baseline"]
                ],
                indent="  ",
            )
        )
    if attachments["conditional"]:
        lines.append("- Conditional for:")
        lines.extend(
            _markdown_bullets(
                [
                    _display_attachment_label(skill_id, agent_id)
                    for agent_id in attachments["conditional"]
                ],
                indent="  ",
            )
        )
    guardrails = sections.get("guardrails", [])
    if guardrails:
        lines.extend(["- " + _sentence_case(guardrails[0])])
    lines.extend(["", "## Workflow", ""])
    lines.extend(
        _numbered_markdown(
            [_sentence_case(str(item)) for item in sections["execution_pattern"]]
        )
    )
    lines.extend(["", "## Escalation Conditions", ""])
    lines.extend(
        _markdown_bullets(
            [_sentence_case(str(item)) for item in sections["escalation"]]
        )
    )
    lines.extend(["", "## Return Contract", ""])
    lines.extend(_markdown_bullets(list(sections["expected_outputs"])))
    lines.extend(
        [
            "",
            "## Traceability",
            "",
            "- Maintenance mode: `generated`",
            "- Canon source:",
            f"  - `{canon_ref.as_posix()}`",
            "- Identity binding source:",
            f"  - `{_MANIFEST_PATH.as_posix()}`",
            "- Adaptation note:",
            (
                "  - workflow and return contract are adapted from the canon "
                "skill's execution pattern and expected outputs"
            ),
        ]
    )
    return _format_markdown(lines)


def build_materialization_plan(
    repo_root: Path, selected_surfaces: set[str] | None = None
) -> MaterializationPlan:
    selected = selected_surfaces or set(_SUPPORTED_SURFACES)
    unknown = selected - _SUPPORTED_SURFACES
    if unknown:
        raise ValueError(f"Unsupported surface selection(s): {sorted(unknown)!r}")

    manifest = _load_simple_yaml(repo_root, _MANIFEST_PATH)
    capacity = _load_simple_yaml(repo_root, _CAPACITY_PATH)
    materializations = _require_list(manifest["materializations"], "materializations")
    codex_materialization = None
    for entry in materializations:
        entry_mapping = _require_mapping(entry, "materialization entry")
        if _require_string(entry_mapping["platform"], "platform") == "Codex" and bool(
            entry_mapping.get("enabled", False)
        ):
            codex_materialization = entry_mapping
            break
    if codex_materialization is None:
        raise ValueError("No enabled Codex materialization found in the manifest")
    runtime_layout = _runtime_layout(codex_materialization)

    role_display_names = _role_display_map(manifest)
    roles = [
        _require_mapping(role, "role entry")
        for role in _require_list(manifest["roles"], "roles")
    ]
    parent_agents = [
        _require_mapping(agent, "parent agent entry")
        for agent in _require_list(manifest["parent_agents"], "parent_agents")
    ]
    parent_by_role = {
        _require_string(agent["role_id"], "parent role_id"): agent
        for agent in parent_agents
    }
    specialists = [
        _require_mapping(entry, "specialist entry")
        for entry in _require_list(manifest["specialists"], "specialists")
    ]
    modes = [
        _require_mapping(mode, "mode entry")
        for mode in _require_list(manifest["modes"], "modes")
    ]
    protocols = [
        _require_mapping(protocol, "protocol entry")
        for protocol in _require_list(manifest["protocols"], "protocols")
    ]
    skills = [
        _require_mapping(skill, "skill entry")
        for skill in _require_list(manifest["skills"], "skills")
    ]

    generated: list[MaterializedSurface] = []
    human_managed: list[MaterializedSurface] = []

    def add_surface(surface: MaterializedSurface) -> None:
        if surface.maintenance_mode == "human":
            human_managed.append(surface)
        else:
            generated.append(surface)

    if "orientation" in selected:
        orientation_surface = _require_mapping(
            codex_materialization["orientation_surface"], "orientation_surface"
        )
        add_surface(
            _surface_from_render(
                relative_path=_require_string(
                    orientation_surface["path"], "orientation path"
                ),
                concept_family="orientation",
                maintenance_mode=_maintenance_mode_for_entry(
                    codex_materialization, "orientation", orientation_surface
                ),
                render=lambda: _render_agents_md(
                    manifest, codex_materialization, runtime_layout
                ),
            )
        )

    if "config" in selected:
        config_surface = _require_mapping(
            codex_materialization["config_surface"], "config_surface"
        )
        add_surface(
            _surface_from_render(
                relative_path=_require_string(config_surface["path"], "config path"),
                concept_family="config",
                maintenance_mode=_maintenance_mode_for_entry(
                    codex_materialization, "config", config_surface
                ),
                render=lambda: _render_config_toml(
                    manifest, capacity, codex_materialization, runtime_layout
                ),
            )
        )

    if "roles" in selected:
        for role in roles:
            role_id = _require_string(role["id"], "role id")
            parent_agent = parent_by_role[role_id]
            add_surface(
                _surface_from_render(
                    relative_path=runtime_layout.role_path(role_id).as_posix(),
                    concept_family="roles",
                    maintenance_mode=_maintenance_mode_for_entry(
                        codex_materialization, "roles", role
                    ),
                    render=lambda role=role, parent_agent=parent_agent: (
                        _render_role_projection(
                            repo_root,
                            manifest,
                            role,
                            parent_agent,
                            runtime_layout,
                        )
                    ),
                )
            )

    if "agents" in selected:
        for agent in parent_agents:
            agent_id = _require_string(agent["id"], "parent agent id")
            add_surface(
                _surface_from_render(
                    relative_path=runtime_layout.agent_path(agent_id).as_posix(),
                    concept_family="agents",
                    maintenance_mode=_maintenance_mode_for_entry(
                        codex_materialization, "parent_agents", agent
                    ),
                    render=lambda agent=agent: _render_agent_descriptor(
                        repo_root, manifest, agent, agent_kind="parent"
                    ),
                )
            )
        for specialist in specialists:
            specialist_id = _require_string(specialist["id"], "specialist id")
            add_surface(
                _surface_from_render(
                    relative_path=runtime_layout.agent_path(specialist_id).as_posix(),
                    concept_family="agents",
                    maintenance_mode=_maintenance_mode_for_entry(
                        codex_materialization, "specialists", specialist
                    ),
                    render=lambda specialist=specialist: _render_agent_descriptor(
                        repo_root, manifest, specialist, agent_kind="specialist"
                    ),
                )
            )

    if "modes" in selected:
        for mode in modes:
            mode_id = _require_string(mode["id"], "mode id")
            add_surface(
                _surface_from_render(
                    relative_path=runtime_layout.mode_path(mode_id).as_posix(),
                    concept_family="modes",
                    maintenance_mode=_maintenance_mode_for_entry(
                        codex_materialization, "modes", mode
                    ),
                    render=lambda mode=mode: _render_mode_surface(
                        repo_root, manifest, mode, role_display_names
                    ),
                )
            )

    if "protocols" in selected:
        for protocol in protocols:
            protocol_id = _require_string(protocol["id"], "protocol id")
            add_surface(
                _surface_from_render(
                    relative_path=runtime_layout.protocol_path(protocol_id).as_posix(),
                    concept_family="protocols",
                    maintenance_mode=_maintenance_mode_for_entry(
                        codex_materialization, "protocols", protocol
                    ),
                    render=lambda protocol=protocol: _render_protocol_surface(
                        repo_root, manifest, protocol, role_display_names
                    ),
                )
            )

    if "skills" in selected:
        for skill in skills:
            skill_id = _require_string(skill["id"], "skill id")
            add_surface(
                _surface_from_render(
                    relative_path=runtime_layout.skill_path(skill_id).as_posix(),
                    concept_family="skills",
                    maintenance_mode=_maintenance_mode_for_entry(
                        codex_materialization, "skills", skill
                    ),
                    render=lambda skill=skill: _render_skill_surface(
                        repo_root, manifest, skill
                    ),
                )
            )

    generated.sort(key=lambda surface: surface.relative_path.as_posix())
    human_managed.sort(key=lambda surface: surface.relative_path.as_posix())
    return MaterializationPlan(
        generated=tuple(generated),
        human_managed=tuple(human_managed),
    )


def _check_human_surface(path: Path) -> list[str]:
    if path.exists():
        return []
    return [
        "[materialize_codex_runtime] Missing human-managed declared surface: "
        f"{path.as_posix()}"
    ]


def _check_plan(repo_root: Path, plan: MaterializationPlan) -> list[str]:
    problems: list[str] = []
    for surface in plan.generated:
        if surface.content is None:
            raise ValueError("Generated surface unexpectedly had no content")
        problems.extend(
            _compare_expected(repo_root / surface.relative_path, surface.content)
        )
    for surface in plan.human_managed:
        problems.extend(_check_human_surface(repo_root / surface.relative_path))
    return problems


def check_materialization_plan(
    repo_root: Path, selected_surfaces: set[str] | None = None
) -> tuple[MaterializationPlan, list[str]]:
    """Build and validate the selected materialization surfaces."""

    plan = build_materialization_plan(repo_root, selected_surfaces)
    return plan, _check_plan(repo_root, plan)


def _write_plan(repo_root: Path, plan: MaterializationPlan) -> tuple[int, list[str]]:
    written = 0
    issues: list[str] = []
    for surface in plan.generated:
        if surface.content is None:
            raise ValueError("Generated surface unexpectedly had no content")
        if _write_if_changed(repo_root / surface.relative_path, surface.content):
            written += 1
    for surface in plan.human_managed:
        issues.extend(_check_human_surface(repo_root / surface.relative_path))
    return written, issues


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Materialize the Context Atlas Codex runtime surface from the "
            "authoritative manifest, bindings, and canon docs."
        )
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root to read from and write to (default: current directory).",
    )
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument(
        "--write",
        action="store_true",
        help="Write the selected generated surfaces back to disk.",
    )
    mode_group.add_argument(
        "--check",
        action="store_true",
        help="Check that the committed selected generated surfaces match expected output.",
    )
    parser.add_argument(
        "--surface",
        action="append",
        choices=sorted(_SUPPORTED_SURFACES),
        help=(
            "Limit work to one or more concept families. Defaults to all "
            "supported surfaces when omitted."
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    selected_surfaces = set(args.surface) if args.surface else set(SUPPORTED_SURFACES)
    plan = build_materialization_plan(repo_root, selected_surfaces)

    if args.check:
        _, problems = check_materialization_plan(repo_root, selected_surfaces)
        if problems:
            for problem in problems:
                print(problem, file=sys.stderr)
            return 1
        print(
            "[materialize_codex_runtime] All selected generated Codex surfaces are in sync."
        )
        return 0

    written, issues = _write_plan(repo_root, plan)
    if issues:
        for issue in issues:
            print(issue, file=sys.stderr)
        return 1
    print(
        "[materialize_codex_runtime] Wrote "
        f"{written} generated surface(s) across {len(selected_surfaces)} selected family(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
