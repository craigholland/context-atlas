# Context Atlas Skill: Recovery Triage

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for diagnosing blocked, unstable, or drifted states and choosing a bounded recovery direction.

## Parent Boundary

- Conditional for:
  - `parent-planner-decomp`
  - `parent-devops`
  - `specialist-delivery-recovery`
- Does not replace full incident-command or operational-governance structures

## Workflow

1. Summarize the current unstable or blocked state
2. Classify likely cause categories
3. Identify the smallest safe next action
4. State whether the path is retry, rollback, hold, repair, or escalate

## Escalation Conditions

- No bounded safe recovery action is visible
- The issue appears systemic rather than local
- Recovery would require destructive or high-authority operations
- The known-good state is uncertain or disputed

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
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
