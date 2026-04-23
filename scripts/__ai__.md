# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 1cd36070ddd5b129060eebef7d3107d77900d885
- timestamp_utc: 2026-04-22T15:51:45Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
## Scope
- folder: scripts
- included:
  - "*.py"
  - "*.toml"
- excluded:
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Holds repository-owned automation scripts that operationalize the local `__ai__.md` contract system, preflight checks, and architecture boundary enforcement.
- Keeps CI and local push enforcement logic in plain Python so it remains inspectable and adaptable by both humans and AI contributors.
- Centralizes architecture-adjacent automation rather than scattering it across workflow YAML and local shell fragments.
- Keeps the local preflight close to GitHub `verify-ai-contracts` behavior so branch pushes usually fail locally before they fail remotely.
- Treats proof-capture tooling as repo-owned automation too, so MVP evidence packaging remains reproducible and reviewable.

## Architectural Rules
- Scripts in this folder should prefer Python standard library implementations unless a dependency is clearly justified.
- These scripts enforce structure, freshness heuristics, contract execution, preflight, and import-boundary rules; they must not claim to prove full architectural correctness.
- Keep repository paths, governed roots, and branch assumptions explicit and configurable rather than hidden in hardcoded globals where practical.
- Diff-based scripts should prefer `development` first when discovering a comparison base, then fall back to `main` and older defaults when needed.
- Avoid project-runtime imports from `src/context_atlas` unless a script truly needs them; most scripts here should operate on files, git state, and declared contracts.
- `preflight.py` is the canonical local gate before push or merge; other scripts should support it rather than compete with it.
- Small private dataclasses are acceptable here when they are local rule/config carriers for the script itself and not part of the package runtime surface.
- User-facing script help and failure messages should prefer portable command guidance first and may mention Windows-specific launcher variants as secondary notes when helpful.
- Repo-owned Codex runtime materialization should stay manifest-driven and deterministic here rather than being hidden in ad hoc prompt steps or one-off shell refresh commands.

## Allowed Dependencies
- may depend on:
  - Python standard library
  - git via subprocess
- must not depend on:
  - `context_atlas` runtime modules for simple repository checks
  - hidden shell aliases or non-portable environment assumptions

## Public API / Key Exports
- `validate_ai_docs.py`:
  - `main`: validates local `__ai__.md` structure against the canonical section shape
- `check_ai_docs.py`:
  - `main`: checks for likely stale or missing owner-file updates in governed roots
- `ai_verify_contracts.py`:
  - `main`: executes declared Verification Contract steps from affected owner files
- `update_last_verified.py`:
  - `main`: rewrites `Last Verified (CI)` metadata in affected owner files
- `check_import_boundaries.py`:
  - `main`: enforces AST-based Python import-boundary rules from TOML config
- `preflight.py`:
  - `main`: runs the repo-wide push/merge preflight
- `check_codex_materialization.py`:
  - `main`: verifies that committed `.codex/` and `.agents/skills/` assets still match the manifest-driven runtime plan
- `materialize_codex_runtime.py`:
  - `build_materialization_plan`: renders the declared Codex runtime surfaces from manifest and authoritative docs
  - `check_materialization_plan`: validates generated and human-managed Codex surfaces against the current manifest-driven plan
  - `main`: writes or checks the generated `.codex/` and `.agents/skills/` surfaces
- `install_git_hooks.py`:
  - `main`: points local git hook execution at the tracked `.githooks` directory

## File Index
- `validate_ai_docs.py`:
  - responsibility: validates structural conformance of local owner files
  - invariants:
    - structural validator only, not semantic reviewer
- `check_ai_docs.py`:
  - responsibility: flags likely stale or ownerless governed files
  - footguns:
    - heuristic output is not proof that prose is correct or incorrect
  - invariants:
    - fallback diff refs should prefer `development` before `main`
- `ai_verify_contracts.py`:
  - responsibility: runs local Verification Contract steps from owner files
  - invariants:
    - must prefer PowerShell on Windows so repository contracts stay consistent with local desktop execution
    - must keep Linux/macOS analogs visible whenever owner-file Verification Contract steps rely on Windows-specific launcher or environment syntax
- `update_last_verified.py`:
  - responsibility: updates `Last Verified (CI)` metadata after successful verification
  - footguns:
    - metadata updates do not replace semantic review
- `check_import_boundaries.py`:
  - responsibility: enforces configured Python layer dependency rules
  - depends_on:
    - `import_boundary_rules.toml`
  - invariants:
    - `BoundaryRule` and `BoundaryConfig` may remain private dataclasses because they are script-local utility state, not package-facing validated models
