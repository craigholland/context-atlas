# Context Atlas Skill: Composition And Integration Planning

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for planning how separately bounded work can be recombined safely, coherently, and in the correct order.

## Parent Boundary

- Baseline for:
  - `parent-planner-decomp`
  - `specialist-planning-change`
- Does not replace architecture conformance review

## Workflow

1. Inspect the work breakdown for recomposition surfaces
2. Identify merge, handoff, and contract-touching seams
3. State which work may proceed in parallel and which must converge first
4. Define the order in which partial outputs should be integrated

## Escalation Conditions

- Multiple slices appear to compete for the same write scope or authority
- Integration risks cannot be bounded without revisiting the decomposition
- Architecture or interface contracts are unstable
- No responsible parent actor is clearly accountable for recomposition

## Return Contract

- integration plan
- ownership-aware recomposition notes
- merge and handoff sequencing guidance
- integration risk summary

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/composition-and-integration-planning.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
