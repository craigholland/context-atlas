---
id: craig-delegation-protocol
title: Delegation Protocol
summary: Defines the portable workflow and structured contract shape used when a broader authority boundary delegates bounded work to a narrower one without transferring ownership.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, protocols, delegation, contracts, workflow]
related:
  - ./Protocol-Template.md
  - ./Handoff-Protocol.md
  - ./Escalation-Protocol.md
  - ../Delegation-Model.md
supersedes: []
---

# Delegation Protocol

## Purpose

Define the portable workflow used when a broader authority boundary delegates
bounded work to a narrower one without transferring accountability.

## Scope

This protocol governs delegation from delegation intent through structured
delegation contract emission and bounded return.

It does not replace the broader delegation model, and it does not define
project-specific worker-discovery behavior.

## Actors

- the delegating boundary
- the delegated boundary
- any broader boundary that may receive escalation back from the delegate

## Trigger / Entry Conditions

- the current boundary identifies a bounded sub-scope that should be performed
  elsewhere
- delegation is structurally preferable to widening current scope

## Preconditions

- the delegated scope is bounded enough to describe explicitly
- the delegating boundary retains accountability for the delegated work unless a
  separate handoff explicitly changes ownership
- the delegated boundary is known or discoverable within the system

## Allowed Mutations

- structured delegation contracts
- bounded delegated-scope notes
- explicit return and escalation instructions tied to that delegated scope

## Required Inputs

- the bounded scope being delegated
- constraints that apply during delegated work
- the expected return shape
- any escalation rules already known

## Required Outputs

- a structured delegation contract that identifies:
  - delegation scope
  - applicable constraints
  - expected outputs
  - return conditions
  - escalation conditions

Example shape:

```yaml
contract_type: delegation
scope_level: task
source_boundary: parent_boundary
target_boundary: delegated_boundary
target_protocol: execution_slice
bounded_scope:
  description: implement the requested bounded work
constraints:
  - stay within the delegated surface
expected_outputs:
  - structured completion or blocked-state return
return_conditions:
  success_contract: handoff
  blocked_contract: escalation
```

## Exit Criteria

- the delegated boundary can begin work without guessing the bounded scope
- the delegating boundary's retained accountability remains explicit

## Handoff Targets

- [Handoff Protocol](./Handoff-Protocol.md)
- [Escalation Protocol](./Escalation-Protocol.md)

## Escalation Conditions

- the delegated scope is not actually bounded enough to assign safely
- the delegated boundary cannot perform the work within the stated constraints
- downstream scope overflow requires return to a broader boundary

## Constraints

- delegation must not silently transfer ownership, approval, or merge authority
- delegated scope should stay narrow enough that return conditions remain
  legible
- structured delegation state should be sufficient for later validation and
  resumption

## Non-Goals

- define project-specific specialist rosters
- replace handoff or escalation workflows
- treat delegation as a casual prose instruction only

## Related Artifacts

- [Protocol Template](./Protocol-Template.md)
- [Handoff Protocol](./Handoff-Protocol.md)
- [Escalation Protocol](./Escalation-Protocol.md)
- [Delegation Model](../Delegation-Model.md)
