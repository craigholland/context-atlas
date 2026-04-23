---
id: context-atlas-013-cleanup-product-definition
title: 013 Cleanup Product Definition
summary: Defines the first review-response Epic for fast-ROI cleanup across product onboarding clarity, product and contributor path separation, portable-canon leak removal, generated-surface defect cleanup, and Linux-first CI alignment.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [planning, epic, cleanup, documentation, onboarding, canon, ci, review-response]
related:
  - ../../Reviews/context-atlas-product-review.md
  - ../../Reviews/context-atlas-agentic-review.md
  - ../../Reviews/context-atlas-architecture-review.md
  - ../../Reviews/context-atlas-ai-governance-review.md
  - ../../Guides/getting_started.md
  - ../../Guides/context_atlas_tour.md
  - ../../Guides/README.md
  - ../../Authoritative/Canon/AgenticDevelopment/README.md
  - ../../Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md
  - ../../Authoritative/Canon/Architecture/Craig-Architecture-Python.md
  - ../../Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md
  - ../../Authoritative/Canon/Ontology/Documentation-Ontology.md
  - ../../../README.md
  - ../../../docs/README.md
  - ../../../.github/workflows/ci.yml
  - ../../../.github/workflows/ai-verify-folder-contracts.yml
  - ../../../.github/workflows/ai-last-verified.yml
  - ../../../scripts/preflight.py
supersedes: []
---

# 013 Cleanup Product Definition

## Objective

Define the first review-response Epic as a bounded cleanup horizon that fixes
the highest-value clarity, trust, and boundary problems surfaced by the cold
reviews without reopening the repo's deeper runtime-model or core-engine
architecture questions.

This Epic is successful only if:

- a new evaluator can understand what Context Atlas does and what it produces
  more quickly
- the product path no longer forces readers through unnecessary agentic or
  governance detail before they can assess the engine itself
- portable Canon surfaces read more cleanly as portable Canon rather than as a
  layer that casually assumes Context Atlas or Codex
- the generated runtime surface no longer contains obvious presentation defects
- active CI and executable verification commands better reflect the likely
  Linux/macOS contributor baseline

This Epic is intentionally about cleanup with immediate return on trust. It is
not the place to redesign the whole agentic runtime model, resolve deeper
code-shape tensions inside `src/context_atlas/`, or decide the final consumer
distribution shape of the product.

## Problem Statement

The recent reviews surface a consistent pattern: Context Atlas is already
architecturally thoughtful, but the most visible surfaces still ask too much
from a first-time reader or contributor in places where the payoff should be
quicker and the boundary between portable, project-specific, and derived
surfaces should be more obvious.

The highest-signal symptoms are:

- product-facing docs still ask readers to absorb too much vocabulary before
  they see a concrete packet or trace outcome
- user-facing guides still contain internal execution residue such as Story
  numbering or hardening-era vocabulary that does not belong on the product
  path
- the Python runtime floor is easy to miss even though it is a real adoption
  gate
- the product path and the richer agentic/governance path still compete for
  attention in the repo's first-impression surfaces
- portable Canon docs still carry a small set of unnecessary Codex-specific or
  Context Atlas-specific examples
- at least one generated runtime artifact still shows materialization residue
  that weakens trust in the derived surface
- active CI and executable contract commands currently imply a Windows-first
  contributor baseline even though many contributors are more likely to expect
  Linux/macOS alignment

None of these issues, by themselves, require a deeper Epic. Together, they are
substantial enough to justify a bounded cleanup Epic with explicit Story-level
decomposition.

## Inputs

