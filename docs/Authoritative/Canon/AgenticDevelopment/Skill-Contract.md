---
id: craig-skill-contract
title: Skill Contract
summary: Defines the portable contract for skills as atomic reusable capability units used by parent agents and specialists.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, skills, canon, capability]
related:
  - ./Agentic-Development-Glossary.md
  - ./Agent-Authority-Model.md
  - ./Agent-Composition-Model.md
  - ./Skill-Attachment-Model.md
  - ./Mode-Model.md
supersedes: []
---

# Skill Contract

## Purpose

Define the portable contract for skills so projects can compose parent agents
and specialists from atomic reusable capabilities without collapsing skills
into roles, modes, or protocols.

## Scope

This document governs the portable meaning of a skill and the expectations that
follow from treating skills as atomic reusable capability units.

It does not define any application's initial skill library or any
environment-specific skill file format.

## Binding Decisions

- A `skill` is an atomic reusable capability unit.
- A skill may encode bounded procedure, technique, knowledge, or verification
  guidance.
- A skill may be used directly by a parent agent or curated into a specialist.
- A skill definition should remain reusable across more than one actor whenever
  the underlying capability truly repeats.
- A skill does not, by itself, own workflow continuity, role accountability,
  protocol transitions, or handoff authority.
- A reusable skill should keep its scope narrow enough that it can be composed
  into more than one agent or workflow path.
- A portable skill contract should make the following concerns explicit:
  - intended purpose
  - entry assumptions
  - bounded outputs or return shape
  - constraints and guardrails
  - escalation conditions when the skill is insufficient on its own

## Constraints

- Skill definitions must remain distinct from role definitions, protocol
  definitions, and mode definitions.
- Skills must not silently expand into disguised specialists or parent agents.
- Skill definitions should not depend on one actor's identity in order to make
  sense as reusable capability units.
- Portable skill semantics must remain valid even when a downstream
  environment materializes them through different file layouts or discovery
  mechanisms.

## Non-Goals

- Choose an application's current specialist roster or parent-agent roster.
- Define an environment-specific `SKILL.md` layout or prompt syntax.
- Define protocol ownership or workflow gate logic.

## Related Artifacts

- [Agentic-Development-Glossary.md](./Agentic-Development-Glossary.md)
- [Agent-Authority-Model.md](./Agent-Authority-Model.md)
- [Agent-Composition-Model.md](./Agent-Composition-Model.md)
- [Skill-Attachment-Model.md](./Skill-Attachment-Model.md)
- [Mode-Model.md](./Mode-Model.md)
