---
id: context-atlas-013-cleanup-task-4-1-defect-inventory-and-upstream-correction
title: Task 4.1 - Defect Inventory And Upstream Correction PR Plan
summary: Defines the PR sequence for inventorying the known generated-surface residue defects and fixing them in the correct authoritative upstream layer.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, task, pr-plan, generated-runtime, defects, generator]
related:
  - ../story_4_immediate_generated_surface_defects.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../scripts/materialize_codex_runtime.py
  - ../../../../../docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md
supersedes: []
---

# Task 4.1 - Defect Inventory And Upstream Correction PR Plan

## Objective

Inventory the currently visible generated-surface residue defects and correct
them in the right upstream source, whether that source is the generator,
template, or related authoritative binding.

## Task Status

PLANNED

## Inputs

- [Story 4 - Immediate Generated-Surface Defects](../story_4_immediate_generated_surface_defects.md)
- [Codex Runtime Materializer](../../../../../scripts/materialize_codex_runtime.py)
- current generated runtime files under `.codex/` and `.agents/skills/`

## Proposed Work

### PR - A: Defect Inventory And Reproduction

- enumerate the currently visible residue defects that belong to this Story's
  bounded defect class
- confirm how each defect reproduces and where the authoritative source of the
  issue most likely lives
- keep the inventory tightly limited to the current residue/stale-link class

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_4_immediate_generated_surface_defects.md`

#### Update AI files

- `.`

### PR - B: Upstream Correction

- fix the defect in the smallest authoritative upstream surface that actually
  causes it
- prefer generator or template fixes over patching generated output by hand
- keep the fix faithful to the current manifest-driven model

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `scripts/materialize_codex_runtime.py`
- touched template or binding docs under
  `docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/`

#### Update AI files

- `scripts/`

### PR - C: Story Reinforcement

- align Story 4 with the actual defect class and chosen upstream fix
- note any adjacent issues intentionally deferred to later runtime-model work

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_4_immediate_generated_surface_defects.md`

#### Update AI files

- `.`

## Sequencing

- inventory and reproduce first
- apply the upstream fix second
- reinforce Story language third

## Risks And Unknowns

- The task can sprawl if contributors turn the inventory into a general audit of
  generated-runtime quality.
- The wrong fix layer can be chosen if the residue source is not reproduced
  clearly first.

## Exit Criteria

- the current residue defect class is inventoried and reproduced
- the fix lands upstream of the generated output
- Story 4 reflects the bounded defect scope clearly

## Related Artifacts

- [Story 4 - Immediate Generated-Surface Defects](../story_4_immediate_generated_surface_defects.md)
- [Codex Runtime Materializer](../../../../../scripts/materialize_codex_runtime.py)

