---
id: craig-role-archetype-planning-decomposition-lead
title: Planning And Decomposition Lead
summary: Defines the portable archetype for a role that owns decomposition quality, dependency-aware sequencing, and planning coherence.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, role-archetype, planning, decomposition]
related:
  - ./README.md
  - ../Agentic-Development-Glossary.md
  - ../Agent-Composition-Model.md
supersedes: []
---

# Planning And Decomposition Lead

## Purpose

Describe the portable role archetype for work that owns decomposition quality,
dependency-aware sequencing, and planning coherence.

## Common Responsibilities

- shape Epics, Stories, Tasks, and implementation slices into a safe delivery
  model
- identify blocking work versus parallelizable work
- keep planning artifacts consistent across decomposition levels
- surface planning risks before implementation begins

## Common Boundaries

- does not automatically own implementation authority
- does not treat planning authorship as merge or release approval
- may use planning-focused specialists, but remains accountable for the final
  decomposition shape

## Common Collaboration Pattern

- collaborates closely with implementation, QA, and operational roles
- often initiates handoffs rather than completing the entire workstream alone

## Related Artifacts

- [Role Archetypes](./README.md)
- [Agentic Development Glossary](../Agentic-Development-Glossary.md)
- [Agent Composition Model](../Agent-Composition-Model.md)
