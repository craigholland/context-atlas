---
id: context-atlas-013-cleanup-task-5-1-active-workflow-runner-alignment
title: Task 5.1 - Active Workflow Runner Alignment PR Plan
summary: Defines the PR sequence for moving the active CI and owner-file verification workflows to a Linux-first runner and shell shape.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, task, pr-plan, ci, linux, workflows]
related:
  - ../story_5_linux_first_ci_and_contract_command_alignment.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../.github/workflows/ci.yml
  - ../../../../../.github/workflows/ai-verify-folder-contracts.yml
  - ../../../../../.github/workflows/ai-last-verified.yml
supersedes: []
---

# Task 5.1 - Active Workflow Runner Alignment PR Plan

## Objective

Move the active CI and owner-file verification workflows to a Linux-first
runner and shell shape where the current scripts already support it.

## Task Status

PLANNED

## Inputs

- [Story 5 - Linux-First CI And Contract Command Alignment](../story_5_linux_first_ci_and_contract_command_alignment.md)
- active workflow files under `.github/workflows/`
- current preflight and verification scripts

## Proposed Work

### PR - A: Primary CI Workflow Alignment

- convert the main CI workflow to a Linux-first runner and shell shape
- keep the workflow logic faithful to the current truth path
- prefer shell/command forms already supported by the scripts

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `.github/workflows/ci.yml`

#### Update AI files

- `.github/workflows/`

### PR - B: Governance Workflow Alignment

- convert the active owner-file verification and last-verified workflows to the
  same Linux-first baseline where appropriate
- keep the scope bounded to the active workflow set rather than every archived
  example

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `.github/workflows/ai-verify-folder-contracts.yml`
- `.github/workflows/ai-last-verified.yml`

#### Update AI files

- `.github/workflows/`

### PR - C: Story Reinforcement

- align Story 5 with the final runner and shell baseline
- document any remaining local Windows analogs as intentionally non-primary

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_5_linux_first_ci_and_contract_command_alignment.md`

#### Update AI files

- `.`

## Sequencing

- align the main CI workflow first
- align the governance workflows second
- reinforce Story language third

## Risks And Unknowns

- Workflow conversion can expose hidden shell assumptions in the current truth
  path.
- The task can sprawl if archived or illustrative workflow examples are pulled
  into scope.

## Exit Criteria

- the active workflows run with a Linux-first baseline
- the current truth path remains intact after the conversion
- Story 5 reflects the settled workflow baseline clearly

## Related Artifacts

- [Story 5 - Linux-First CI And Contract Command Alignment](../story_5_linux_first_ci_and_contract_command_alignment.md)
- [CI Workflow](../../../../../.github/workflows/ci.yml)

