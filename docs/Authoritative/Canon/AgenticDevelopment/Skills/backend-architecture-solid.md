---
id: craig-skill-backend-architecture-solid
title: Backend Architecture SOLID
summary: Defines the portable skill for evaluating backend changes against cohesion, responsibility, and interface design concerns commonly associated with SOLID reasoning.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, backend, architecture, solid]
related:
  - ./README.md
  - ./backend-architecture-clean.md
  - ../RoleArchetypes/backend-staff-engineer.md
supersedes: []
---

# Backend Architecture SOLID

## Purpose

Define the portable skill for reasoning about backend design through cohesion,
responsibility, substitution, interface, and dependency-inversion concerns
commonly associated with SOLID analysis.

## Common Mode Affinity

- implementation
- review
- rework

## Common Role Affinity

- Backend Staff Engineer
- Quality Assurance Engineer

## Bounded Capability

- assess whether responsibilities are well-bounded
- identify brittle abstractions or oversized interfaces
- surface object and module design issues before they become architectural drift

## Common Outputs

- design-quality notes
- abstraction or cohesion findings
- focused refactoring guidance

## Guardrails

- does not replace full system-architecture reasoning
- does not turn every implementation choice into an abstraction exercise
- should remain reviewable and tied to concrete design concerns

## Related Artifacts

- [Skills](./README.md)
- [Backend Architecture CLEAN](./backend-architecture-clean.md)
- [Backend Staff Engineer](../RoleArchetypes/backend-staff-engineer.md)
