# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: 53a11d1fa71fcd3ce74c066cf24e1aca8299f469
- timestamp_utc: 2026-04-19T23:06:13Z
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
- Reassessment-oriented bundle refreshes should be able to clear an existing workflow/scenario bundle first so new review passes do not inherit stale files silently.
- Reassessment-oriented bundle refreshes must preserve regenerated bundle artifacts even when the source artifacts already live inside the bundle directory being refreshed.
- Bundle refresh logic must validate that the workflow/scenario bundle path stays under the declared bundle root before any recursive delete occurs.
- Bundle generation should be idempotent when rerun against an existing workflow/scenario directory; proof capture must not fail just because the current artifact paths already point at the target bundle files.
- Proof capture should validate that the packet and trace it packages still look like one canonical workflow run, including matching trace identifiers and a trace `request_workflow` that matches the declared workflow name.
- When a proof scenario is explicitly marked as budget-constrained, capture should also verify that the packaged artifacts show visible budget-pressure evidence rather than only narrative claims.
- When a proof scenario is explicitly marked as authority-focused, capture should also verify that the packaged packet shows authoritative repository documents alongside lower-authority document material in the expected packet order.
- That authority-focused validation should key off the canonical `source.authority` values in the packet artifacts, not only document classes, so front-matter authority overrides remain visible in proof review.
- Story 5 hardening proof should keep this folder bounded to the existing packet/trace/rendered-context plus evidence-package bundle family; retrieval-reuse and duplicate-acceptance proof should remain primarily regression-backed rather than creating new proof-only bundle types here.

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
    - should support an explicit reassessment refresh path that clears stale bundle contents before rewriting a workflow/scenario bundle
    - should preserve bundle artifacts when refresh is requested against in-place source files that already live under the target bundle directory
    - should reject unsafe workflow/scenario bundle paths before recursive delete can target directories outside the declared bundle root
    - should tolerate regeneration into an already-populated bundle directory when the source artifacts already live at the target paths
    - should reject packet/trace inputs that do not look like one canonical workflow run over the shared engine path
    - should support an explicit budget-pressure expectation for constrained scenarios and reject artifact sets that do not show visible pressure signals
    - should require budget trace metadata before accepting a constrained budget-pressure bundle, even when packet-level compression metadata is present
    - should support an explicit `--expect-document-authority-contrast` expectation for authority-focused scenarios and reject packet artifacts that do not keep higher-authority repository documents ahead of lower-authority ones based on canonical `source.authority`
    - should embed the standard review order and rubric-dimension list so evidence packages stay reviewable without extra private instructions

## Known Gaps / Future-State Notes
- This folder currently focuses on evidence packaging and validation for the supported local MVP workflows, not on running or orchestrating those workflows itself.
- The proof path still assumes the standard artifact filenames emitted by the supported examples; future workflow types should extend that shared convention rather than reintroducing workflow-specific bundle logic.
- If proof tooling grows beyond packaging, validation, and close review helpers, this folder may need further subdivision to stay coherent.

## Cross-Folder Contracts
- `examples/`: example-facing proof docs may show how to invoke these scripts, but should not replace them with copy-paste shell fragments.
- `examples/mvp_proof/`: proof docs there may name which hardening scenarios deserve bundle-backed human-readable review, but they should keep that inventory bounded to the canonical packet/trace bundle story rather than inventing new artifact families that this folder does not produce.
- `docs/Reviews/`: review artifacts may depend on the evidence packages produced here, but should remain human-readable assessments rather than script outputs.
- `scripts/`: the parent folder should keep this proof-specific tooling visible in repo governance and freshness checks.

## Verification Contract
```yaml
steps:
  - name: compile_mvp_proof_scripts
    run: |
      python -m compileall scripts/mvp_proof

  - name: help_output
    run: |
      python scripts/mvp_proof/capture_evidence.py --help
```
