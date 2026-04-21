---
id: craig-skill-python-debugging
title: Python Debugging
summary: Defines the portable skill for reproducing, isolating, and explaining faults in Python behavior without expanding into unbounded incident ownership.
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

## Common Mode Affinity

- review
- rework
- recovery

## Common Role Affinity

- Backend Staff Engineer
- Quality Assurance Engineer

## Bounded Capability

- reproduce failure conditions
- narrow faults to specific code paths or state transitions
- explain likely root cause and candidate remediation paths

## Common Outputs

- reproduction notes
- fault isolation summary
- candidate fix direction

## Guardrails

- does not replace implementation ownership
- does not automatically approve a fix once a cause is understood
- should not become a vague catch-all for architectural redesign

## Related Artifacts

- [Skills](./README.md)
- [Python Authoring](./python-authoring.md)
- [Quality Assurance Engineer](../RoleArchetypes/quality-assurance-engineer.md)
