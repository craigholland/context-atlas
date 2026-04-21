---
id: craig-skill-operational-delivery-readiness
title: Operational Delivery Readiness
summary: Defines the portable skill for judging whether a bounded work unit appears ready for delivery-oriented operational handling.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, delivery, readiness, operations]
related:
  - ./README.md
  - ./ci-cd-pipeline-operations.md
  - ../RoleArchetypes/devops-engineer.md
supersedes: []
---

# Operational Delivery Readiness

## Purpose

Define the portable skill for deciding whether a bounded work unit appears
ready to enter delivery-oriented operational handling.

## Common Mode Affinity

- review
- operational_delivery

## Common Role Affinity

- DevOps Engineer
- Quality Assurance Engineer

## Bounded Capability

- check whether required evidence and handoffs appear present
- identify obvious readiness blockers before operational movement
- communicate whether work seems ready, blocked, or risky for delivery

## Common Outputs

- readiness summary
- blocker list
- proceed / hold recommendation

## Guardrails

- does not replace release authority
- does not override role-specific acceptance or governance rules
- should remain bounded to readiness judgment rather than broad project status

## Related Artifacts

- [Skills](./README.md)
- [CI/CD Pipeline Operations](./ci-cd-pipeline-operations.md)
- [DevOps Engineer](../RoleArchetypes/devops-engineer.md)
