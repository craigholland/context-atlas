---
id: craig-skill-python-authoring
title: Python Authoring
summary: Defines the portable skill for creating and evolving Python implementation surfaces while preserving local codebase conventions, ecosystem fit, and bounded architectural intent.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, python, implementation]
related:
  - ./README.md
  - ../Skill-Contract.md
  - ../RoleArchetypes/backend-staff-engineer.md
supersedes: []
---

# Python Authoring

## Purpose

Define the portable skill for authoring and modifying Python implementation
surfaces in a bounded, reviewable way.

## Knowledge Scope

This skill should cover:

- core Python language behavior across the common maintained range `3.12-3.14`
- typing, dataclasses, iterators, exceptions, context managers, async
  boundaries, and standard-library design patterns
- packaging and environment conventions commonly seen around modern Python work
- common test-facing integration expectations in `pytest` and `unittest` style
  codebases
- working familiarity with common ecosystem families such as:
  - web and service frameworks like `Flask`, `Django`, and comparable HTTP
    application patterns
  - persistence and migration tooling like `SQLAlchemy` and `Alembic`
  - data and numerical libraries like `NumPy` and `Pandas`
  - machine-learning libraries like `PyTorch`

Portable familiarity here means the skill should be able to orient inside those
families and preserve idiomatic usage when they are present. It does not mean
every downstream project must adopt all of them.

## Common Mode Affinity

- implementation
- rework

## Common Role Affinity

- Backend Staff Engineer
- Quality Assurance Engineer

## Common Inputs

- the requested behavior change
- the surrounding Python modules and tests
- local coding conventions and architecture constraints
- any framework or library-specific patterns already in use

## Decision Heuristics

- prefer the smallest coherent change that satisfies the intended behavior
- preserve local module boundaries and framework idioms rather than imposing a
  generic Python style on every codebase
- update nearby tests when behavior changes materially
- prefer typed, explicit, readable interfaces when the surrounding codebase
  supports them
- escalate when the required library or framework semantics exceed the evidence
  available in the current codebase

## Execution Pattern

- inspect the local code context before editing
- identify the relevant Python, framework, and architectural surfaces
- make the bounded implementation change
- update tests or supporting evidence surfaces as needed
- summarize what changed and how it was verified

## Expected Outputs

- focused Python diffs
- supporting test adjustments
- concise verification notes
- framework-aware implementation rationale when needed

## Verification And Evidence

A well-used instance of this skill should usually leave behind:

- code that matches the surrounding Python and framework conventions
- test or execution evidence for changed behavior
- enough explanation that a reviewer can see why the chosen implementation fits
  the local architecture

## Escalation Conditions

Escalate when:

- the work requires deep framework or library knowledge not evidenced locally
- the requested change crosses architecture boundaries rather than staying in a
  bounded Python surface
- multiple incompatible implementation patterns already exist and no governing
  rule is clear
- correctness depends on data, infrastructure, or runtime state not available
  to the current actor

## Guardrails

- does not replace debugging, testing, or review skills
- does not independently settle architectural disputes
- does not own acceptance, merge, or release authority

## Related Artifacts

- [Skills](./README.md)
- [Skill Contract](../Skill-Contract.md)
- [Backend Staff Engineer](../RoleArchetypes/backend-staff-engineer.md)
