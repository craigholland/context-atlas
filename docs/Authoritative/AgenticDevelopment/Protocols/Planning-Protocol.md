---
id: craig-planning-protocol
title: Planning Protocol
summary: Defines the portable workflow for decomposition, sequencing, and planning output so planning state can move into later execution through explicit structured handoff.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, protocols, planning, decomposition, workflow]
related:
  - ./Protocol-Template.md
  - ./Execution-Slice-Protocol.md
  - ./Recovery-Protocol.md
  - ../Agent-Authority-Model.md
supersedes: []
---

# Planning Protocol

## Purpose

Define the portable workflow used when work must be decomposed, sequenced, or
clarified before safe deliverable creation can proceed.

## Scope

This protocol governs planning work from intake through structured planning
output.

It does not define a project's role roster, planning artifact naming, or
runtime-specific planning prompts.

## Actors

- the accountable planning boundary
- optional bounded delegates participating under that planning boundary
- the downstream boundary that will receive planning output

## Trigger / Entry Conditions

- a new work scope requires decomposition or sequencing
- execution cannot proceed safely because planning shape is incomplete
- recovery returns work for replanning or structural clarification

## Preconditions

- the work scope is identifiable enough to plan against
- relevant authoritative inputs are discoverable
- the planning boundary is known

## Allowed Mutations

- planning artifacts
- decomposition artifacts
- sequencing notes
- explicit risk and dependency notes

This protocol should not be used for ordinary deliverable-producing mutations.

## Required Inputs

- a planning-intake contract or equivalent structured statement of scope
- relevant authoritative inputs
- any current dependency, risk, or sequencing context already known

## Required Outputs

- a structured planning-output contract
- identified scope slices or work phases
- stated dependencies, risks, and blocked conditions
- a named downstream handoff target when one is ready

## Exit Criteria

- the work has a governed next shape
- the downstream boundary and recommended next action are explicit
- unresolved risks and unknowns are surfaced rather than hidden

## Handoff Targets

- [Execution Slice Protocol](./Execution-Slice-Protocol.md)
- [Recovery Protocol](./Recovery-Protocol.md)
- a downstream review or approval surface when planning itself is the scope

## Escalation Conditions

- authoritative guidance is contradictory or missing
- the planning boundary cannot determine a safe next slice
- required downstream ownership is unclear

## Constraints

- planning output should remain structured enough that execution does not have
  to reconstruct scope from prose alone
- planning should prefer bounded next slices over oversized ambiguous output
- delegates may contribute analysis without becoming the planning owner

## Non-Goals

- perform ordinary deliverable creation
- replace the execution or review workflow families
- define project-specific branch, file, or PR conventions

## Related Artifacts

- [Protocol Template](./Protocol-Template.md)
- [Execution Slice Protocol](./Execution-Slice-Protocol.md)
- [Recovery Protocol](./Recovery-Protocol.md)
- [Agent Authority Model](../Agent-Authority-Model.md)
