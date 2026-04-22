---
id: craig-skill-python-debugging
title: Python Debugging
summary: Defines the portable skill for reproducing, isolating, and explaining faults in Python behavior with disciplined evidence and bounded remediation direction.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, python, debugging]
related:
  - ./README.md
  - ./python-authoring.md
  - ../RoleArchetypes/quality-assurance-engineer.md
supersedes: []
---

# Python Debugging

## Purpose

Define the portable skill for reproducing, isolating, and explaining Python
faults or unexpected behavior.

## Knowledge Scope

This skill should cover:

- traceback interpretation, stack navigation, and exception reasoning in Python
  `3.12-3.14`
- common debugging methods such as targeted reproduction, logging inspection,
  local instrumentation, and interactive investigation
- test-driven repro patterns in `pytest` and related tooling
- common failure modes around async behavior, environment assumptions,
  serialization, data-shape drift, and framework lifecycle hooks
- working familiarity with debugging inside common framework and library
  families such as `Flask`, `Django`, `SQLAlchemy`, `Alembic`, `NumPy`,
  `Pandas`, and `PyTorch`

## Common Mode Affinity

- review
- rework
- recovery

## Common Role Affinity

- Backend Staff Engineer
- Quality Assurance Engineer

## Common Inputs

- failing tests, traces, logs, or observed behavior reports
- the relevant Python code and configuration context
- known environmental assumptions
- prior findings or symptoms already collected by review actors

## Decision Heuristics

- reproduce before asserting root cause whenever possible
- isolate whether the failure is caused by code, data, environment, or
  contract drift
- prefer the smallest reliable reproduction over speculative wide fixes
- distinguish clearly between confirmed cause, likely cause, and open question
- escalate when the issue appears architectural, operational, or data-bound
  rather than locally debuggable

## Execution Pattern

- establish a reproducible symptom
- narrow the failing surface to a smaller scope
- inspect state, inputs, and recent change surfaces
- state the likely cause and candidate remediation direction
- hand back a bounded explanation and evidence trail

## Expected Outputs

- reproduction notes
- fault-isolation summary
- candidate fix direction
- explicit confidence level on the suspected root cause

## Verification And Evidence

A well-used instance of this skill should usually leave behind:

- a stable repro or at least a constrained symptom description
- evidence linking the suspected cause to the observed failure
- a clear distinction between what is proven and what is inferred

## Escalation Conditions

Escalate when:

- the bug cannot be reproduced with available inputs or environments
- the likely cause depends on unavailable operational, data, or infrastructure
  state
- the issue appears to stem from architecture or workflow design rather than a
  bounded implementation fault
- the required remediation would cross major ownership boundaries

## Guardrails

- does not replace implementation ownership
- does not automatically approve a fix once a cause is understood
- should not become a vague catch-all for architectural redesign

## Related Artifacts

- [Skills](./README.md)
- [Python Authoring](./python-authoring.md)
- [Quality Assurance Engineer](../RoleArchetypes/quality-assurance-engineer.md)
