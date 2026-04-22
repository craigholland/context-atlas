# Context Atlas Skill: Recovery Triage

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to diagnose blocked, unstable, or drifted states and choose a
bounded recovery direction.

## Parent Boundary

- Conditional for:
  - `parent-planner-decomp`
  - `parent-devops`
  - `specialist-delivery-recovery`
- This skill triages recovery. It does not replace incident command or hide the
  need for escalation when authority is insufficient.

## Workflow

1. Summarize the unstable or blocked state and the recent evidence around it.
2. Classify the likely failure as local, workflow-level, or systemic.
3. Identify the smallest safe next step: retry, rollback, hold, repair, or
   escalate.
4. Return the chosen recovery path with explicit rationale and follow-up risk.

## Escalation Conditions

- No bounded safe recovery action is visible.
- The issue appears systemic rather than local.
- Recovery would require destructive or high-authority operations.

## Return Contract

- recovery-state summary
- likely cause categories
- immediate next-step recommendation
- recovery-risk note

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/recovery-triage.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
