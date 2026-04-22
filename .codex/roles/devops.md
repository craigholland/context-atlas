# DevOps Role Projection

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the Context Atlas `DevOps` role as the accountable surface for
merge, release, workflow, versioning, and other operational-delivery actions
that should remain distinct from ordinary implementation.

## Direct Ownership

- CI and workflow definitions under `.github/workflows/`
- release-process documentation and release summaries
- versioning, tagging, merge, and operational delivery artifacts
- operational scripts whose primary purpose is repository delivery

## Parent-Agent Binding

- Materialized by `.codex/agents/parent-devops.toml`
- Delegated delivery and recovery support may return through
  `.codex/agents/specialist-delivery-recovery.toml`

## Mode Participation

- Primary:
  - `operational-delivery`
- Conditional:
  - `rework`
  - `recovery`

## Protocol Participation

- Owns:
  - none in the initial shared protocol family
- Participates in:
  - `review`
  - `rework`
  - `recovery`
  - `delegation`
  - `handoff`
  - `escalation`
- Consumes structured review state before merge or release action

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
