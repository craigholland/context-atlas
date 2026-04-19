# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 30288f3a4fabbb74b4b7eea53502113879f366bb
- timestamp_utc: 2026-04-19T17:39:31Z
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).
## Scope
- folder: scripts/mvp_proof
- included:
  - "*.py"
- excluded:
  - "__pycache__/**"
  - "**/__pycache__/**"
  - "**/*.pyc"

## Purpose
- Holds MVP-proof helper scripts that package evidence artifacts without becoming a second workflow engine.
- Keeps proof capture reproducible and inspectable through tracked Python scripts rather than ad hoc terminal notes or screenshots.

## Architectural Rules
- Scripts here should package already-generated workflow artifacts; they must not bypass the supported workflow paths to fabricate packet or trace outputs directly.
- Keep the proof artifact shape workflow-agnostic so the same capture path can be reused across the repository, docs-plus-database, and low-code workflows.
- Prefer standard-library implementations and simple file-shape transformations over runtime imports from `src/context_atlas`.

## Allowed Dependencies
- may depend on:
  - Python standard library
- must not depend on:
  - `context_atlas` runtime modules for simple proof packaging
  - workflow-specific example scripts as a hidden import dependency

## Public API / Key Exports
- `capture_evidence.py`:
  - `main`: writes one reproducible MVP-proof evidence package from already-generated workflow artifacts

## File Index
- `capture_evidence.py`:
  - responsibility: normalize one proof scenario into a stable JSON evidence package
  - invariants:
    - should capture both naive baseline and Atlas artifacts together
    - should accept workflow artifacts as inputs rather than generating them itself
    - should embed the standard review order and rubric-dimension list so evidence packages stay reviewable without extra private instructions

## Known Gaps / Future-State Notes
- This folder currently defines only the evidence package shape, not the full workflow runners that will feed it.
- Later Story 6 tasks may add comparison or assessment helpers, but they should remain downstream of real workflow execution.
- The current capture script now also carries the standard review order for comparing naive and Atlas artifacts; future additions should extend that path carefully instead of inventing workflow-specific review steps.

## Cross-Folder Contracts
- `examples/`: example-facing proof docs may show how to invoke these scripts, but should not replace them with copy-paste shell fragments.
- `docs/Reviews/`: review artifacts may depend on the evidence packages produced here, but should remain human-readable assessments rather than script outputs.
- `scripts/`: the parent folder should keep this proof-specific tooling visible in repo governance and freshness checks.

## Verification Contract
```yaml
steps:
  - name: compile_mvp_proof_scripts
    run: |
      py -3 -m compileall scripts/mvp_proof

  - name: help_output
    run: |
      py -3 scripts/mvp_proof/capture_evidence.py --help > $null
```
