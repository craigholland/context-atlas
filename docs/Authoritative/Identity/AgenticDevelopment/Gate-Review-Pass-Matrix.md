---
id: context-atlas-gate-review-pass-matrix
title: Context Atlas Gate Review Pass Matrix
summary: Defines which QA review passes are required at each governed workflow gate in Context Atlas and clarifies when earlier additional passes are warranted.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, review, qa, gates]
related:
  - ./Role-Authority-Matrix.md
  - ./Protocol-Role-Bindings.md
  - ../Canon/RepoManagement/GitHub/Agentic-Integration-Model.md
  - ../../Canon/AgenticDevelopment/Protocols/Review-Pass-Model.md
  - ../../Canon/AgenticDevelopment/Protocols/Review-Protocol.md
supersedes: []
---

# Context Atlas Gate Review Pass Matrix

## Purpose

Define which QA review passes are required at each governed workflow gate in
Context Atlas.

## Scope

This document maps project workflow gates to required review passes.

It does not redefine the portable review-pass taxonomy, and it does not define
runtime-specific provider permissions or merge rights.

## Gate Review Pass Matrix

| Workflow Gate | Required Review Passes | Typical Intake Contract | Default QA Outcome Target |
| --- | --- | --- | --- |
| `Task -> Story` | `code` | `implementation_complete` with `scope_level: task` | readiness for Story-branch integration |
| `Story -> Epic` | `architecture`, `security` | `implementation_complete` with `scope_level: story` | readiness for Epic-branch integration |
| `Epic -> development` | `product` | `implementation_complete` with `scope_level: epic` | readiness for `development` merge |

## Binding Decisions

### 1. Task-Level Review Defaults To Code Pass

The default QA review at the `Task -> Story` gate is the `code` pass.

That pass checks the local changed-surface correctness and implementation
quality of the completed task slice before the Story branch absorbs it.

### 2. Story-Level Review Defaults To Architecture And Security Passes

The default QA review at the `Story -> Epic` gate is the combination of:

- `architecture`
- `security`

This gate checks whether the completed Story preserved structural integrity and
introduced no unreviewed security or authority drift before the Epic branch
absorbs it.

### 3. Epic-Level Review Defaults To Product Pass

The default QA review at the `Epic -> development` gate is the `product` pass.

This gate checks whether the assembled Epic delivers a coherent user-facing or
operator-facing outcome and whether the visible product surfaces remain aligned.

### 4. Additional Earlier Passes Are Allowed By Risk Or Escalation

Context Atlas may request additional passes earlier than the default gate map
when:

- the current scope carries unusual security risk
- the current scope materially changes user-facing product surfaces
- escalation or recovery determines that a broader pass is needed before the
  normal gate

Those earlier passes should be explicit in the structured review-intake
contract rather than assumed informally.

### 5. Gate Level Should Be Carried By `scope_level`

This gate map does not create separate completion contract types for each
workflow gate.

The normal structured review-intake contract remains
`implementation_complete`, and the gate level should be carried through
`scope_level`, for example:

- `task`
- `story`
- `epic`

This keeps the portable contract catalog small while still allowing downstream
bindings and validators to distinguish gate-specific review requirements.

### 6. Gate Mapping Does Not Create New Roles Or Modes

This matrix maps QA review passes onto workflow gates.

It does not create:

- a separate QA role per pass
- a separate execution mode per pass
- a separate protocol family per pass

### 7. The Current Review Surface Is Bound Downstream

This matrix defines which QA passes are required at each workflow gate.

The current GitHub PR review surface, principal behavior, and merge
integration remain downstream concerns defined by the RepoManagement binding.

## Constraints

- The gate map should remain small and explicit.
- Additional passes should be justified by real risk, not habit.
- Gate bindings should remain downstream of the portable review-pass model.

## Non-Goals

- Redefine the portable review-pass taxonomy.
- Define every possible future gate.
- Define runtime-specific automation triggers.

## Related Artifacts

- [Context Atlas Role Authority Matrix](./Role-Authority-Matrix.md)
- [Protocol Role Bindings](./Protocol-Role-Bindings.md)
- [GitHub Agentic Integration Model](../Canon/RepoManagement/GitHub/Agentic-Integration-Model.md)
- [Review Pass Model](../../Canon/AgenticDevelopment/Protocols/Review-Pass-Model.md)
- [Review Protocol](../../Canon/AgenticDevelopment/Protocols/Review-Protocol.md)

