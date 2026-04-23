---
id: context-atlas-013-cleanup-task-4-2-regeneration-surface-refresh-and-guardrail
title: Task 4.2 - Regeneration, Surface Refresh, And Guardrail PR Plan
summary: Defines the PR sequence for regenerating the affected runtime surfaces after the upstream defect fix and adding the narrowest cheap guardrail against recurrence.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: implemented
created: 2026-04-22
last_reviewed: 2026-04-23
owners: [core]
tags: [cleanup, task, pr-plan, regeneration, tests, generated-runtime]
related:
  - ../story_4_immediate_generated_surface_defects.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../scripts/check_codex_materialization.py
  - ../../../../../tests/test_codex_materialization.py
supersedes: []
---

# Task 4.2 - Regeneration, Surface Refresh, And Guardrail PR Plan

## Objective

Regenerate the affected runtime surfaces after the upstream fix, verify that
the visible defect class is gone, and add the smallest cheap guardrail that
would catch recurrence.

Because the single affected generated file was already refreshed in Task 4.1 to
keep the manifest-driven drift path green, this Task's real work is to confirm
that clean refresh state and add the narrow recurrence guardrail.

## Task Status

IMPLEMENTED

## Inputs

- [Story 4 - Immediate Generated-Surface Defects](../story_4_immediate_generated_surface_defects.md)
- settled upstream fix from Task 4.1
- current materialization and drift-check surfaces

## Proposed Work

### PR - A: Runtime Surface Regeneration And Refresh

- confirm the affected runtime surfaces are still clean after the upstream fix
  and the already-applied bounded refresh from Task 4.1
- confirm that related links, generated notices, and content sections are fully
  materialized for a reader
- keep the refresh downstream and mechanical

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- affected files under `.codex/`
- affected files under `.agents/skills/`

#### Update AI files

- `.`

### PR - B: Narrow Guardrail

- add the smallest reasonable checker or test assertion that would catch the
  same visible defect class in future runs
- avoid expanding this work into broad semantic validation of generated files

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `tests/test_codex_materialization.py`
- `scripts/check_codex_materialization.py`

#### Update AI files

- `tests/`
- `scripts/`

### PR - C: Story And Epic Reinforcement

- align Story 4 and the Cleanup Epic with the refreshed generated surface and
  the final guardrail decision
- record any remaining runtime-model questions as intentionally deferred

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_4_immediate_generated_surface_defects.md`
- `docs/Planning/013_Cleanup/013_cleanup_product_definition.md`

#### Update AI files

- `.`

## Sequencing

- regenerate and refresh the runtime surface first
- add the narrow guardrail second
- reinforce Story and Epic language third

## Risks And Unknowns

- Regeneration can mask the real fix if the upstream change is not already
  settled.
- The guardrail can over-broaden if contributors try to validate overall
  generated-file quality instead of this bounded defect class.

## Exit Criteria

- the affected runtime surfaces are refreshed and visibly clean
- a narrow recurrence guardrail exists if it can be added cheaply
- Story 4 and the Epic describe the final fix boundary honestly

## Completed Outcome

- The affected generated mode surface remained clean after the Task 4.1 parser
  fix and bounded downstream refresh.
- A focused regression now proves `Operational Delivery` mode-transition
  extraction stops at the next same-or-higher heading rather than swallowing
  later constraints or non-goals.
- Story 4 can therefore close as a bounded section-boundary bleed cleanup
  rather than a broader generated-runtime audit.

## Related Artifacts

- [Story 4 - Immediate Generated-Surface Defects](../story_4_immediate_generated_surface_defects.md)
- [Codex Drift Checker](../../../../../scripts/check_codex_materialization.py)
- [Codex Materialization Tests](../../../../../tests/test_codex_materialization.py)

