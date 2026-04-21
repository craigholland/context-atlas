---
id: context-atlas-mode-transition-rules
title: Context Atlas Mode Transition Rules
summary: Defines entry conditions, exit conditions, and structured transition expectations for the Context Atlas mode model.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, modes, transitions]
related:
  - ./Mode-Model.md
  - ./Mode-Transition-Graph.md
  - ./Mode-Mutation-Matrix.md
  - ../Roles/Role-Mode-Matrix.md
  - ../../../Context-Atlas-Agentic-Development-Profile.md
supersedes: []
---

# Context Atlas Mode Transition Rules

## Purpose

Define how Context Atlas modes may be entered or exited so the mode model has
operational meaning instead of acting as a label set only.

## Scope

This document defines project-specific entry and exit expectations for each
Context Atlas mode.

It does not define the full protocol catalog, and it does not replace the
separate role or authority model.

## Binding Decisions

### 1. Mode Entry And Exit Must Be Explicit

Context Atlas should treat a mode as entered or exited only when the workflow
state makes that move explicit.

That means:

- mode shifts should not depend on silent prompt changes
- prose-only status updates are not enough to change execution state
- a structured contract, protocol step, or governed workflow event should make
  the transition legible

### 2. Planning

#### Enter

- when decomposition, sequencing, dependency clarification, or planning-shape
  revision is the current work
- when a prior review or recovery outcome routes work back to planning

#### Exit

- when a structured planning-output handoff is emitted for downstream work such
  as implementation or another protocol-defined next step
- when work is returned for rework or forced into recovery

### 3. Implementation

#### Enter

- when a role owns a bounded deliverable slice and the current work is
  producing that slice
- when recovery resolves into fresh deliverable work rather than continued
  planning or review

#### Exit

- when a structured completion handoff is emitted for downstream review or the
  next protocol-defined step
- when the work is blocked badly enough to require recovery

### 4. Review

#### Enter

- only when a valid structured review-intake contract exists
- when the current work is governed assessment, findings, or acceptance
  analysis rather than primary feature delivery

#### Exit

- when a structured review-outcome contract is emitted
- when the review outcome routes work to rework, operational delivery, or
  recovery

### 5. Rework

#### Enter

- when a valid return contract requests changes on already-delivered work
- when clarification or correction is the current work rather than first-pass
  delivery

#### Exit

- when a renewed structured completion handoff is emitted
- when the work becomes blocked or ambiguous enough to require recovery

### 6. Recovery

#### Enter

- when workflow state is broken, ambiguous, invalid, or materially blocked
- when a contract is missing, malformed, contradictory, or insufficient for
  safe continuation

#### Exit

- only through a structured recovery outcome that explicitly routes work into
  another mode

### 7. Operational Delivery

#### Enter

- when upstream readiness conditions are satisfied and the current work is
  merge, release, workflow, versioning, or similar operational action
- when an accepted review outcome or recovery outcome routes work to an
  operational next step

#### Exit

- when an operational outcome contract is emitted
- when an operational artifact is handed to review
- when the operational path becomes blocked badly enough to require recovery

## Constraints

- Mode rules should remain legible without turning into full protocol docs.
- Entry and exit rules should rely on structured state changes rather than
  conversational implication.
- Recovery should stay explicit instead of becoming a vague catch-all for work
  that simply lacks a clean handoff.

## Non-Goals

- Define the detailed shape of every handoff contract.
- Define full role applicability or mutation authority.
- Replace the later protocol model.

## Related Artifacts

- [Context Atlas Mode Model](./Mode-Model.md)
- [Mode Transition Graph](./Mode-Transition-Graph.md)
- [Mode Mutation Matrix](./Mode-Mutation-Matrix.md)
- [Context Atlas Role-Mode Matrix](../Roles/Role-Mode-Matrix.md)
- [Context Atlas Agentic Development Profile](../../../Context-Atlas-Agentic-Development-Profile.md)

