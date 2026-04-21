---
id: craig-skill-python-testing
title: Python Testing
summary: Defines the portable skill for executing, extending, and interpreting Python test surfaces in support of reviewable evidence.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, python, testing, validation]
related:
  - ./README.md
  - ./review-findings-analysis.md
  - ../RoleArchetypes/quality-assurance-engineer.md
supersedes: []
---

# Python Testing

## Purpose

Define the portable skill for using Python tests as bounded validation and
evidence surfaces.

## Common Mode Affinity

- review
- implementation
- rework

## Common Role Affinity

- Quality Assurance Engineer
- Backend Staff Engineer

## Bounded Capability

- run targeted or broader Python test suites
- interpret failures and pass conditions in context
- add or refine tests when bounded evidence is missing

## Common Outputs

- test execution result summary
- focused test additions or updates
- evidence notes tied to observed behavior

## Guardrails

- does not equate a green test run with total acceptance
- does not replace debugging or architectural review
- should stay bounded to evidence production and interpretation

## Related Artifacts

- [Skills](./README.md)
- [Review Findings Analysis](./review-findings-analysis.md)
- [Quality Assurance Engineer](../RoleArchetypes/quality-assurance-engineer.md)
