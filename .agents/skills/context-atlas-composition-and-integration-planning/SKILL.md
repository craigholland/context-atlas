# Context Atlas Skill: Composition And Integration Planning

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to plan how separately bounded work returns to a coherent whole
without violating ownership, architecture, or review sequencing.

## Parent Boundary

- Baseline for:
  - `parent-planner-decomp`
  - `specialist-planning-change`
- This skill helps with recomposition and integration planning. It does not
  grant release or merge authority.

## Workflow

1. Inspect the existing breakdown for integration seams and shared write scope.
2. Identify merge, handoff, contract, and review convergence points.
3. Decide what may stay parallel and what must converge first.
4. Return an ownership-aware reintegration order with explicit risk notes.

## Escalation Conditions

- Multiple slices appear to compete for the same authority or write scope.
- Integration risk cannot be bounded without revisiting decomposition.
- No accountable parent actor is clear for recomposition.

## Return Contract

- an integration plan
- recomposition and merge sequencing notes
- ownership-aware reintegration guidance
- integration risk summary

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/composition-and-integration-planning.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
