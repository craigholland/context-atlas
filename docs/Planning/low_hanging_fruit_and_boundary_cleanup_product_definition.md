---
id: context-atlas-low-hanging-fruit-and-boundary-cleanup-product-definition
title: Context Atlas Low-Hanging Fruit And Boundary Cleanup Product Definition
summary: Defines a fast-ROI epic for first-impression clarity, obvious documentation defects, and portable-canon purity cleanup surfaced by recent cold reviews.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [planning, quick-wins, documentation, onboarding, canon, review-response]
related:
  - ../Reviews/context-atlas-product-review.md
  - ../Reviews/context-atlas-agentic-review.md
  - ../Reviews/context-atlas-architecture-review.md
  - ../Reviews/context-atlas-ai-governance-review.md
  - ../Guides/getting_started.md
  - ../Guides/context_atlas_tour.md
  - ../Authoritative/Canon/AgenticDevelopment/README.md
  - ../Authoritative/Canon/Architecture/Craig-Architecture-Python.md
  - ../Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md
  - ../Authoritative/Canon/Ontology/Documentation-Ontology.md
  - ../../README.md
  - ../../.github/workflows/ci.yml
  - ../../.github/workflows/ai-verify-folder-contracts.yml
  - ../../.github/workflows/ai-last-verified.yml
  - ../../scripts/preflight.py
supersedes: []
---

# Context Atlas Low-Hanging Fruit And Boundary Cleanup Product Definition

## Objective

Define a short-horizon Epic for the highest-value review follow-ups that:

- improve the first product impression for new readers
- remove obvious user-facing clarity defects
- tighten a small set of avoidable Canon purity leaks
- correct immediately visible generated-surface issues without waiting for a
  broader runtime-model redesign

This Epic is successful only if a new evaluator can understand the product
path more quickly, while portable Canon surfaces also stop carrying a handful
of unnecessary Context Atlas- or Codex-specific leaks.

The goal is not to reopen the entire architecture. The goal is to fix the
highest-signal issues that are cheap enough to address now and meaningful
enough to improve trust immediately.

## Inputs

- [Context Atlas Product Review](../Reviews/context-atlas-product-review.md)
- [Context Atlas Agentic Review](../Reviews/context-atlas-agentic-review.md)
- [Context Atlas Architecture Review](../Reviews/context-atlas-architecture-review.md)
- [Context Atlas AI Governance Review](../Reviews/context-atlas-ai-governance-review.md)
- [README](../../README.md)
- [Getting Started Guide](../Guides/getting_started.md)
- [Context Atlas Tour](../Guides/context_atlas_tour.md)
- [AgenticDevelopment Canon README](../Authoritative/Canon/AgenticDevelopment/README.md)
- [Craig Architecture - Python](../Authoritative/Canon/Architecture/Craig-Architecture-Python.md)
- [Craig Architecture - AI Guidance](../Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md)
- [Documentation Ontology](../Authoritative/Canon/Ontology/Documentation-Ontology.md)
- [CI Workflow](../../.github/workflows/ci.yml)
- [AI Contract Verification Workflow](../../.github/workflows/ai-verify-folder-contracts.yml)
- [Last Verified Update Workflow](../../.github/workflows/ai-last-verified.yml)
- [Preflight Script](../../scripts/preflight.py)
- generated runtime surface under `.codex/` and `.agents/skills/`

Recent review findings that motivate this Epic include:

- product-facing docs still require too much vocabulary before a reader sees a
  concrete payoff
- user-facing guides still contain internal planning-language residue such as
  `Story 4 vocabulary`
- product-evaluator guidance is improved but still competes with the repo's
  richer agentic and governance story
- portable Canon docs still contain a small set of Codex-specific or
  Context Atlas-specific references that should be generalized
- at least one generated runtime file still contains template residue that a
  runtime reader should never see
- active CI and executable contract checks currently present a Windows-first
  runner shape that does not match the likely Linux/macOS contributor baseline

## Proposed Work

### Thesis

Context Atlas should act more like a layered product entry surface and less
like a repo that requires outsiders to reverse-engineer internal development
history before they can decide whether the product is credible.

At the same time, the portable Canon should read more cleanly as portable
Canon, not as a layer that casually assumes Context Atlas or Codex whenever an
example is convenient.

### Product-Facing Quick Wins

This Epic should establish or strengthen these product-facing quick wins:

- a clearer product-evaluator route that explicitly says the `.codex/` and
  `.agents/skills/` runtime surfaces are not required to use the shared Atlas
  engine as a library
- at least one concrete packet/trace output sample in the product-facing guide
  path so new readers can see what success looks like before they run the code
- removal of internal planning-language residue from user-facing guides
- a short outsider-friendly definition of `Codex` wherever that term is needed
  on the product path
- tighter separation between setup steps shared across workflows and the
  workflow-specific differences that actually matter

