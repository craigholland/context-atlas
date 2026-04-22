# QA Role Projection

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the Context Atlas `QA` role as the accountable surface for governed
review, findings quality, acceptance analysis, and rework feedback loops.

## Direct Ownership

- structured review intake and outcome artifacts
- findings, acceptance judgments, and proof summaries
- QA-owned validation additions and review-facing evidence surfaces
- readiness framing for governed workflow gates

## Parent-Agent Binding

- Materialized by `.codex/agents/parent-qa.toml`
- Delegated review support may return through
  `.codex/agents/specialist-review-readiness.toml`

## Mode Participation

- Primary:
  - `review`
- Conditional:
  - `rework`
  - `recovery`

## Protocol Participation

- Owns:
  - `review`
- Participates in:
  - `rework`
  - `recovery`
  - `delegation`
  - `handoff`
  - `escalation`
- Gate review defaults:
  - `Task -> Story`: `code`
  - `Story -> Epic`: `architecture`, `security`
  - `Epic -> development`: `product`

## Traceability

- Maintenance mode: `generated`
- Upstream sources:
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Model.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Accountability-Matrix.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Authority-Matrix.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Agent-Binding-Model.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Mode-Matrix.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Gate-Review-Pass-Matrix.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
