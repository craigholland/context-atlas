---
id: context-atlas-013-cleanup-story-2-product-path-separation-from-agentic-and-governance-surfaces
title: Story 2 - Product Path Separation From Agentic And Governance Surfaces
summary: Defines how the cleanup Epic should separate product-evaluator guidance from contributor, agentic-runtime, and __ai__ governance surfaces without hiding those surfaces from readers who actually need them.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-23
owners: [core]
tags: [cleanup, story, routing, product-path, agentic, governance]
related:
  - ../013_cleanup_product_definition.md
  - ../../../../README.md
  - ../../../../__ai__.md
  - ../../../../docs/README.md
  - ../../../Guides/README.md
  - ../../../Authoritative/Canon/AgenticDevelopment/README.md
  - ../../../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml
  - ../../../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md
  - ../../../../.codex/AGENTS.md
supersedes: []
---

# Story 2 - Product Path Separation From Agentic And Governance Surfaces

## Objective

Clarify the boundary between:

- using Context Atlas as a product/library
- contributing to the repo
- inspecting the repo's derived agentic runtime surface
- participating in the repo's `__ai__.md` governance model

This Story should make those paths easier to choose without pretending that the
agentic or governance layers do not exist.

## Inputs

- [013 Cleanup Product Definition](../013_cleanup_product_definition.md)
- [README](../../../../README.md)
- [Docs README](../../../../docs/README.md)
- [Root Owner File](../../../../__ai__.md)
- [Guides README](../../../Guides/README.md)
- [AgenticDevelopment Canon README](../../../Authoritative/Canon/AgenticDevelopment/README.md)
- [Materialization Manifest](../../../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml)
- [Codex Materialization README](../../../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md)
- current generated runtime surface under `.codex/` and `.agents/skills/`

## Proposed Tasks

### Task 1: Audience Routing And Boundary Statement

Task 1 now settles the repo-edge audience statement around four distinct
reader jobs:

- product evaluation and use
- generated-runtime inspection
- Canon/Identity architecture reading
- `__ai__.md` governance participation

That split now appears consistently across the root
[README](../../../../README.md), [docs/README.md](../../../../docs/README.md),
and [docs/Guides/README.md](../../../Guides/README.md) without pretending that
all readers need the same path.

- define the shortest truthful statement of what a product evaluator does and
  does not need to care about
- route readers toward product, contributor, and agentic/governance surfaces
  based on intent instead of forcing one blended path
- keep the routing language honest about the repo's complexity without turning
  every entry surface into a warning label

### Task 2: Optionality And Dependency Truth

Task 2 now settles the dependency-truth boundary for the Story:

- `.codex/`, `.agents/skills/`, and `__ai__.md` remain important repo layers
- those layers are contributor/runtime/governance surfaces rather than product
  prerequisites
- evaluators following the product route should be pointed first toward
  guides/examples instead of being told to absorb the full repo operating
  model

That contract now appears consistently across the root
[README](../../../../README.md), [docs/README.md](../../../../docs/README.md),
[docs/Guides/README.md](../../../Guides/README.md), and the project-specific
[Codex materialization binding](../../../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md).

- make it explicit where `.codex/`, `.agents/skills/`, and `__ai__.md` are
  downstream or contributor-facing surfaces rather than product prerequisites
- ensure the shared engine can be evaluated without implying that a reader must
  adopt the repo's full agentic/governance operating model
- preserve truthful language about when those surfaces do matter for
  contributors or architecture readers

### Task 3: Docs Index And Cross-Link Alignment

Task 3 now settles the index hierarchy and cross-link model for the Story:

- `README.md` is the repo map
- `docs/README.md` is the documentation route splitter
- `docs/Guides/README.md` is the product guide hub

Those surfaces now express the same audience split while keeping their jobs
distinct. Deeper links into the portable
[AgenticDevelopment canon](../../../Authoritative/Canon/AgenticDevelopment/README.md)
and the project-specific
[Codex binding](../../../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md)
are now labeled as intentional architecture/runtime routes instead of
bleeding back into the product path as hidden setup steps.

- align the root README, `docs/README.md`, and guide index so the same audience
  split is visible at each routing layer
- remove accidental path competition where product, governance, and runtime
  surfaces all present themselves as the same kind of "start here"
- keep deeper contributor-facing detail discoverable by link rather than by
  expanding the product route

### Task 4: Contributor-Path Containment

Task 4 now settles the contributor-path containment rule for the Story:

- product-facing repo-edge docs should not carry detailed Codex refresh or
  governance-operation commands inline
- contributor refresh and drift-check workflow for generated runtime assets
  should live in the owning
  `docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/`
  surfaces
- product and docs-index routes may still point contributors there, but they
  should do so as intentional contributor/governance routes rather than as
  hidden product prerequisites

- ensure contributor and governance instructions live where they belong instead
  of bleeding back into product-facing docs
- keep any remaining cross-links intentional and purpose-labeled
- leave a structure that later packaging or contributor-experience work can
  refine without having to first undo this Story's routing decisions

## Planned Task Decomposition

- [Task 2.1 - Audience Routing And Boundary Statement](./Tasks/task_2_1_audience_routing_and_boundary_statement.md)
- [Task 2.2 - Optionality And Dependency Truth](./Tasks/task_2_2_optionality_and_dependency_truth.md)
- [Task 2.3 - Docs Index And Cross-Link Alignment](./Tasks/task_2_3_docs_index_and_cross_link_alignment.md)
- [Task 2.4 - Contributor-Path Containment](./Tasks/task_2_4_contributor_path_containment.md)

## Sequencing

- define the intended audience split first
- make dependency truth explicit next so the routing language has a real basis
- align the docs indexes and cross-links after the boundaries are settled
- contain contributor-path detail last so the product route stays clean

## Risks And Unknowns

- The Story can become hand-wavy if it only rearranges links without making the
  optionality of agentic/governance surfaces explicit.
- It is easy to hide contributor surfaces too aggressively and make them harder
  to find for the readers who actually need them.
- Product/contributor separation can drift toward packaging policy if the Story
  starts deciding what should ship rather than what should be routed.

## Exit Criteria

- product-facing docs state clearly that Atlas can be evaluated without
  adopting the repo's full contributor/agentic/governance stack
- product, contributor, and generated-runtime surfaces are easier to
  distinguish at the repo edge
- cross-links remain discoverable but no longer compete as one blended route

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- product-facing surfaces remain truthful about optional versus required
  contributor/runtime/governance layers
- The repository preflight command passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge

## Related Artifacts

- [013 Cleanup Product Definition](../013_cleanup_product_definition.md)
- [README](../../../../README.md)
- [Docs README](../../../../docs/README.md)
- [Root Owner File](../../../../__ai__.md)
- [Materialization Manifest](../../../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml)
- [Task docs](./Tasks/)
