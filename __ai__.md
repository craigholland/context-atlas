# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 53a11d1fa71fcd3ce74c066cf24e1aca8299f469
- timestamp_utc: 2026-04-19T23:06:13Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
## Scope
- folder: .
- included:
  - "README.md"
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
- Establishes hook and packaging expectations for the standalone Context Atlas library repo.
- Keeps the tracked example environment surface aligned with supported runtime settings.
- Makes the visible runtime knob surface reviewable at the repo root as ranking, compression, memory, and observability defaults begin to grow.
- Treats runtime config dependencies as part of the visible package contract when infrastructure moves from ad hoc parsing to validated libraries like Pydantic.
- Treats canonical domain artifacts as part of the visible package contract when the domain model standard shifts from starter dataclasses to frozen Pydantic models.
- Treats public policy request/result/configuration objects as part of the same modeling contract so the repo does not drift back to mixed boundary styles.

## Architectural Rules
- Before recommending a push or merge, contributors should run `py -3 scripts/preflight.py`.
- The tracked pre-push hook under `.githooks/pre-push` is the preferred enforcement mechanism for local pushes.
- Repo-root policy should stay thin: package/runtime behavior belongs in `src/`, enforcement logic in `scripts/`, and reusable architecture canon in `docs/`.
- The root owner file should express repo-wide operational rules and delegate folder-specific rules to nearer `__ai__.md` files rather than duplicating them.
- When hardening slices materially change governed package or test contracts, this root owner file should still be updated alongside the nearer owner files so repo-level freshness checks remain honest.
- The repo's logging/message surface is the direct `LogMessage` pattern with stable event-name fields; contributors should not reintroduce a separate `domain/events` layer unless the authoritative docs change first.
- The repo's canonical domain-artifact standard is now frozen Pydantic models with explicit domain validation; contributors should not introduce new non-trivial dataclass artifacts without first updating the hardening plan and local owner files.
- The repo's public policy-surface standard is now also validated Pydantic models; the remaining dataclasses should be explicitly justified as private helpers or script-local records.
- The authoritative Craig Architecture docs now explicitly treat decomposition depth, folder flatness, file size, and helper-sprawl as real architectural governance concerns, not just style preferences.
- The authoritative architecture canon now includes `docs/Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md` as the detailed supplement for planning mechanics, decomposition sanity checks, and code-shape governance.
- The planning/decomposition canon now also treats branch naming as part of the delivery model: task-level feature branches should reflect the Task, and Codex PR-slice branches should reflect the Story, Task, and PR slice.
- The planning/decomposition canon now also treats the task-level feature PR as the main review gate: contributors should finish the Task's planned slice branches, run preflight on the feature branch, request `@codex review`, resolve findings there, and only then hand the feature PR to a human reviewer.
- Contributors should not start the next Task until the current task-level feature PR has been reviewed, fixed if needed, and merged, unless an explicit parallelization decision has been made.
- MVP planning work should now be expected to decompose from Epic to Stories to Tasks to PR plans, and those PR plans should identify expected new files, expected updated files, and relevant `__ai__.md` updates.
- The planning stack under `docs/Planning/` should include an orienting README, and Story docs should carry a lightweight Definition Of Done so review expectations stay visible before implementation starts.
- MVP Task PR-plan docs should carry a basic `Task Status` field using `PLANNED`, `WORKING`, or `IMPLEMENTED` so task-level progress remains visible before contributors open individual PR-plan slices.
- There is no currently active MVP task; Story 7 is complete and the current baseline is the merged `MVP Ready` recommendation plus its standing proof scenarios.
- The Task 7.3 configuration-surface decision is now part of the active proof baseline: the supported env-backed surface includes `CONTEXT_ATLAS_DEFAULT_MEMORY_BUDGET_FRACTION`, while ranking authority tables, memory-scoring semantics, and canonical slot identifiers remain internal by design.
- The architecture canon under `docs/Authoritative/Architecture/` should include a directory-level README so contributors can orient to the full Craig Architecture set before jumping into individual supplements.
- The current MVP-supported package surface is now centered on `context_atlas.api`; repo-level docs and examples should prefer that curated starter namespace over deep internal module paths unless they are deliberately teaching architectural seams.
- Product-facing repo guidance should stay aligned around one visible golden path from install to configure to assemble to inspect; contributors should not let root docs, examples, and runtime-knob docs drift into separate onboarding stories.
- The getting-started guide and starter context-flow example are now part of that visible onboarding path; contributors should keep them aligned with the supported starter imports, runtime knobs, and inspection surfaces.
- The starter context-flow example is now the recommended first-run path, while the smoke script is secondary; root guidance should preserve that distinction instead of presenting both as equal onboarding surfaces.
- The recommended first-run story should prefer the editable-install path and the quieter starter example output; repo-local `PYTHONPATH` usage and smoke scripts should stay secondary and clearly labeled.
- Product-facing docs should not imply that `.env.example` or a copied `.env` file is loaded automatically; the current runtime settings loader reads the live process environment only.
- Product-facing docs should keep the supported env-backed surface intentionally narrow and should not imply that every starter constant in `domain/policies/` or `services/` is automatically a public runtime knob.
- The guides under `docs/Guides/` should stay aligned with the actual runnable example boundaries, including which workflows support one-shot budget overrides or proof-artifact emission and which ones do not.
- The technical-builder documents-plus-database workflow is now a first-class product-facing guide path alongside the starter and repository workflows; repo-facing docs should keep its already-fetched-record boundary and shared runtime-knob story aligned across README, examples, and guide docs.
- The starter inspection story should surface packet and trace views as derived renderers under `context_atlas.rendering`, not as alternate canonical models or prompt-first strings.
- The first product-facing packet inspection surface should emphasize selected sources, retained memory, budget state, and compression without requiring direct model dumps.
- The first trace inspection surface should emphasize ordered decisions, exclusions, transformations, and trace metadata rather than raw `model_dump()` output.

## Allowed Dependencies
- may depend on:
  - repository metadata files
  - repo-owned scripts and hooks
- must not depend on:
  - folder-specific rules being restated here when a nearer owner file already governs them
  - hidden local-only push behavior that is not represented by tracked scripts or hooks

## Public API / Key Exports
- `pyproject.toml`:
  - project metadata, Python floor, and dev-tool declarations
- `__ai__.template.md`:
  - baseline authoring template for local contract files
- `.env.example`:
  - tracked example environment surface for supported runtime knobs
- `__ai__.md`:
  - repo-level operational contract for preflight and push readiness
- `.githooks/pre-push`:
  - tracked pre-push hook that runs repo preflight

## File Index
- `pyproject.toml`:
  - responsibility: defines package metadata and repo-local developer tool dependencies
  - invariants:
    - Python floor here should match active CI and local preflight assumptions
    - runtime validation libraries added here should correspond to real package behavior, not speculative future plans
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

## Cross-Folder Contracts
- `scripts/`: root policy delegates actual enforcement logic to repo-owned scripts; changing script entrypoints should update this contract.
- `src/context_atlas/`: preflight should prove repo readiness without redefining package-layer rules that belong to nearer owner files.
- `src/context_atlas/infrastructure/`: supported environment variable keys in config loaders should stay mirrored in `.env.example`.
- `src/context_atlas/infrastructure/`: assembly and memory default settings plus structured observability helpers should not grow new env knobs without updating the repo root surface.
- `.github/workflows/`: CI should mirror the local preflight closely enough that GitHub failures are usually reproducible before push.

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
