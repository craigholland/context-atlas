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

### 1. Materialization Is Downstream Of Authoritative Semantics

- Materialization is downstream of:
  - portable canon
  - application-specific bindings
  - environment-specific conventions
- Materialized assets are operational artifacts, not the authoritative source
  of truth for agentic-development concepts.

### 2. Materialization May Produce Runtime-Facing Asset Surfaces

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

### 3. Upstream Semantic Changes Must Originate Upstream

If a change affects:

- the meaning of a role, mode, skill, protocol, capacity rule, or boundary
- the project's chosen bindings
- the intended semantics of a runtime-facing artifact

then the change should originate in the relevant upstream authoritative layer
before the materialized assets are updated.

### 4. Runtime-Facing Updates Should Not Quietly Redefine Meaning

If a runtime-facing artifact appears to require meaning that is not already
authorized upstream, the correct response is to update the canon or binding
layer first.

Materialization should not become an informal place where semantic drift is
introduced and only discovered later during review.

### 5. Materialization Updates May Originate Downstream Only When Semantics Stay Stable

Some changes are legitimately downstream-first, such as:

- formatting changes
- non-semantic template refinements
- environment-specific layout adjustments that do not change meaning
- traceability or regeneration metadata refinements

Those changes are acceptable so long as they do not implicitly redefine the
underlying authoritative semantics.

### 6. Discovery Mechanics Are Bound Downstream From The Portable Model

The portable materialization layer may define what asset classes must be
discoverable, but the concrete discovery mechanics that satisfy that need
belong downstream.

That includes choices such as:

- folder conventions
- filenames
- manifests
- indexes
- explicit configuration hooks

Those choices should bind to the portable discovery model rather than replace
it.

### 7. Maintenance Mode And Regeneration Expectations Should Be Declared

Materialization should make it possible for downstream bindings to declare
whether runtime-facing assets are:

- hand-maintained
- generated
- mixed

That declaration belongs downstream, but the expectation that it be explicit
belongs in the portable materialization model.

## Constraints

- Portable materialization rules must not hard-code an environment-specific
  file
  layout.
- Asset discovery rules belong to the environment-specific layer, not the
  portable canon.
- Downstream discovery mechanics should document how they satisfy the portable
  discovery model and template vocabulary.
- Downstream regeneration or maintenance choices should preserve traceability
  back to the canon, bindings, and template surfaces that authorize the
  runtime-facing asset.
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
