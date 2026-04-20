---
id: context-atlas-mode-mutation-matrix
title: Context Atlas Mode Mutation Matrix
summary: Defines the classes of artifacts Context Atlas modes may mutate so mode state has concrete behavioral boundaries.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, modes, mutation-scope]
related:
  - ./Mode-Model.md
  - ./Mode-Transition-Rules.md
  - ./Role-Mode-Matrix.md
  - ./Role-Authority-Matrix.md
supersedes: []
---

# Context Atlas Mode Mutation Matrix

## Purpose

Define what classes of artifacts each Context Atlas mode may mutate so mode
state can guide later protocol and validation work.

## Scope

This document governs mode-to-artifact mutation classes only.

It does not define which role owns those artifacts. Role ownership and
approval authority remain separate concerns.

## Mutation Matrix

| Mode | Allowed Mutation Classes | Default Non-Goals / Not Allowed By Default |
| --- | --- | --- |
| `planning` | planning artifacts, decomposition updates, planning-oriented sequencing notes | primary feature delivery, review findings, merge/release execution |
| `implementation` | role-owned deliverable artifacts plus directly necessary validation or explanation updates | self-acceptance findings, merge/release actions, broad recovery reshaping |
| `review` | review findings, acceptance artifacts, validation evidence, QA-owned regression additions, proof summaries | primary product implementation, merge/release execution, unrelated scope expansion |
| `rework` | previously returned owned work plus directly necessary validation updates | unrelated new scope, approval actions, open-ended exploratory changes |
| `recovery` | recovery notes, state-reconstruction artifacts, bounded stabilization edits needed to restore workflow clarity | net-new feature scope, silent ownership transfer, ordinary completion work disguised as recovery |
| `operational_delivery` | merge/release artifacts, workflow definitions, versioning surfaces, release summaries, operational automation assets | ordinary feature implementation, self-acceptance findings, broad planning/decomposition rewrites |

## Binding Decisions

### 1. Mutation Scope Is Mode-Level, Not Role-Level

The matrix describes what kinds of surfaces a mode may touch in principle.

It does not answer:

- which role is accountable for those surfaces
- which role may approve them
- which exact protocol step is currently active

Those remain separate binding layers.

### 2. Review May Mutate Validation Surfaces, But Not Primary Owned Delivery

Context Atlas review work may add or adjust review findings, validation
evidence, proof artifacts, or QA-owned regression additions.

It should not quietly become the place where the reviewing role rewrites the
primary implementation on its own authority.

### 3. Rework Is Narrower Than Fresh Implementation

`rework` should stay bounded to the returned work and the directly necessary
supporting changes needed to satisfy the return contract.

It should not be used to smuggle in unrelated scope once review or recovery has
already narrowed the focus.

### 4. Recovery Mutations Must Be Minimal And Structural

`recovery` may touch artifacts needed to restore clarity or a safe workflow
path, but it should remain narrower than an ordinary implementation pass.

If recovery repeatedly becomes ordinary feature work, the workflow model is
being misused.

## Constraints

- The matrix should stay concrete enough to support later validation checks.
- Mode mutation classes should not be mistaken for role ownership or merge
  authority.
- If a role needs broader or narrower access inside a shared mode, that should
  be expressed in the role-to-mode overlay rather than by splitting the mode.

## Non-Goals

- Replace the role authority matrix.
- Define file-by-file mutation permissions.
- Define runtime-specific enforcement mechanisms.

## Related Artifacts

- [Context Atlas Mode Model](./Mode-Model.md)
- [Mode Transition Rules](./Mode-Transition-Rules.md)
- [Context Atlas Role-Mode Matrix](./Role-Mode-Matrix.md)
- [Context Atlas Role Authority Matrix](./Role-Authority-Matrix.md)
