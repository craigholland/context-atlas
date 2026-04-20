---
id: craig-agentic-development-boundary-model
title: Boundary Model
summary: Defines the three-layer boundary between portable agentic canon, application-specific bindings, and environment-specific materialization.
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
  - ./Agentic-Development-Glossary.md
  - ./Agent-Authority-Model.md
  - ./Platform-Materialization-Model.md
supersedes: []
---

# Boundary Model

## Purpose

Define the three-layer boundary that keeps portable agentic canon,
application-specific bindings, and environment-specific materialization
distinct.

## Scope

This document governs where agentic-development content belongs when moving
from generic definitions toward application-specific interpretation and then to
environment-facing assets.

It does not choose any application's actual role set, current modes, or
current execution environment.

## Binding Decisions

- The agentic-development system is separated into three layers:
  - portable canon
  - application-specific bindings
  - environment-specific materialization
- The `portable canon` defines vocabulary, invariant rules, and reusable
  boundary concepts.
- The `application-specific bindings` declare which roles, modes, protocols,
  specialists, skills, runtime-capacity inputs, and environment choices a
  system actually uses.
- The `environment-specific materialization` layer expresses the canon and
  bindings as discoverable environment-facing assets for a specific execution
  environment.
- Application-specific bindings are the first layer where concrete role names,
  concrete mode sets, protocol selections, capacity settings, and environment
  choices may appear.
- Runtime assets are derived operational artifacts, not the source of truth for
  agentic-development concepts.
- Application-specific role names, workflow gates, current capacity numbers,
  and environment-specific folder conventions do not belong in the portable
  canon.

## Constraints

- Portable canon documents must remain reusable across applications and
  environments.
- Application-specific bindings must not be mistaken for universal
  definitions.
- Environment-specific materialization must preserve traceability back to the
  bindings and portable canon that it expresses.
- Changes to environment-facing assets must not silently redefine the canon.

## Non-Goals

- Replace application-specific bindings with a fully generic meta-model.
- Treat environment-discoverable files as the canonical semantics for agentic
  development.
- Define any concrete environment layout here.

## Related Artifacts

- [README.md](./README.md)
- [Platform-Materialization-Model.md](./Platform-Materialization-Model.md)
