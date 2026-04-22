# Context Atlas Skill: Operational Delivery Readiness

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for deciding whether a bounded work unit appears ready to enter delivery-oriented operational handling.

## Parent Boundary

- Baseline for:
  - `parent-devops`
  - `specialist-delivery-recovery`
- Does not replace release authority

## Workflow

1. Inspect the current evidence and handoff state
2. Compare it against the expected gate inputs
3. Identify blockers, risks, or missing artifacts
4. State whether the work appears ready, blocked, or uncertain

## Escalation Conditions

- Delivery readiness depends on authority outside the current actor
- Gate policy is ambiguous or contradictory
- Evidence from review, testing, or release surfaces conflicts materially
- Moving forward would create unclear rollback or recovery posture

## Return Contract

- readiness summary
- blocker list
- proceed / hold recommendation
- missing-evidence list when relevant

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/operational-delivery-readiness.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
