# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: fc9ae3174b35205b3c9935e2dd103b5c83d7c0eb
- timestamp_utc: 2026-04-19T21:37:03Z
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
- When the supported workflows emit one shared artifact filename set, this folder should prefer accepting an artifact directory plus those standard filenames over duplicating per-workflow path conventions.
- When proof work is being packaged for review, this folder should prefer writing a predictable bundle directory that keeps copied artifacts and the packaged evidence JSON together for one workflow/scenario pair.
- Bundle generation should be idempotent when rerun against an existing workflow/scenario directory; proof capture must not fail just because the current artifact paths already point at the target bundle files.
- Proof capture should validate that the packet and trace it packages still look like one canonical workflow run, including matching trace identifiers and a trace `request_workflow` that matches the declared workflow name.
- When a proof scenario is explicitly marked as budget-constrained, capture should also verify that the packaged artifacts show visible budget-pressure evidence rather than only narrative claims.
- When a proof scenario is explicitly marked as authority-focused, capture should also verify that the packaged packet shows authoritative repository documents alongside lower-authority document material in the expected packet order.

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
    - should support the shared Atlas artifact-directory convention used by the selected MVP workflows without losing backward compatibility for explicit file paths
    - should support a reviewable bundle-root output path so reviewers can open copied artifacts directly without first unpacking the JSON evidence record
    - should tolerate regeneration into an already-populated bundle directory when the source artifacts already live at the target paths
    - should reject packet/trace inputs that do not look like one canonical workflow run over the shared engine path
    - should support an explicit budget-pressure expectation for constrained scenarios and reject artifact sets that do not show visible pressure signals
    - should require budget trace metadata before accepting a constrained budget-pressure bundle, even when packet-level compression metadata is present
    - should support an explicit `--expect-document-authority-contrast` expectation for authority-focused scenarios and reject packet artifacts that do not keep authoritative documents ahead of lower-authority repository docs
    - should embed the standard review order and rubric-dimension list so evidence packages stay reviewable without extra private instructions

## Known Gaps / Future-State Notes
- This folder currently defines only the evidence package shape, not the full workflow runners that will feed it.
- Later Story 6 tasks may add comparison or assessment helpers, but they should remain downstream of real workflow execution.
- The current capture script now also carries the standard review order for comparing naive and Atlas artifacts; future additions should extend that path carefully instead of inventing workflow-specific review steps.
- The current capture script should stay aligned with the standard artifact filenames emitted by the selected MVP workflows so later proof slices do not reintroduce workflow-specific file naming.
- The current capture script should also stay aligned with the documented bundle layout under `examples/mvp_proof/evidence/README.md` so later proof slices do not create competing review directory shapes.

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
