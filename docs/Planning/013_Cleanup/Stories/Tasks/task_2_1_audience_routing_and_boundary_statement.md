---
id: context-atlas-013-cleanup-task-2-1-audience-routing-and-boundary-statement
title: Task 2.1 - Audience Routing And Boundary Statement PR Plan
summary: Defines the PR sequence for stating the product, contributor, generated-runtime, and governance boundaries plainly at the repo edge.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: implemented
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, task, pr-plan, routing, boundaries, readme]
related:
  - ../story_2_product_path_separation_from_agentic_and_governance_surfaces.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../README.md
  - ../../../../../docs/README.md
supersedes: []
---

# Task 2.1 - Audience Routing And Boundary Statement PR Plan

## Objective

State the repo-edge audience split plainly enough that readers can tell whether
they are here to use Atlas, contribute to it, inspect its derived runtime
surface, or understand its governance model.

## Task Status

IMPLEMENTED

## Inputs

- [Story 2 - Product Path Separation From Agentic And Governance Surfaces](../story_2_product_path_separation_from_agentic_and_governance_surfaces.md)
- [README](../../../../../README.md)
- [Docs README](../../../../../docs/README.md)
- current routing language across root and docs index surfaces

## Proposed Work

### PR - A: Root Audience Statement

- define the shortest truthful statement of the repo's main audience paths
- make the product path clearly primary for evaluators without hiding the other
  paths
- keep the language honest about complexity without turning it into a warning

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `README.md`

#### Update AI files

- `.`

### PR - B: Docs-Index Routing Alignment

- align `docs/README.md` and related index language with the same audience
  split
- keep the docs index discoverable for contributors, architecture readers, and
  governance readers

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/README.md`
- `docs/Guides/README.md`

#### Update AI files

- `.`

### PR - C: Story Reinforcement

- reinforce Story 2 with the final routing statement and any intentionally
  deferred boundary concerns

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_2_product_path_separation_from_agentic_and_governance_surfaces.md`

#### Update AI files

- `.`

## Sequencing

- settle the root audience statement first
- align docs indexes second
- reinforce Story language last

## Risks And Unknowns

- Routing language can become too abstract if it does not name concrete
  surfaces readers will actually open.
- Over-optimizing for product evaluators can make contributor surfaces harder to
  discover if the boundary is not balanced carefully.

## Completed Outcome

Task 2.1 now settles the repo-edge audience statement around four distinct
reader jobs:

- evaluating or using Context Atlas as a product/library
- inspecting the derived agentic runtime surface
- reading the Canon/Identity architecture and binding model
- understanding the repo's `__ai__.md` governance system

The root [README](../../../../../README.md) now labels those routes more
plainly, while [docs/README.md](../../../../../docs/README.md) and
[docs/Guides/README.md](../../../../../docs/Guides/README.md) inherit the same
split instead of competing as blended "start here" surfaces. The route split
is now explicit enough that later Story 2 tasks can focus on optionality and
containment rather than re-litigating who the repo edge is for.

## Exit Criteria

- the repo edge states the main audience paths clearly
- root and docs index routing language no longer compete with each other
- Story 2 reflects the chosen boundary statement explicitly

## Related Artifacts

- [Story 2 - Product Path Separation From Agentic And Governance Surfaces](../story_2_product_path_separation_from_agentic_and_governance_surfaces.md)
- [README](../../../../../README.md)
- [Docs README](../../../../../docs/README.md)

