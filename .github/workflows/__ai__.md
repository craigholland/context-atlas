# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: b426e06579cd10414a3e3b6a7786ff836f6909ba
- timestamp_utc: 2026-04-17T18:01:00Z
- verified_by: local
- notes: Verified means "the commands in Verification Contract passed locally" (not a human review and not yet a dedicated CI workflow).

## Scope
- folder: .github/workflows
- included:
  - "*.yml"
- excluded:
  - "__pycache__/**"

## Purpose
- Holds repository CI workflows that operationalize the local `__ai__.md` contract system and baseline architectural checks.
- Keeps workflow logic thin by delegating meaningful checks to repo-owned scripts under `scripts/`.
- Makes workflow ownership and expectations explicit before automation expands further.
- Establishes `development` as the current integration/default branch for automation that writes back to the repository.

## Architectural Rules
- Workflows in this folder should prefer calling repo-owned scripts over duplicating validation logic inline in YAML.
- Fetch full git history when diff-based owner-file checks need commit range information.
- These workflows are architecture-adjacent enforcement, not proof of semantic correctness.
- Keep runner and shell choices aligned with the repository's declared Verification Contract commands.
- The folder-contract workflow should enforce owner-file freshness, not just structural validity.

## Allowed Dependencies
- may depend on:
  - GitHub Actions official setup/checkout actions
  - repo-owned scripts under `scripts/`
- must not depend on:
  - opaque third-party workflow logic for core `__ai__` enforcement when a repo-owned script already exists
  - assumptions that bypass local owner-file verification contracts

## Public API / Key Exports
- `ci.yml`:
  - baseline repo preflight for code and architecture checks
- `ai-verify-folder-contracts.yml`:
  - validates `__ai__.md` structure, freshness, and local verification contracts
- `ai-last-verified.yml`:
  - updates `Last Verified (CI)` metadata after successful verification on the `development` integration branch

## File Index
- `ci.yml`:
  - responsibility: installs dev tooling and runs the repo preflight
  - depends_on:
    - `scripts/preflight.py`
- `ai-verify-folder-contracts.yml`:
  - responsibility: validates and exercises local owner-file contracts
  - depends_on:
    - `scripts/validate_ai_docs.py`
    - `scripts/check_ai_docs.py`
    - `scripts/ai_verify_contracts.py`
  - invariants:
    - should stay aligned with the local preflight freshness and contract-execution path
- `ai-last-verified.yml`:
  - responsibility: rewrites `Last Verified (CI)` metadata after successful verification
  - depends_on:
    - `scripts/update_last_verified.py`
  - invariants:
    - branch targeting here should match the repo's active integration branch

## Known Gaps / Future-State Notes
- Workflow coverage is intentionally minimal and focused on the contract system plus bootstrap code checks.
- The current automation model assumes `development` is the active integration branch rather than `main`.
- If the repo later adds multiple apps, packaging jobs, or release workflows, this folder may need more granular guidance.

## Cross-Folder Contracts
- `scripts/`: workflows should treat repository scripts as the source of truth for owner-file validation, freshness checks, contract execution, import-boundary enforcement, and preflight.
- root `__ai__.md`: CI should remain aligned with the repo-level preflight expectation before push or merge.
- `scripts/`: if remote freshness checks are stricter than local preflight, local preflight should be brought back into parity quickly.
- `src/context_atlas/`: workflow checks should reinforce the package's local contracts rather than inventing conflicting layer rules in YAML.
- `tests/`: workflow test steps should invoke the documented test contract rather than quietly changing how the suite is run.

## Verification Contract
```yaml
steps:
  - name: validate_owner_file
    run: |
      py -3 scripts/validate_ai_docs.py --repo-root . --files .github/workflows/__ai__.md

  - name: workflow_presence
    run: |
      @('ci.yml', 'ai-verify-folder-contracts.yml', 'ai-last-verified.yml') | ForEach-Object {
        if (-not (Test-Path (Join-Path '.github/workflows' $_))) {
          throw "Missing workflow file: $_"
        }
      }

  - name: validate_related_owner_files
    run: |
      py -3 scripts/validate_ai_docs.py --repo-root . --files __ai__.md scripts/__ai__.md src/context_atlas/__ai__.md src/context_atlas/domain/__ai__.md src/context_atlas/infrastructure/__ai__.md tests/__ai__.md .github/workflows/__ai__.md
```
