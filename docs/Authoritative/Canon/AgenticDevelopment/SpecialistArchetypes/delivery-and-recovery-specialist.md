---
id: craig-specialist-archetype-delivery-and-recovery
title: Delivery And Recovery Specialist
summary: Defines the portable specialist archetype for bounded operational-delivery preparation, repository workflow handling, pipeline interpretation, and recovery triage.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, specialist-archetype, delivery, recovery, devops]
related:
  - ./README.md
  - ../Skills/git-branch-and-history.md
  - ../Skills/github-pr-review-and-handoff.md
  - ../Skills/ci-cd-pipeline-operations.md
  - ../Skills/operational-delivery-readiness.md
  - ../Skills/recovery-triage.md
  - ../Skills/change-management.md
supersedes: []
---

# Delivery And Recovery Specialist

## Purpose

Describe the portable specialist archetype for delegated repository workflow,
pipeline, readiness, and recovery support in delivery-facing situations.

## Common Skill Composition

- [git-branch-and-history](../Skills/git-branch-and-history.md)
- [github-pr-review-and-handoff](../Skills/github-pr-review-and-handoff.md)
- [ci-cd-pipeline-operations](../Skills/ci-cd-pipeline-operations.md)
- [operational-delivery-readiness](../Skills/operational-delivery-readiness.md)
- [recovery-triage](../Skills/recovery-triage.md)
- [change-management](../Skills/change-management.md)

## Common Mode Affinity

- operational_delivery
- recovery

## Common Boundaries

- does not automatically become release authority
- does not absorb application-level implementation ownership
- should keep operational actions traceable and bounded

## Common Collaboration Pattern

- commonly invoked by DevOps-oriented parent agents
- collaborates with QA and implementation actors when recovery or readiness
  depends on evidence from their surfaces

## Related Artifacts

- [Specialist Archetypes](./README.md)
- [CI/CD Pipeline Operations](../Skills/ci-cd-pipeline-operations.md)
- [Recovery Triage](../Skills/recovery-triage.md)
