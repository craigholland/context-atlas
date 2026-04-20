---
id: craig-agent-composition-model
title: Agent Composition Model
summary: Defines the portable composition pattern for parent agents and specialists, including their expected contract shapes and structural differences.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, composition, parent-agent, specialist, canon]
related:
  - ./Agent-Authority-Model.md
  - ./Delegation-Model.md
  - ./Skill-Contract.md
  - ./Agentic-Development-Glossary.md
supersedes: []
---

# Agent Composition Model

## Purpose

Define the portable composition pattern for parent agents and specialists so
later application bindings can assemble actors without blurring their contract
shapes or authority boundaries.

## Scope

This document governs the expected structural shape of parent-agent and
specialist-agent definitions, including what each kind of actor must make
explicit before later role, protocol, or environment bindings are added.

It does not define an application's actual agent roster or any
environment-specific manifest format.

## Binding Decisions

- A parent agent is a broader accountable actor composed from:
  - a role-bearing authority boundary
  - direct reusable skills
  - delegation rights over narrower specialists
  - responsibility for workflow continuity
- A specialist is a narrower actor composed from:
  - a focused scope
  - curated skills selected for that scope
  - explicit constraints
  - explicit return and escalation expectations
- Parent and specialist definitions should not differ only by name; they should
  differ in accountable shape.

### Parent-Agent Contract Shape

- A parent-agent definition should make explicit:
  - what broader responsibility it carries
  - what direct skills it may use itself
  - what kinds of work it may delegate
  - what decisions or artifacts remain parent-owned
  - what escalations it must absorb from narrower delegates

### Specialist Contract Shape

- A specialist definition should make explicit:
  - the narrow scope it is allowed to operate within
  - the curated skills that justify its existence
  - the constraints that prevent scope sprawl
  - the return contract it owes to its parent boundary
  - the escalation conditions that force work back upward

## Constraints

- A specialist definition must not quietly become an alternate parent-agent
  definition with equivalent lifecycle authority.
- Parent-agent composition must not be reduced to "a bag of skills"; accountable
  ownership remains the defining difference.
- Composition rules should stay portable enough to survive later application
  binding and environment materialization.

## Non-Goals

- Choose an application's concrete parent-agent roster.
- Choose an application's concrete specialist roster.
- Define the exact skills attached to any specific actor.

## Related Artifacts

- [Agent Authority Model](./Agent-Authority-Model.md)
- [Delegation Model](./Delegation-Model.md)
- [Skill Contract](./Skill-Contract.md)
- [Agentic Development Glossary](./Agentic-Development-Glossary.md)
