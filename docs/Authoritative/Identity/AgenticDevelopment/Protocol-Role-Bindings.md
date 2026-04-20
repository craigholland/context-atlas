---
id: context-atlas-protocol-role-bindings
title: Context Atlas Protocol Role Bindings
summary: Defines how the Context Atlas role model binds to the shared protocol family so protocol ownership and participation remain explicit without collapsing into role redefinitions.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, protocols, roles]
related:
  - ./Role-Model.md
  - ./Role-Authority-Matrix.md
  - ./Gate-Review-Pass-Matrix.md
  - ../../Canon/AgenticDevelopment/Protocols/Planning-Protocol.md
  - ../../Canon/AgenticDevelopment/Protocols/Execution-Slice-Protocol.md
  - ../../Canon/AgenticDevelopment/Protocols/Review-Protocol.md
  - ../../Canon/AgenticDevelopment/Protocols/Rework-Protocol.md
  - ../../Canon/AgenticDevelopment/Protocols/Recovery-Protocol.md
  - ../../Canon/AgenticDevelopment/Protocols/Delegation-Protocol.md
  - ../../Canon/AgenticDevelopment/Protocols/Handoff-Protocol.md
  - ../../Canon/AgenticDevelopment/Protocols/Escalation-Protocol.md
supersedes: []
---

# Context Atlas Protocol Role Bindings

## Purpose

Define how Context Atlas roles bind to the shared protocol family.

## Scope

This document governs protocol participation and ownership by role.

It does not redefine role accountability, approval authority, or mode
semantics.

## Binding Decisions

### 1. Planning Protocol Is Planner/Decomp-Owned

`Planner/Decomp` is the normal owning role for the
[Planning Protocol](../../Canon/AgenticDevelopment/Protocols/Planning-Protocol.md).

`Backend` and `Documentation/UAT` may participate in bounded planning work
through explicit delegation, but they do not become planning owners by default.

### 2. Execution Slice Protocol Is Deliverable-Owner-Owned

The [Execution Slice Protocol](../../Canon/AgenticDevelopment/Protocols/Execution-Slice-Protocol.md)
is normally owned by the role that owns the deliverable surface.

For the current repository, that means:

- `Backend` for backend-owned product surfaces
- `Documentation/UAT` for user-facing documentation, examples, and evaluation
  surfaces

`Planner/Decomp`, `QA`, and `DevOps` do not normally own first-pass execution
for those surfaces.

### 3. Review Protocol Is QA-Owned

`QA` is the owning role for the
[Review Protocol](../../Canon/AgenticDevelopment/Protocols/Review-Protocol.md).

Producing roles participate as:

- the source of structured completion handoffs
- the responder to findings or clarification requests

They do not become the owning review boundary merely because they produced the
work.

### 4. Rework Protocol Returns To The Owning Producing Role

The [Rework Protocol](../../Canon/AgenticDevelopment/Protocols/Rework-Protocol.md)
normally returns work to the role that owns the affected deliverable surface.

That means:

- backend rework returns to `Backend`
- documentation and evaluator-surface rework returns to `Documentation/UAT`
- planning-artifact rework returns to `Planner/Decomp`
- operational-surface rework returns to `DevOps`

`QA` may perform rework only on QA-owned validation or review artifacts.

### 5. Recovery Protocol Is Context-Dependent But Not Ownership-Free

The [Recovery Protocol](../../Canon/AgenticDevelopment/Protocols/Recovery-Protocol.md)
may be entered by multiple roles, but recovery ownership should remain with the
role closest to the broken workflow state unless explicit escalation changes
that.

### 6. Delegation, Handoff, And Escalation Are Cross-Cutting Protocols

The delegation, handoff, and escalation protocols are cross-cutting.

They are not owned by one permanent top-level role. Instead, they are used by
the currently accountable role while moving work across boundaries.

### 7. QA Owns Review-Pass Execution

Review-pass execution belongs to `QA`.

Producing roles may:

- emit structured completion handoffs
- respond to findings
- provide rationale or patch work

They do not self-execute the required QA pass as a substitute for independent
review.

### 8. DevOps Consumes Review State For Merge And Release Decisions

`DevOps` is normally a downstream consumer of structured review outcomes rather
than the owner of the review workflow itself.

That means merge or release action should rely on explicit upstream review
state instead of bypassing it.

## Constraints

- Protocol ownership should remain distinct from mere participation.
- Review ownership should stay with QA even when implementation roles supply
  evidence or respond to findings.
- Cross-cutting protocols should not be mistaken for a separate top-level role
  family.

## Non-Goals

- Replace the role accountability or authority matrices.
- Define the mode mapping for each protocol.
- Define runtime-specific worker or PR names.

## Related Artifacts

- [Context Atlas Role Model](./Role-Model.md)
- [Context Atlas Role Authority Matrix](./Role-Authority-Matrix.md)
- [Gate Review Pass Matrix](./Gate-Review-Pass-Matrix.md)
- [Planning Protocol](../../Canon/AgenticDevelopment/Protocols/Planning-Protocol.md)
- [Execution Slice Protocol](../../Canon/AgenticDevelopment/Protocols/Execution-Slice-Protocol.md)
- [Review Protocol](../../Canon/AgenticDevelopment/Protocols/Review-Protocol.md)
- [Rework Protocol](../../Canon/AgenticDevelopment/Protocols/Rework-Protocol.md)
- [Recovery Protocol](../../Canon/AgenticDevelopment/Protocols/Recovery-Protocol.md)
- [Delegation Protocol](../../Canon/AgenticDevelopment/Protocols/Delegation-Protocol.md)
- [Handoff Protocol](../../Canon/AgenticDevelopment/Protocols/Handoff-Protocol.md)
- [Escalation Protocol](../../Canon/AgenticDevelopment/Protocols/Escalation-Protocol.md)

