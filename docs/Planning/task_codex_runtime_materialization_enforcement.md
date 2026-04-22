---
id: context-atlas-task-codex-runtime-materialization-enforcement
title: Task - Codex Runtime Materialization Enforcement PR Plan
summary: Defines the small follow-up execution plan for turning the first Codex runtime materialization into a reproducible, drift-checked, enforced generation path.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [planning, task, codex, materialization, enforcement, drift]
related:
  - ./README.md
  - ../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml
  - ../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md
  - ../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/creation_guidance.md
  - ../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/governance.md
  - ../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md
  - ./completed/Agentic/Stories/story_8_codex_materialization_for_context_atlas.md
  - ../../.codex/AGENTS.md
supersedes: []
---

# Task - Codex Runtime Materialization Enforcement PR Plan

## Objective

Close the gap between the now-materialized Codex runtime surface and a truly
enforced materialization pipeline.

This Task intentionally compresses the earlier three-step follow-up idea into
two implementation PRs:

- PR `A` establishes deterministic generation plus upstream
  `maintenance_mode` policy
- PR `B` adds drift detection and then wires that check into preflight and CI

## Task Status

PLANNED

## Inputs

- the current generated runtime surface under `.codex/` and `.agents/skills/`
- [Context Atlas Materialization Manifest](../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml)
- [Context Atlas Codex Binding](../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md)
- [Context Atlas Codex Creation Guidance](../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/creation_guidance.md)
- [Context Atlas Codex Governance](../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/governance.md)

## Proposed Work

### PR - A: Deterministic Generator And Manifest Maintenance Policy

- add a repo-owned generator, expected at
  `scripts/materialize_codex_runtime.py`
- extend `materialization_manifest.yaml` so runtime surfaces can declare
  `maintenance_mode: generated | mixed | human`
- make the generator deterministically rebuild the current Codex runtime
  surface from the manifest, bindings, and templates instead of relying on
  manual regeneration
- define the intended maintenance semantics explicitly:
  - `generated`: generator fully owns and rewrites the surface
  - `mixed`: generator owns generated sections and preserves explicit manual
    blocks only
  - `human`: generator does not rewrite the surface, but the surface remains
    declared and reviewable
- support `generated` and `human` directly in the first deterministic
  generator pass, and only treat `mixed` as supported once the manual-block
  format is explicitly defined and validated
- if `mixed` is introduced in this PR, require explicit manual-block markers;
  do not allow ambiguous freeform preservation behavior

#### Expected New Files

- `scripts/materialize_codex_runtime.py`

#### Expected Existing Files Updated

- `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- `docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/creation_guidance.md`
- `docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/governance.md`
- `docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/agent.template.toml`
- generated runtime assets under `.codex/`
- generated runtime assets under `.agents/skills/`

#### Update AI files

- `.`
- `scripts`

### PR - B: Drift Check Plus Preflight And CI Enforcement

- add a repo-owned drift checker, expected at
  `scripts/check_codex_materialization.py`
- verify that the committed runtime surface matches the manifest, template
  rules, and generated output where `maintenance_mode` says the generator owns
  the file
- verify that `human` surfaces remain present, typed correctly, and traceable
  even when they are not overwritten
- if `mixed` surfaces are supported, verify that required generated sections
  still match the upstream derivation and that manual regions stay within the
  declared preservation boundary
- integrate the checker into:
  - `scripts/preflight.py`
  - local push enforcement where appropriate
  - CI validation

#### Expected New Files

- `scripts/check_codex_materialization.py`

#### Expected Existing Files Updated

- `scripts/preflight.py`
- `.githooks/pre-push`
- `.github/workflows/ci.yml`
- `docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/governance.md`
- `README.md` only if contributor workflow needs a short regeneration note

#### Update AI files

- `.`
- `.github/workflows`
- `scripts`

## Sequencing

- implement the generator and `maintenance_mode` policy first so there is a
  deterministic source for later drift checks
- add the checker second and immediately bind it into preflight and CI instead
  of leaving it as an optional helper script

## Risks And Unknowns

- `mixed` can become vague quickly if manual preservation is not fenced by an
  explicit block format
- file-level `maintenance_mode` policy must remain upstream in the manifest;
  runtime files must not become the place that decides whether they may be
  overwritten
- the first generator pass may expose gaps in template completeness or
  traceability wording that were previously hidden by manual materialization

## Exit Criteria

- Context Atlas has a deterministic generator for `.codex/` and
  `.agents/skills/`
- `materialization_manifest.yaml` is the authoritative source for runtime
  overwrite policy through `maintenance_mode`
- drift between manifest/templates and committed runtime assets is mechanically
  detectable
- preflight and CI fail when required generated surfaces drift

## Final Handoff State

- completing this Task should leave Codex runtime materialization provable
  rather than merely described
- follow-on runtime binding work, such as future Claude materialization, should
  be able to reuse the same generator/checker/enforcement pattern instead of
  inventing a parallel governance loop

## Related Artifacts

- [Planning README](./README.md)
- [Context Atlas Materialization Manifest](../Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml)
- [Context Atlas Codex Binding](../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md)
- [Context Atlas Codex Creation Guidance](../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/creation_guidance.md)
- [Context Atlas Codex Governance](../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/governance.md)
