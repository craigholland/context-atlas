---
id: craig-platform-materialization-model
title: Platform Materialization Model
summary: Defines the portable rules for turning canon and project bindings into runtime-specific discoverable assets without making those assets the source of truth.
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
  - ../../Planning/Agentic/Stories/story_7_platform_materialization_model.md
supersedes: []
---

# Platform Materialization Model

## Purpose

Define the portable rules for turning portable canon and project-specific
bindings into runtime-specific discoverable assets without making those runtime
assets the source of truth.

## Scope

This document governs the portable concept of materialization and the boundary
between authoritative definitions and runtime-facing artifacts.

It does not choose a specific platform such as Codex, Claude, or any other AI
environment.

## Binding Decisions

- Runtime materialization is downstream of:
  - portable canon
  - project-specific bindings
  - platform-specific conventions
- Runtime assets are operational artifacts, not the authoritative source of
  truth for agentic-development concepts.
- Materialization may produce runtime-facing artifacts such as:
  - agent descriptors
  - mode descriptors
  - skill artifacts
  - protocol artifacts
  - configuration files
  - folder conventions
  - generated helper surfaces
- The same portable canon may be materialized into more than one runtime
  platform.
- Platform materialization should preserve traceability back to the canon and
  project-specific bindings that it expresses.

## Constraints

- Portable materialization rules must not hard-code a vendor-specific file
  layout.
- Runtime asset discovery rules belong to the runtime-specific layer, not the
  portable canon.
- A project should be able to change runtime platforms or support more than one
  platform without rewriting the portable definitions.

## Non-Goals

- Define Context Atlas's current runtime platform choice.
- Define the current runtime folder layout for any specific AI environment.
- Replace project-specific bindings with generated runtime assets.

## Related Artifacts

- [Agentic-Development-Glossary.md](./Agentic-Development-Glossary.md)
- [Agent-Authority-Model.md](./Agent-Authority-Model.md)
- [Mode-Model.md](./Mode-Model.md)
- [Skill-Contract.md](./Skill-Contract.md)
- [Story 7 - Platform Materialization Model](../../Planning/Agentic/Stories/story_7_platform_materialization_model.md)
