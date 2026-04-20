---
id: context-atlas-agentic-development-profile
title: Context Atlas Agentic Development Profile
summary: Defines the project-specific structural binding that applies the portable parent-agent, specialist, and skill canon to Context Atlas.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, structural-binding, profile]
related:
  - ./Context-Atlas-Charter.md
  - ./Context-Atlas-System-Model.md
  - ./AgenticDevelopment/Role-Model.md
  - ./AgenticDevelopment/Role-Accountability-Matrix.md
  - ./AgenticDevelopment/Role-Authority-Matrix.md
  - ../AgenticDevelopment/Agent-Composition-Model.md
  - ../AgenticDevelopment/Composition-Decision-Model.md
  - ../AgenticDevelopment/Boundary-Model.md
supersedes: []
---

# Context Atlas Agentic Development Profile

## Purpose

Define the project-specific structural binding that applies the portable
parent-agent, specialist, and skill canon to Context Atlas.

## Scope

This document governs the structural shape that Context Atlas intends to use
for agentic development before named roles, modes, protocols, or
environment-specific materialization files are chosen.

It does not define the full role roster, mode set, protocol catalog, or any
environment-specific file layout.

## Binding Decisions

### 1. Context Atlas Uses A Parent-Agent Plus Specialist Structure

Context Atlas will not model its governed agentic-development surface as a flat
set of peer workers.

Instead, it will treat top-level accountable actors as parent agents and treat
delegated narrow-scope actors as specialists.

### 2. Top-Level Project Accountability Lives In The Parent Layer

The parent layer is where Context Atlas will bind future project-facing
accountabilities.

That means the later role model must name project accountabilities at the
parent layer rather than introducing a parallel specialist-owned accountability
system.

### 3. Specialists Are Bounded Delegates, Not A Second Role Layer

Specialists exist to execute narrow recurring scopes with curated skills and
explicit return contracts.

They are not the place where Context Atlas defines top-level project
responsibilities, workflow ownership, or final authority boundaries.

### 4. Skills Remain Atomic Reusable Units Across The Structure

Context Atlas adopts the portable skill model directly:

- skills are atomic reusable capabilities
- skills may attach to parent agents or specialists
- skills do not become alternate role, protocol, or mode definitions

### 5. The Initial Structural Bias Is Conservative

Context Atlas should prefer:

- adding a skill before introducing a new specialist
- introducing a specialist only when a real bounded authority difference exists
- keeping work parent-owned when delegation would mostly escalate back upward

This keeps the initial project structure governable and discourages specialist
sprawl.

### 6. Later Stories Must Bind Through This Profile

Later role, mode, protocol, capacity, and materialization stories should treat
this profile as the project-specific structural source of truth.

They should not bypass it by binding directly from the portable canon to
environment-facing assets.

### 7. Named Roles Must Bind At The Parent Layer

When Context Atlas defines named project roles, those roles should bind at the
parent-agent layer described by this profile.

That means the project role roster should be interpreted as top-level
accountability carried by parent agents, while specialists remain subordinate
delegates beneath those parent-owned roles.

### 8. Specialist Participation Does Not Change Role Ownership

When specialists contribute to a workstream, they do so beneath a
parent-owned role.

That means planning artifacts remain Planner/Decomp-owned, engine
implementation remains Backend-owned, user-facing product surfaces remain
Frontend-owned, governed validation remains QA-owned, and operational delivery
remains DevOps-owned unless a later authority or protocol artifact explicitly
changes the handoff state.

### 9. Authority Must Stay Bound To Parent-Owned Roles Until Explicit Handoff

Context Atlas should treat approval, merge, release, and operational workflow
authority as role-bound parent-agent authority rather than as an ambient
capability available to any participant in the work.

That means delegation and escalation may route work or decisions, but they
should not implicitly reassign authority without an explicit downstream
contract.

## Constraints

- Context Atlas should keep the parent layer small enough that top-level
  accountability remains legible.
- Specialists should justify themselves by repeated bounded value, not by
  one-off task convenience.
- Project-specific structural bindings must remain distinct from later
  environment-specific materialization choices.

## Non-Goals

- Define the final named parent-agent role roster.
- Define the project's execution modes.
- Define the project's workflow protocol set.
- Define concrete environment-discovery files or folder layouts.

## Related Artifacts

- [Context Atlas Charter](./Context-Atlas-Charter.md)
- [Context Atlas System Model](./Context-Atlas-System-Model.md)
- [Context Atlas Role Model](./AgenticDevelopment/Role-Model.md)
- [Context Atlas Role Accountability Matrix](./AgenticDevelopment/Role-Accountability-Matrix.md)
- [Context Atlas Role Authority Matrix](./AgenticDevelopment/Role-Authority-Matrix.md)
- [Agent Composition Model](../AgenticDevelopment/Agent-Composition-Model.md)
- [Composition Decision Model](../AgenticDevelopment/Composition-Decision-Model.md)
- [Boundary Model](../AgenticDevelopment/Boundary-Model.md)
