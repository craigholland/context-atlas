---
id: craig-rework-protocol
title: Rework Protocol
summary: Defines the portable workflow used when previously delivered work has been returned with findings, required changes, or clarifications and must be addressed under structured review state.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, protocols, rework, review, workflow]
related:
  - ./Protocol-Template.md
  - ./Review-Protocol.md
  - ./Execution-Slice-Protocol.md
  - ./Recovery-Protocol.md
supersedes: []
---

# Rework Protocol

## Purpose

Define the portable workflow used when previously delivered work has been
returned with findings, required changes, or clarifications.

## Scope

This protocol governs returned work from structured rework intake through a new
completion handoff.

It does not replace first-pass execution or recovery of broken workflow state.

## Actors

- the accountable boundary performing the returned work
- any reviewing boundary that produced the rework-triggering outcome
- any downstream boundary that will receive rework completion

## Trigger / Entry Conditions

- a structured review-outcome or recovery contract returns work for correction
  or clarification

## Preconditions

- the returned findings or required changes are explicit
- the accountable boundary for the returned work is known

## Allowed Mutations

- the previously delivered owned surfaces that must change to address the
  returned state
- supporting evidence or clarification artifacts linked to that rework

## Required Inputs

- a structured review-outcome or recovery contract
- the relevant returned findings or clarification requests
- any prior completion state that the rework must supersede or amend

## Required Outputs

- a structured rework-completion contract
- updated deliverable surfaces as needed
- explicit linkage to the returned findings or requests that were addressed

## Exit Criteria

- the returned-work scope has been addressed or explicitly escalated
- downstream review or next-step intake can see what was changed and why

## Handoff Targets

- [Review Protocol](./Review-Protocol.md)
- [Recovery Protocol](./Recovery-Protocol.md)

## Escalation Conditions

- the returned findings conflict or cannot be satisfied safely
- the required changes exceed the boundary's owned scope
- structural ambiguity means recovery is needed before rework can continue

## Constraints

- rework should remain visibly distinct from first-pass execution
- rework output should preserve traceability back to the returned findings or
  requests
- rework should not silently discard the prior review state that caused it

## Non-Goals

- replace ordinary execution slices
- define project-specific approval loops
- treat all returned work as recovery

## Related Artifacts

- [Protocol Template](./Protocol-Template.md)
- [Review Protocol](./Review-Protocol.md)
- [Execution Slice Protocol](./Execution-Slice-Protocol.md)
- [Recovery Protocol](./Recovery-Protocol.md)
