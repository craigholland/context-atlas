---
id: craig-recovery-protocol
title: Recovery Protocol
summary: Defines the portable workflow used when ordinary planning, execution, review, or rework cannot proceed safely because workflow state, ownership, or contract integrity is broken or unclear.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, protocols, recovery, blocked-state, workflow]
related:
  - ./Protocol-Template.md
  - ./Planning-Protocol.md
  - ./Review-Protocol.md
  - ./Rework-Protocol.md
supersedes: []
---

# Recovery Protocol

## Purpose

Define the portable workflow used when ordinary workflow progression cannot
continue safely because state, ownership, or contract integrity is broken or
unclear.

## Scope

This protocol governs restoration of workable state.

It does not replace ordinary planning, execution, review, or rework when those
can proceed safely under valid structured state.

## Actors

- the boundary responsible for recovering workable state
- any upstream or downstream boundary whose state is implicated in the break

## Trigger / Entry Conditions

- structured workflow state is missing, contradictory, or invalid
- ownership or allowed mutation scope is unclear
- ordinary protocol progression would require guesswork to continue

## Preconditions

- the broken or ambiguous condition is identifiable
- the recovering boundary has enough visibility to diagnose the break

## Allowed Mutations

- recovery notes or state-restoration artifacts
- explicit contract corrections
- clarified ownership or next-step declarations

Recovery should avoid unrelated deliverable creation unless the recovery result
explicitly re-enters another protocol.

## Required Inputs

- the broken or ambiguous workflow state
- any available prior contracts or evidence that explain how the break occurred

## Required Outputs

- a structured recovery-outcome contract
- clarified next-step ownership
- the recommended next protocol or escalation target

## Exit Criteria

- workflow can re-enter another protocol without guesswork
- or the broken state has been escalated explicitly to a broader boundary

## Handoff Targets

- [Planning Protocol](./Planning-Protocol.md)
- [Execution Slice Protocol](./Execution-Slice-Protocol.md)
- [Review Protocol](./Review-Protocol.md)
- [Rework Protocol](./Rework-Protocol.md)

## Escalation Conditions

- the recovering boundary cannot restore workable state within its authority
- required clarification depends on a broader ownership decision

## Constraints

- recovery should restore clarity, not quietly continue work under vague state
- recovery outputs should make the next workflow step explicit
- recovery should preserve traceability to the broken condition it addressed

## Non-Goals

- become a catch-all substitute for every ordinary workflow
- hide ownership or contract mistakes under vague blocked-state language
- replace upstream protocol design with recovery improvisation

## Related Artifacts

- [Protocol Template](./Protocol-Template.md)
- [Planning Protocol](./Planning-Protocol.md)
- [Review Protocol](./Review-Protocol.md)
- [Rework Protocol](./Rework-Protocol.md)
