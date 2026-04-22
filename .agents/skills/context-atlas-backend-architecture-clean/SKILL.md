# Context Atlas Skill: Backend Architecture CLEAN

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for evaluating backend work against separation of concerns, dependency direction, and inward architectural boundaries associated with CLEAN-style design.

## Parent Boundary

- Baseline for:
  - `parent-backend`
  - `parent-qa`
- Conditional for:
  - `specialist-python-implementation`
  - `specialist-review-readiness`
- Does not replace the complete architecture canon

## Workflow

1. Inspect where the behavior lives today
2. Identify the relevant boundary and dependency directions
3. Test the placement against the intended layer responsibilities
4. Surface conformance notes or targeted remediation guidance

## Escalation Conditions

- The architecture profile itself is unclear or contradictory
- The proposed remediation would require broader system restructuring
- Multiple layers already share responsibility in a way that cannot be
  resolved locally
- The issue is really about protocol or role ownership rather than code
  placement

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
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
