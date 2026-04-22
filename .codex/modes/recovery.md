# Recovery Mode

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the Context Atlas `recovery` mode as the Codex-facing execution state for restoring a safe workflow path when ownership, contracts, or state are broken or ambiguous.

## Entry Conditions

- when workflow state is broken, ambiguous, invalid, or materially blocked
- when a contract is missing, malformed, contradictory, or insufficient for
  safe continuation

## Exit Conditions

- only through a structured recovery outcome that explicitly routes work into
  another mode

## Allowed Mutations

- recovery notes
- state-reconstruction artifacts
- bounded stabilization edits needed to restore workflow clarity

Not allowed by default:

- net-new feature scope
- silent ownership transfer
- ordinary completion work disguised as recovery

## Role And Protocol Participation

- Conditional roles:
  - `Planner/Decomp`
  - `Backend`
  - `Documentation/UAT`
  - `QA`
  - `DevOps`
- Primary protocol:
  - `recovery`
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
