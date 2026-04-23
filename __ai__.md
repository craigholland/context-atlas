# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 709dcc3c6ff05f9358111025d2c611b702eb5b98
- timestamp_utc: 2026-04-22T19:21:07Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
## Scope
- folder: .
- included:
  - "README.md"
  - "CONTRIBUTING.md"
  - "pyproject.toml"
  - ".gitignore"
  - ".env.example"
  - "__ai__.md"
  - "__ai__.template.md"
  - ".githooks/**"
- excluded:
  - "docs/**"
  - "src/**"
  - "tests/**"
  - "scripts/**"
  - ".github/workflows/**"
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Defines repo-level operational rules that apply before recommending a push or merge.
- Connects the local `__ai__.md` contract system to a single repo-wide preflight entrypoint.
- Establishes the repo-wide boundary between root policy, nearer folder contracts, authoritative docs, and generated runtime assets.
- Keeps the visible package, contributor, and runtime-knob surfaces aligned at the repo root.
- Makes planning archives, release notes, and generated runtime materializations discoverable without turning the root owner file into a second changelog.
- Provides the contributor on-ramp for using the ontology system correctly when adding new project documents.

## Architectural Rules
- Before recommending a push or merge, contributors should run `py -3 scripts/preflight.py`.
- The tracked pre-push hook under `.githooks/pre-push` is the preferred enforcement mechanism for local pushes.
- Repo-root policy should stay thin: package/runtime behavior belongs in `src/`, enforcement logic in `scripts/`, and reusable architecture canon in `docs/`.
- The root owner file should express repo-wide operational rules and delegate folder-specific rules to nearer `__ai__.md` files rather than duplicating them.
- Repo-level and layer-level owner files should stay curated current-state contracts; file-specific nuance belongs in `File Index`, future caveats in `Known Gaps / Future-State Notes`, and boundary assumptions in `Cross-Folder Contracts`.
- The repo's logging/message surface is the direct `LogMessage` pattern with stable event-name fields; contributors should not reintroduce a separate `domain/events` layer unless the authoritative docs change first.
- The repo's canonical domain-artifact standard is now frozen Pydantic models with explicit domain validation; contributors should not introduce new non-trivial dataclass artifacts without first updating the authoritative docs and local owner files.
- The repo's public policy-surface standard is now also validated Pydantic models; the remaining dataclasses should be explicitly justified as private helpers or script-local records.
- The current authoritative split is stable: `docs/Authoritative/Canon/` holds portable cross-project canon, and `docs/Authoritative/Identity/` holds Context Atlas-specific bindings.
- Active planning work belongs under `docs/Planning/`, completed planning stacks belong under `docs/Planning/completed/`, and implementation work should honor the planning canon's task-level feature-PR review gate unless an explicit parallelization decision says otherwise.
- Small follow-up planning tasks may live directly under `docs/Planning/` when they are shaping a bounded documentation, governance, or workflow refactor without needing a full Epic/Story stack.
- `docs/Planning/013_Cleanup/`: is the current active cleanup Epic surface, and future cleanup planning should extend that numbered stack rather than reintroducing a second top-level cleanup product definition; as the Epic is decomposed, its downstream `Stories/` and `Stories/Tasks/` surfaces should be treated as part of that same live stack.
- `docs/Planning/013_Cleanup/Stories/` and `docs/Planning/013_Cleanup/Stories/Tasks/`: may land incrementally on Story branches while the Cleanup Epic PR is still open, but those downstream docs should still be treated as one stacked planning surface rather than as independent planning horizons.
- The curated product-facing package surface is `context_atlas.api`; root docs and examples should prefer that starter namespace unless they are deliberately teaching internal architecture.
- The root README should act as the repo's map and multi-audience routing surface; deeper product walkthrough and workflow-tour content should usually live in linked guides under `docs/Guides/` rather than continuing to accumulate in the root file.
- The root README and top-level docs indexes should distinguish four repo-edge concerns cleanly: product evaluation/use, contributor work, generated-runtime inspection, and `__ai__` governance. They should not force those concerns back into one blended "start here" path.
- `docs/README.md` should act as a documentation route splitter rather than as a second root README, and `docs/Guides/README.md` should stay explicitly product-facing instead of silently inheriting contributor/runtime/governance duties.
- The three main entry surfaces should keep distinct roles visible in their own copy: `README.md` is the repo map, `docs/README.md` is the documentation route splitter, and `docs/Guides/README.md` is the product guide hub.
- Product-facing routing surfaces should state dependency truth plainly: `.codex/`, `.agents/skills/`, and `__ai__.md` are real repo layers, but they are not prerequisites for evaluating Atlas as a library or following the current guide path.
- Docs and Identity binding surfaces that explain generated runtime materialization should present themselves as contributor/runtime layers explicitly, and they should point product evaluators back toward `docs/Guides/` rather than behaving like required setup steps.
- `docs/Planning/013_Cleanup/Stories/`: Story 2 currently carries a settled audience-routing contract: the repo edge should distinguish product use, generated-runtime inspection, Canon/Identity architecture reading, and `__ai__` governance as separate reader jobs rather than one blended route.
- `docs/Planning/013_Cleanup/Stories/`: Story 2 also carries a settled dependency-truth contract: `.codex/`, `.agents/skills/`, and `__ai__.md` remain discoverable repo layers, but product evaluators should be routed toward guides/examples first and should not be told those layers are prerequisites for using Atlas as a library.
- Product-facing docs, guides, example READMEs, and `.env.example` should stay aligned around one truthful onboarding story, should not imply automatic `.env` loading, and should not introduce Windows-only operator guidance without a Linux/macOS analog.
- Release-prep changes should keep `README.md`, `pyproject.toml`, `src/context_atlas/__init__.py`, `tests/test_cli.py`, and the current note under `docs/Release/` aligned to the same version.
- Generated Codex runtime assets under `.codex/` and `.agents/skills/` are downstream of the manifest, bindings, templates, and repo-owned generator; durable semantic edits belong upstream first, then the runtime surface should be regenerated.
- Repo-level preflight and CI should fail when that generated runtime surface drifts from the manifest-driven materialization plan; contributors changing those authoritative inputs should regenerate and re-check before push.

