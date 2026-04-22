# Recovery Protocol

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the workflow path used when ordinary Context Atlas planning,
execution, review, or rework cannot proceed safely because workflow state,
ownership, or contract integrity is broken or unclear.

## Trigger / Enter Conditions

- structured workflow state is missing, contradictory, or invalid
- ownership or allowed mutation scope is unclear
- ordinary protocol progression would require guesswork

## Participating Roles And Modes

- ownership is context-dependent and stays with the role closest to the broken
  workflow state unless escalation changes that
- any role may participate when its workflow state is implicated
- Primary mode:
  - `recovery`

## Structured Contract Expectations

- consumes the broken or ambiguous workflow state plus available prior
  contracts or evidence
- emits a structured recovery outcome naming clarified ownership and the
  recommended next protocol
- may escalate when the recovering boundary cannot restore workable state

## Exit Criteria

- workflow can re-enter another protocol without guesswork
- or the broken condition has been escalated explicitly to a broader boundary

## Traceability

- Maintenance mode: `generated`
- Upstream sources:
  - `docs/Authoritative/Canon/AgenticDevelopment/Protocols/Recovery-Protocol.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Mode-Bindings.md`
