---
id: craig-skill-review-findings-analysis
title: Review Findings Analysis
summary: Defines the portable skill for converting observed evidence into explicit findings, risk statements, and acceptance judgments.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, review, findings, qa]
related:
  - ./README.md
  - ./python-testing.md
  - ../Escalation-Model.md
  - ../RoleArchetypes/quality-assurance-engineer.md
supersedes: []
---

# Review Findings Analysis

## Purpose

Define the portable skill for turning evidence into explicit findings, risk
statements, and review outcomes.

## Common Mode Affinity

- review

## Common Role Affinity

- Quality Assurance Engineer
- User Acceptance Tester

## Bounded Capability

- interpret evidence from tests, diffs, traces, or review surfaces
- frame concerns as explicit findings instead of vague discomfort
- state whether work appears acceptable, blocked, risky, or unclear

## Common Outputs

- findings summary
- acceptance or risk statement
- escalation or rework recommendation

## Guardrails

- does not replace the underlying evidence-producing skills
- should not become implementation ownership by proxy
- must remain specific enough to support rework or follow-up

## Related Artifacts

- [Skills](./README.md)
- [Python Testing](./python-testing.md)
- [Escalation Model](../Escalation-Model.md)
- [Quality Assurance Engineer](../RoleArchetypes/quality-assurance-engineer.md)
