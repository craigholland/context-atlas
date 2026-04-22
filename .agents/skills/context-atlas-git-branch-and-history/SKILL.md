# Context Atlas Skill: Git Branch And History

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for managing Git history and branch state in support of reviewable collaboration.

## Parent Boundary

- Baseline for:
  - `parent-backend`
  - `parent-devops`
  - `specialist-delivery-recovery`
- Does not by itself grant merge authority

## Workflow

1. Inspect current branch and history state
2. Identify the intended integration target
3. Choose the smallest safe history or branch action
4. Confirm the resulting state is reviewable and attributable

## Escalation Conditions

- Multiple collaborators' work would be rewritten or obscured
- The required integration path conflicts with branch governance rules
- Conflict resolution cannot be done safely without product or implementation
  clarification
- The work appears to need provider-specific authority not owned by the actor

## Return Contract

- branch-status summary
- commit preparation
- history or integration notes
- bounded conflict-resolution rationale

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/git-branch-and-history.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
