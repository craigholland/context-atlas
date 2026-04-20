---
id: craig-platform-materialization-model
title: Platform Materialization Model
summary: Defines the portable rules for turning canon and application bindings into environment-specific discoverable assets without making those assets the source of truth.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, materialization, canon, portability]
related:
  - ./Agentic-Development-Glossary.md
  - ./Agent-Authority-Model.md
  - ./Mode-Model.md
  - ./Skill-Contract.md
supersedes: []
---

# Platform Materialization Model

## Purpose

Define the portable rules for turning portable canon and application-specific
bindings into environment-specific discoverable assets without making those
assets the source of truth.

## Scope

This document governs the portable concept of materialization and the boundary
between authoritative definitions and environment-facing artifacts.

It does not choose any specific execution environment.

## Binding Decisions

- Materialization is downstream of:
  - portable canon
  - application-specific bindings
  - environment-specific conventions
- Materialized assets are operational artifacts, not the authoritative source
  of truth for agentic-development concepts.
- Materialization may produce environment-facing artifacts such as:
  - agent descriptors
  - mode descriptors
  - skill artifacts
  - protocol artifacts
  - configuration files
  - folder conventions
  - generated helper surfaces
- The same portable canon may be materialized into more than one execution
  environment.
- Environment materialization should preserve traceability back to the canon
  and bindings that it expresses.

## Constraints

- Portable materialization rules must not hard-code an environment-specific
  file
  layout.
- Asset discovery rules belong to the environment-specific layer, not the
  portable canon.
- A system should be able to change execution environments or support more than
  one environment without rewriting the portable definitions.

## Non-Goals

- Define any application's current environment choice.
- Define the current folder layout for any specific execution environment.
- Replace application-specific bindings with generated environment-facing
  assets.

## Related Artifacts

- [Agentic-Development-Glossary.md](./Agentic-Development-Glossary.md)
- [Agent-Authority-Model.md](./Agent-Authority-Model.md)
- [Mode-Model.md](./Mode-Model.md)
- [Skill-Contract.md](./Skill-Contract.md)
