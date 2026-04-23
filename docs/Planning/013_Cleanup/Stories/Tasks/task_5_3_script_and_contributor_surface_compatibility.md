---
id: context-atlas-013-cleanup-task-5-3-script-and-contributor-surface-compatibility
title: Task 5.3 - Script And Contributor-Surface Compatibility PR Plan
summary: Defines the PR sequence for making any needed script or contributor-doc adjustments after the workflow and contract-command baseline shifts to Linux-first.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: implemented
created: 2026-04-22
last_reviewed: 2026-04-23
owners: [core]
tags: [cleanup, task, pr-plan, scripts, contributors, validation]
related:
  - ../story_5_linux_first_ci_and_contract_command_alignment.md
  - ../../013_cleanup_product_definition.md
  - ../../../../../scripts/preflight.py
  - ../../../../../scripts/ai_verify_contracts.py
  - ../../../../../README.md
supersedes: []
---

# Task 5.3 - Script And Contributor-Surface Compatibility PR Plan

## Objective

Make any needed support-script or contributor-facing documentation adjustments
after the Linux-first workflow and contract-command shift, then verify the
integrated truth path end to end.

## Task Status

IMPLEMENTED

## Inputs

- [Story 5 - Linux-First CI And Contract Command Alignment](../story_5_linux_first_ci_and_contract_command_alignment.md)
- settled workflow and command changes from Tasks 5.1 and 5.2
- current contributor-facing docs that still describe the truth path

## Proposed Work

### PR - A: Support-Script Compatibility Adjustments

- make any needed bounded support changes in preflight or contract-runner code
  so the new Linux-first baseline remains truthful
- avoid broadening this work into a general script portability Epic

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `scripts/preflight.py`
- `scripts/ai_verify_contracts.py`

#### Update AI files

- `scripts/`

### PR - B: Contributor-Facing Surface Alignment

- update contributor-facing docs where they still imply a Windows-first truth
  path
- preserve useful Windows analog guidance without presenting it as the primary
  baseline

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `README.md`
- contributor-facing docs under `docs/`

#### Update AI files

- `.`

### PR - C: Story And Epic Closeout Reinforcement

- validate the integrated truth path after the support and docs changes
- align Story 5 and the Cleanup Epic with the final bounded Linux-first
  baseline

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `docs/Planning/013_Cleanup/Stories/story_5_linux_first_ci_and_contract_command_alignment.md`
- `docs/Planning/013_Cleanup/013_cleanup_product_definition.md`

#### Update AI files

- `.`

## Sequencing

- apply any needed support-script adjustments first
- align contributor-facing docs second
- validate and reinforce Story/Epic language third

## Risks And Unknowns

- The task can become a catch-all portability bucket if its scope is not kept
  tied to the new Linux-first truth path.
- Contributor-facing wording can drift into governance philosophy if it is not
  kept focused on operator expectations.

## Exit Criteria

- any needed support-script changes are in place for the Linux-first baseline
- contributor-facing docs no longer imply Windows as the primary truth path
- Story 5 and the Epic describe the final bounded CI/command alignment
  honestly

## Completed Outcome

Task 5.3 is complete. The remaining contributor-facing surfaces now present
portable `python ...` commands as the primary repo-wide truth path for
repo-owned scripts, while still allowing Windows launcher variants to remain
secondary local analogs where they help operators.

No further support-script change was needed in this Task because the necessary
contract-runner compatibility adjustment already landed during Task 5.2 in
`scripts/ai_verify_contracts.py`. Task 5.3 therefore focused on contributor
docs plus final Story/Epic closeout reinforcement, then revalidated the full
truth path through repository preflight.

## Related Artifacts

- [Story 5 - Linux-First CI And Contract Command Alignment](../story_5_linux_first_ci_and_contract_command_alignment.md)
- [Preflight Script](../../../../../scripts/preflight.py)
- [AI Verify Contracts Script](../../../../../scripts/ai_verify_contracts.py)

