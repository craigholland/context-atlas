# Implementation Mode

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the Context Atlas `implementation` mode as the Codex-facing execution state for role-owned deliverable creation and bounded first-pass work on owned surfaces.

## Entry Conditions

- when a role owns a bounded deliverable slice and the current work is
  producing that slice
- when recovery resolves into fresh deliverable work rather than continued
  planning or review

## Exit Conditions

- when a structured completion handoff is emitted for downstream review or the
  next protocol-defined step
- when the work is blocked badly enough to require recovery

## Allowed Mutations

- role-owned deliverable artifacts plus directly necessary validation or
  explanation updates

Not allowed by default:

- self-acceptance findings
- merge/release actions
- broad recovery reshaping

## Role And Protocol Participation

- Primary roles:
  - `Backend`
  - `Documentation/UAT`
- Primary protocol:
  - `execution-slice`
- Cross-cutting contract protocols may appear at the edges:
  - `delegation`
  - `handoff`
  - `escalation`

## Traceability

- Maintenance mode: `generated`
- Upstream sources:
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Modes/Mode-Model.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Modes/Mode-Transition-Rules.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Modes/Mode-Mutation-Matrix.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Roles/Role-Mode-Matrix.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Mode-Bindings.md`
