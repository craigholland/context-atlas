---
id: context-atlas-013-cleanup-task-2-3-docs-index-and-cross-link-alignment
title: Task 2.3 - Docs Index And Cross-Link Alignment PR Plan
summary: Defines the PR sequence for aligning the README, docs index, and guide index so product, contributor, governance, and generated-runtime routes no longer compete as one blended path.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, task, pr-plan, docs, cross-links, routing]
related:
  - ../story_2_product_path_separation_from_agentic_and_governance_surfaces.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../README.md
  - ../../../../../docs/README.md
  - ../../../../../docs/Guides/README.md
supersedes: []
---

# Task 2.3 - Docs Index And Cross-Link Alignment PR Plan

## Objective

Align the main routing surfaces so the root README, docs index, and guide index
all express the same audience split and link hierarchy instead of competing as
parallel "start here" claims.

## Task Status

PLANNED

## Inputs

- [Story 2 - Product Path Separation From Agentic And Governance Surfaces](../story_2_product_path_separation_from_agentic_and_governance_surfaces.md)
- [README](../../../../../README.md)
- [Docs README](../../../../../docs/README.md)
- [Guides README](../../../../../docs/Guides/README.md)

## Proposed Work

### PR - A: Index-Surface Routing Pass

- align the root, docs, and guide indexes around the same audience split
- remove cases where one index re-opens ambiguity that another already solved
- keep the differences between map, docs index, and guide index intentional

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `README.md`
- `docs/README.md`
- `docs/Guides/README.md`

#### Update AI files

- `.`

### PR - B: Cross-Link Cleanup

- clean up competing or mislabeled cross-links across the touched routing
  surfaces
- ensure deeper contributor-facing or architecture-facing paths are reachable
  by explicit labeled links rather than by accidental bleed-through

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/README.md`
- `docs/Guides/README.md`
- `docs/Authoritative/Canon/AgenticDevelopment/README.md`

#### Update AI files

- `.`

### PR - C: Story Reinforcement

- align Story 2 with the final routing and cross-link model
- note any remaining index cleanup that belongs to later consumer-packaging or
  agentic-runtime work

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_2_product_path_separation_from_agentic_and_governance_surfaces.md`

#### Update AI files

- `.`

## Sequencing

- align the main indexes first
- clean up cross-links second
- reinforce Story language third

## Risks And Unknowns

- Cross-link cleanup can turn into subjective reshuffling if the main audience
  split is not already settled.
- It is easy to over-minimize cross-links and make non-product routes feel
  buried.

## Exit Criteria

- root and docs indexes no longer compete as one blended route
- cross-links are labeled more intentionally by audience and purpose
- Story 2 reflects the final routing model clearly

## Related Artifacts

- [Story 2 - Product Path Separation From Agentic And Governance Surfaces](../story_2_product_path_separation_from_agentic_and_governance_surfaces.md)
- [Docs README](../../../../../docs/README.md)
- [Guides README](../../../../../docs/Guides/README.md)

