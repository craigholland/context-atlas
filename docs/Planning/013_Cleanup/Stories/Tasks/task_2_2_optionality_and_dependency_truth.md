---
id: context-atlas-013-cleanup-task-2-2-optionality-and-dependency-truth
title: Task 2.2 - Optionality And Dependency Truth PR Plan
summary: Defines the PR sequence for making it explicit which agentic and governance surfaces are downstream or contributor-facing rather than product prerequisites.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, task, pr-plan, optionality, dependencies, governance]
related:
  - ../story_2_product_path_separation_from_agentic_and_governance_surfaces.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../README.md
  - ../../../../../__ai__.md
  - ../../../../../.codex/AGENTS.md
supersedes: []
---

# Task 2.2 - Optionality And Dependency Truth PR Plan

## Objective

Make it explicit that `.codex/`, `.agents/skills/`, and `__ai__.md` are not
prerequisites for simply evaluating or using Atlas as a library, while still
describing honestly when those surfaces matter.

## Task Status

PLANNED

## Inputs

- [Story 2 - Product Path Separation From Agentic And Governance Surfaces](../story_2_product_path_separation_from_agentic_and_governance_surfaces.md)
- [README](../../../../../README.md)
- [Root Owner File](../../../../../__ai__.md)
- current generated runtime surface under `.codex/` and `.agents/skills/`

## Proposed Work

### PR - A: Product-Path Optionality Language

- clarify the product path so it does not imply that repo governance or derived
  runtime assets are required for product use
- keep the language truthful about what those surfaces are for
- avoid framing optionality as irrelevance when the surfaces do matter for
  contributors

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `README.md`
- `docs/Guides/README.md`

#### Update AI files

- `.`

### PR - B: Runtime/Governance Surface Framing

- align nearby descriptions of `.codex/`, `.agents/skills/`, and `__ai__.md`
  so they read as downstream or contributor-facing surfaces
- preserve truthful cross-links for readers who intentionally want those layers

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/README.md`
- `docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md`
- `__ai__.md`

#### Update AI files

- `.`

### PR - C: Story Reinforcement

- align Story 2 with the settled optionality language
- make any remaining tension with future packaging work explicit as deferred

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_2_product_path_separation_from_agentic_and_governance_surfaces.md`

#### Update AI files

- `.`

## Sequencing

- settle product-path optionality first
- align runtime/governance framing second
- reinforce Story language last

## Risks And Unknowns

- Optionality wording can become misleading if it hides the real importance of
  governance or runtime surfaces for contributors.
- It is easy to over-correct and make product use sound entirely separate from
  the repo when the product still lives here.

## Exit Criteria

- product-facing docs no longer imply that agentic or governance surfaces are
  prerequisites for product use
- contributor/runtime/governance surfaces still remain discoverable and
  truthfully described
- Story 2 reflects that dependency boundary clearly

## Related Artifacts

- [Story 2 - Product Path Separation From Agentic And Governance Surfaces](../story_2_product_path_separation_from_agentic_and_governance_surfaces.md)
- [README](../../../../../README.md)
- [Root Owner File](../../../../../__ai__.md)

