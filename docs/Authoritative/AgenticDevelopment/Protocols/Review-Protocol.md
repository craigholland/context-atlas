---
id: craig-review-protocol
title: Review Protocol
summary: Defines the portable workflow used when a structured review-intake contract is assessed and review outcomes are produced through one or more explicit review passes.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, protocols, review, qa, workflow]
related:
  - ./Protocol-Template.md
  - ./Review-Pass-Model.md
  - ./Handoff-Protocol.md
  - ./Escalation-Protocol.md
  - ./Rework-Protocol.md
  - ./Recovery-Protocol.md
supersedes: []
---

# Review Protocol

## Purpose

Define the portable workflow used when a structured review-intake contract is
assessed and review outcomes are produced.

## Scope

This protocol governs review from valid intake through structured outcome.

It does not define a project's specific gate-to-pass map or runtime-specific PR
comment behavior.

## Actors

- the accountable reviewing boundary
- the producing boundary whose work is being assessed
- any downstream boundary that will receive accepted or rejected review state

## Trigger / Entry Conditions

- a valid structured review-intake contract is received
- the reviewing boundary has enough scope and evidence to begin assessment

## Preconditions

- the intake identifies the reviewed scope
- required evidence or verification results are available
- requested review passes are explicit when the workflow requires them

## Gate Context

Review may occur at different workflow gates.

Portable protocol semantics allow gate context to be carried explicitly without
embedding one project's gate map into the protocol itself.

## Review Pass Expectations

- one or more review passes may be requested for the same review intake
- requested passes should be treated as evaluation lenses, not as separate
  workflow families
- omitted passes should be visible rather than silently assumed complete

## Allowed Mutations

- structured review findings
- structured review outcome state
- review evidence or acceptance-analysis artifacts

This protocol should not silently rewrite the produced deliverable surface as a
substitute for returning findings or outcome state.

## Required Inputs

- a structured review-intake contract
- relevant changed-surface or produced-surface context
- any verification evidence referenced by the intake
- requested review passes when the workflow uses explicit pass selection

Review intake should follow the structured handoff semantics from
[Handoff Protocol](./Handoff-Protocol.md) when review is entered from upstream
completion state.

## Required Outputs

- a structured review-outcome contract
- any findings emitted during review
- explicit pass-level outcome state when passes are tracked distinctly
- a named recommended next action

## Review Outcome States

Typical review outcomes include:

- `accepted`
- `changes_required`
- `needs_clarification`
- `blocked`
- `escalated`

Projects may refine those outcomes downstream so long as the resulting state
remains structured.

## Exit Criteria

- the requested review work is complete enough that downstream action can begin
  without guessing the reviewer outcome
- any findings or blocked state are explicit

## Handoff Targets

- [Rework Protocol](./Rework-Protocol.md)
- [Recovery Protocol](./Recovery-Protocol.md)
- a downstream approval or delivery protocol when review accepts the work

## Escalation Conditions

- the review intake is invalid or incomplete
- contradictory evidence prevents a safe outcome
- required authority lies outside the reviewing boundary

## Constraints

- review should remain independent from the producing boundary's self-claim of
  completion
- pass execution should stay inside one review workflow rather than becoming a
  separate role or mode system
- outcome state should stay structured enough for later automation and
  validation

## Non-Goals

- define project-specific gate policy
- define project-specific review comment formatting
- silently convert review into implementation ownership

## Related Artifacts

- [Protocol Template](./Protocol-Template.md)
- [Review Pass Model](./Review-Pass-Model.md)
- [Handoff Protocol](./Handoff-Protocol.md)
- [Escalation Protocol](./Escalation-Protocol.md)
- [Rework Protocol](./Rework-Protocol.md)
- [Recovery Protocol](./Recovery-Protocol.md)
