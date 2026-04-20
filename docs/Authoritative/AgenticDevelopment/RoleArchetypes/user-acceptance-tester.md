---
id: craig-role-archetype-user-acceptance-tester
title: User Acceptance Tester
summary: Defines the portable role archetype for work that owns evaluator-facing scenarios, product walkthroughs, and user-acceptance-style validation.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, role-archetype, acceptance, evaluation]
related:
  - ./README.md
  - ../Escalation-Model.md
supersedes: []
---

# User Acceptance Tester

## Purpose

Describe the portable role archetype for work that owns evaluator-facing
scenarios, product walkthroughs, and user-acceptance-style validation.

## Common Responsibilities

- define or exercise acceptance-oriented evaluation scenarios
- validate whether the current product surface supports intended user outcomes
- surface evaluator-facing gaps that may not appear in lower-level technical
  validation alone

## Common Boundaries

- does not replace deeper QA engineering or automated validation
- does not automatically own implementation authority
- may drive acceptance feedback, but does not automatically own merge or
  release approval

## Common Collaboration Pattern

- collaborates with technical documentation and QA-oriented roles
- often participates late in a workflow to validate the outward product
  experience

## Related Artifacts

- [Role Archetypes](./README.md)
- [Escalation Model](../Escalation-Model.md)
