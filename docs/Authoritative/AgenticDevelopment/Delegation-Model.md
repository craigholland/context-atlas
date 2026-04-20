---
id: craig-delegation-model
title: Delegation Model
summary: Defines the portable delegation rules that keep parent-agent accountability distinct from specialist execution scope.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, delegation, parent-agent, specialist, canon]
related:
  - ./Agent-Authority-Model.md
  - ./Agentic-Development-Glossary.md
  - ./Boundary-Model.md
  - ../Architecture/Craig-Architecture.md
supersedes: []
---

# Delegation Model

## Purpose

Define the portable delegation rules that keep accountable parent agents and
bounded specialists structurally distinct.

## Scope

This document governs how bounded work may be delegated from a parent agent to
another actor without collapsing accountability, workflow ownership, or
authority boundaries.

It does not define an application's role roster, workflow protocols, or
environment-specific delegate-discovery mechanism.

## Binding Decisions

- Delegation is the bounded assignment of execution work from a broader
  authority boundary to a narrower one.
- A parent agent remains accountable for delegated work unless a separate
  protocol-governed handoff explicitly transfers workflow ownership.
- Delegation should name:
  - the bounded scope being delegated
  - the constraints that apply while it is performed
  - the expected return shape
  - the escalation conditions that return control upward
- A specialist performs delegated work inside a constrained scope and returns
  results, findings, or blocked-state information to the parent boundary.
- Delegation should not be treated as a silent transfer of:
  - workflow ownership
  - protocol control
  - role accountability
  - unrestricted mutation authority
- When a system distinguishes parent agents from specialists, the distinction
  should reflect real authority asymmetry rather than mere naming preference.

## Constraints

- Parent-owned workflow continuity must stay explicit while work is delegated.
- Delegates must not widen their own scope merely because adjacent work would
  be convenient to absorb.
- Delegation should prefer bounded scopes over open-ended standing authority.
- Delegation semantics should remain portable across execution environments.

## Non-Goals

- Define a project-specific role set or mode set.
- Define the complete protocol catalog a system adopts.
- Define environment-specific file conventions for delegate discovery.

## Related Artifacts

- [Agent Authority Model](./Agent-Authority-Model.md)
- [Agentic Development Glossary](./Agentic-Development-Glossary.md)
- [Boundary Model](./Boundary-Model.md)
- [Craig Architecture](../Architecture/Craig-Architecture.md)
