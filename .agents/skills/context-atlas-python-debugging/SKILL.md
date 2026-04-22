# Context Atlas Skill: Python Debugging

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for reproducing, isolating, and explaining Python faults or unexpected behavior.

## Parent Boundary

- Baseline for:
  - `specialist-python-implementation`
- Conditional for:
  - `parent-backend`
  - `parent-qa`
  - `specialist-review-readiness`
- Does not replace implementation ownership

## Workflow

1. Establish a reproducible symptom
2. Narrow the failing surface to a smaller scope
3. Inspect state, inputs, and recent change surfaces
4. State the likely cause and candidate remediation direction
5. Hand back a bounded explanation and evidence trail

## Escalation Conditions

- The bug cannot be reproduced with available inputs or environments
- The likely cause depends on unavailable operational, data, or infrastructure
  state
- The issue appears to stem from architecture or workflow design rather than a
  bounded implementation fault
- The required remediation would cross major ownership boundaries

## Return Contract

- reproduction notes
- fault-isolation summary
- candidate fix direction
- explicit confidence level on the suspected root cause

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/python-debugging.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
