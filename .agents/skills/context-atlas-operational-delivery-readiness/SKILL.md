# Context Atlas Skill: Operational Delivery Readiness

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to judge whether a bounded work unit appears ready to move into
delivery-oriented operational handling.

## Parent Boundary

- Baseline for:
  - `parent-devops`
  - `specialist-delivery-recovery`
- This skill produces a readiness judgment. It does not replace release
  authority or override gate policy.

## Workflow

1. Inspect the current branch, PR, review, evidence, and release-facing state.
2. Compare the current state against the expected gate inputs.
3. Identify blockers, missing artifacts, and remaining operational risks.
4. Return a proceed or hold recommendation with explicit missing evidence.

## Escalation Conditions

- Delivery readiness depends on authority outside the current actor.
- Gate policy is ambiguous or contradictory.
- Review, testing, or release evidence conflicts materially.

## Return Contract

- readiness summary
- blocker and missing-evidence list
- proceed or hold recommendation
- explicit remaining-risk note

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/operational-delivery-readiness.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