## Allowed Dependencies
- may depend on:
  - repository metadata files
  - repo-owned scripts and hooks
- must not depend on:
  - folder-specific rules being restated here when a nearer owner file already governs them
  - hidden local-only push behavior that is not represented by tracked scripts or hooks

## Public API / Key Exports
- `README.md`:
  - repo-facing entrypoint for product framing, audience routing, release context, and links into deeper guide or architecture surfaces
- `pyproject.toml`:
  - project metadata, author info, Python floor, dev-tool declarations, and installable starter script
- `CONTRIBUTING.md`:
  - root contributor on-ramp for choosing the right document class, template, and destination
- `__ai__.template.md`:
  - baseline authoring template for local contract files
- `.env.example`:
  - tracked example environment surface for supported runtime knobs
- `__ai__.md`:
  - repo-level operational contract for preflight and push readiness
- `.githooks/pre-push`:
  - tracked pre-push hook that runs repo preflight

## File Index
- `README.md`:
  - responsibility: acts as the repo's top-level map and multi-audience entry surface without becoming the full walkthrough for every workflow and subsystem
  - invariants:
    - should keep the primary product-evaluator path explicit
    - should preserve a short mental-model anchor near the top
    - should route deeper walkthrough readers into guide material instead of carrying every tour-level section in full
    - should distinguish shipped-release review from evolving-branch review when suggesting AI-assisted critique paths
    - any playful review prompt should remain clearly secondary to the serious route guidance and should still ask for substantive criticism
    - its `Status` section should stay aligned with the current shipped release note and should describe the top-level product story without collapsing back into a second system tour
- `pyproject.toml`:
  - responsibility: defines package metadata and repo-local developer tool dependencies
  - invariants:
    - Python floor here should match active CI and local preflight assumptions
    - runtime validation libraries added here should correspond to real package behavior, not speculative future plans
- `CONTRIBUTING.md`:
  - responsibility: gives contributors one clear path into the ontology/template system before they author new repo documents
  - invariants:
    - should point to the current ontology canon rather than restating a parallel document-class system
    - should keep Canon versus Identity placement guidance explicit for contributors adding authoritative docs
- `__ai__.template.md`:
  - responsibility: provides the reusable authoring shape for local owner files
  - footguns:
    - changes here should be reflected intentionally in validator expectations and local owner files
- `.env.example`:
  - responsibility: makes the supported environment-backed runtime settings visible at the repo root
  - invariants:
    - keys here should reflect the actual environment surface supported by infrastructure config loaders
    - assembly and memory default knobs should stay intentionally small and clearly operator-facing
- `src/context_atlas/domain/models/*.py`:
  - responsibility: define the canonical Pydantic-backed artifacts consumed across the package
  - invariants:
    - non-trivial canonical artifacts should remain frozen Pydantic models rather than drifting back to mixed constructor styles
    - inner metadata maps should stay immutable so packet/source state remains trustworthy once assembled
- `__ai__.md`:
  - responsibility: states repo-wide operational rules before push or merge
  - invariants:
    - must call out the canonical preflight entrypoint
