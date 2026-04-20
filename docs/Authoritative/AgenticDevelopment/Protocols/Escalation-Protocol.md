---
id: craig-escalation-protocol
title: Escalation Protocol
summary: Defines the portable workflow and structured contract shape used when a boundary cannot proceed safely within its authority and must return blocked or higher-judgment state upward.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, protocols, escalation, contracts, workflow]
related:
  - ./Protocol-Template.md
  - ./Handoff-Protocol.md
  - ./Recovery-Protocol.md
  - ../Escalation-Model.md
supersedes: []
---

# Escalation Protocol

## Purpose

Define the portable workflow used when a boundary cannot proceed safely within
its authority and must return blocked or higher-judgment state upward.

## Scope

This protocol governs escalation from blocked-state detection through a
structured escalation contract.

It does not replace ordinary handoff when work can move forward cleanly.

## Actors

- the escalating boundary
- the broader boundary receiving the escalation

## Trigger / Entry Conditions

- the current boundary encounters a blocked or higher-authority condition
- safe progress would require widening scope beyond the current boundary

## Preconditions

- the blocked condition is identifiable
- the escalating boundary can describe what was completed and what remains
  unresolved

## Allowed Mutations

- structured escalation contracts
- explicit blocked-state and recommended-next-action records

## Required Inputs

- the blocked or unresolved condition
- any relevant completed work or partial outputs
- the broader boundary that should receive the escalation

## Required Outputs

- a structured escalation contract identifying:
  - escalation reason
  - completed scope so far
  - unresolved items
  - broader boundary being asked to act
  - recommended next action

Example shape:

```yaml
contract_type: escalation
scope_level: task
source_boundary: delegated_boundary
target_boundary: broader_boundary
reason: required decision exceeds delegated authority
completed_scope:
  - bounded analysis completed
unresolved_items:
  - approval needed for next mutation
recommended_next_action: broader judgment
```

## Exit Criteria

- the broader boundary can resume decision-making without guessing why
  escalation occurred
- blocked state is explicit and traceable

## Handoff Targets

- [Recovery Protocol](./Recovery-Protocol.md)
- [Planning Protocol](./Planning-Protocol.md)
- [Review Protocol](./Review-Protocol.md)

## Escalation Conditions

- the current boundary cannot safely continue within allowed scope
- approval, ownership, or structural judgment must move upward
- contradictory signals prevent a clean handoff forward

## Constraints

- escalation contracts should preserve what was completed before the block
- escalation should not silently transfer final authority; it should request it
- escalation should stay distinct from ordinary review findings or ordinary
  completion handoff

## Non-Goals

- replace recovery work after escalation is received
- disguise scope overflow as ordinary completion
- define project-specific approval actors

## Related Artifacts

- [Protocol Template](./Protocol-Template.md)
- [Handoff Protocol](./Handoff-Protocol.md)
- [Recovery Protocol](./Recovery-Protocol.md)
- [Escalation Model](../Escalation-Model.md)
