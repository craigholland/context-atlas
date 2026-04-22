# Rework Protocol

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the workflow path used when previously delivered work has been returned with findings, required changes, or clarifications.

## Trigger / Enter Conditions

- a structured review-outcome or recovery contract returns work for correction
  or clarification

## Participating Roles And Modes

- Owning roles depend on the returned surface:
  - `Planner/Decomp` for planning rework
  - `Backend` for backend rework
  - `Documentation/UAT` for documentation/UAT rework
  - `DevOps` for operational rework
  - `QA` only for QA-owned validation artifacts
- Primary mode:
  - `rework`

## Structured Contract Expectations

- consumes structured review outcomes or recovery outputs
- should keep traceability back to the returned finding or request
- emits a renewed completion handoff or a structured escalation when the
  return cannot be satisfied safely

## Exit Criteria

- the returned-work scope has been addressed or explicitly escalated
- downstream review or next-step intake can see what was changed and why

## Traceability

- Maintenance mode: `generated`
- Upstream sources:
  - `docs/Authoritative/Canon/AgenticDevelopment/Protocols/Rework-Protocol.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Mode-Bindings.md`
