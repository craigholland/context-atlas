---
id: context-atlas-codex-binding-readme
title: Context Atlas Codex Binding
summary: Defines Codex as the first concrete runtime materialization target for Context Atlas and positions the Codex-specific surfaces as downstream bindings of the portable canon and project identity layer.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, codex, materialization]
related:
  - ../Role-Model.md
  - ../Role-Agent-Binding-Model.md
  - ../Mode-Model.md
  - ../Protocol-Role-Bindings.md
  - ../Protocol-Mode-Bindings.md
  - ../Gate-Review-Pass-Matrix.md
  - ../../Context-Atlas-Agentic-Development-Profile.md
  - ../../../AgenticDevelopment/Platform-Materialization-Model.md
  - ../../../AgenticDevelopment/Materialization-Boundary-Model.md
  - ../../../AgenticDevelopment/Template-Model.md
  - ../../../AgenticDevelopment/Templates/README.md
  - ../../../AgenticDevelopment/Discovery-Model.md
  - ../../../AgenticDevelopment/Materialization-Traceability-Model.md
supersedes: []
---

# Context Atlas Codex Binding

## Purpose

Define Codex as the first concrete runtime materialization target for Context
Atlas and establish the project-specific binding surface that later Codex
folder, template, and governance docs should extend.

## Scope

This document governs the decision to support Codex first, the upstream
authoritative surfaces that Codex materialization must consume, and the
boundary between Codex-specific artifacts and the portable canon.

It does not redefine the portable concepts themselves, and it does not replace
later Codex layout, template, or governance docs.

## Binding Decisions

### 1. Context Atlas Supports Codex As Its First Runtime Materialization Target

Context Atlas will use Codex as its first concrete environment for
materializing the project's agentic-development model into runtime-facing
assets.

That decision is a project binding, not a portable canon claim.

### 2. Codex Binding Is Downstream Of The Portable Canon And The Identity Layer

The Codex surface must inherit meaning from:

- the portable AgenticDevelopment canon
- the Context Atlas Identity bindings
- the Story 7 materialization boundary, template, discovery, and traceability
  model

Codex assets must not become a substitute source of truth for roles, modes,
protocols, skills, or materialization semantics.

### 3. Codex Binding Must Materialize Distinct Concept Families Explicitly

Codex materialization should preserve the explicit distinctions between:

- roles as accountability
- parent agents as materialized accountable actors
- specialists as bounded delegates
- skills as atomic reusable capabilities
- modes as execution states
- protocols as workflow paths

Codex convenience surfaces may aggregate or cross-reference those concepts, but
they should not erase the upstream distinctions that authorize them.

### 4. Codex Is The First Binding, Not The Final Binding

Context Atlas is not declaring Codex to be the only valid future runtime
target.

The Codex binding should therefore:

- remain clearly project-specific
- inherit the generic materialization model
- leave room for later non-Codex bindings without forcing Codex mechanics back
  into the portable layer

### 5. Later Codex Docs Must Make The Binding Mechanically Usable

The downstream Codex surface should eventually make it possible for a
contributor to answer:

- which Codex-discoverable folders and files exist
- which abstract concepts each Codex surface expresses
- which templates or creation instructions generate or refresh those surfaces
- which governance hooks keep those assets aligned over time

Those details belong in the later Codex binding docs, not in this initial
decision record.

### 6. Codex Binding Must Consume One Explicit Upstream Input Set

The Codex binding should treat the following upstream surfaces as its normal
authoritative input set:

- the project structural profile
- the project role model and role-accountability/authority/binding docs
- the project mode model and mode-transition/mutation docs
- the project protocol-role, protocol-mode, and gate-review-pass bindings
- the portable materialization-boundary, template, discovery, and traceability
  docs

If a later Codex artifact appears to require meaning outside that set, the
correct response is to update the upstream canon or binding layer first.

### 7. Future Non-Codex Bindings Should Reuse The Same Upstream Categories

A later non-Codex binding should need the same kinds of upstream inputs even if
it materializes them very differently.

That means the Codex binding should record which upstream categories it needs
without pretending those categories are unique to Codex itself.

## Constraints

- Codex-specific wording should stay in the Codex binding layer instead of
  leaking upward into the portable canon.
- The Codex binding should cite its upstream sources explicitly rather than
  relying on implicit project memory.
- The Codex binding should stay compatible with the Story 7 materialization
  rules around boundary, template, discovery, traceability, and regeneration.
- The Codex binding should remain readable as a downstream consumer of the
  project identity layer rather than as a substitute binding layer of its own.

## Non-Goals

- Define the full Codex folder layout.
- Define the final Codex templates.
- Define the final Codex governance hooks.
- Materialize the runtime-facing Codex assets themselves.

## Related Artifacts

- [Context Atlas Agentic Development Profile](../../Context-Atlas-Agentic-Development-Profile.md)
- [Role Model](../Role-Model.md)
- [Role-Agent Binding Model](../Role-Agent-Binding-Model.md)
- [Mode Model](../Mode-Model.md)
- [Protocol Role Bindings](../Protocol-Role-Bindings.md)
- [Protocol Mode Bindings](../Protocol-Mode-Bindings.md)
- [Gate Review Pass Matrix](../Gate-Review-Pass-Matrix.md)
- [Platform Materialization Model](../../../AgenticDevelopment/Platform-Materialization-Model.md)
- [Materialization Boundary Model](../../../AgenticDevelopment/Materialization-Boundary-Model.md)
- [Template Model](../../../AgenticDevelopment/Template-Model.md)
- [Generic Template Contracts](../../../AgenticDevelopment/Templates/README.md)
- [Discovery Model](../../../AgenticDevelopment/Discovery-Model.md)
- [Materialization Traceability Model](../../../AgenticDevelopment/Materialization-Traceability-Model.md)
