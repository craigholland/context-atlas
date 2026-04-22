# Review Protocol

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the workflow path used when Context Atlas QA assesses a structured
review-intake contract and produces findings, readiness framing, and a
structured review outcome.

## Trigger / Enter Conditions

- a valid structured review-intake contract is received
- the reviewing boundary has enough scope and evidence to begin assessment

## Participating Roles And Modes

- Owning role:
  - `QA`
- Producing participants:
  - `Backend`
  - `Documentation/UAT`
  - other roles when their owned work is under review
- Primary mode:
  - `review`

## Structured Contract Expectations

- normally consumes `implementation_complete`
- carries gate scope through `scope_level` instead of ad hoc contract types
- requested review passes stay explicit:
  - `Task -> Story`: `code`
  - `Story -> Epic`: `architecture`, `security`
  - `Epic -> development`: `product`
- emits structured review outcomes such as:
  - `accepted`
  - `changes_required`
  - `needs_clarification`
  - `blocked`
  - `escalated`

## Exit Criteria

- requested review work is complete enough that the next action is explicit
- findings, acceptance state, and blocked conditions are structured rather than
  implied

## Traceability

- Maintenance mode: `generated`
- Upstream sources:
  - `docs/Authoritative/Canon/AgenticDevelopment/Protocols/Review-Protocol.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Mode-Bindings.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Gate-Review-Pass-Matrix.md`
