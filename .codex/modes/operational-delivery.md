# Operational Delivery Mode

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the Context Atlas `operational_delivery` mode as the Codex-facing execution state for merge, release, workflow, versioning, and similar delivery-oriented operational actions.

## Entry Conditions

- when upstream readiness conditions are satisfied and the current work is
  merge, release, workflow, versioning, or similar operational action
- when an accepted review outcome or recovery outcome routes work to an
  operational next step

## Exit Conditions

- when an operational outcome contract is emitted
- when an operational artifact is handed to review
- when the operational path becomes blocked badly enough to require recovery
- Mode rules should remain legible without turning into full protocol docs.
- Entry and exit rules should rely on structured state changes rather than
  conversational implication.
- Recovery should stay explicit instead of becoming a vague catch-all for work
  that simply lacks a clean handoff.
- Define the detailed shape of every handoff contract.
- Define full role applicability or mutation authority.
- Replace the later protocol model.
- [Context Atlas Mode Model](./Mode-Model.md)
- [Mode Transition Graph](./Mode-Transition-Graph.md)
- [Mode Mutation Matrix](./Mode-Mutation-Matrix.md)
- [Context Atlas Role-Mode Matrix](../Roles/Role-Mode-Matrix.md)
- [Context Atlas Agentic Development
  Profile](../../../Context-Atlas-Agentic-Development-Profile.md)

## Allowed Mutations

- merge/release artifacts
- workflow definitions
- versioning surfaces
- release summaries
- operational automation assets

Not allowed by default:

- ordinary feature implementation
- self-acceptance findings
- broad planning/decomposition rewrites

## Role And Protocol Participation

- Primary role:
  - `DevOps`
- There is no dedicated initial shared operational-delivery protocol in the
  current protocol family
- Common cross-cutting contracts:
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
