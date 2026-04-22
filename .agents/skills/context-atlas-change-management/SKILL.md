# Context Atlas Skill: Change Management

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for evolving systems in a way that preserves traceability, reviewability, and bounded recovery paths.

## Parent Boundary

- Conditional for:
  - `parent-planner-decomp`
  - `parent-documentation-uat`
  - `parent-devops`
  - `specialist-planning-change`
  - `specialist-delivery-recovery`
- Does not replace implementation work

## Workflow

1. Classify the change by type and owning layer
2. Identify affected downstream surfaces
3. State sequencing, review, and rollback implications
4. Name required validation and documentation follow-up

## Escalation Conditions

- Ownership of the change is unclear across canon, binding, and
  materialization layers
- Compatibility or migration consequences are not understood
- The change would require hidden operational authority not currently granted
- Rollback or recovery would be unsafe or ambiguous

## Return Contract

- change proposal notes
- risk and sequencing summary
- required follow-up or validation list
- drift-sensitive surface inventory

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/change-management.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