### Contributor-Path Quick Wins

This Epic should also include the smallest high-value contributor trust fixes
that do not require a deeper governance redesign:

- align active GitHub workflows to a Linux-first runner shape so CI more
  closely matches the likely local environment of many contributors
- convert workflow shell snippets away from PowerShell-specific forms where a
  portable or bash-oriented equivalent is straightforward
- normalize executable owner-file verification commands toward
  Linux/macOS-friendly forms while still documenting Windows analogs for local
  use
- keep this scope bounded to workflow and command-shape alignment rather than
  expanding it into a broader rethink of the `__ai__.md` governance system

### Canon Purity Quick Wins

This Epic should also address the smallest, clearest Canon-boundary leaks:

- replace Context Atlas runtime IDs used as portable examples in Canon
  orientation surfaces with project-neutral placeholders
- remove Codex runtime folder examples from portable architecture docs where
  those examples are meant to describe a runtime-agnostic project layout
- move or reword Canon guidance that currently references `@codex review`
  directly when the point is really a portable review boundary, not a specific
  platform invocation
- generalize validation/governance language that names `Codex` where the model
  really means `platform-bound runtime assets`
- reduce project branding in the portable ontology layer where that branding
  weakens reuse

### Immediate Defect Cleanup

This Epic should include the small but concrete runtime-surface issues that are
cheap to fix now:

- remove template residue from generated agentic runtime files that should be
  fully materialized for a reader
- correct any stale or broken related links created by those same residue
  sections

The important rule is that this Epic should stop at visible cleanup. It should
not absorb the larger validation and model-strengthening work that belongs in a
later agentic runtime Epic.

### Epic Structure

This document should be treated as a rough-draft quick-wins Epic.

The current draft Story shape is:

- Story 1: Product Evaluator On-Ramp And Output Clarity
- Story 2: Product Path Separation From Agentic/Governance Surfaces
- Story 3: Portable Canon Leak Cleanup
- Story 4: Immediate Generated-Surface Defects
- Story 5: Linux-First CI And Contract Command Alignment

The draft decomposition is intentionally shallow. The point of this Epic is to
capture the obvious high-ROI work first, then decide whether any Story needs a
deeper follow-on Epic afterward.

### Target Users

`1. Product evaluator`

- Primary job: decide quickly whether Context Atlas is a credible shared
  context-assembly library worth trying
- Value from this Epic: sees what Atlas produces, what Atlas does not require,
  and where the product path begins without being forced through agentic or
  governance detail first

`2. Architecture reader`

- Primary job: understand the repo's layering model without tripping over
  platform-specific examples in portable docs
- Value from this Epic: sees a cleaner distinction between portable Canon and
  project/runtime-specific bindings

`3. Runtime-surface reviewer`

- Primary job: inspect generated agentic files as runtime artifacts
- Value from this Epic: avoids obvious template-residue defects that weaken
  trust in the materialized surface

`4. Contributor using Linux or macOS`

- Primary job: trust that local expectations and CI behavior roughly match the
  environment they are most likely to use
- Value from this Epic: sees CI and contract examples that no longer imply a
  Windows-first contributor workflow unless Windows-specific behavior is truly
  required

## Deliverables

This Epic should ultimately produce:

- a more concrete product-facing onboarding path with at least one visible
  packet/trace output example
- cleaner user-facing docs without internal Story-number vocabulary
- a crisper statement that Atlas the product can be evaluated separately from
  the repo's Codex/agentic governance system
- a cleaned portable Canon layer with the most obvious Codex- and
  Context Atlas-specific leaks removed
- corrected generated runtime files where materialization residue is visibly
  wrong today
- a Linux-first CI and executable-contract surface that better matches likely
  contributor environments without dropping Windows analog guidance

## Non-Goals For This Epic

- publishing to PyPI or redesigning the project's distribution model
- introducing Claude as a second fully adopted runtime for Context Atlas
- redesigning the whole agentic runtime model or protocol family
- resolving the deeper Craig Architecture code tensions around ports,
  Pydantic-in-domain, or infrastructure/composition boundaries
- replacing the current generated-runtime validator with a much broader
  section-level semantic validator
- redesigning the whole `__ai__.md` governance system or introducing governed
  dirt / prose-correctness features that belong in the dedicated AI governance
  Epic

## Open Questions

- Should the product path include a static checked-in output sample, or should
  it generate that sample from a tracked proof artifact during docs upkeep?
- How much ontology branding can be generalized without weakening the fact that
  Context Atlas is the current proving ground for that canon?
- Should the generated-surface cleanup stop at fixing known residue, or should
  this Epic also add the smallest possible guardrail that would catch the same
  residue class in future generation runs?
- Should Linux-first CI alignment stop at the active GitHub workflows and
  executable contract commands, or should this Epic also update nearby docs and
  examples to make the new baseline more visible to contributors?
