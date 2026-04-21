---
id: craig-skill-ci-cd-pipeline-operations
title: CI/CD Pipeline Operations
summary: Defines the portable skill for working with build, validation, and delivery pipelines as bounded operational surfaces.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, ci-cd, delivery, operations]
related:
  - ./README.md
  - ./operational-delivery-readiness.md
  - ../RoleArchetypes/devops-engineer.md
supersedes: []
---

# CI/CD Pipeline Operations

## Purpose

Define the portable skill for reasoning about build, validation, and delivery
pipelines as bounded operational systems.

## Common Mode Affinity

- operational_delivery
- recovery

## Common Role Affinity

- DevOps Engineer
- Quality Assurance Engineer

## Bounded Capability

- inspect pipeline state and failure surfaces
- interpret build, test, and deployment pipeline signals
- make bounded operational adjustments or escalation recommendations

## Common Outputs

- pipeline status summary
- failure interpretation notes
- bounded remediation or escalation recommendation

## Guardrails

- does not automatically grant infrastructure-administration authority
- does not replace application-level debugging
- should remain centered on bounded pipeline behavior

## Related Artifacts

- [Skills](./README.md)
- [Operational Delivery Readiness](./operational-delivery-readiness.md)
- [DevOps Engineer](../RoleArchetypes/devops-engineer.md)
