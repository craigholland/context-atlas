---
id: craig-skill-composition-and-integration-planning
title: Composition And Integration Planning
summary: Defines the portable skill for reasoning about how bounded work slices fit back together without violating architectural or workflow boundaries.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, planning, composition, integration]
related:
  - ./README.md
  - ../Agent-Composition-Model.md
  - ../Protocols/Planning-Protocol.md
supersedes: []
---

# Composition And Integration Planning

## Purpose

Define the portable skill for planning how separately bounded work can be
recombined safely and coherently.

## Common Mode Affinity

- planning
- recovery

## Common Role Affinity

- Planning/Decomposition Lead
- Backend Staff Engineer
- DevOps Engineer

## Bounded Capability

- reason about integration seams between slices or agents
- identify where composition must happen and who remains accountable
- preserve layering and boundary constraints while planning recomposition
- surface coordination risks early

## Common Outputs

- integration plan
- ownership-aware recomposition notes
- merge or handoff sequencing guidance

## Guardrails

- does not replace architecture conformance review
- does not grant merge or release authority
- should not silently absorb change-management or operational-delivery work

## Related Artifacts

- [Skills](./README.md)
- [Agent Composition Model](../Agent-Composition-Model.md)
- [Planning Protocol](../Protocols/Planning-Protocol.md)
