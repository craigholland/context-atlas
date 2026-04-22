# Handoff Protocol

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the workflow path used when completed or clarified Context Atlas
state moves from one boundary to another.

## Trigger / Enter Conditions

- a source boundary has completed a bounded slice
- or a source boundary has produced clarified next-step state for downstream
  work

## Participating Roles And Modes

- no permanent owning top-level role
- used by whichever accountable boundary is handing work forward
- mode-spanning contract protocol:
  - often occurs at the edge of leaving one mode and entering the next

## Structured Contract Expectations

- handoff contracts should stay structured and machine-readable
- normal completion handoff type:
  - `implementation_complete`
- scope is carried through:
  - `scope_level: task`
  - `scope_level: story`
  - `scope_level: epic`
- downstream target, next action, changed surfaces, verification, and open
  risks should remain explicit

## Exit Criteria

- downstream intake can begin without reconstructing upstream state from prose
- the next workflow step is explicit

## Traceability

- Maintenance mode: `generated`
- Upstream sources:
  - `docs/Authoritative/Canon/AgenticDevelopment/Protocols/Handoff-Protocol.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Mode-Bindings.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Gate-Review-Pass-Matrix.md`
