# Planning Protocol

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the workflow path used when work must be decomposed, sequenced, or clarified before safe deliverable creation can proceed.

## Trigger / Enter Conditions

- a new work scope requires decomposition or sequencing
- execution cannot proceed safely because planning shape is incomplete
- recovery returns work for replanning or structural clarification

## Participating Roles And Modes

- Owning role:
  - `Planner/Decomp`
- Conditional participants:
  - `Backend`
  - `Documentation/UAT`
- Primary mode:
  - `planning`

## Structured Contract Expectations

- consumes a planning-intake contract or other structured statement of scope
- may use `delegation` for bounded planning analysis
- should emit a structured planning-output handoff when downstream work is
  ready
- should use `escalation` when ownership or safe next-step shape remains
  unclear

## Exit Criteria

- the work has a governed next shape
- the downstream boundary and recommended next action are explicit
- unresolved risks and unknowns are surfaced rather than hidden

## Traceability

- Maintenance mode: `generated`
- Upstream sources:
  - `docs/Authoritative/Canon/AgenticDevelopment/Protocols/Planning-Protocol.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Mode-Bindings.md`
