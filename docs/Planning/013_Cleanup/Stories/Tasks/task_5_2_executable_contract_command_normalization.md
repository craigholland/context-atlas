---
id: context-atlas-013-cleanup-task-5-2-executable-contract-command-normalization
title: Task 5.2 - Executable Contract Command Normalization PR Plan
summary: Defines the PR sequence for normalizing executable owner-file verification commands toward Linux/macOS-friendly forms where portability is intended.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, task, pr-plan, commands, contracts, portability]
related:
  - ../story_5_linux_first_ci_and_contract_command_alignment.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../__ai__.md
  - ../../../../../scripts/ai_verify_contracts.py
supersedes: []
---

# Task 5.2 - Executable Contract Command Normalization PR Plan

## Objective

Normalize executable owner-file verification commands toward Linux/macOS-
friendly forms where the commands are intended to be portable, without
rewriting the broader governance model.

## Task Status

PLANNED

## Inputs

- [Story 5 - Linux-First CI And Contract Command Alignment](../story_5_linux_first_ci_and_contract_command_alignment.md)
- executable verification-contract blocks in current owner files
- current contract-runner behavior in `scripts/ai_verify_contracts.py`

## Proposed Work

### PR - A: Contract Command Inventory And Normalization Rules

- inventory the executable contract commands that still imply Windows-first
  operation
- define the smallest normalization rule set for portable commands
- keep platform-specific commands explicit where they truly must remain local

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `__ai__.md`
- touched owner files that carry executable contract commands

#### Update AI files

- `.`

### PR - B: Owner-File Command Normalization

- update the affected owner-file commands toward Linux/macOS-friendly forms
- preserve the distinction between executable truth checks and nearby prose
- keep Windows analog guidance only where it still adds local operator value

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- touched `__ai__.md` files across the repo

#### Update AI files

- affected owner-file directories

### PR - C: Story Reinforcement

- align Story 5 with the actual contract-command normalization boundary
- document any remaining platform-specific commands as intentional exceptions

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_5_linux_first_ci_and_contract_command_alignment.md`

#### Update AI files

- `.`

## Sequencing

- inventory and define normalization rules first
- normalize the touched owner-file commands second
- reinforce Story language third

## Risks And Unknowns

- Command translation can silently change the meaning of a truth check if it is
  treated as syntax cleanup only.
- The task can drift into prose-correctness redesign if contributors start
  revisiting owner-file narrative rather than executable commands.

## Exit Criteria

- portable executable contract commands no longer imply a Windows-only baseline
- intentional platform-specific commands remain explicitly justified
- Story 5 reflects the normalization boundary clearly

## Related Artifacts

- [Story 5 - Linux-First CI And Contract Command Alignment](../story_5_linux_first_ci_and_contract_command_alignment.md)
- [Root Owner File](../../../../../__ai__.md)

