---
id: craig-skill-github-pr-review-and-handoff
title: GitHub PR Review And Handoff
summary: Defines the portable skill for preparing, interpreting, and responding to pull-request review surfaces in GitHub-style workflows.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, github, review, handoff]
related:
  - ./README.md
  - ./review-findings-analysis.md
  - ../RoleArchetypes/quality-assurance-engineer.md
  - ../RoleArchetypes/devops-engineer.md
supersedes: []
---

# GitHub PR Review And Handoff

## Purpose

Define the portable skill for using pull-request review surfaces as structured
handoff and findings channels.

## Common Mode Affinity

- review
- rework
- operational_delivery

## Common Role Affinity

- Quality Assurance Engineer
- DevOps Engineer
- Backend Staff Engineer

## Bounded Capability

- prepare review-ready PR context
- publish or interpret findings on the review surface
- respond to findings with fixes, clarifications, or handoff notes

## Common Outputs

- PR review summary
- inline findings or responses
- handoff commentary tied to the review surface

## Guardrails

- does not replace provider-specific authority rules
- does not automatically imply approval or merge
- should remain structured and review-centered rather than conversationally vague

## Related Artifacts

- [Skills](./README.md)
- [Review Findings Analysis](./review-findings-analysis.md)
- [Quality Assurance Engineer](../RoleArchetypes/quality-assurance-engineer.md)
- [DevOps Engineer](../RoleArchetypes/devops-engineer.md)
