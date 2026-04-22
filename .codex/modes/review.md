# Review Mode

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the Context Atlas `review` mode as the Codex-facing execution state for governed assessment, findings production, and acceptance analysis.

## Entry Conditions

- only when a valid structured review-intake contract exists
- when the current work is governed assessment, findings, or acceptance
  analysis rather than primary feature delivery

## Exit Conditions

- when a structured review-outcome contract is emitted
- when the review outcome routes work to rework, operational delivery, or
  recovery

## Allowed Mutations

- review findings
- acceptance artifacts
- validation evidence
- QA-owned regression additions
- proof summaries

Not allowed by default:

- primary product implementation
- merge/release execution
- unrelated scope expansion

## Role And Protocol Participation

- Primary role:
  - `QA`
- Primary protocol:
  - `review`
- Multiple required review passes may occur within one `review` span without
  creating extra mode nodes
- Cross-cutting contract protocols may appear at the edges:
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
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Gate-Review-Pass-Matrix.md`
