---
id: craig-role-archetype-devops-engineer
title: DevOps Engineer
summary: Defines the portable role archetype for work that owns merge, release, CI, and operational delivery surfaces.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, role-archetype, devops, release, operations]
related:
  - ./README.md
  - ../Platform-Materialization-Model.md
supersedes: []
---

# DevOps Engineer

## Purpose

Describe the portable role archetype for work that owns merge, release, CI,
and operational delivery surfaces.

## Common Responsibilities

- govern merge and release actions
- maintain CI, automation, and operational workflow surfaces
- manage delivery readiness from an operational perspective
- keep operational changes explicit rather than implicit in implementation work

## Common Boundaries

- does not automatically own product implementation decisions
- should not bypass required planning or QA gates merely because it owns the
  operational action
- may collaborate with implementation roles, but remains centered on delivery
  operations

## Common Collaboration Pattern

- collaborates with planning, implementation, and QA roles at the boundary
  where operational action becomes necessary
- often receives explicit handoff signals before executing merge or release
  actions

## Related Artifacts

- [Role Archetypes](./README.md)
- [Platform Materialization Model](../Platform-Materialization-Model.md)
