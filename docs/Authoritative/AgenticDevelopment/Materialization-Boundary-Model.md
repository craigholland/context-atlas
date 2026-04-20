---
id: craig-materialization-boundary-model
title: Materialization Boundary Model
summary: Defines the portable source-of-truth boundary for agentic materialization and clarifies which inputs feed materialization and which outputs it may produce.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, materialization, boundaries, portability, source-of-truth]
related:
  - ./Boundary-Model.md
  - ./Platform-Materialization-Model.md
  - ./Agentic-Development-Glossary.md
supersedes: []
---

# Materialization Boundary Model

## Purpose

Define the portable source-of-truth boundary for agentic materialization.

## Scope

This document governs what feeds a materialization step, what that step may
produce, and where authority remains when runtime-facing assets are created or
updated.

It does not define any one platform's file layout, discovery behavior, or
regeneration toolchain.

## Binding Decisions

### 1. Materialization Is A Translation Step, Not A Source-Of-Truth Layer

Materialization is the downstream translation of authoritative semantics into
runtime-facing assets.

The materialization step may project authoritative meaning into a form a
runtime can discover or use, but it does not become the new canonical meaning
of those concepts.

### 2. Materialization Inputs Come From Upstream Authoritative Layers

The normal materialization inputs are:

- portable canon
- application-specific bindings
- platform-specific materialization decisions

Those inputs may be expressed through different documents or structured data,
but they should all remain upstream of the runtime-facing assets that result.

### 3. Materialization Outputs Are Runtime-Facing Assets

Materialization may produce assets such as:

- agent descriptors
- role, mode, or protocol projections
- skill artifacts
- configuration files
- discovery-oriented folder layouts
- traceability or regeneration metadata

Those outputs exist so a runtime can consume the governed model. They do not
replace the authoritative docs that defined the model.

### 4. Runtime Assets Must Not Redefine Upstream Meaning Silently

If a runtime-facing asset needs semantics that are not already authorized by
the upstream canon or project bindings, the correct fix is to update the
upstream authoritative source first.

Runtime assets should not silently accumulate meaning that later readers would
have to reverse-engineer back into the canon.

### 5. The Materialization Step Must Stay Traceable

A reviewer should be able to answer:

- which authoritative sources fed this materialized asset
- which layer chose the semantics being expressed
- whether a change belongs in canon, binding, or runtime materialization

If that cannot be answered, the materialization boundary is probably too weak.

### 6. Materialization Should Preserve Layering

The materialization boundary should preserve the three-layer model:

- portable canon defines reusable concepts and invariants
- application-specific bindings define what a project actually uses
- platform-specific materialization defines how that chosen model becomes
  runtime-facing assets

Materialization is therefore downstream of interpretation, not a shortcut
around interpretation.

## Constraints

- Runtime-facing assets must remain downstream of authoritative semantics.
- The materialization boundary must stay portable and vendor-agnostic.
- The boundary must remain explicit enough to support later traceability and
  drift-control work.

## Non-Goals

- Define generic template shapes in detail.
- Define discovery folder conventions.
- Define whether assets are generated, hand-maintained, or mixed.

## Related Artifacts

- [Boundary Model](./Boundary-Model.md)
- [Platform Materialization Model](./Platform-Materialization-Model.md)
- [Agentic Development Glossary](./Agentic-Development-Glossary.md)
