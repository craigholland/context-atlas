# Context Atlas Skill: Python Testing

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to produce and interpret bounded Python validation evidence for
behavior, regressions, and robustness.

## Parent Boundary

- Baseline for:
  - `parent-qa`
  - `specialist-python-implementation`
  - `specialist-review-readiness`
- Conditional for:
  - `parent-backend`
- This skill should include negative-path and boundary-breaking tests when
  robustness matters. It does not equate a green run with full acceptance.

## Workflow

1. Identify the contract or behavior that needs proof.
2. Choose the narrowest useful test boundary.
3. Run existing tests first when possible, then add or refine focused tests.
4. Include invalid, missing, extreme, or unexpected inputs when resilience is
   part of the claim.
5. Return what passed, what failed, and what remains outside evidence.

## Escalation Conditions

- Required evidence depends on unavailable environments, services, or data.
- The correct test boundary is blocked by unresolved architecture decisions.
- Tests are too unstable or slow to provide trustworthy evidence.

## Return Contract

- test execution summary
- focused test additions or updates
- negative-path and robustness notes when relevant
- explicit statement of what was and was not validated

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/python-testing.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
