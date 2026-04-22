# Planner/Decomp Role Projection

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the Context Atlas `Planner/Decomp` role as a Codex-facing accountability surface for decomposition quality, sequencing coherence, and planning-layer integrity across Epics, Stories, Tasks, and PR slices.

## Direct Ownership

- planning artifacts under `docs/Planning/`
- decomposition updates that keep Epic, Story, Task, and PR-plan layers
  aligned
- planning readmes or orientation notes that govern how decomposition should
  be consumed
- decisions about work breakdown, dependency shape, and sequencing clarity

## Parent-Agent Binding

- Materialized by `.codex/agents/parent-planner-decomp.toml`
- Delegated planning support may return through
  `.codex/agents/specialist-planning-change.toml`

## Mode Participation

- Primary:
  - `planning`
  - `rework`
- Conditional:
  - `recovery`

## Protocol Participation

- Owns:
  - `planning`
  - `rework` when planning artifacts are returned
- Participates in:
  - `recovery`
  - `delegation`
  - `handoff`
  - `escalation`

## Traceability

- Maintenance mode: `generated`
- Upstream sources:
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Model.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Accountability-Matrix.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Authority-Matrix.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Agent-Binding-Model.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Mode-Matrix.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
