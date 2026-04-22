# Context Atlas Skill: Planning Decomposition

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for turning a larger objective into bounded, sequenced, reviewable work slices that preserve architectural and workflow clarity.

## Parent Boundary

- Baseline for:
  - `parent-planner-decomp`
  - `parent-backend` when breaking an already-assigned task into PR-sized
    slices
  - `specialist-planning-change`
- Does not, by itself, authorize protocol transitions or role ownership

## Workflow

1. Restate the objective in concrete outcome terms
2. Identify affected boundaries, roles, and proof surfaces
3. Separate critical-path work from parallelizable work
4. Place epic, story, and task boundaries deliberately
5. State sequencing, dependencies, and handoff points clearly

## Escalation Conditions

- The objective is too ambiguous to decompose responsibly
- The governing architecture is missing, contradictory, or unstable
- Ownership boundaries between roles or parent agents are unclear
- The work implies product decisions that have not been settled
- The requested scope cannot be made reviewable without revising expectations

## Return Contract

- decomposition outline
- proposed epic/story/task breakdown
- dependency and sequencing notes
- handoff and proof-surface notes

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/planning-decomposition.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
