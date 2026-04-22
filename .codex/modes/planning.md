# Planning Mode

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the Context Atlas `planning` mode as the Codex-facing execution
state for decomposition, sequencing, dependency clarification, and
planning-shape revision.

## Entry Conditions

- a new work scope requires decomposition or sequencing
- a prior review or recovery outcome routes work back to planning
- the current work is planning-shaped rather than deliverable creation

## Exit Conditions

- a structured planning-output handoff is emitted for downstream work
- planning work is returned for rework
- workflow state breaks badly enough to require `recovery`

## Allowed Mutations

- planning artifacts
- decomposition updates
- planning-oriented sequencing notes

Not allowed by default:

- primary feature delivery
- review findings
- merge or release execution

## Role And Protocol Participation

- Primary roles:
  - `Planner/Decomp`
- Conditional roles:
  - `Backend`
  - `Documentation/UAT`
- Primary protocol:
  - `planning`
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
