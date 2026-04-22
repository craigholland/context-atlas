# Escalation Protocol

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the workflow path used when a Context Atlas boundary cannot proceed
safely within its current authority and must return blocked or higher-judgment
state upward.

## Trigger / Enter Conditions

- the current boundary encounters a blocked or higher-authority condition
- safe progress would require widening scope beyond the current boundary

## Participating Roles And Modes

- no permanent owning top-level role
- used by the currently accountable boundary when authority or safe next action
  must move upward
- mode-spanning contract protocol:
  - commonly appears at blocked edges of planning, execution, review, rework,
    or recovery

## Structured Contract Expectations

- escalation contracts should preserve:
  - escalation reason
  - completed scope so far
  - unresolved items
  - broader target boundary
  - recommended next action
- escalation stays distinct from ordinary completion handoff and ordinary review
  findings

## Exit Criteria

- the broader boundary can resume decision-making without guessing why
  escalation occurred
- blocked state is explicit and traceable

## Traceability

- Maintenance mode: `generated`
- Upstream sources:
  - `docs/Authoritative/Canon/AgenticDevelopment/Protocols/Escalation-Protocol.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Mode-Bindings.md`
