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

## Knowledge Scope

This skill should cover:

- the difference between implementation completeness and delivery readiness
- common readiness signals such as review state, evidence state, branch state,
  checks, release notes, and rollback posture
- how delivery gates differ from implementation or QA gates
- how missing handoffs or missing evidence should affect operational movement

## Common Mode Affinity

- review
- operational_delivery

## Common Role Affinity

- DevOps Engineer
- Quality Assurance Engineer

## Common Inputs

- current branch or PR state
- validation and review evidence
- release-facing notes or required operational artifacts
- known gate policy for the target integration or delivery step

## Decision Heuristics

- treat missing required evidence as a hold, not as implied readiness
- distinguish a work unit that is technically correct from one that is
  operationally ready to move
- prefer explicit holds over optimistic movement when gate inputs are unclear
- keep readiness judgments tied to known gates rather than intuition alone

## Execution Pattern

- inspect the current evidence and handoff state
- compare it against the expected gate inputs
- identify blockers, risks, or missing artifacts
- state whether the work appears ready, blocked, or uncertain

## Expected Outputs

- readiness summary
- blocker list
- proceed / hold recommendation
- missing-evidence list when relevant

## Verification And Evidence

A well-used instance of this skill should make it possible to explain:

- what made the work appear ready or not ready
- which required gate inputs were present
- which risks remain open even if movement is allowed

## Escalation Conditions

Escalate when:

- delivery readiness depends on authority outside the current actor
- gate policy is ambiguous or contradictory
- evidence from review, testing, or release surfaces conflicts materially
- moving forward would create unclear rollback or recovery posture

## Guardrails

- does not replace release authority
- does not override role-specific acceptance or governance rules
- should remain bounded to readiness judgment rather than broad project status

## Related Artifacts

- [Skills](./README.md)
- [CI/CD Pipeline Operations](./ci-cd-pipeline-operations.md)
- [DevOps Engineer](../RoleArchetypes/devops-engineer.md)
