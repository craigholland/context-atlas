---
id: context-atlas-task-ai-owner-file-compaction-and-hygiene
title: Task - __ai__ Owner-File Compaction And Hygiene PR Plan
summary: Defines the small follow-up execution plan for reducing cognitive load in repo-level and layer-level `__ai__.md` files whose `Architectural Rules` sections have drifted toward append-only historical summaries.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [planning, task, ai-docs, owner-files, governance, hygiene]
related:
  - ./README.md
  - ../../__ai__.md
  - ../../__ai__.template.md
  - ../../.github/workflows/__ai__.md
  - ../Authoritative/Canon/AgenticDevelopment/__ai__.md
  - ../Authoritative/Canon/RepoManagement/__ai__.md
  - ../../scripts/validate_ai_docs.py
  - ../../scripts/check_ai_docs.py
  - ../../scripts/ai_verify_contracts.py
supersedes: []
---

# Task - __ai__ Owner-File Compaction And Hygiene PR Plan

## Objective

Reduce unnecessary cognitive load in repo-level and layer-level `__ai__.md`
files by turning append-only rule growth into a more curated current-state
instruction surface.

This Task should preserve real governance and boundary guidance while making it
easier for contributors to tell:

- which rules are durable current-state expectations
- which details belong in `File Index`, `Known Gaps`, or `Cross-Folder Contracts`
- which completed-work memory belongs in planning archives, release notes, or
  neighboring authoritative docs instead of accumulating indefinitely inside
  `Architectural Rules`

## Task Status

PLANNED

## Inputs

- the current repo-level owner file at [__ai__.md](../../__ai__.md)
- layer-level owner files with higher cognitive load, especially:
  - [.github/workflows/__ai__.md](../../.github/workflows/__ai__.md)
  - [docs/Authoritative/Canon/AgenticDevelopment/__ai__.md](../Authoritative/Canon/AgenticDevelopment/__ai__.md)
  - [docs/Authoritative/Canon/RepoManagement/__ai__.md](../Authoritative/Canon/RepoManagement/__ai__.md)
- the reusable owner-file template at [__ai__.template.md](../../__ai__.template.md)
- the current owner-file validation and freshness scripts:
  - [validate_ai_docs.py](../../scripts/validate_ai_docs.py)
  - [check_ai_docs.py](../../scripts/check_ai_docs.py)
  - [ai_verify_contracts.py](../../scripts/ai_verify_contracts.py)

## Proposed Work

### PR - A: Owner-File Compaction Standard And Section Allocation Rules

- define a clearer expectation for what belongs in `Architectural Rules`
  versus `Known Gaps / Future-State Notes` versus `Cross-Folder Contracts`
- reinforce that completed-work memory should not continue to accumulate as an
  append-only rules list when the same information already lives in planning
  archives, release notes, or nearby authoritative docs
- tighten the template and any lightweight validation/guidance only insofar as
  needed to protect the intended section shape without turning style
  preferences into a brittle linter

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `__ai__.template.md`
- `scripts/validate_ai_docs.py` only if a minimal section-allocation guardrail
  is added
- `scripts/check_ai_docs.py` only if freshness guidance needs to become more
  explicit about curated owner-file updates

#### Update AI files

- `.`
- `scripts`

### PR - B: Repo-Level And Layer-Level Compaction Pass

- compact the highest-load owner files first, especially the repo root and the
  major canon/layer entrypoints
- preserve durable governance and boundary rules while collapsing append-only
  historical accretion into a shorter current-state instruction set
- move details into the more appropriate section when they are:
  - historical execution memory
  - file-specific nuance that belongs in `File Index`
  - folder-boundary guidance that belongs in `Cross-Folder Contracts`
  - future-state caveats that belong in `Known Gaps / Future-State Notes`

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `__ai__.md`
- `.github/workflows/__ai__.md`
- `docs/Authoritative/Canon/AgenticDevelopment/__ai__.md`
- `docs/Authoritative/Canon/RepoManagement/__ai__.md`

#### Update AI files

- `.`
- `.github/workflows`
- `docs/Authoritative/Canon/AgenticDevelopment`
- `docs/Authoritative/Canon/RepoManagement`

## Sequencing

- define the compaction standard and section-allocation expectations first so
  the cleanup pass has an explicit target shape
- compact the repo-level and layer-level owner files second, keeping the
  highest-load surfaces in sync rather than rewriting only one file in
  isolation

## Risks And Unknowns

- Over-compaction could remove real current-state guidance if the cleanup pass
  treats every specific rule as mere historical residue.
- A validator or template change can become too prescriptive if it tries to
  score tone or prose style instead of protecting section boundaries.
- Moving details into the wrong section can make the owner files shorter but
  harder to audit if contributors can no longer tell where cross-folder rules
  or future-state caveats are supposed to live.

## Exit Criteria

- repo-level and layer-level `__ai__.md` files read as curated current-state
  contracts rather than append-only summaries of completed work
- the intended difference between `Architectural Rules`, `Known Gaps`, and
  `Cross-Folder Contracts` is explicit and durable
- the highest-load owner files preserve their real governance value while
  becoming meaningfully easier to scan and maintain

## Final Handoff State

- completing this Task should leave the owner-file system easier to extend
  without turning every merged slice into another permanent `Architectural
  Rules` bullet
- later owner-file updates should add new rules more selectively and should
  prefer updating the right section over appending another historical note to
  the root contract

## Related Artifacts

- [Planning README](./README.md)
- [Repo-Level Owner File](../../__ai__.md)
- [Owner-File Template](../../__ai__.template.md)
- [Workflows Owner File](../../.github/workflows/__ai__.md)
- [Agentic Canon Owner File](../Authoritative/Canon/AgenticDevelopment/__ai__.md)
- [RepoManagement Canon Owner File](../Authoritative/Canon/RepoManagement/__ai__.md)