- [Context Atlas Product Review](../../Reviews/context-atlas-product-review.md)
- [Context Atlas Agentic Review](../../Reviews/context-atlas-agentic-review.md)
- [Context Atlas Architecture Review](../../Reviews/context-atlas-architecture-review.md)
- [Context Atlas AI Governance Review](../../Reviews/context-atlas-ai-governance-review.md)
- [Craig Architecture - Planning And Decomposition](../../Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md)
- [README](../../../README.md)
- [Docs README](../../../docs/README.md)
- [Guides README](../../Guides/README.md)
- [Getting Started Guide](../../Guides/getting_started.md)
- [Context Atlas Tour](../../Guides/context_atlas_tour.md)
- [AgenticDevelopment Canon README](../../Authoritative/Canon/AgenticDevelopment/README.md)
- [Craig Architecture - Python](../../Authoritative/Canon/Architecture/Craig-Architecture-Python.md)
- [Craig Architecture - AI Guidance](../../Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md)
- [Documentation Ontology](../../Authoritative/Canon/Ontology/Documentation-Ontology.md)
- active generated runtime surface under `.codex/` and `.agents/skills/`
- active CI and owner-file verification surfaces under `.github/workflows/`
  and `scripts/`

## Scope Boundary

### In Scope

- product-facing docs cleanup where the improvement is immediate, visible, and
  bounded
- stronger audience routing between product-evaluator, contributor, agentic,
  and governance entry surfaces
- small Canon leak cleanup where the portable/project-specific boundary is
  obviously wrong today
- immediate generated-surface defect correction and the smallest guardrail that
  prevents recurrence if that guardrail stays cheap and local
- Linux-first CI and contract-command alignment where the work is clearly
  surface cleanup rather than governance-system redesign

### Out Of Scope

- consumer packaging, PyPI strategy, or public-install distribution policy
- Claude adoption or multi-runtime support for Context Atlas
- runtime-policy placement questions such as `Canon/AgenticDevelopment/Runtime`
- protocol-family, skill-model, namespacing, or specialist-roster redesign
- `__ai__.md` prose-correctness evolution, governed dirt, or broader
  verification-philosophy changes
- deeper code-shape tensions in `src/context_atlas/` such as port ownership,
  Pydantic-in-domain, or service/policy coupling

## Epic Thesis

Context Atlas should feel more legible and trustworthy at the repo edge before
it asks readers to evaluate its richer architecture.

That means this Epic should prefer:

- earlier concrete payoff over longer orientation ramps
- cleaner routing over piling more explanation into the root surfaces
- portable examples in Canon over convenient but local examples
- small visible runtime-surface correctness fixes over waiting for a larger
  future redesign
- contributor-environment alignment where the change is cheap and obvious

It should not try to solve every interesting problem raised by the reviews. Its
job is to remove the avoidable friction that is currently blocking the next
layer of evaluation.

## Proposed Story Decomposition

This Epic is intentionally decomposed into five Story-level architectural
increments. Each Story owns a distinct surface or seam rather than acting as a
grab-bag of unrelated cleanup items.

### Story 1: Product Evaluator On-Ramp And Output Clarity

Owns the product-evaluator path through the root README and guide surfaces so a
new reader can see:

- what Context Atlas is
- what version/runtime floor it expects
- what packet/trace-shaped output success looks like

without first learning the repo's internal execution history.

### Story 2: Product Path Separation From Agentic And Governance Surfaces

Owns the audience-routing boundary between:

- product use
- contributor/governance participation
- agentic/runtime materialization inspection

so product evaluators do not treat `.codex/`, `.agents/skills/`, or
`__ai__.md` as prerequisites for simply using Atlas.

### Story 3: Portable Canon Leak Cleanup

Owns the smallest high-value cleanup of Canon surfaces that currently leak
Context Atlas- or Codex-specific assumptions where the surface is meant to be
portable and reusable.

This Story is bounded to obvious leak cleanup. It does not absorb the broader
runtime-policy and platform-binding redesign that belongs in the later agentic
runtime Epic.

### Story 4: Immediate Generated-Surface Defects

Owns the visible cleanup of runtime-materialization defects in the generated
surface, including the now-confirmed section-boundary bleed defect in generated
mode output, while stopping short of a broader materialization-model redesign.

