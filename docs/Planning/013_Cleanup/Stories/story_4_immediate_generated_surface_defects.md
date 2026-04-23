---
id: context-atlas-013-cleanup-story-4-immediate-generated-surface-defects
title: Story 4 - Immediate Generated-Surface Defects
summary: Defines a bounded cleanup pass for visible defects in the currently materialized Codex runtime surface without broadening into a larger runtime-model redesign.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, story, generated-runtime, codex, defects, materialization]
related:
  - ../013_cleanup_product_definition.md
  - ../../../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml
  - ../../../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md
  - ../../../../scripts/materialize_codex_runtime.py
  - ../../../../scripts/check_codex_materialization.py
  - ../../../../tests/test_codex_materialization.py
  - ../../../../.codex
  - ../../../../.agents/skills
supersedes: []
---

# Story 4 - Immediate Generated-Surface Defects

## Objective

Fix the known visible defect class in the currently materialized runtime
surface so a reviewer reading `.codex/` or `.agents/skills/` sees fully
materialized downstream artifacts instead of template residue or stale local
references.

This Story is intentionally small and defect-oriented. It should stop after the
visible cleanup and the narrowest cheap regression/guardrail that protects the
same defect class if such a guardrail is straightforward.

## Inputs

- [013 Cleanup Product Definition](../013_cleanup_product_definition.md)
- [Materialization Manifest](../../../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml)
- [Codex Materialization README](../../../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md)
- [Codex Runtime Materializer](../../../../scripts/materialize_codex_runtime.py)
- [Codex Drift Checker](../../../../scripts/check_codex_materialization.py)
- [Codex Materialization Tests](../../../../tests/test_codex_materialization.py)
- current generated runtime surface under `.codex/` and `.agents/skills/`

## Current Inventory Snapshot

As of the current Story start, the bounded visible residue class is confirmed in
the generated mode surface for:

- `.codex/modes/operational-delivery.md`

The current reproduction is:

- the final `#### Exit` block in
  `docs/Authoritative/Identity/AgenticDevelopment/Bindings/Modes/Mode-Transition-Rules.md`
  is parsed too broadly by the materializer
- that parser bleed causes later `## Constraints`, `## Non-Goals`, and
  `## Related Artifacts` bullets to appear as if they were part of the
  generated `Exit Conditions` section
- the issue is therefore an upstream extraction/generation defect rather than a
  downstream hand-edit or stale generated file

## Proposed Tasks

### Task 1: Defect Inventory And Reproduction

- identify every current visible residue defect that belongs to the same
  cleanup class as the reported template leftovers
- confirm whether the issue comes from the generator, template source, manifest
  binding, or a stale generated output
- keep the scope bounded to the defect class rather than expanding it into a
  general quality audit of every generated artifact

### Task 2: Upstream Correction

- fix the defect in the smallest authoritative upstream surface that actually
  causes it
- prefer template or generator fixes over hand-editing generated runtime
  artifacts
- keep any change faithful to the existing manifest-driven generation model

### Task 3: Regeneration And Surface Refresh

- regenerate the affected runtime surfaces after the upstream fix
- verify that generated notices, related links, and content sections are fully
  materialized for a reader
- ensure the refresh does not introduce new drift against the manifest-driven
  checker path

### Task 4: Narrow Defect Guardrail

- add the smallest reasonable test or checker assertion that would catch the
  same visible defect class in future runs if that addition stays local and
  cheap
- avoid broadening this Story into a whole new semantic validator for generated
  content

## Planned Task Decomposition

- [Task 4.1 - Defect Inventory And Upstream Correction](./Tasks/task_4_1_defect_inventory_and_upstream_correction.md)
- [Task 4.2 - Regeneration, Surface Refresh, And Guardrail](./Tasks/task_4_2_regeneration_surface_refresh_and_guardrail.md)

## Sequencing

- inventory and reproduce the defect first
- apply the upstream fix next
- regenerate the runtime surface after the fix is in place
- add the narrow guardrail last once the actual failure mode is understood

## Risks And Unknowns

- The Story can sprawl if "visible defect" turns into a broad runtime-model
  critique.
- A generated-surface fix can accidentally be applied downstream if the
  authoritative source of the defect is not identified first.
- Even a small guardrail can expand beyond the Epic's intent if it starts
  validating semantic quality rather than this known residue class.
- The current inventory may reveal additional files of the same defect class
  once regeneration is rerun, but Story 4 should still stay limited to the same
  section-boundary bleed behavior rather than widening into a general runtime
  content audit.

## Exit Criteria

- the known visible generated-surface residue defects are gone
- the fix is made upstream of the generated runtime artifacts
- the refreshed generated surface passes the existing materialization and drift
  checks
- if a new guardrail is added, it stays narrow and directly related to this
  defect class

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- the generated runtime surface remains downstream of the manifest, templates,
  and generator rather than becoming a hand-maintained patch target
- The repository preflight command passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge

## Related Artifacts

- [013 Cleanup Product Definition](../013_cleanup_product_definition.md)
- [Codex Runtime Materializer](../../../../scripts/materialize_codex_runtime.py)
- [Codex Drift Checker](../../../../scripts/check_codex_materialization.py)
- [Codex Materialization Tests](../../../../tests/test_codex_materialization.py)
- [Task docs](./Tasks/)
