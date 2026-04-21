---
id: craig-skill-planning-decomposition
title: Planning Decomposition
summary: Defines the portable skill for breaking work into bounded, reviewable slices with explicit sequencing and dependency reasoning.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, planning, decomposition]
related:
  - ./README.md
  - ../Skill-Contract.md
  - ../Protocols/Planning-Protocol.md
  - ../RoleArchetypes/planning-decomposition-lead.md
supersedes: []
---

# Planning Decomposition

## Purpose

Define the portable skill for turning a larger objective into bounded,
sequenced, reviewable work slices.

## Common Mode Affinity

- planning
- recovery

## Common Role Affinity

- Planning/Decomposition Lead
- Backend Staff Engineer
- DevOps Engineer

## Bounded Capability

- identify the meaningful units of work inside a broader objective
- separate critical-path work from parallelizable work
- state ordering, dependencies, and handoff points clearly
- keep slices small enough for validation and review

## Common Outputs

- decomposition outline
- task or slice sequencing proposal
- dependency and handoff notes

## Guardrails

- does not, by itself, authorize protocol transitions or role ownership
- does not replace implementation or review evidence
- should not become an unbounded product-management or architecture document

## Related Artifacts

- [Skills](./README.md)
- [Skill Contract](../Skill-Contract.md)
- [Planning Protocol](../Protocols/Planning-Protocol.md)
- [Planning/Decomposition Lead](../RoleArchetypes/planning-decomposition-lead.md)
