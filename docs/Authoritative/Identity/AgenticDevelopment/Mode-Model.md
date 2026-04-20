---
id: context-atlas-mode-model
title: Context Atlas Mode Model
summary: Defines the initial project-specific execution mode set for Context Atlas and the semantics attached to each mode.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, modes, workflow-state]
related:
  - ../Context-Atlas-Agentic-Development-Profile.md
  - ./Role-Model.md
  - ./Role-Mode-Matrix.md
  - ./Mode-Transition-Rules.md
  - ./Mode-Mutation-Matrix.md
  - ./Mode-Transition-Graph.md
  - ../../AgenticDevelopment/Mode-Model.md
supersedes: []
---

# Context Atlas Mode Model

## Purpose

Define the initial project-specific execution mode set for Context Atlas so
execution state is governed explicitly instead of hiding inside role notes,
prompt habits, or protocol prose.

## Scope

This document defines the Context Atlas mode set and the project-level
semantics attached to each mode.

It does not replace the portable mode canon, and it does not define detailed
protocol sequencing, runtime-specific files, or vendor-specific discovery
rules.

## Binding Decisions

### 1. Context Atlas Uses Six Initial Modes

The initial project-specific mode set for Context Atlas is:

- `planning`
- `implementation`
- `review`
- `rework`
- `recovery`
- `operational_delivery`

This set is intentionally bounded. Context Atlas should not invent additional
modes casually when a workflow nuance can be expressed through protocol steps,
structured handoffs, or role constraints.

### 2. Modes Remain Execution States, Not Alternate Roles

Within Context Atlas, a mode describes how work is currently being performed.

It does not redefine:

- who is accountable for the work
- which protocol is being followed
- which runtime assets later materialize that work

That means role, protocol, and mode should remain distinct even when the same
role tends to appear in the same mode repeatedly.

### 3. Planning Covers Decomposition And Sequencing Work

`planning` is the execution state used when the current work is decomposition,
sequencing, dependency analysis, or planning-shape clarification.

It is not a synonym for project leadership, and it is not a substitute for
later protocol or review behavior.

### 4. Implementation Covers Role-Owned Deliverable Creation

`implementation` is the execution state used when a role is producing or
updating its owned deliverable surfaces.

For Context Atlas, that includes work such as product-engine changes and
Documentation/UAT deliverable changes. It does not include governed review
intake or operational merge/release actions.

### 5. Review Is A Distinct Acceptance-Oriented State

`review` is the execution state used when a valid structured review-intake
contract is being assessed and findings or acceptance outcomes are being
produced.

It should stay distinct from implementation so review judgment does not blur
into self-acceptance by the producing role.

### 6. Rework Is A Returned-Work State, Not A Generic Second Implementation Mode

`rework` is the execution state used when previously delivered work has been
returned with required changes or clarifications.

It exists so Context Atlas can distinguish:

- first-pass deliverable creation
- returned work that is being addressed under a structured review or recovery
  outcome

### 7. Recovery Handles Broken Or Ambiguous Workflow State

`recovery` is the execution state used when the current workflow cannot safely
proceed under ordinary planning, implementation, review, rework, or
operational-delivery assumptions.

It is the mode for restoring structural clarity, not for quietly continuing
new work under a vague blocked state.

### 8. Operational Delivery Is Distinct From Ordinary Implementation

`operational_delivery` is the execution state used for merge, release,
workflow, tagging, and similar repository-delivery actions that should not
collapse into ordinary implementation.

This keeps operational action explicit and prevents merge/release surfaces from
becoming ambient rights of every implementation role.

### 9. Modes May Recur Across Protocols

The same mode may appear in more than one protocol, and a single protocol may
remain in the same mode across several steps.

Context Atlas should therefore avoid modeling every protocol step as a unique
mode shift.

### 10. Structured Contracts Gate Movement Between Modes

Mode changes in Context Atlas should be driven by explicit structured
contracts, not by prose-only status changes.

That means mode entry and exit should be interpretable later through contract
artifacts and protocol rules rather than reconstructed from freeform comments.

## Constraints

- The mode set should remain small enough to govern clearly.
- Context Atlas should not add a new mode just because one role or runtime
  prefers a particular local workflow habit.
- Mode semantics must stay project-specific without drifting into vendor file
  conventions or runtime prompt syntax.

## Non-Goals

- Define every role-to-mode binding.
- Define every entry/exit condition or allowed mutation rule in this document.
- Define protocol-specific step sequences.
- Define runtime-specific files that materialize the mode model.

## Related Artifacts

- [Context Atlas Agentic Development Profile](../Context-Atlas-Agentic-Development-Profile.md)
- [Context Atlas Role Model](./Role-Model.md)
- [Context Atlas Role-Mode Matrix](./Role-Mode-Matrix.md)
- [Mode Transition Rules](./Mode-Transition-Rules.md)
- [Mode Mutation Matrix](./Mode-Mutation-Matrix.md)
- [Mode Transition Graph](./Mode-Transition-Graph.md)
- [Portable Mode Model](../../AgenticDevelopment/Mode-Model.md)
