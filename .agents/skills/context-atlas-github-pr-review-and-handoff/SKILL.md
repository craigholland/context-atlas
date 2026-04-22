# Context Atlas Skill: GitHub PR Review And Handoff

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to treat the GitHub pull-request surface as a structured handoff,
findings, and response channel.

## Parent Boundary

- Baseline for:
  - `parent-documentation-uat`
  - `parent-devops`
  - `specialist-review-readiness`
  - `specialist-delivery-recovery`
- Conditional for:
  - `parent-qa`
- This skill uses the PR surface well. It does not imply approval or merge
  authority by itself.

## Workflow

1. Inspect the PR, checks, target branch, and current review state.
2. Prepare a structured summary, finding, or response tied to the active diff.
3. Keep observation, rationale, requested action, and open state explicit.
4. Leave the PR in a clearer review or handoff state than it started.

## Escalation Conditions

- Required PR actions exceed the actor's provider permissions.
- Review state, authority state, and readiness state conflict materially.
- Findings imply architectural or product decisions beyond the current scope.

## Return Contract

- PR review or handoff summary
- inline findings or responses
- explicit statement of what remains open, blocked, or accepted

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/github-pr-review-and-handoff.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
