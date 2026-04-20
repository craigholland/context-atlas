---
id: craig-handoff-protocol
title: Handoff Protocol
summary: Defines the portable workflow and structured contract shape used when completed work or clarified workflow state moves from one authority boundary to another.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, protocols, handoff, contracts, workflow]
related:
  - ./Protocol-Template.md
  - ./Review-Protocol.md
  - ./Escalation-Protocol.md
  - ../Escalation-Model.md
supersedes: []
---

# Handoff Protocol

## Purpose

Define the portable workflow used when completed work or clarified workflow
state moves from one authority boundary to another.

## Scope

This protocol governs ordinary workflow handoff from structured completion or
clarification output through valid downstream intake.

It does not replace escalation for blocked-state return, and it does not define
project-specific PR or comment surfaces.

## Actors

- the source boundary completing or clarifying work
- the target boundary receiving the next-step responsibility

## Trigger / Entry Conditions

- the source boundary has completed a bounded slice
- or the source boundary has produced valid clarified state for downstream work

## Preconditions

- the downstream target is known
- the next action is explicit
- the source boundary can describe what was completed, what remains open, and
  what downstream work is expected

## Allowed Mutations

- structured handoff contracts
- explicit next-step and downstream-intake state

## Required Inputs

- completed or clarified workflow state
- the intended downstream target and next action
- any verification or evidence results the downstream boundary needs

## Required Outputs

- a structured handoff contract identifying:
  - contract type
  - source boundary
  - target boundary
  - target protocol
  - scope level
  - changed or relevant artifacts
  - verification state
  - open risks or assumptions
  - required review passes when review is the next action

Example `implementation_complete` handoff shape:

```yaml
contract_type: implementation_complete
scope_level: task
source_boundary: producing_boundary
target_boundary: reviewing_boundary
target_protocol: review
required_review_passes:
  - code
artifacts:
  changed_surfaces:
    - path/to/changed_surface
verification:
  summary:
    - required checks passed
open_risks:
  - none
requested_next_action: review_intake
```

### `implementation_complete` Scope Semantics

`implementation_complete` is the portable completion-handoff contract type for
work that has reached a governed review or downstream-intake boundary.

Projects should reuse that contract type across multiple workflow levels
instead of inventing a different completion contract type for each gate.

The workflow level should be carried by `scope_level`, for example:

- `task` for task-completion intake
- `story` for story-completion intake
- `epic` for epic-completion intake

When review is the next action, downstream bindings may use `scope_level`
together with `required_review_passes` to determine which governed review work
must occur at the receiving gate.

## Exit Criteria

- downstream intake can begin without reconstructing the upstream state from
  prose
- the next workflow step is explicit

## Handoff Targets

- [Review Protocol](./Review-Protocol.md)
- [Planning Protocol](./Planning-Protocol.md)
- [Execution Slice Protocol](./Execution-Slice-Protocol.md)
- [Recovery Protocol](./Recovery-Protocol.md)

## Escalation Conditions

- the downstream target is unclear
- the next action cannot be expressed safely
- blocked state should be returned upward instead of handed forward

## Constraints

- handoff contracts should remain structured and machine-readable
- requested review-pass state should stay explicit when review is the next step
- handoff should not be used to hide blocked or escalated state that needs a
  different protocol

## Non-Goals

- replace escalation
- define project-specific role names or branch names
- rely on freeform prose as the canonical handoff mechanism

## Related Artifacts

- [Protocol Template](./Protocol-Template.md)
- [Review Protocol](./Review-Protocol.md)
- [Escalation Protocol](./Escalation-Protocol.md)
- [Escalation Model](../Escalation-Model.md)
