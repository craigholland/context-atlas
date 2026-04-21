---
id: craig-skill-backend-architecture-clean
title: Backend Architecture CLEAN
summary: Defines the portable skill for reasoning about backend changes through separation-of-concerns and directional-dependency constraints associated with CLEAN-style architecture.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, backend, architecture, clean]
related:
  - ./README.md
  - ../Boundary-Model.md
  - ../RoleArchetypes/backend-staff-engineer.md
supersedes: []
---

# Backend Architecture CLEAN

## Purpose

Define the portable skill for evaluating backend work against separation of
concerns, dependency direction, and inward architectural boundaries associated
with CLEAN-style design.

## Common Mode Affinity

- implementation
- review
- rework

## Common Role Affinity

- Backend Staff Engineer
- Quality Assurance Engineer

## Bounded Capability

- check whether code placement and dependency direction preserve intended layers
- identify boundary leaks between domain, infrastructure, service, and adapter
  concerns
- frame remediation guidance without absorbing full architectural ownership

## Common Outputs

- architectural conformance notes
- boundary-risk findings
- targeted remediation guidance

## Guardrails

- does not replace the complete architecture canon
- does not decide product or release readiness
- should remain focused on bounded conformance analysis

## Related Artifacts

- [Skills](./README.md)
- [Boundary Model](../Boundary-Model.md)
- [Backend Staff Engineer](../RoleArchetypes/backend-staff-engineer.md)
