# Context Atlas Skill: Python Testing

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for using Python tests as bounded validation and evidence surfaces.

## Parent Boundary

- Baseline for:
  - `parent-qa`
  - `specialist-python-implementation`
  - `specialist-review-readiness`
- Conditional for:
  - `parent-backend`
- Does not equate a green test run with total acceptance

## Workflow

1. Identify the contract or behavior that needs proof
2. Choose the right testing level
3. Run existing tests first when possible
4. Add or refine tests if the current evidence is insufficient
5. Include negative-path or boundary-breaking cases when robustness is part of the contract being tested
6. Interpret the resulting pass/fail signal in context

## Escalation Conditions

- The required evidence depends on unavailable environments, data, or services
- The correct testing boundary is blocked by unresolved architecture decisions
- Tests are too unstable or slow to provide trustworthy evidence
- The issue appears to be in review interpretation rather than test coverage

## Return Contract

- test execution result summary
- focused test additions or updates
- evidence notes tied to observed behavior

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/python-testing.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
