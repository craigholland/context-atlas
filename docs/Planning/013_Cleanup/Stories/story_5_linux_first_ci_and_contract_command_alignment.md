---
id: context-atlas-013-cleanup-story-5-linux-first-ci-and-contract-command-alignment
title: Story 5 - Linux-First CI And Contract Command Alignment
summary: Defines a bounded contributor-trust cleanup pass that aligns active CI runners, shell usage, and executable owner-file contract commands with a Linux-first baseline.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [cleanup, story, ci, linux, contracts, contributor-trust]
related:
  - ../013_cleanup_product_definition.md
  - ../../../../.github/workflows/ci.yml
  - ../../../../.github/workflows/ai-verify-folder-contracts.yml
  - ../../../../.github/workflows/ai-last-verified.yml
  - ../../../../scripts/preflight.py
  - ../../../../scripts/ai_verify_contracts.py
  - ../../../../__ai__.md
supersedes: []
---

# Story 5 - Linux-First CI And Contract Command Alignment

## Objective

Align the active CI and executable owner-file contract-command surface with a
Linux-first contributor expectation so the repo no longer implies that Windows
is the primary environment for truth-checking or contribution.

This Story is a bounded surface-alignment story. It should not turn into a
deeper redesign of the `__ai__.md` governance model or a broader portability
initiative across every local workflow in the repo.

## Inputs

- [013 Cleanup Product Definition](../013_cleanup_product_definition.md)
- [CI Workflow](../../../../.github/workflows/ci.yml)
- [AI Contract Verification Workflow](../../../../.github/workflows/ai-verify-folder-contracts.yml)
- [Last Verified Update Workflow](../../../../.github/workflows/ai-last-verified.yml)
- [Preflight Script](../../../../scripts/preflight.py)
- [AI Verify Contracts Script](../../../../scripts/ai_verify_contracts.py)
- executable verification-contract blocks in current owner files
- contributor-facing docs that currently imply Windows-first command usage

## Proposed Tasks

### Task 1: Active Workflow Runner Alignment

- convert the active GitHub workflows to a Linux-first runner shape where the
  current scripts already support it
- replace PowerShell-specific workflow snippets with bash or portable shell
  equivalents where doing so is straightforward
- keep the Story focused on the active CI surface rather than on every
  historical example in the repo

### Task 2: Executable Contract Command Normalization

- normalize executable owner-file contract commands toward Linux/macOS-friendly
  forms where the command is intended to be portable
- avoid overstating portability where a command is still genuinely
  platform-specific
- preserve the distinction between executable truth checks and nearby human
  guidance in owner-file prose

### Task 3: Script And Contributor-Surface Compatibility

- make any necessary local adjustments in contract-runner or preflight support
  code so the normalized command surface remains truthful
- update contributor-facing docs where they currently imply Windows-first
  operation for the active truth path
- keep Windows analog guidance where it remains useful, but stop presenting it
  as the only first-class shape

### Task 4: CI Trust Validation

- validate that the Linux-first active workflow and normalized contract-command
  surface still passes the repository truth path
- make any final bounded documentation updates so contributors understand the
  new baseline
- leave later governance-evolution work to the dedicated AI governance Epic

## Planned Task Decomposition

- [Task 5.1 - Active Workflow Runner Alignment](./Tasks/task_5_1_active_workflow_runner_alignment.md)
- [Task 5.2 - Executable Contract Command Normalization](./Tasks/task_5_2_executable_contract_command_normalization.md)
- [Task 5.3 - Script And Contributor-Surface Compatibility](./Tasks/task_5_3_script_and_contributor_surface_compatibility.md)

## Sequencing

- align the active CI runners and shell shape first
- normalize the executable contract commands next
- adjust support scripts and contributor-facing docs after the new command
  baseline is clear
- validate the integrated truth path last

## Risks And Unknowns

- The Story can grow too large if it tries to make every local command surface
  in the repo perfectly cross-platform.
- Contract-command cleanup can accidentally change the meaning of a truth check
  if shell translation is done carelessly.
- This Story can drift into governance redesign if contributors use it to solve
  prose-correctness or `ai-dirt` questions that belong in a later Epic.

## Exit Criteria

- active GitHub workflows use a Linux-first runner shape
- executable owner-file verification commands no longer imply Windows as the
  only first-class contributor environment where portability is intended
- the repo's main truth path still passes through preflight and CI after the
  change

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- workflow and contract-command changes remain bounded to contributor-trust
  cleanup and do not silently redesign the wider governance model
- The repository preflight command passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge

## Related Artifacts

- [013 Cleanup Product Definition](../013_cleanup_product_definition.md)
- [CI Workflow](../../../../.github/workflows/ci.yml)
- [AI Contract Verification Workflow](../../../../.github/workflows/ai-verify-folder-contracts.yml)
- [Last Verified Update Workflow](../../../../.github/workflows/ai-last-verified.yml)
- [Preflight Script](../../../../scripts/preflight.py)
- [Task docs](./Tasks/)
