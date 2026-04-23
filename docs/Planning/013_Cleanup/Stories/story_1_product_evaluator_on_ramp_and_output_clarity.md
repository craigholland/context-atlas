---
id: context-atlas-013-cleanup-story-1-product-evaluator-on-ramp-and-output-clarity
title: Story 1 - Product Evaluator On-Ramp And Output Clarity
summary: Defines how the first cleanup Epic should make the product-evaluator path clearer, faster, and more concrete by foregrounding prerequisites, mental model, and packet/trace-shaped output.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, story, onboarding, docs, output, product-path]
related:
  - ../013_cleanup_product_definition.md
  - ../../../Guides/getting_started.md
  - ../../../Guides/context_atlas_tour.md
  - ../../../Guides/README.md
  - ../../../../README.md
  - ../../../../docs/README.md
  - ../../../../examples
supersedes: []
---

# Story 1 - Product Evaluator On-Ramp And Output Clarity

## Objective

Make the product-evaluator route legible enough that a first-time reader can
quickly answer three questions without falling into contributor-only detail:

- what Context Atlas is
- what is required to try it locally
- what concrete packet/trace-shaped output success looks like

This Story should treat the root README as the repo map, the guide layer as the
product tour, and examples or proof artifacts as the place where visible output
evidence should come from.

## Inputs

- [013 Cleanup Product Definition](../013_cleanup_product_definition.md)
- [README](../../../../README.md)
- [Docs README](../../../../docs/README.md)
- [Guides README](../../../Guides/README.md)
- [Getting Started Guide](../../../Guides/getting_started.md)
- [Context Atlas Tour](../../../Guides/context_atlas_tour.md)
- current examples and proof surfaces under `examples/`
- current release-facing docs under `docs/Release/`

## Proposed Tasks

Task 1 is now settled around one entry-surface contract: the root README and
the guide entry path both surface the real Python `3.12+` starter floor early,
and the root repo map keeps `Codex` mentions brief and outsider-friendly.

### Task 1: Product Entry Surface And Runtime-Floor Visibility

- keep the root README focused on the product mental model and routing
- make the Python runtime floor visible early enough that a product evaluator
  does not miss a real prerequisite
- keep any needed explanation of `Codex` or related terms short and outsider-
  friendly when those terms still appear on the product path
- ensure the product path does not require opening deep architecture or
  governance docs to understand the first install/run expectation

### Task 2: Concrete Output Sample Surface

Task 2's first slice now settles the bounded sample-source decision: the
product-facing starter command and repository-local starter companion should
use the checked-in sample repository docs under
`examples/codex_repository_workflow/sample_repo/docs` rather than the repo root
`docs/` tree as the reproducible first-run corpus.

Task 2 is now settled around one visible product-facing sample too: the bounded
starter output artifact lives at
`examples/starter_context_flow_sample_output.md`, and both
[Getting Started](../../../Guides/getting_started.md) and
[Context Atlas Tour](../../../Guides/context_atlas_tour.md) point at that same
canonical starter sample instead of inventing a second packet/trace demo
surface.

- choose the product-facing place where a first packet/trace-shaped output
  sample should live
- make the sample concrete enough that readers can understand what Atlas
  produces before they run the code
- derive the sample from the canonical packet/trace story rather than inventing
  a second demo-only representation
- keep the sample surface bounded so it teaches the shared product outcome
  rather than narrating internal engine detail

### Task 3: Guide Path Cleanup And Wording Normalization

Task 3 is now settled around one explicit guide order: product-facing docs tell
readers to learn the first-run setup in
[Getting Started](../../../Guides/getting_started.md), use
[Context Atlas Tour](../../../Guides/context_atlas_tour.md) as the second
system-layer step, and drop into workflow-specific guides only after that
shared starter baseline is clear. The product path no longer uses Story-number
or hardening-era residue to explain that route.

- remove internal planning residue such as Story-number vocabulary from
  product-facing guides
- tighten the golden-path setup flow so shared setup steps are not buried under
  workflow-specific branches before they matter
- align the guide path around one truthful starter story instead of several
  competing partial narratives

### Task 4: Product-Facing Surface Alignment

- align the root README, guides, examples, and release-facing docs around the
  same basic evaluator story
- keep the README as the map and move deeper walkthrough detail to guides or
  example surfaces where appropriate
- ensure the product path stays coherent even if the repo continues to evolve
  its internal architecture and contributor tooling

## Planned Task Decomposition

- [Task 1.1 - Product Entry Surface And Runtime-Floor Visibility](./Tasks/task_1_1_product_entry_surface_and_runtime_floor_visibility.md)
- [Task 1.2 - Concrete Output Sample Surface](./Tasks/task_1_2_concrete_output_sample_surface.md)
- [Task 1.3 - Guide Path Cleanup And Wording Normalization](./Tasks/task_1_3_guide_path_cleanup_and_wording_normalization.md)
- [Task 1.4 - Product-Facing Surface Alignment](./Tasks/task_1_4_product_facing_surface_alignment.md)

## Sequencing

- establish the product entry shape and runtime-floor visibility first
- choose and shape the output sample surface next
- normalize the guide wording and remove execution residue after the desired
  route is clear
- align examples and release-facing surfaces last so they inherit the settled
  evaluator story rather than competing with it

## Risks And Unknowns

- A sample can drift into a second demo vocabulary if it is not anchored to the
  canonical packet/trace representation.
- Product docs can accidentally absorb too much tour content if the README/map
  boundary is not preserved.
- A prerequisite callout can become noisy if it is repeated mechanically across
  every surface instead of placed intentionally near first use.

## Exit Criteria

- a first-time evaluator can identify the Python/runtime prerequisites quickly
- the product route shows at least one concrete packet/trace-shaped output
  example
- product-facing guides no longer contain internal planning residue
- the README still behaves as the repo map rather than drifting back into a
  full walkthrough layer

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- the root README, guides, examples, and release-facing docs tell a consistent
  evaluator story
- The repository preflight command passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge

## Related Artifacts

- [013 Cleanup Product Definition](../013_cleanup_product_definition.md)
- [README](../../../../README.md)
- [Getting Started Guide](../../../Guides/getting_started.md)
- [Context Atlas Tour](../../../Guides/context_atlas_tour.md)
- [Guides README](../../../Guides/README.md)
- [Task docs](./Tasks/)
