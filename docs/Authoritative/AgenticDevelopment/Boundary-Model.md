---
id: craig-agentic-development-boundary-model
title: Boundary Model
summary: Defines the three-layer boundary between portable agentic canon, project-specific bindings, and runtime-specific materialization.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, boundaries, canon, materialization]
related:
  - ./README.md
  - ./Platform-Materialization-Model.md
  - ../../Planning/Agentic/agentic_development_product_definition.md
  - ../../Planning/Agentic/Stories/story_1_portable_agentic_development_canon.md
supersedes: []
---

# Boundary Model

## Purpose

Define the three-layer boundary that keeps portable agentic canon,
project-specific bindings, and runtime-specific materialization distinct.

## Scope

This document governs where agentic-development content belongs when moving
from generic definitions toward Context Atlas-specific interpretation and then
to runtime-facing assets.

It does not choose Context Atlas's actual role set, current modes, or current
runtime platform.

## Binding Decisions

- The agentic-development system is separated into three layers:
  - portable canon
  - project-specific bindings
  - runtime-specific materialization
- The `portable canon` defines vocabulary, invariant rules, and reusable
  boundary concepts.
- The `project-specific bindings` declare which roles, modes, protocols,
  specialists, skills, runtime-capacity inputs, and platform choices a project
  actually uses.
- The `runtime-specific materialization` layer expresses the canon and project
  bindings as discoverable runtime-facing assets for a specific AI environment.
- Runtime assets are derived operational artifacts, not the source of truth for
  agentic-development concepts.
- Project-specific role names, workflow gates, current capacity numbers, and
  vendor-specific folder conventions do not belong in the portable canon.

## Constraints

- Portable canon documents must remain reusable across projects and AI
  environments.
- Project-specific bindings must not be mistaken for universal definitions.
- Runtime-specific materialization must preserve traceability back to the
  project bindings and portable canon that it expresses.
- Changes to runtime-facing assets must not silently redefine the canon.

## Non-Goals

- Replace project-specific bindings with a fully generic meta-model.
- Treat runtime-discoverable files as the canonical semantics for agentic
  development.
- Define the concrete Codex, Claude, or other platform layouts here.

## Related Artifacts

- [README.md](./README.md)
- [Platform-Materialization-Model.md](./Platform-Materialization-Model.md)
- [Context Atlas Agentic Development Product Definition](../../Planning/Agentic/agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](../../Planning/Agentic/Stories/story_1_portable_agentic_development_canon.md)
