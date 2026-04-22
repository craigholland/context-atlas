# Execution Slice Protocol

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Materialize the workflow path used when a Context Atlas producing role creates
or updates an owned deliverable surface as a bounded first-pass execution
slice.

## Trigger / Enter Conditions

- a valid planning or upstream handoff contract authorizes execution
- the producing boundary owns the target deliverable surface

## Participating Roles And Modes

- Owning roles:
  - `Backend`
  - `Documentation/UAT`
- Common delegated participant:
  - backend-oriented implementation specialists
- Primary mode:
  - `implementation`

## Structured Contract Expectations

- consumes a structured planning or upstream handoff contract
- may use `delegation` for bounded specialist work
- emits a structured `implementation_complete` handoff when review is next
- should include changed surfaces, verification summary, and open risks

## Exit Criteria

- the bounded slice is complete enough for governed downstream intake
- review or next-step consumers do not have to guess what changed or what was
  verified

## Traceability

- Maintenance mode: `generated`
- Upstream sources:
  - `docs/Authoritative/Canon/AgenticDevelopment/Protocols/Execution-Slice-Protocol.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Role-Bindings.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Protocols/Protocol-Mode-Bindings.md`
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
