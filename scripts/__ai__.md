# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: b426e06579cd10414a3e3b6a7786ff836f6909ba
- timestamp_utc: 2026-04-17T18:01:00Z
- verified_by: local
- notes: Verified means "the commands in Verification Contract passed locally" (not a human review and not yet a dedicated CI workflow).

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

## Architectural Rules
- Scripts in this folder should prefer Python standard library implementations unless a dependency is clearly justified.
- These scripts enforce structure, freshness heuristics, contract execution, preflight, and import-boundary rules; they must not claim to prove full architectural correctness.
- Keep repository paths, governed roots, and branch assumptions explicit and configurable rather than hidden in hardcoded globals where practical.
- Diff-based scripts should prefer `development` first when discovering a comparison base, then fall back to `main` and older defaults when needed.
- Avoid project-runtime imports from `src/context_atlas` unless a script truly needs them; most scripts here should operate on files, git state, and declared contracts.
- `preflight.py` is the canonical local gate before push or merge; other scripts should support it rather than compete with it.
- Small private dataclasses are acceptable here when they are local rule/config carriers for the script itself and not part of the package runtime surface.

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
    - `check_import_boundaries.py`
    - `ai_verify_contracts.py`
  - invariants:
    - should stay as close as practical to the remote `verify-ai-contracts` and `ci` workflow behavior
- `install_git_hooks.py`:
  - responsibility: configures `git` to use the tracked `.githooks` directory
- `import_boundary_rules.toml`:
  - responsibility: declares current `context_atlas` layer boundary rules for the import checker

## Known Gaps / Future-State Notes
- The current scripts focus on structural and architectural enforcement for the bootstrap repo; richer repo automation may arrive later.
- Some scripts still assume git-based diffing rather than a more abstract change detector.
- Local preflight parity with CI is intentional but still heuristic-driven rather than perfectly identical in every environment.
- If the package grows multiple governed subsystems, this folder may eventually need nested owner files of its own.

## Cross-Folder Contracts
- `src/context_atlas/`: scripts may validate local contracts and import boundaries there, but must not redefine the package's semantic rules.
- `tests/`: test execution is part of several verification contracts; script changes that alter invocation assumptions should update test folder guidance too.
- `.github/workflows/`: workflows should call these repo-owned scripts rather than reimplement the same logic inline in YAML.
- `.github/workflows/`: local preflight should mirror the same owner-file freshness expectations that workflow jobs enforce remotely.
- `.githooks/`: the tracked pre-push hook should delegate to `preflight.py` instead of duplicating local gate logic.

## Verification Contract
```yaml
steps:
  - name: compile_scripts
    run: |
      py -3 -m compileall scripts

  - name: script_help
    run: |
      py -3 scripts/validate_ai_docs.py --help > $null
      py -3 scripts/check_ai_docs.py --help > $null
      py -3 scripts/ai_verify_contracts.py --help > $null
      py -3 scripts/update_last_verified.py --help > $null
      py -3 scripts/check_import_boundaries.py --help > $null
      py -3 scripts/preflight.py --help > $null

  - name: validate_owner_files
    run: |
      py -3 scripts/validate_ai_docs.py --repo-root . --files __ai__.md scripts/__ai__.md src/context_atlas/__ai__.md src/context_atlas/domain/__ai__.md src/context_atlas/infrastructure/__ai__.md tests/__ai__.md .github/workflows/__ai__.md
```
