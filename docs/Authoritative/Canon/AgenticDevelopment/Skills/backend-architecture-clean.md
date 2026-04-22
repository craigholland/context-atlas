---
id: craig-skill-backend-architecture-clean
title: Backend Architecture CLEAN
summary: Defines the portable skill for evaluating backend work against separation-of-concerns and directional-dependency constraints associated with CLEAN-style architecture.
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

## Knowledge Scope

This skill should cover:

- the distinction between domain, use-case/service, adapter, and infrastructure
  concerns
- inward dependency direction and why outer layers should not own inner policy
- interface placement and boundary crossing
- how framework, storage, and transport details should remain at the edges
- how to recognize boundary leaks and misplaced orchestration

## Common Mode Affinity

- implementation
- review
- rework

## Common Role Affinity

- Backend Staff Engineer
- Quality Assurance Engineer

## Common Inputs

- the changed code or proposed design
- the local architectural profile or boundary rules
- existing module placement and dependency structure
- known review findings or drift concerns

## Decision Heuristics

- keep business policy inward and delivery/storage details outward
- prefer introducing or using an interface boundary rather than letting an
  inner layer depend directly on an outer detail
- do not move code inward merely because it is important; move it inward only
  when it represents policy rather than mechanism
- flag orchestration that has leaked into domain surfaces or domain decisions
  that have leaked outward into adapters

## Execution Pattern

- inspect where the behavior lives today
- identify the relevant boundary and dependency directions
- test the placement against the intended layer responsibilities
- surface conformance notes or targeted remediation guidance

## Expected Outputs

- architectural conformance notes
- boundary-risk findings
- targeted remediation guidance

## Verification And Evidence

A well-used instance of this skill should make it possible to explain:

- which layer owns the behavior
- whether dependencies point in the intended direction
- whether the proposed placement reduces or increases architectural drift

## Escalation Conditions

Escalate when:

- the architecture profile itself is unclear or contradictory
- the proposed remediation would require broader system restructuring
- multiple layers already share responsibility in a way that cannot be resolved
  locally
- the issue is really about protocol or role ownership rather than code
  placement

## Guardrails

- does not replace the complete architecture canon
- does not decide product or release readiness
- should remain focused on bounded conformance analysis

## Related Artifacts

- [Skills](./README.md)
- [Boundary Model](../Boundary-Model.md)
- [Backend Staff Engineer](../RoleArchetypes/backend-staff-engineer.md)
