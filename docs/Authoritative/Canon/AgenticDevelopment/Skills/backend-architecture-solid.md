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

## Knowledge Scope

This skill should cover:

- responsibility sizing at the class, module, and service level
- when interfaces are helpful versus when they add needless indirection
- how substitution and inheritance assumptions can create fragility
- how oversized interfaces and leaky abstractions degrade maintainability
- how dependency inversion should improve boundaries rather than obscure them

## Common Mode Affinity

- implementation
- review
- rework

## Common Role Affinity

- Backend Staff Engineer
- Quality Assurance Engineer

## Common Inputs

- the design or implementation under review
- surrounding abstractions and interface patterns
- local architectural conventions
- current or expected extension points

## Decision Heuristics

- prefer one clear responsibility per module or class-sized unit
- introduce abstractions when they protect a real seam, not merely to satisfy a
  stylistic preference
- keep interfaces as small as the consuming contracts allow
- treat dependency inversion as a boundary tool, not a universal requirement
- flag abstraction layers that increase indirection without increasing clarity

## Execution Pattern

- inspect the current responsibility and dependency shape
- test whether the abstraction surface matches real change and substitution
  pressure
- surface findings about cohesion, interface size, and inversion strategy
- propose the narrowest design improvement that addresses the risk

## Expected Outputs

- design-quality notes
- abstraction or cohesion findings
- focused refactoring guidance

## Verification And Evidence

A well-used instance of this skill should make it possible to explain:

- why the current design is cohesive or fragmented
- whether an abstraction is earning its complexity
- how the proposed structure improves maintainability without unnecessary
  indirection

## Escalation Conditions

Escalate when:

- the design issue is really a higher-level architecture or ownership issue
- remediation would require broad public-interface changes
- the current codebase lacks a stable design direction to anchor the analysis

## Guardrails

- does not replace full system-architecture reasoning
- does not turn every implementation choice into an abstraction exercise
- should remain reviewable and tied to concrete design concerns

## Related Artifacts

- [Skills](./README.md)
- [Backend Architecture CLEAN](./backend-architecture-clean.md)
- [Backend Staff Engineer](../RoleArchetypes/backend-staff-engineer.md)
