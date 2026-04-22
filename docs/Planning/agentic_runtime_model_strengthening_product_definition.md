---
id: context-atlas-agentic-runtime-model-strengthening-product-definition
title: Context Atlas Agentic Runtime Model Strengthening Product Definition
summary: Defines the next agentic-runtime epic for reusable platform bindings, stronger protocol contracts, more execution-ready skills, and higher-fidelity runtime materialization.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [planning, agentic-development, runtime, protocols, materialization, codex, claude]
related:
  - ../Reviews/context-atlas-agentic-review.md
  - ../Reviews/context-atlas-architecture-review.md
  - ../Exploratory/agentic_runtime_materialization_shortcomings.md
  - ../Authoritative/Canon/AgenticDevelopment/README.md
  - ../Authoritative/Canon/AgenticDevelopment/Materialization-Boundary-Model.md
  - ../Authoritative/Canon/AgenticDevelopment/Platform-Materialization-Model.md
  - ../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml
  - ../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md
  - ../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md
  - ./completed/Agentic/agentic_development_product_definition.md
supersedes: []
---

# Context Atlas Agentic Runtime Model Strengthening Product Definition

## Objective

Define the next agentic-runtime Epic for Context Atlas so that the current
manifest-driven Codex surface becomes:

- more operationally complete
- more execution-ready for real agent work
- cleaner in its Canon-versus-Identity boundary
- more reusable across AI client ecosystems than the current Codex-first shape

This Epic is successful only if Context Atlas strengthens the runtime model in
two directions together:

- downward, by making protocols, skills, and generated assets concrete enough
  for real execution and review
- upward, by making reusable platform-binding guidance live in the portable
  Canon while keeping Context Atlas-specific runtime choice in Identity

The goal is not merely to add more generated files. The goal is to make the
derived configuration model stronger, more portable, and more faithful to the
layering it already claims.

## Inputs

- [Context Atlas Agentic Review](../Reviews/context-atlas-agentic-review.md)
- [Context Atlas Architecture Review](../Reviews/context-atlas-architecture-review.md)
- [Agentic Runtime Materialization Shortcomings](../Exploratory/agentic_runtime_materialization_shortcomings.md)
- [AgenticDevelopment Canon README](../Authoritative/Canon/AgenticDevelopment/README.md)
- [Materialization Boundary Model](../Authoritative/Canon/AgenticDevelopment/Materialization-Boundary-Model.md)
- [Platform Materialization Model](../Authoritative/Canon/AgenticDevelopment/Platform-Materialization-Model.md)
- [Delegation Model](../Authoritative/Canon/AgenticDevelopment/Delegation-Model.md)
- [Escalation Model](../Authoritative/Canon/AgenticDevelopment/Escalation-Model.md)
- [Skill Contract](../Authoritative/Canon/AgenticDevelopment/Skill-Contract.md)
- [Context Atlas Agentic Development Profile](../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md)
- [Materialization Manifest](../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml)
- current Codex binding surface under
  `docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/`
- generated runtime assets under `.codex/` and `.agents/skills/`

Recent review findings and follow-up discussion that motivate this Epic include:

- operational delivery currently has no primary governing protocol
- escalation and delegation have trigger guidance but no concrete output schema
- skill workflows remain stronger as capability descriptions than as
  followable execution guides
- generated runtime fidelity needs section-level quality checks, not just file
  presence and drift checks
- reusable Codex-specific guidance may belong in portable Canon rather than in
  Context Atlas-only Identity docs
- Context Atlas likely wants Codex as its current `AI de jure`, while still
  making room for future Claude guidance as a portable sibling binding
- the Canon README would benefit from a clearer explanation of why this repo
  prefers derived runtime configuration over hand-maintained agent files

## Proposed Work

### Thesis

Context Atlas should continue treating runtime agent assets as generated
downstream artifacts, not as the place where agent semantics are authored.

But if the repo wants that derived model to stay credible as more than a
proof-of-concept, it needs:

- stronger upstream protocol and skill semantics
- clearer placement of reusable platform-binding guidance
- better validation of generated runtime fidelity

Story 1 in this Epic should make that derived-configuration stance explicit in
the Canon entry surface itself, rather than assuming readers will infer it from
the manifest, generator, and drift-check tooling alone.

The intended shape is a short section near the top of
[AgenticDevelopment Canon README](../Authoritative/Canon/AgenticDevelopment/README.md)
called `Why Derived Configuration`, using guidance close to this:

> Many agentic development setups are built from static runtime files: a flat
> `AGENTS.md`, a handful of per-agent configs, or a small rules folder. Those
> surfaces are fast to write and immediately legible, but they have an inherent
> correctness problem: there is no upstream source of truth to compare them
> against, so drift is difficult to detect and cross-agent consistency is often
> maintained only by discipline.
>
> This canon prefers a derived model instead. Portable canon defines terms,
> invariants, and reusable structures. A project-specific Identity layer binds
> those structures to a real project. A machine-readable manifest expresses the
> binding decisions. Runtime-facing agent assets are then generated downstream
> from that upstream source of truth.
>
> This is the same broad architectural pattern used by systems such as
> protobuf, OpenAPI, and dbt: the artifact used at runtime is not the thing
> edited by hand. Semantic changes happen upstream; downstream assets are
> derived and validation checks that the derivation remains faithful.

