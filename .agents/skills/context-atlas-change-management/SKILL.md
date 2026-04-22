# Context Atlas Skill: Change Management

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to frame change in a way that preserves traceability,
reviewability, drift awareness, and bounded recovery paths.

## Parent Boundary

- Conditional for:
  - `parent-planner-decomp`
  - `parent-documentation-uat`
  - `parent-devops`
  - `specialist-planning-change`
  - `specialist-delivery-recovery`
- This skill classifies and sequences change. It does not replace actual
  implementation, merge, or release authority.

## Workflow

1. Classify the change by type and identify the authoritative owning layer.
2. Name affected downstream surfaces, including runtime assets and docs.
3. State sequencing, review, rollback, and compatibility implications.
4. Return an explicit follow-up and validation list so drift does not become
   hidden.

## Escalation Conditions

- Ownership is unclear across canon, binding, and materialization layers.
- Compatibility or migration consequences are not understood.
- Recovery or rollback posture is unsafe or ambiguous.

## Return Contract

- a change classification summary
- owning-layer and downstream-surface notes
- sequencing and rollback implications
- required validation and documentation follow-up

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/change-management.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
