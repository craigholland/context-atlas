---
id: craig-skill-python-testing
title: Python Testing
summary: Defines the portable skill for executing, extending, and interpreting Python test surfaces as bounded validation evidence.
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

## Knowledge Scope

This skill should cover:

- unit, integration, and regression testing patterns in Python `3.12-3.14`
- `pytest` and `unittest` style execution, fixtures, parametrization, and
  mocking patterns
- negative-path and robustness testing, including attempts to break methods,
  classes, and contract boundaries through invalid, missing, extreme, or
  unexpected inputs
- how to decide whether a behavior belongs in unit, service, adapter, or
  end-to-end evidence
- how framework and library choices can change the right testing boundary
- how to interpret green and failing tests without overstating certainty

## Common Mode Affinity

- review
- implementation
- rework

## Common Role Affinity

- Quality Assurance Engineer
- Backend Staff Engineer

## Common Inputs

- the behavior or regression under examination
- existing tests and surrounding implementation
- local test tooling and execution commands
- findings, bug reports, or changed code paths needing evidence

## Decision Heuristics

- add the narrowest test that proves the behavior in question
- prefer regression tests close to the failing contract or surface
- do not stop at happy-path validation when robustness depends on defensive
  behavior, validation rules, or failure handling
- deliberately probe negative paths and boundary conditions when methods or
  classes claim to be resilient, validated, or error-tolerant
- do not use a broad integration test when a smaller deterministic test would
  prove the same point
- do not assume coverage percentage equals correctness
- escalate when meaningful evidence depends on unavailable external systems or
  unresolved product expectations

## Execution Pattern

- identify the contract or behavior that needs proof
- choose the right testing level
- run existing tests first when possible
- add or refine tests if the current evidence is insufficient
- include negative-path or boundary-breaking cases when robustness is part of
  the contract being tested
- interpret the resulting pass/fail signal in context

## Expected Outputs

- test execution result summary
- focused test additions or updates
- evidence notes tied to observed behavior

## Verification And Evidence

A well-used instance of this skill should usually leave behind:

- explicit proof for the changed or questioned behavior
- a clear statement of what was and was not validated
- evidence that important failure modes, invalid inputs, or break attempts were
  considered when robustness matters
- test surfaces that remain understandable and maintainable

## Escalation Conditions

Escalate when:

- the required evidence depends on unavailable environments, data, or services
- the correct testing boundary is blocked by unresolved architecture decisions
- tests are too unstable or slow to provide trustworthy evidence
- the issue appears to be in review interpretation rather than test coverage

## Guardrails

- does not equate a green test run with total acceptance
- does not replace debugging or architectural review
- should stay bounded to evidence production and interpretation

## Related Artifacts

- [Skills](./README.md)
- [Review Findings Analysis](./review-findings-analysis.md)
- [Quality Assurance Engineer](../RoleArchetypes/quality-assurance-engineer.md)
