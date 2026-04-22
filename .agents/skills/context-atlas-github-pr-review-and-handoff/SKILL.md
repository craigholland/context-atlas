# Context Atlas Skill: GitHub PR Review And Handoff

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for using pull-request review surfaces as structured handoff and findings channels.

## Parent Boundary

- Baseline for:
  - `parent-documentation-uat`
  - `parent-devops`
  - `specialist-review-readiness`
  - `specialist-delivery-recovery`
- Conditional for:
  - `parent-qa`
- Does not replace provider-specific authority rules

## Workflow

1. Inspect the PR, checks, and current review state
2. Prepare a structured review or handoff comment
3. Respond to findings or questions with explicit rationale or corrective action
4. Leave the PR in a clearer review state than it started

## Escalation Conditions

- Required review actions exceed the actor's provider permissions
- The PR contains unresolved conflicts between authority, readiness, and
  review state
- Findings imply architectural or product decisions beyond the current review
  scope

## Return Contract

- PR review summary
- inline findings or responses
- handoff commentary tied to the review surface
- explicit statement of what remains open or accepted

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/github-pr-review-and-handoff.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
