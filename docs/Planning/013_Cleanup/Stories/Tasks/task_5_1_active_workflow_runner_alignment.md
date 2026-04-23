---
id: context-atlas-013-cleanup-task-5-1-active-workflow-runner-alignment
title: Task 5.1 - Active Workflow Runner Alignment PR Plan
summary: Defines the PR sequence for moving the active CI and owner-file verification workflows to a Linux-first runner and shell shape.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: implemented
created: 2026-04-22
last_reviewed: 2026-04-23
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
runner and shell shape where the current scripts already support it, while
leaving local executable owner-file command normalization to the later Story 5
tasks.

## Task Status

IMPLEMENTED

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
- `docs/Planning/013_Cleanup/Stories/Tasks/task_5_1_active_workflow_runner_alignment.md`

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

## Completed Outcome

Task 5.1 is complete.

The active GitHub workflow surface now uses `ubuntu-latest` plus bash-compatible
command forms across:

- `.github/workflows/ci.yml`
- `.github/workflows/ai-verify-folder-contracts.yml`
- `.github/workflows/ai-last-verified.yml`

The `.github/workflows/__ai__.md` owner file now records the intended
separation between:

- the Linux-first GitHub workflow baseline already in place
- the still-pending local executable owner-file command normalization that
  belongs to Task 5.2 and Task 5.3

The repository preflight path remained green after the workflow conversion on
the Task branch.

## Related Artifacts

- [Story 5 - Linux-First CI And Contract Command Alignment](../story_5_linux_first_ci_and_contract_command_alignment.md)
- [CI Workflow](../../../../../.github/workflows/ci.yml)

