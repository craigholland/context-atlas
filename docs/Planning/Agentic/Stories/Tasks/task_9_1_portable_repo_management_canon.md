---
id: context-atlas-agentic-task-9-1-portable-repo-management-canon
title: Task 9.1 - Portable RepoManagement Canon PR Plan
summary: Defines the PR sequence for establishing the portable RepoManagement canon that governs principals, authorization, operations, and audit identity independently of any specific provider.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, task, pr-plan, repo-management, canon]
related:
  - ../story_9_repo_management.md
  - ../../agentic_development_product_definition.md
  - ../../../../Authoritative/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 9.1 - Portable RepoManagement Canon PR Plan

## Objective

Define the portable RepoManagement canon so repository principals,
authorization, operations, and audit identities are governed outside the
portable AgenticDevelopment canon and outside any one repository provider.

## Task Status

PLANNED

## Inputs

- [Story 9 - RepoManagement](../story_9_repo_management.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
- the current Context Atlas branch/PR workflow and role authority model

## Proposed Work

### PR - A: RepoManagement Surface And Vocabulary

- define the top-level RepoManagement authoritative surface and its reading
  purpose
- establish the base vocabulary for principals, authorization scopes,
  operations, branch-target policy, and audit identity
- keep the new canon clearly separate from AgenticDevelopment

#### Expected New Files
- `docs/Authoritative/RepoManagement/README.md`
- `docs/Authoritative/RepoManagement/RepoManagement-Glossary.md`

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_9_repo_management.md`
- `docs/Planning/Agentic/agentic_development_product_definition.md`

#### Update AI files
- `.`

### PR - B: Core Portable Models

- define the portable models for principals, authorization, operations,
  branch-target policy, and audit identity
- keep them provider-agnostic while concrete enough to bind later into GitHub
  and other providers
- clarify what belongs in portable repo-management canon versus project or
  provider bindings

#### Expected New Files
- `docs/Authoritative/RepoManagement/Principal-Model.md`
- `docs/Authoritative/RepoManagement/Authorization-Model.md`
- `docs/Authoritative/RepoManagement/Operation-Model.md`
- `docs/Authoritative/RepoManagement/Branch-Target-Policy-Model.md`
- `docs/Authoritative/RepoManagement/Audit-Identity-Model.md`

#### Expected Existing Files Updated
- `docs/Authoritative/RepoManagement/README.md`

#### Update AI files
- `.`

### PR - C: Story Reinforcement

- align the Agentic epic and RepoManagement Story with the new portable canon
- reduce the chance that later GitHub work reinvents a second repo vocabulary
- document any provider-specific questions that should wait for Task 9.2

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_9_repo_management.md`
- `docs/Planning/Agentic/Stories/story_10_validation_governance_and_drift_control.md`
- `docs/README.md`

#### Update AI files
- `.`

## Sequencing

- define the top-level RepoManagement surface first
- define the core portable models second
- reinforce Story usage third

## Risks And Unknowns

- The portable repo-management canon could become too provider-shaped too early.
- The new canon could overlap awkwardly with AgenticDevelopment if the
  boundaries are not explicit.
- Later provider bindings may still invent their own vocabulary if the
  portable models are too vague.

## Exit Criteria

- the RepoManagement authoritative surface exists
- the portable repo-management vocabulary is explicit
- later provider bindings can inherit one stable portable model

## Related Artifacts

- [Story 9 - RepoManagement](../story_9_repo_management.md)
- [Craig Architecture](../../../../Authoritative/Architecture/Craig-Architecture.md)
