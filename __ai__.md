# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 18dbfa5fc5381bc73bbe1f0e96e843c01010231b
- timestamp_utc: 2026-04-19T04:37:02Z
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
- The architecture canon under `docs/Authoritative/Architecture/` should include a directory-level README so contributors can orient to the full Craig Architecture set before jumping into individual supplements.
- The current MVP-supported package surface is now centered on `context_atlas.api`; repo-level docs and examples should prefer that curated starter namespace over deep internal module paths unless they are deliberately teaching architectural seams.
- Product-facing repo guidance should stay aligned around one visible golden path from install to configure to assemble to inspect; contributors should not let root docs, examples, and runtime-knob docs drift into separate onboarding stories.
- The getting-started guide and starter context-flow example are now part of that visible onboarding path; contributors should keep them aligned with the supported starter imports, runtime knobs, and inspection surfaces.
- The starter context-flow example is now the recommended first-run path, while the smoke script is secondary; root guidance should preserve that distinction instead of presenting both as equal onboarding surfaces.
- The recommended first-run story should prefer the editable-install path and the quieter starter example output; repo-local `PYTHONPATH` usage and smoke scripts should stay secondary and clearly labeled.
- Product-facing docs should not imply that `.env.example` or a copied `.env` file is loaded automatically; the current runtime settings loader reads the live process environment only.
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
- The current root contract focuses on push readiness and repo governance rather than deeper release automation.
- The hook path still needs to be configured locally in each clone unless automation or contributor setup scripts do that explicitly.
- The current feature branch is now in an implementation-hardening phase documented under `docs/Planning/Initial-Implementation-Hardening-PR-Plan.md`; follow-up slices should keep repo-level push rules aligned with those contract changes.
- The original conversion plan has been aligned to the direct `LogMessage` surface so the branch roadmap no longer implies a separate event-enum package.
- The current hardening phase now includes a Pydantic-first canonical-model standard; remaining non-trivial dataclasses outside the core model package should be treated as intentional follow-up debt until converted.
- The current hardening phase now also covers public policy surfaces; any remaining dataclasses should now be explainable as deliberate keeps rather than unfinished boundary work.
- The current hardening phase now also covers outer composition of those policy surfaces; supported env/settings knobs should match the real starter policy constructors used by infrastructure factories.
- The repo-root README should now describe the project as post-bootstrap: the architecture/governance foundation is in place and the current work is starter-implementation hardening rather than pure architectural setup.
- The repo-root README should not use absolute paths to the repo.
- The root README, `examples/README.md`, and `.env.example` should now tell a consistent MVP onboarding story for the starter flow rather than requiring users to reconstruct that path from internal modules.
- `docs/Guides/getting_started.md` and `examples/starter_context_flow.py` should now tell the same starter story as the root README and example index.
- That starter story should now use `python` after venv activation rather than `py -3`, and it should describe `.env.example` as a reference surface rather than an auto-loaded dotenv mechanism.
- The repo now includes a planning stack under `docs/Planning/MVP/` that decomposes MVP work from an Epic document into Story docs and then into task-level PR plans.
- The planning stack now also includes `docs/Planning/README.md` plus lightweight Definition Of Done sections in the MVP Story docs so contributors can orient without inferring the planning model from individual files.
- The planning stack now also expects task execution to pause at the feature-PR review boundary rather than rolling directly into the next Task after slice branches merge.
- When contributors edit governed documents, they should review the front YAML metadata as part of the same change rather than treating it as static boilerplate; `summary`, `last_reviewed`, `tags`, `related`, and when relevant `status` or `supersedes`, should stay aligned with the document's current role.
- The reusable Craig Architecture canon now also includes `docs/Authoritative/Architecture/README.md` so the documentation root can point contributors to the architecture set as a coherent whole rather than only to individual files.
- The architecture canon now expects planning work to surface shape risks early, including duplicate file creation, hotspot files, folder flatness, large-file growth, and junk-drawer helper chains.
- The planning/decomposition supplement now also defines preferred Git branch naming that mirrors the Task and PR-slice hierarchy rather than broad work themes.
- The starter API story has now introduced `context_atlas.api` as the curated MVP namespace, while the package root remains intentionally thin and stable subpackage imports remain valid for architecture-oriented documentation.
- The starter API story now also includes a smoke example under `examples/` that should continue to validate the curated API rather than drift back to deep internal imports.
- Story 2 Task 2.4 is now the active task-level feature branch and should keep mixed-source support aligned with Craig Architecture boundaries.
- That task should keep canonical semantics and source-family-agnostic meaning inward while pushing source-specific parsing, shaping, and provenance mechanics outward into adapters.
- PR A of that task should audit the current mixed-source path for boundary leaks, especially adapter-local semantics or source-specific mechanics drifting into shared canonical models.
- That audit is now hardening around one explicit rule: adapters should cross into canonical sources through one resolved semantic profile instead of restating semantic fields piecemeal or echoing source meaning through adapter-local tags and metadata.
- The latest Task 2.4 slice now uses that rule as the mixed-source boundary baseline, so follow-up PRs should preserve provenance-rich outward adapters without reintroducing semantic duplication in source tags or metadata.
- PR B of that task should refactor any confirmed leaks so services stay source-family-agnostic, canonical source meaning stays domain-owned, and adapters stay outward and translation-focused.
- PR C of that task should reinforce the intended boundary through docs, examples, and owner-file guidance so future mixed-source work does not reopen the same architectural seams.
- The root README should keep describing structured records as adapter-facing inputs supplied by outer integration code rather than as evidence that Atlas owns database access.

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
