---
id: craig-skill-change-management
title: Change Management
summary: Defines the portable skill for proposing, sequencing, and communicating changes in a governed way that preserves reviewability and drift awareness.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, change-management, governance]
related:
  - ./README.md
  - ../Change-Management-Model.md
  - ../Drift-Model.md
supersedes: []
---

# Change Management

## Purpose

Define the portable skill for evolving systems in a way that preserves
traceability, reviewability, and recovery paths.

## Common Mode Affinity

- planning
- rework
- recovery

## Common Role Affinity

- Planning/Decomposition Lead
- DevOps Engineer
- Quality Assurance Engineer

## Bounded Capability

- frame a change in terms of scope, risk, sequencing, and downstream impact
- identify where drift, validation, or documentation updates are required
- keep change proposals aligned with the governing canon and binding layers

## Common Outputs

- change proposal notes
- risk and sequencing summary
- required follow-up or validation list

## Guardrails

- does not replace implementation work
- does not override release or merge authority
- should not become a catch-all justification for skipping validation

## Related Artifacts

- [Skills](./README.md)
- [Change Management Model](../Change-Management-Model.md)
- [Drift Model](../Drift-Model.md)
