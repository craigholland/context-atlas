---
id: context-atlas-role-agent-binding-model
title: Context Atlas Role-Agent Binding Model
summary: Defines how the Context Atlas role model binds to parent agents and how specialists participate under those parent-owned roles without creating a parallel role layer.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, roles, parent-agents, bindings]
related:
  - ./Role-Model.md
  - ./Role-Authority-Matrix.md
  - ../Context-Atlas-Agentic-Development-Profile.md
  - ../../AgenticDevelopment/Agent-Composition-Model.md
supersedes: []
---

# Context Atlas Role-Agent Binding Model

## Purpose

Define how the project role model binds to the structural parent-agent plus
specialist model adopted by Context Atlas.

This document makes it explicit which parent-agent layer carries role
accountability and how specialists participate without becoming a second role
system.

## Scope

This document defines:

- how top-level roles are embodied by parent agents
- how specialists participate beneath those role-owning parent agents
- how direct skills and delegated skills coexist within the same parent-owned
  role boundary

It does not define runtime-specific files, vendor folder conventions, or the
final specialist roster.

## Binding Decisions

### 1. Each Top-Level Role Is Embodied By A Parent Agent

Context Atlas binds each top-level role to a parent agent rather than to a
specialist or a runtime file.

That means the parent-agent layer is where the role's accountability,
authority, and protocol participation begin.

### 2. The Initial Binding Is One Parent Agent Per Top-Level Role

The initial project binding is:

- Planner/Decomp role -> Planner/Decomp parent agent
- Backend role -> Backend parent agent
- Frontend role -> Frontend parent agent
- QA role -> QA parent agent
- DevOps role -> DevOps parent agent

This is a project-specific binding decision, not a portable canon rule.

### 3. Parent Agents Combine Direct Skills And Delegation Rights

Each parent agent may:

- perform some work directly through attached skills
- delegate bounded work to specialists in its domain
- retain accountability for the role-owned output even when delegation occurs

This keeps the role model and the skill model compatible without collapsing the
parent into either a pure orchestrator or a pure skill bundle.

### 4. Specialists Participate Beneath One Parent-Owned Role Context

Specialists should participate as bounded delegates under a parent-owned role
context.

They may contribute expertise, narrow execution, or validation work, but they
do not become alternate embodiments of the top-level role itself.

### 5. Specialist Labels Must Not Become A Shadow Role Model

If a specialist carries a narrow name or focused domain, that name should be
interpreted as delegated scope rather than project accountability.

The role roster remains the parent-owned accountability layer, and the
specialist roster remains subordinate execution structure.

### 6. Later Runtime Materialization Must Derive From This Binding

When Context Atlas later materializes roles into a concrete AI environment,
that materialization should inherit this binding model rather than redefining
roles, parent agents, or specialists ad hoc.

## Constraints

- Role bindings should stay project-specific without drifting into vendor file
  assumptions.
- Specialists should remain subordinate to parent-owned accountability and
  authority.
- The binding model should stay compatible with later protocol and mode work
  rather than replacing them.

## Non-Goals

- Define the detailed specialist roster.
- Define runtime-discovery file names or templates.
- Define mode transitions or protocol sequencing.

## Related Artifacts

- [Context Atlas Role Model](./Role-Model.md)
- [Context Atlas Role Authority Matrix](./Role-Authority-Matrix.md)
- [Context Atlas Agentic Development Profile](../Context-Atlas-Agentic-Development-Profile.md)
- [Agent Composition Model](../../AgenticDevelopment/Agent-Composition-Model.md)
