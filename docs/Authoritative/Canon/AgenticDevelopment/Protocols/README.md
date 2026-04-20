---
id: craig-agentic-protocols-readme
title: Protocols
summary: Introduces the portable protocol canon for agentic development and orients readers to the shared workflow surfaces and template that downstream bindings should inherit.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, protocols, workflow, canon]
related:
  - ../README.md
  - ./Protocol-Template.md
  - ./Planning-Protocol.md
  - ./Execution-Slice-Protocol.md
  - ./Review-Pass-Model.md
  - ./Review-Protocol.md
  - ./Rework-Protocol.md
  - ./Recovery-Protocol.md
  - ./Delegation-Protocol.md
  - ./Handoff-Protocol.md
  - ./Escalation-Protocol.md
supersedes: []
---

# Protocols

## Purpose

Introduce the portable protocol canon for agentic development.

This surface defines shared workflow concepts and reusable protocol shapes that
downstream applications may bind to their own roles, modes, review gates, and
runtime materializations.

## Scope

This directory holds portable protocol artifacts only.

It may define:

- the canonical structure protocol documents should follow
- portable workflow protocols such as planning, execution, review, rework, and
  recovery
- portable delegation, handoff, and escalation protocol concepts
- portable review-pass concepts that downstream bindings may map onto project
  gates

It does not define:

- an application's chosen role roster
- an application's chosen mode set
- an application's chosen gate map
- environment-specific PR, comment, or worker-discovery behavior

## Binding Decisions

### 1. Protocols Are First-Class Workflow Surfaces

Protocols should define workflow paths, transition points, required inputs,
required outputs, and handoff expectations explicitly.

They should not be left implicit inside role notes, mode definitions, or
runtime prompt bundles.

### 2. Protocols Stay Distinct From Roles And Modes

Portable protocols answer how work progresses.

They do not replace:

- roles as accountability concepts
- modes as execution states
- skills as atomic reusable capabilities

Downstream bindings may connect protocols to those layers, but the protocol
canon should not collapse them together.

### 3. The Protocol Template Governs Shape

Protocol documents in this directory should inherit the common structure
defined in [Protocol Template](./Protocol-Template.md).

That template keeps protocol docs readable, comparable, and later
machine-checkable without forcing every protocol to restate the same shape
from scratch.

### 4. Review Passes Are Protocol-Local Evaluation Lenses

Review passes belong to the review workflow family.

They should be treated as evaluation lenses inside review work, not as
standalone roles, modes, or independent workflow families.

Which passes apply at which project gates is a downstream binding concern.

### 5. Structured Contracts Stay Central

Where protocols accept or emit handoff, delegation, escalation, or review
state, they should describe that state as structured machine-readable contract
content rather than prose-only status.

## Reading Order

The intended progression inside this directory is:

1. [Protocol Template](./Protocol-Template.md)
2. [Planning Protocol](./Planning-Protocol.md)
3. [Execution Slice Protocol](./Execution-Slice-Protocol.md)
4. [Review Pass Model](./Review-Pass-Model.md)
5. [Review Protocol](./Review-Protocol.md)
6. [Rework Protocol](./Rework-Protocol.md)
7. [Recovery Protocol](./Recovery-Protocol.md)
8. [Delegation Protocol](./Delegation-Protocol.md)
9. [Handoff Protocol](./Handoff-Protocol.md)
10. [Escalation Protocol](./Escalation-Protocol.md)

This order is intentional:

- the template establishes the reusable shape
- the core workflow protocols define the main workflow family
- the review-pass model clarifies review lenses before downstream bindings map
  them to gates
- the delegation, handoff, and escalation protocols describe the bounded
  structured contracts that move work between authority boundaries

## Constraints

- Protocol docs should stay portable and should not encode application-specific
  gates or runtime folder conventions.
- Protocol docs should stay workflow-centered and should not become disguised
  role matrices or prompt templates.
- Review-pass terminology should stay local to review semantics rather than
  drifting into mode or role language.

## Non-Goals

- Define a project-specific gate-to-review-pass map.
- Define runtime-specific comment formats or bot-dispatch behavior.
- Replace the portable authority, mode, or skill canon.

## Related Artifacts

- [Agentic Development README](../README.md)
- [Protocol Template](./Protocol-Template.md)
- [Delegation Model](../Delegation-Model.md)
- [Escalation Model](../Escalation-Model.md)
- [Mode Model](../Mode-Model.md)
- [Agent Authority Model](../Agent-Authority-Model.md)
