---
id: context-atlas-role-mode-matrix
title: Context Atlas Role-Mode Matrix
summary: Defines which Context Atlas roles may operate in which modes and what additional constraints apply when they do.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, roles, modes]
related:
  - ./Role-Model.md
  - ./Role-Authority-Matrix.md
  - ./Mode-Model.md
  - ./Mode-Mutation-Matrix.md
  - ./Mode-Transition-Rules.md
supersedes: []
---

# Context Atlas Role-Mode Matrix

## Purpose

Define which Context Atlas roles may operate in which modes and what
role-specific constraints still apply inside those shared mode semantics.

## Scope

This document governs role applicability and overlays for the mode model.

It does not redefine role ownership, approval authority, or protocol
sequencing.

## Applicability Matrix

`Primary` means the role commonly owns work in that mode.

`Conditional` means the role may enter the mode only under an explicit bounded
context.

`Not Expected` means the role should not normally be modeled there.

| Role | `planning` | `implementation` | `review` | `rework` | `recovery` | `operational_delivery` |
| --- | --- | --- | --- | --- | --- | --- |
| `Planner/Decomp` | Primary | Not Expected | Not Expected | Primary | Conditional | Not Expected |
| `Backend` | Conditional | Primary | Not Expected | Primary | Conditional | Not Expected |
| `Documentation/UAT` | Conditional | Primary | Not Expected | Primary | Conditional | Not Expected |
| `QA` | Not Expected | Not Expected | Primary | Conditional | Conditional | Not Expected |
| `DevOps` | Not Expected | Not Expected | Not Expected | Conditional | Conditional | Primary |

## Constraint Overlay

### Planner/Decomp

- `planning` is the normal state for parent-owned decomposition work.
- `rework` is allowed when planning artifacts are returned with required
  changes.
- `recovery` is conditional and should be used only when planning state is
  broken or ambiguous.

### Backend

- `planning` is conditional and should appear only under explicit
  Planner/Decomp-owned delegation for bounded technical analysis.
- `implementation` and `rework` apply to backend-owned deliverable work.
- `recovery` is conditional and should be used to restore workflow clarity, not
  to keep implementing under a blocked state.

### Documentation/UAT

- `planning` is conditional and should appear only under explicit
  Planner/Decomp-owned delegation for bounded evaluator-surface or
  documentation analysis.
- `implementation` and `rework` apply to documentation/UAT-owned deliverable
  work.
- `recovery` is conditional and should remain bounded to restoring a safe path.

### QA

- `review` is the primary QA mode.
- multiple required review passes may execute within the same `review` span
  without changing modes.
- `rework` is conditional and should be limited to QA-owned validation or
  review artifacts rather than core product implementation.
- if core deliverable changes are required, QA should return the work to the
  originating owning role instead of absorbing implementation ownership.

### DevOps

- `operational_delivery` is the primary DevOps mode.
- `rework` is conditional and should apply only to returned operational
  surfaces such as workflows, versioning, or release artifacts.
- `recovery` is conditional and should remain bounded to restoring a valid
  delivery path rather than bypassing upstream gates.

## Constraints

- Shared modes must not turn into role aliases.
- Role-specific constraints should narrow or clarify a shared mode, not invent
  a shadow mode set.
- The matrix should stay concise enough that protocols can consume it instead
  of restating it.

## Non-Goals

- Replace the role ownership or authority matrices.
- Define every protocol step for each role.
- Define runtime-specific files or prompts for mode selection.

## Related Artifacts

- [Context Atlas Role Model](./Role-Model.md)
- [Context Atlas Role Authority Matrix](./Role-Authority-Matrix.md)
- [Context Atlas Mode Model](./Mode-Model.md)
- [Mode Mutation Matrix](./Mode-Mutation-Matrix.md)
- [Mode Transition Rules](./Mode-Transition-Rules.md)
