---
id: craig-execution-slice-protocol
title: Execution Slice Protocol
summary: Defines the portable workflow used when an accountable boundary creates or updates owned deliverable surfaces and then emits structured completion state for downstream review or handoff.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, protocols, execution, implementation, workflow]
related:
  - ./Protocol-Template.md
  - ./Planning-Protocol.md
  - ./Review-Protocol.md
  - ./Rework-Protocol.md
supersedes: []
---

# Execution Slice Protocol

## Purpose

Define the portable workflow used when an accountable boundary creates or
updates owned deliverable surfaces as a bounded execution slice.

## Scope

This protocol governs first-pass deliverable creation from valid intake through
structured completion handoff.

It does not define returned-work rework behavior, and it does not define a
project's specific review gate map.

## Actors

- the accountable producing boundary
- optional bounded delegates participating under that boundary
- the downstream boundary that will review, accept, or otherwise receive the
  work

## Trigger / Entry Conditions

- a valid planning or upstream handoff contract authorizes execution
- the producing boundary owns the target deliverable surface

## Preconditions

- owned surfaces and scope boundaries are explicit
- the producing boundary knows the intended deliverable outcome
- required upstream constraints are available in structured form

## Allowed Mutations

- the owned deliverable surfaces for the current bounded slice
- supporting verification artifacts or evidence linked to that slice

This protocol should not silently mutate unrelated workflow or operational
surfaces merely because they are nearby.

## Required Inputs

- a structured planning or upstream handoff contract
- relevant authoritative constraints
- any verification expectations already attached to the slice

## Required Outputs

- a structured completion handoff contract
- changed deliverable surfaces
- stated verification or evidence results
- any declared risks, assumptions, or unresolved follow-up needs

## Exit Criteria

- the producing boundary has finished its bounded slice
- downstream review or next-step intake can proceed without guessing what was
  changed or what was verified

## Handoff Targets

- [Review Protocol](./Review-Protocol.md)
- [Recovery Protocol](./Recovery-Protocol.md)
- another downstream protocol when review is intentionally not the next step

## Escalation Conditions

- required scope or authority is ambiguous
- blocked conditions prevent safe completion
- the next needed mutation lies outside the producing boundary's allowed scope

## Constraints

- execution slices should stay bounded enough that downstream review remains
  legible
- completion state should be emitted as structured handoff content rather than
  prose-only completion claims
- delegates may contribute work without becoming the producing owner

## Non-Goals

- define project-specific code review rules
- replace rework, review, or recovery workflows
- silently self-accept produced work

## Related Artifacts

- [Protocol Template](./Protocol-Template.md)
- [Planning Protocol](./Planning-Protocol.md)
- [Review Protocol](./Review-Protocol.md)
- [Rework Protocol](./Rework-Protocol.md)
