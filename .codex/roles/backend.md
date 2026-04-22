# Backend Role Projection

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the Context Atlas `Backend` role as the accountable surface for
engine, domain, service, adapter, infrastructure, rendering, and backend test
work that defines how Context Atlas behaves as a system.

## Direct Ownership

- product-engine implementation under `src/context_atlas/`
- backend-oriented tests under `tests/`
- implementation-facing technical surfaces that move with backend behavior
- bounded completion handoffs for downstream QA review

## Parent-Agent Binding

- Materialized by `.codex/agents/parent-backend.toml`
- Delegated implementation support may return through
  `.codex/agents/specialist-python-implementation.toml`

## Mode Participation

- Primary:
  - `implementation`
  - `rework`
- Conditional:
  - `planning`
  - `recovery`

## Protocol Participation

- Owns:
  - `execution-slice`
  - `rework` for backend-owned returned work
- Participates in:
  - `planning`
  - `review`
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
