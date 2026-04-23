---
id: context-atlas-013-cleanup-task-3-2-portable-example-replacement-and-rewording
title: Task 3.2 - Portable Example Replacement And Rewording PR Plan
summary: Defines the PR sequence for replacing the clearest local platform and project examples in Canon with project-neutral or platform-neutral wording.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, task, pr-plan, canon, examples, wording]
related:
  - ../story_3_portable_canon_leak_cleanup.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../docs/Authoritative/Canon/AgenticDevelopment/README.md
  - ../../../../../docs/Authoritative/Canon/Architecture/Craig-Architecture-Python.md
  - ../../../../../docs/Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md
supersedes: []
---

# Task 3.2 - Portable Example Replacement And Rewording PR Plan

## Objective

Replace the clearest `.codex/`, `@codex review`, Context Atlas runtime-ID, and
similar local examples where portable Canon should instead use general or
project-neutral wording.

## Task Status

PLANNED

## Inputs

- [Story 3 - Portable Canon Leak Cleanup](../story_3_portable_canon_leak_cleanup.md)
- leak inventory and classification from Task 3.1
- current touched Canon surfaces in AgenticDevelopment and Architecture

## Proposed Work

### PR - A: AgenticDevelopment Canon Rewording

- clean up the clearest local examples in the AgenticDevelopment canon entry
  surfaces
- prefer readable neutral placeholders over abstract jargon
- keep the cleanup tied to the classification rules from Task 3.1

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Authoritative/Canon/AgenticDevelopment/README.md`
- neighboring touched docs under `docs/Authoritative/Canon/AgenticDevelopment/`

#### Update AI files

- `docs/Authoritative/Canon/AgenticDevelopment/`

### PR - B: Architecture Canon Rewording

- remove or generalize the clearest local examples in Architecture canon docs
- preserve the underlying architecture rule while stripping the accidental
  platform/project assumption

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Authoritative/Canon/Architecture/Craig-Architecture-Python.md`
- `docs/Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md`

#### Update AI files

- `docs/Authoritative/Canon/Architecture/`

### PR - C: Story Reinforcement

- align Story 3 with the replacement decisions now reflected in Canon
- record any remaining intentional examples left for later deeper runtime work

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_3_portable_canon_leak_cleanup.md`

#### Update AI files

- `.`

## Sequencing

- clean the AgenticDevelopment canon surfaces first
- clean the Architecture canon surfaces second
- reinforce Story language third

## Risks And Unknowns

- Replacement wording can become too vague if it removes all specificity.
- Architecture cleanup can drift into deeper runtime-policy work if the edits
  start moving conceptual ownership instead of just fixing examples.

## Exit Criteria

- the clearest local examples in the targeted Canon surfaces are generalized
- the replacement wording stays readable and useful
- Story 3 reflects the actual replacement boundary clearly

## Related Artifacts

- [Story 3 - Portable Canon Leak Cleanup](../story_3_portable_canon_leak_cleanup.md)
- [AgenticDevelopment Canon README](../../../../../docs/Authoritative/Canon/AgenticDevelopment/README.md)

