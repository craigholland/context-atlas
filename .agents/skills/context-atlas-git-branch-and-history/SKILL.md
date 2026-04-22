# Context Atlas Skill: Git Branch And History

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to inspect and prepare Git branch and commit history in a way
that remains readable, attributable, and reviewable.

## Parent Boundary

- Baseline for:
  - `parent-backend`
  - `parent-devops`
  - `specialist-delivery-recovery`
- This skill supports branch and history handling. It does not grant merge
  authority on its own.

## Workflow

1. Inspect branch topology, divergence, and intended integration target.
2. Choose the smallest safe branch or history action that preserves audit
   clarity.
3. Keep unrelated work separated and unusual history actions explicit.
4. Return the resulting branch state and any conflict-resolution rationale.

## Escalation Conditions

- The required history surgery would rewrite or obscure collaborators' work.
- The integration path conflicts with branch-governance rules.
- Conflict resolution requires product or implementation clarification.

## Return Contract

- branch-status summary
- commit and history preparation notes
- conflict or integration rationale when needed
- explicit note if unusual history operations were required

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/git-branch-and-history.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
