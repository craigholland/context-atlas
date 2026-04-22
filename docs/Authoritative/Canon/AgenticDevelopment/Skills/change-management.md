---
id: craig-skill-change-management
title: Change Management
summary: Defines the portable skill for proposing, sequencing, and communicating changes in a governed way that preserves reviewability, drift awareness, and recovery paths.
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
traceability, reviewability, and bounded recovery paths.

## Knowledge Scope

This skill should cover:

- the difference between cosmetic, structural, semantic, and operational change
- how to identify the authoritative layer that actually owns the change
- how drift, validation, release, and documentation surfaces are affected
- how backward-compatibility and migration concerns alter rollout shape
- how to express change in a way that supports review and rollback

## Common Mode Affinity

- planning
- rework
- recovery

## Common Role Affinity

- Planning/Decomposition Lead
- DevOps Engineer
- Quality Assurance Engineer

## Common Inputs

- the proposed change or observed problem
- the authoritative layer or surface being touched
- affected roles, protocols, or runtime assets
- current validation, release, or review obligations
- known compatibility or migration constraints

## Decision Heuristics

- originate semantic changes at the authoritative layer that owns the meaning
- separate runtime-materialization updates from canon or binding changes
- treat compatibility-impacting changes as higher-governance work than purely
  local edits
- require explicit follow-up when documentation, validation, or release surfaces
  would otherwise drift silently
- prefer reversible rollout shapes when uncertainty remains high

## Execution Pattern

- classify the change by type and owning layer
- identify affected downstream surfaces
- state sequencing, review, and rollback implications
- name required validation and documentation follow-up

## Expected Outputs

- change proposal notes
- risk and sequencing summary
- required follow-up or validation list
- drift-sensitive surface inventory

## Verification And Evidence

A well-used instance of this skill should make it possible to answer:

- what kind of change this is
- which authoritative layer owns it
- which downstream surfaces must be updated to stay truthful
- what recovery path exists if the change proves unsound

## Escalation Conditions

Escalate when:

- ownership of the change is unclear across canon, binding, and materialization
  layers
- compatibility or migration consequences are not understood
- the change would require hidden operational authority not currently granted
- rollback or recovery would be unsafe or ambiguous

## Guardrails

- does not replace implementation work
- does not override release or merge authority
- should not become a catch-all justification for skipping validation

## Related Artifacts

- [Skills](./README.md)
- [Change Management Model](../Change-Management-Model.md)
- [Drift Model](../Drift-Model.md)