### Story 5: Linux-First CI And Contract Command Alignment

Owns the contributor-trust quick wins around:

- active GitHub workflow runner choice
- shell/command portability
- executable owner-file contract examples

while remaining explicitly out of scope for broader `__ai__.md` governance
evolution.

## Story Sequencing And Dependency Model

The recommended sequence inside this Epic is:

1. Story 1 - Product Evaluator On-Ramp And Output Clarity
2. Story 2 - Product Path Separation From Agentic And Governance Surfaces
3. Story 3 - Portable Canon Leak Cleanup
4. Story 4 - Immediate Generated-Surface Defects
5. Story 5 - Linux-First CI And Contract Command Alignment

The reasoning is:

- Story 1 improves the first-impression product surface directly and gives the
  later Stories a cleaner "what the product path should feel like" reference
  point.
- Story 2 then clarifies which repo surfaces belong to product use versus
  contributor/governance participation.
- Story 3 benefits from that clearer boundary because it can generalize Canon
  examples without simultaneously redesigning the product route.
- Story 4 can move once the product and Canon boundaries are cleaner, because
  the generated runtime surface is easier to judge as a downstream artifact.
- Story 5 is bounded contributor-trust work that can run late without changing
  the meaning of the first four Stories.

Acceptable bounded parallelism:

- Story 4 may run in parallel with Story 3 if the generated-defect work stays
  strictly upstream of the existing materializer and does not pull runtime
  policy questions back into this Epic.
- Story 5 may run in parallel with Stories 3 or 4 if the CI/workflow changes
  remain limited to surface alignment and do not start redesigning governance.

## Epic Success Criteria

This Epic should be considered successful when:

- the root product path gets a faster and more truthful evaluator route
- at least one concrete packet/trace-shaped output sample is visible in the
  product path
- product-facing docs no longer contain internal Story-level residue
- product-facing docs make it clear that the shared engine can be evaluated
  without adopting the repo's full agentic/governance surface
- portable Canon no longer contains the clearest unnecessary local platform
  leaks
- generated runtime artifacts no longer contain obvious residue defects
- active CI and executable contract-command examples better match a Linux-first
  contributor expectation

## Deliverables

This Epic should ultimately produce:

- a numbered Epic stack under `docs/Planning/013_Cleanup/`
- five Story docs under `docs/Planning/013_Cleanup/Stories/`
- implementation-ready Task PR plans under
  `docs/Planning/013_Cleanup/Stories/Tasks/`
- a cleaner product-evaluator route through `README.md` and guide surfaces
- at least one visible packet/trace output sample in the product-facing guide
  path
- clearer Python/runtime prerequisite visibility
- tighter separation between product, contributor, and generated-runtime entry
  surfaces
- a cleaner portable Canon layer with the smallest obvious local leaks removed
- corrected generated runtime artifacts for the known defect class
- Linux-first workflow and command-shape alignment where the change is bounded
  and cheap

## Non-Goals For This Epic

- publishing to PyPI or redesigning the product distribution model
- introducing a second adopted runtime such as Claude for Context Atlas
- relocating platform-binding docs into Canon or creating
  `Canon/AgenticDevelopment/Runtime`
- redesigning protocols, skills, specialists, or runtime namespacing policy
- broad generated-runtime section validation beyond the smallest cheap guardrail
- redesigning the `__ai__.md` governance model
- resolving deeper code-architecture tensions in `src/context_atlas/`

## Open Questions

- Should the first output sample be a static checked-in artifact, or should it
  be regenerated from a canonical proof/example surface during doc upkeep?
- Should the generated-surface defect story add only the narrowest regression
  that protects against the current residue class, or should that wait for the
  later runtime-model Epic if even the narrow fix starts to broaden?
- Should Linux-first CI alignment stop at the active workflows and executable
  contract commands, or should nearby contributor docs also be updated in the
  same Story when those docs still imply Windows-first operation?
