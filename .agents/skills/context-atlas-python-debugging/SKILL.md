# Context Atlas Skill: Python Debugging

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to reproduce, isolate, and explain bounded Python faults with
disciplined evidence instead of speculative fix attempts.

## Parent Boundary

- Conditional for:
  - `parent-backend`
  - `parent-qa`
  - `specialist-review-readiness`
- Baseline for:
  - `specialist-python-implementation`
- This skill isolates faults. It does not automatically approve the remedy or
  widen implementation ownership.

## Workflow

1. Establish a reproducible symptom or tightly bounded failing condition.
2. Narrow the failing surface to code, data, environment, or contract drift.
3. State confirmed cause, likely cause, and open questions separately.
4. Return a bounded remediation direction with evidence and confidence level.

## Escalation Conditions

- The issue cannot be reproduced with available inputs or environments.
- The likely cause depends on unavailable operational or data state.
- The issue is really architectural or ownership-level rather than local.

## Return Contract

- reproduction notes
- fault-isolation summary
- candidate remediation direction
- explicit confidence statement

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/python-debugging.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
