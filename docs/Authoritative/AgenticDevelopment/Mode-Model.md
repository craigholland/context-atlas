---
id: craig-mode-model
title: Mode Model
summary: Defines the portable semantics of modes as execution states entered while agents follow protocols.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, modes, canon, execution-state]
related:
  - ./Agentic-Development-Glossary.md
  - ./Agent-Authority-Model.md
  - ./Skill-Contract.md
supersedes: []
---

# Mode Model

## Purpose

Define the portable meaning of a mode so later application-specific bindings can
choose concrete modes without redefining what a mode is.

## Scope

This document governs the semantics of modes as execution states used while an
agent follows a protocol.

It does not choose an application's current mode set or name specific modes.

## Binding Decisions

- A `mode` is the current execution state an agent is operating in while
  following a protocol.
- A mode describes how work is being performed, not who is accountable for the
  work.
- A mode may appear in more than one protocol.
- A protocol may revisit the same mode more than once.
- A mode may constrain:
  - allowed mutations
  - expected evidence
  - verification expectations
  - exit conditions
- Mode transitions should be explicit and governed by protocol semantics rather
  than inferred from ad hoc prompt changes.
- A mode is not a role, not a protocol, and not a skill.

## Constraints

- Portable mode semantics must stay runtime-agnostic.
- Mode definitions must not silently absorb application-specific workflow gates
  or environment-specific file conventions.
- Mode semantics should remain reusable across roles instead of becoming
  role-specific mini-protocols.

## Non-Goals

- Choose an application's initial mode set.
- Define protocol-specific gates or step sequences.
- Define environment-specific files for mode discovery.

## Related Artifacts

- [Agentic-Development-Glossary.md](./Agentic-Development-Glossary.md)
- [Agent-Authority-Model.md](./Agent-Authority-Model.md)
- [Skill-Contract.md](./Skill-Contract.md)