- `.githooks/pre-push`:
  - responsibility: executes repo preflight before local pushes when hooks are installed
  - footguns:
    - tracked hook file is inert until `core.hooksPath` points at `.githooks`

## Known Gaps / Future-State Notes
- The current root contract is strong on push readiness and repo governance, but it is still thinner on release/versioning policy, packaging/publication workflow, and post-merge operational automation.
- The tracked Git hook remains opt-in per clone until local setup tooling configures `core.hooksPath` automatically.
- The supported runtime-knob surface is intentionally narrow; many ranking, memory, and slot-level constants remain internal implementation details rather than env-backed settings.
- The flagship repository workflow is still governed-docs-first. It does not yet represent full code crawling, git/history awareness, issue-system ingestion, or broader repository connector coverage.
- The mixed-source technical-builder workflow still assumes already-fetched record payloads. Atlas shapes and governs those payloads, but it does not yet own database, vector-store, or API client integration.
- The low-code workflow is still a small preset-driven wrapper over the shared engine, not a broader no-code product surface with connector management or hidden config loading.
- The current MVP proof set is evidence-backed and sufficient for the `MVP Ready` recommendation, but it is still limited to the tracked local scenarios under the three supported workflows rather than a broader external-service or production-style evaluation matrix.
- Product-facing docs must continue to stay synchronized across the root README, `docs/Guides/`, `examples/README.md`, and `.env.example`; drift between those surfaces remains an ongoing maintainability risk.
- Release-history documentation now has an in-repo home, but the repo still does not have a fuller release-process canon for branching, cutover, publication cadence, or post-release follow-up.
- The README should not become the full walkthrough for every workflow and subsystem;

## Cross-Folder Contracts
- `scripts/`: root policy delegates actual enforcement logic to repo-owned scripts; changing script entrypoints should update this contract.
- `docs/Authoritative/Canon/AgenticDevelopment/`: roles, protocols, runtime-capacity semantics, materialization rules, drift vocabulary, validation expectations, and governed change paths should stay portable here and flow downward into project bindings rather than being restated in planning or runtime docs.
- `docs/Authoritative/Canon/RepoManagement/`: repository-principal, authorization, operation-family, branch-target, and audit-identity semantics should stay portable here and flow downward into project bindings rather than being restated in runtime docs.
- `docs/Exploratory/`: speculative investigations and pickup notes may live here, but they must stay explicitly non-binding and must not become backdoor authority over Canon, Identity, or Planning surfaces.
- `docs/Authoritative/Canon/AgenticDevelopment/__ai__.md` and `docs/Authoritative/Canon/RepoManagement/__ai__.md`: the nearest owner files for those canon surfaces should stay aligned when Story-level governance or validation expectations change.
- `.codex/` and `.agents/skills/`: the generated runtime surface should stay downstream of the materialization manifest and Codex binding docs; changes there should be treated as derived refresh work, not as the authoritative place to redefine roster, mode, protocol, or skill meaning.
- `docs/Planning/`: active future-planning work should live here until it is complete, and `docs/Planning/completed/` should hold the historical MVP, Agentic, and Hardening stacks once they are no longer the active future-planning surface. Small active task plans may also live at the top level here when they are intentionally narrower than a full Epic/Story decomposition.
- `docs/Guides/`: product-facing setup help, workflow walkthroughs, and system-tour material should live here so the root README can stay the map instead of absorbing the whole walkthrough layer.
- `src/context_atlas/`: preflight should prove repo readiness without redefining package-layer rules that belong to nearer owner files.
- `src/context_atlas/infrastructure/`: supported environment variable keys in config loaders should stay mirrored in `.env.example`.
- `src/context_atlas/infrastructure/`: assembly and memory default settings plus structured observability helpers should not grow new env knobs without updating the repo root surface.
- `.github/workflows/`: CI should mirror the local preflight closely enough that GitHub failures are usually reproducible before push.
- `.codex/` and `.agents/skills/`: generated Codex runtime assets should remain both regenerable through `scripts/materialize_codex_runtime.py` and drift-checkable through `scripts/check_codex_materialization.py`.

## Verification Contract
```yaml
steps:
  - name: validate_root_owner
    run: |
      py -3 scripts/validate_ai_docs.py --repo-root . --files __ai__.md

  - name: import_boundaries
    run: |
      py -3 scripts/check_import_boundaries.py --repo-root . --config scripts/import_boundary_rules.toml

  - name: test_and_typecheck
    run: |
      py -3 -m ruff check .
      py -3 -m ruff format --check .
      py -3 -m mypy src
      py -3 -m pytest
```

