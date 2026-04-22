# Context Atlas Skill: Planning Decomposition

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to turn an objective into bounded, reviewable work slices with
explicit sequencing, ownership, and handoff placement.

## Parent Boundary

- Baseline for:
  - `parent-planner-decomp`
  - `parent-backend` when breaking an already-assigned task into PR-sized
    slices
  - `specialist-planning-change`
- This skill supports decomposition. It does not grant broader role ownership,
  QA acceptance, or merge authority.

## Workflow

1. Restate the objective in concrete outcome terms.
2. Identify the affected boundaries, review gates, and capacity constraints.
3. Choose the right level of work split and separate critical path from
   parallelizable work.
4. Return explicit slice, dependency, and handoff notes instead of prose-only
   planning.

## Escalation Conditions

- The objective is too ambiguous to decompose responsibly.
- Governing architecture or ownership boundaries are unclear.
- The requested scope cannot be made reviewable without changing expectations.

## Return Contract

- a bounded decomposition outline
- explicit task or PR-slice recommendations
- dependency and sequencing notes
- handoff and proof-surface notes

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/planning-decomposition.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
