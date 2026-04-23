---
id: context-atlas-consumer-packaging-and-distribution-product-definition
title: Context Atlas Consumer Packaging And Distribution Product Definition
summary: Defines a rough-draft Epic for the installable consumer product surface, distribution model, and separation between product users and contributor/governance infrastructure.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [planning, packaging, distribution, product-surface, onboarding, pypi]
related:
  - ../Reviews/context-atlas-product-review.md
  - ../../README.md
  - ../../pyproject.toml
  - ../Guides/README.md
  - ../Guides/getting_started.md
  - ../Release/README.md
  - ../Authoritative/Identity/Context-Atlas-Charter.md
  - ../Authoritative/Identity/Context-Atlas-System-Model.md
  - ./013_Cleanup/013_cleanup_product_definition.md
  - ./deeper_architectural_tensions_product_definition.md
supersedes: []
---

# Context Atlas Consumer Packaging And Distribution Product Definition

## Objective

Define the next product-facing Epic for Context Atlas so that people who want
to install and use the engine as consumers can do so without first
understanding the repo's contributor governance, agentic-development system,
planning archives, or `__ai__.md` enforcement machinery.

This Epic is successful only if Context Atlas becomes easier to consume as a
product in three ways together:

- the supported installable product surface is narrower and clearer
- the distribution model is explicit and credible
- product users can find the product path without being pulled through the
  contributor/governance stack

The goal is not to reduce the repo's internal richness. The goal is to make
that richness stop feeling like a prerequisite for ordinary product adoption.

## Inputs

- [Context Atlas Product Review](../Reviews/context-atlas-product-review.md)
- [README](../../README.md)
- [pyproject.toml](../../pyproject.toml)
- [Guides Index](../Guides/README.md)
- [Getting Started Guide](../Guides/getting_started.md)
- [Release Notes Index](../Release/README.md)
- [Context Atlas Charter](../Authoritative/Identity/Context-Atlas-Charter.md)
- [Context Atlas System Model](../Authoritative/Identity/Context-Atlas-System-Model.md)
- current install path:
  - local repository checkout
  - editable install
  - starter CLI and starter API namespace
- current governance and contributor surfaces:
  - `__ai__.md`
  - `docs/Authoritative/Canon/`
  - `docs/Authoritative/Identity/`
  - `.codex/`
  - `.agents/skills/`

Recent review findings and follow-up discussion that motivate this Epic
include:

- consumers who only want to use Atlas should not need to mentally parse the
  repo's governance and agentic infrastructure
- the current install story is still repo-first and editable-install-first
- there is no clear distinction yet between the installable product and the
  contributor-oriented repo surface
- product docs are better than before, but they still live inside a repo whose
  primary audience is often a contributor or architecture reviewer
- broader packaging/distribution questions should not be hidden inside deeper
  architectural cleanup because the primary success criteria are product-facing

## Proposed Work

### Thesis

Context Atlas can remain a rich governed repo for contributors while also
becoming a narrower, cleaner product for consumers.

Those two concerns should be related but not collapsed:

- contributors need Canon, Identity, agentic runtime materialization,
  governance enforcement, planning archives, and release-process context
- consumers need a supported package, a supported API/CLI surface, a credible
  install path, and a small number of truthful guides

This Epic should explicitly design that distinction instead of leaving
consumers to infer it from the same repo that maintainers use to build Atlas.

### Product Shape

This Epic should define a consumer-facing product shape with:

- one clearly named installable package surface
- one explicitly supported public API and starter CLI path
- one consumer-oriented onboarding path
- one explicit statement of which repo surfaces are product-facing versus
  contributor-only

The important rule is that this Epic should treat packaging and distribution as
first-class product work, not as an incidental byproduct of the repo already
having a `pyproject.toml`.

### Core Capability Areas

This Epic should establish or strengthen these capability areas:

- a clearly bounded public consumer surface for Atlas usage
- a stated distribution model:
  - repo-only
  - PyPI package
  - or a staged path from one to the other
- a consumer install path that does not assume the user wants the full dev
  extras and contributor toolchain unless that is truly required
- a clearer separation between:
  - product docs for users of Atlas
  - contributor docs for builders of Atlas
  - governance/agentic docs for operators of the repo itself
- a release/publication story that explains what a shipped version actually
  means for consumers, not just for repo maintainers

### Epic Structure

This document should be treated as a rough-draft consumer-packaging Epic.

The current draft Story shape is:

- Story 1: Supported Consumer Surface And Public API
- Story 2: Distribution Model And Packaging Boundaries
- Story 3: Consumer Onboarding And Install Path
- Story 4: Repo-Only Governance And Contributor Surface Separation
- Story 5: Release, Publication, And Consumer Trust Signals

This Story set is intentionally product-facing. It should take inputs from the
deeper architectural Epic where needed, but it should not disappear inside
internal architecture cleanup.

### Target Users

`1. Python library consumer`

- Primary job: install Atlas and call the supported API or starter CLI
- Value from this Epic: gets a clear supported entrypoint and a credible
  install story without parsing repo-internal governance surfaces

`2. Product evaluator`

- Primary job: decide whether Atlas is real, usable, and worth adopting
- Value from this Epic: can distinguish the shipped product from the richer
  contributor and governance scaffolding around it

`3. Maintainer thinking about distribution`

- Primary job: decide what should ship, what should remain repo-only, and how
  releases should signal supported usage
- Value from this Epic: gets one planning surface dedicated to packaging and
  consumer trust rather than scattering those decisions across docs cleanup and
  architectural debates

## Deliverables

This Epic should ultimately produce:

- a more explicit definition of the supported installable consumer surface
- a clearer decision about Context Atlas distribution and publication model
- a narrower, more consumer-friendly install and onboarding path
- a stronger separation between product-facing docs and repo-only contributor
  or governance surfaces
- clearer release/publication expectations for consumers evaluating shipped
  versions

## Non-Goals For This Epic

- redesigning the core engine architecture
- moving all governance and agentic-development material out of the repo
- fully solving the deeper Craig Architecture tensions that may influence the
  final public API shape
- implementing a full marketplace of runtime integrations
- forcing immediate PyPI publication before the supported consumer surface is
  actually clear

## Open Questions

- Is Context Atlas fundamentally a repo-first framework, a packaged library, or
  a staged combination of both?
- Which current docs should become consumer-primary, and which should remain
  contributor-only even if they stay public?
- Should the first consumer packaging milestone be a clarified repo-first
  install path, or a true package publication milestone?
- How much of the current examples, proof surfaces, and generated runtime
  assets should ship with the consumer-facing product versus remain repo-only?
