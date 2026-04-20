---
id: craig-skill-attachment-model
title: Skill Attachment Model
summary: Defines the portable model for how parent agents and specialists attach to and consume skills without turning skill attachments into role, protocol, or mode definitions.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, skills, attachment, composition, canon]
related:
  - ./Skill-Contract.md
  - ./Agent-Composition-Model.md
  - ./Agent-Authority-Model.md
  - ./Agentic-Development-Glossary.md
supersedes: []
---

# Skill Attachment Model

## Purpose

Define the portable model for how parent agents and specialists attach to and
consume skills without letting attachment semantics absorb role, protocol, or
mode concerns.

## Scope

This document governs the relationship between actor definitions and the skills
they use, including how skills may be attached, curated, or activated in a way
that remains structurally portable.

It does not define any application's concrete skill inventory or any
environment-specific skill-discovery format.

## Binding Decisions

- Skills are attached to actors; they are not themselves actors.
- A parent agent may carry:
  - direct baseline skills it is expected to use itself
  - conditional skills it may invoke in narrower contexts
  - delegation rights over specialists with their own curated skills
- A specialist should carry a curated skill set that is narrow enough to
  justify its delegated scope.
- Skill attachment should make explicit whether a skill is:
  - baseline for the actor
  - conditional for a bounded context
  - prohibited from implying broader authority than the actor already has
- The same portable skill may be attached to more than one actor.
- Attachment semantics should describe capability availability, not workflow
  ownership or role accountability.

## Constraints

- Skill attachment must not be used as a hidden way to introduce role-specific
  or protocol-specific behavior.
- A specialist's attached skills must reinforce its narrow scope rather than
  quietly broadening it.
- Parent-agent attachment rules must preserve the distinction between direct
  skill use and delegated specialist use.
- Attachment semantics should remain portable across execution environments.

## Non-Goals

- Define a specific application's concrete skill library.
- Define environment-specific skill manifests or discovery folders.
- Decide which protocol step should invoke a specific skill.

## Related Artifacts

- [Skill Contract](./Skill-Contract.md)
- [Agent Composition Model](./Agent-Composition-Model.md)
- [Agent Authority Model](./Agent-Authority-Model.md)
- [Agentic Development Glossary](./Agentic-Development-Glossary.md)
