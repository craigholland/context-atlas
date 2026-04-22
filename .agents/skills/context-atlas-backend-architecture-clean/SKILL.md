# Context Atlas Skill: Backend Architecture CLEAN

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to evaluate backend changes against separation of concerns,
dependency direction, and inward boundary expectations associated with
CLEAN-style architecture.

## Parent Boundary

- Baseline for:
  - `parent-backend`
  - `parent-qa`
- Conditional for:
  - `specialist-python-implementation`
  - `specialist-review-readiness`
- This skill performs bounded conformance analysis. It does not replace the
  full architecture canon or decide release readiness.

## Workflow

1. Inspect where the relevant behavior lives today.
2. Identify the current layer, dependency direction, and boundary crossings.
3. Test the placement against domain, service, adapter, and infrastructure
   expectations.
4. Return conformance notes and narrow remediation guidance.

## Escalation Conditions

- The local architecture profile is unclear or contradictory.
- Remediation would require broader system restructuring.
- The issue is really about ownership or workflow design rather than code
  placement.

## Return Contract

- architectural conformance notes
- boundary-risk findings
- targeted remediation guidance

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/backend-architecture-clean.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
