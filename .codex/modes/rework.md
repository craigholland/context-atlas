# Rework Mode

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the Context Atlas `rework` mode as the Codex-facing execution state for returned work that is being corrected or clarified under an explicit review or recovery outcome.

## Entry Conditions

- when a valid return contract requests changes on already-delivered work
- when clarification or correction is the current work rather than first-pass
  delivery

## Exit Conditions

- when a renewed structured completion handoff is emitted
- when the work becomes blocked or ambiguous enough to require recovery

## Allowed Mutations

- previously returned owned work plus directly necessary validation updates

Not allowed by default:

- unrelated new scope
- approval actions
- open-ended exploratory changes

## Role And Protocol Participation

- Primary roles:
  - `Planner/Decomp`
  - `Backend`
  - `Documentation/UAT`
- Conditional roles:
  - `QA`
  - `DevOps`
- Primary protocol:
  - `rework`
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