- `preflight.py`:
  - responsibility: runs the canonical local preflight before push or merge
  - depends_on:
    - dev tools declared in `pyproject.toml`
    - `validate_ai_docs.py`
    - `check_ai_docs.py`
    - `check_codex_materialization.py`
    - `check_import_boundaries.py`
    - `ai_verify_contracts.py`
  - invariants:
    - should stay as close as practical to the remote `verify-ai-contracts` and `ci` workflow behavior
- `check_codex_materialization.py`:
  - responsibility: performs the dedicated manifest-versus-runtime drift check for Codex materialization
  - depends_on:
    - `materialize_codex_runtime.py`
  - invariants:
    - should verify both generated and declared-human surfaces through the shared manifest-driven plan rather than reimplementing Codex layout assumptions
    - should stay cheap enough to run inside local preflight and CI on every relevant branch push
- `materialize_codex_runtime.py`:
  - responsibility: deterministically materializes the Codex runtime surface from the authoritative manifest, bindings, and canon docs
  - invariants:
    - `maintenance_mode` must remain upstream-owned by `materialization_manifest.yaml`
    - `mixed` must fail loudly until an explicit manual-block preservation format exists
    - generated runtime files must be reproducible from repo state alone without hidden local prompts
    - document-cache reuse must stay scoped by repository root and current file state so repeated runs cannot bleed content across repos or stale edits
    - generated and checked runtime paths must derive from manifest-declared `runtime_root`, `skills_root`, and surface paths instead of assuming fixed `.codex` or `.agents` locations
    - heading-block extraction must stop nested sections at the next heading of the same or higher level so generated mode and protocol surfaces cannot absorb later constraints or non-goal bullets into runtime-facing sections
- `install_git_hooks.py`:
  - responsibility: configures `git` to use the tracked `.githooks` directory
- `import_boundary_rules.toml`:
  - responsibility: declares current `context_atlas` layer boundary rules for the import checker

## Known Gaps / Future-State Notes
- This folder still focuses on preflight, contract enforcement, and proof packaging rather than broader release, publication, or contributor-environment automation.
- Some enforcement logic still assumes local git/diff semantics and repository-specific layout rather than a more abstract change-detection model.
- If script scope continues to widen, additional nested owner files or directory splits may be needed so one contract does not cover too many unrelated automation concerns.

## Cross-Folder Contracts
- `src/context_atlas/`: scripts may validate local contracts and import boundaries there, but must not redefine the package's semantic rules.
- `tests/`: test execution is part of several verification contracts; script changes that alter invocation assumptions should update test folder guidance too.
- `.github/workflows/`: workflows should call these repo-owned scripts rather than reimplement the same logic inline in YAML.
- `.github/workflows/`: local preflight should mirror the same owner-file freshness expectations that workflow jobs enforce remotely.
- `.githooks/`: the tracked pre-push hook should delegate to `preflight.py` instead of duplicating local gate logic.
- `scripts/mvp_proof/`: proof-specific packaging scripts may live under a nested governed folder when they would otherwise flatten the root scripts directory.

## Verification Contract
```yaml
steps:
  - name: compile_scripts
    run: |
      # Linux/macOS analog: python3 -m compileall scripts
      py -3 -m compileall scripts

  - name: script_help
    run: |
      # Linux/macOS analog: replace `py -3` with `python3` and `> $null` with `> /dev/null`
      py -3 scripts/validate_ai_docs.py --help > $null
      py -3 scripts/check_ai_docs.py --help > $null
      py -3 scripts/ai_verify_contracts.py --help > $null
      py -3 scripts/update_last_verified.py --help > $null
      py -3 scripts/check_import_boundaries.py --help > $null
      py -3 scripts/check_codex_materialization.py --help > $null
      py -3 scripts/materialize_codex_runtime.py --help > $null
      py -3 scripts/preflight.py --help > $null

  - name: validate_owner_files
    run: |
      # Linux/macOS analog: python3 scripts/validate_ai_docs.py --repo-root . --files __ai__.md scripts/__ai__.md src/context_atlas/__ai__.md src/context_atlas/domain/__ai__.md src/context_atlas/infrastructure/__ai__.md tests/__ai__.md .github/workflows/__ai__.md
      py -3 scripts/validate_ai_docs.py --repo-root . --files __ai__.md scripts/__ai__.md src/context_atlas/__ai__.md src/context_atlas/domain/__ai__.md src/context_atlas/infrastructure/__ai__.md tests/__ai__.md .github/workflows/__ai__.md
```