That wording should stay portable in Canon. The concrete Context Atlas and
Codex runtime details should still live one layer down in Identity and the
generated runtime surface.

### Product Shape

This Epic should strengthen the current four-layer shape:

- portable Canon defines reusable concepts and platform-binding patterns
- Identity defines what Context Atlas actually chooses
- the manifest binds project choices in machine-readable form
- runtime assets remain generated downstream

The key refinement is:

- reusable `Codex` and future `Claude` client-binding guidance should live in
  Canon when it is reusable across projects
- Context Atlas Identity should say which platform(s) this project adopts and
  how it binds them locally

That means Identity `Materializations/` should increasingly read as project
selection and local override, not as the universal home of all Codex or Claude
guidance for every future adopter.

### Core Capability Areas

This Epic should establish or strengthen these capability areas:

- a dedicated operational-delivery protocol with explicit readiness,
  verification, and outcome expectations
- concrete output schemas for escalation and delegation, comparable in clarity
  to the existing handoff contract
- skill workflows that move beyond high-level imperatives into more followable
  execution guidance, including bounded activation conditions where needed
- reusable platform-binding canon for Codex and a portable path for Claude
  guidance, without implying that Context Atlas has already adopted Claude as a
  runtime
- clearer derived-configuration rationale near the top of the
  AgenticDevelopment Canon README so readers understand why this system prefers
  manifest-driven generation over hand-maintained runtime files
- stronger validation of generated runtime files so template residue or
  half-materialized sections are caught automatically
- clearer maintenance-mode semantics for `generated`, `human`, and future
  `mixed` support so the runtime layer does not get ahead of what tooling can
  actually enforce

### Epic Structure

This document should be treated as a rough-draft agentic-runtime Epic.

The current draft Story shape is:

- Story 1: Derived Configuration Orientation And Canon README Strengthening
- Story 2: Platform-Binding Canon For Codex And Claude
- Story 3: Identity Runtime Choice And Local Materialization Boundaries
- Story 4: Operational Delivery, Delegation, And Escalation Protocol Concreteness
- Story 5: Skill Workflow Grounding And Activation Rules
- Story 6: Generated Surface Fidelity And Maintenance-Mode Validation

This decomposition intentionally combines review findings and recent design
discussion instead of pretending they are separate concerns. The Canon/Identity
placement decision is part of the runtime-model problem, not a side note.

### Target Users

`1. Agentic-system maintainer`

- Primary job: evolve the runtime model without collapsing the distinction
  between portable canon, project binding, and generated surface
- Value from this Epic: gets a cleaner authoritative structure and stronger
  runtime validation

`2. Runtime-asset reviewer`

- Primary job: inspect `.codex/` and `.agents/skills/` as trustworthy derived
  artifacts
- Value from this Epic: sees clearer protocols, better-generated files, and
  fewer half-specified runtime surfaces

`3. Future non-Codex adopter`

- Primary job: understand whether the agentic system is portable beyond one
  AI client
- Value from this Epic: finds reusable client-binding guidance in Canon rather
  than interpreting Codex-first Identity docs as a universal design limit

`4. Context Atlas operator`

- Primary job: understand which runtime Context Atlas actually chose and why
- Value from this Epic: sees Codex as the current project choice without
  confusing that local choice for the full portable agentic canon

## Deliverables

This Epic should ultimately produce:

- a `Why Derived Configuration` section in the AgenticDevelopment Canon entry
  surface that explains the upstream-then-derived model in portable terms
- reusable platform-binding canon for Codex and a portable sibling path for
  Claude guidance
- a sharper Identity materialization layer that clearly reads as Context
  Atlas-specific runtime choice and local binding
- one operational-delivery protocol plus concrete escalation and delegation
  schemas
- more execution-ready skill workflow definitions
- stronger generated-surface validation that catches section-level residue or
  malformed runtime guidance

## Non-Goals For This Epic

- adopting Claude as a fully materialized runtime for Context Atlas right now
- replacing the manifest-driven generated model with hand-maintained runtime
  files
- building a live agent scheduler or true multi-runtime orchestration layer
- turning every skill into a provider-specific step-by-step tool script
- reopening the deeper package-layer Craig Architecture tensions inside
  `src/context_atlas/`

## Open Questions

- Should the reusable platform-binding canon live under a new
  `PlatformBindings/` directory, or should it extend the existing
  AgenticDevelopment materialization-model surface in a lighter way?
- How should Context Atlas express `Codex` as its current `AI de jure` without
  making the Canon look Codex-bound?
- Should `maintenance_mode: mixed` become part of this Epic if manual-block
  semantics can be defined cleanly, or should that stay deferred until after
  the current runtime-fidelity work lands?
- How far should skill activation rules go before they stop being portable
  skill canon and start becoming project- or runtime-specific execution policy?
