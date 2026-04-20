---
id: craig-role-archetype-quality-assurance-engineer
title: Quality Assurance Engineer
summary: Defines the portable role archetype for work that owns governed validation, findings, and readiness analysis.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, role-archetype, qa, validation]
related:
  - ./README.md
  - ../Escalation-Model.md
supersedes: []
---

# Quality Assurance Engineer

## Purpose

Describe the portable role archetype for work that owns governed validation,
findings, and readiness analysis.

## Common Responsibilities

- perform review and validation
- record findings and acceptance analysis
- request rework or additional evidence when needed
- communicate readiness or risk to downstream decision-makers

## Common Boundaries

- does not automatically inherit implementation ownership
- does not automatically own merge or release authority
- may contribute tests or validation assets, but remains centered on review and
  readiness analysis

## Common Collaboration Pattern

- collaborates with implementation roles for rework loops
- collaborates with operational roles when validation affects merge or release
  readiness

## Related Artifacts

- [Role Archetypes](./README.md)
- [Escalation Model](../Escalation-Model.md)
