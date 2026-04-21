---
id: craig-skill-python-authoring
title: Python Authoring
summary: Defines the portable skill for creating and evolving Python implementation surfaces while preserving local codebase conventions and bounded architectural intent.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, python, implementation]
related:
  - ./README.md
  - ../Skill-Contract.md
  - ../RoleArchetypes/backend-staff-engineer.md
supersedes: []
---

# Python Authoring

## Purpose

Define the portable skill for authoring and modifying Python implementation
surfaces in a bounded, reviewable way.

## Common Mode Affinity

- implementation
- rework

## Common Role Affinity

- Backend Staff Engineer
- Quality Assurance Engineer

## Bounded Capability

- add or modify Python modules, functions, classes, and tests
- preserve surrounding style and local conventions
- keep changes small enough to remain reviewable and attributable

## Common Outputs

- focused Python diffs
- supporting test adjustments
- concise verification notes

## Guardrails

- does not replace debugging, testing, or review skills
- does not independently settle architectural disputes
- does not own acceptance, merge, or release authority

## Related Artifacts

- [Skills](./README.md)
- [Skill Contract](../Skill-Contract.md)
- [Backend Staff Engineer](../RoleArchetypes/backend-staff-engineer.md)
