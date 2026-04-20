---
id: context-atlas-agentic-story-9-repo-management
title: Story 9 - RepoManagement
summary: Defines the repo-management canon and Context Atlas binding for governed interaction with external repository systems, beginning with GitHub.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, story, repo-management, github, governance]
related:
  - ../agentic_development_product_definition.md
  - ./story_3_context_atlas_role_model.md
  - ./story_5_protocol_model.md
  - ./story_8_codex_materialization_for_context_atlas.md
  - ./story_10_validation_governance_and_drift_control.md
  - ../../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Role-Authority-Matrix.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Gate-Review-Pass-Matrix.md
supersedes: []
---

# Story 9 - RepoManagement

## Objective

Define the repo-management layer that governs how agentic roles interact with
external repository systems through scoped principals, explicit permissions,
provider-specific bindings, and auditable operational identities.

## Inputs

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 3 - Context Atlas Role Model](./story_3_context_atlas_role_model.md)
- [Story 5 - Protocol Model](./story_5_protocol_model.md)
- [Story 8 - Codex Materialization For Context Atlas](./story_8_codex_materialization_for_context_atlas.md)
- [Story 10 - Validation, Governance, And Drift Control](./story_10_validation_governance_and_drift_control.md)
- [Context Atlas Agentic Development Profile](../../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md)
- [Role Authority Matrix](../../../Authoritative/Identity/AgenticDevelopment/Role-Authority-Matrix.md)
- [Gate Review Pass Matrix](../../../Authoritative/Identity/AgenticDevelopment/Gate-Review-Pass-Matrix.md)
- Current repository delivery model using GitHub branches, PR reviews, and
  human merges

## Proposed Tasks

### Task 1: Portable RepoManagement Canon

- define the portable repo-management vocabulary and boundaries
- establish concepts like principals, authorization scopes, repo operations,
  branch-target policy, and audit identity outside the AgenticDevelopment canon
- keep the repo-management layer provider-agnostic at this level

### Task 2: GitHub Provider Canon

- define the reusable GitHub-specific model for bot principals, GitHub Apps,
  PR operations, review surfaces, merge behavior, and branch protections
- keep GitHub guidance reusable across projects while remaining clearly
  downstream of the portable RepoManagement canon
- avoid turning GitHub-specific setup guidance into a project-specific binding

### Task 3: Context Atlas GitHub Binding

- define how Context Atlas uses GitHub specifically
- bind project roles to GitHub-facing principals, operation scopes, branch
  targets, and merge authority
- make audit-friendly GitHub-visible identities explicit so closed PRs remain
  readable to humans

### Task 4: Agentic Integration And Handoff Hooks

- define how the RepoManagement layer integrates with agentic roles,
  protocols, review passes, structured handoff contracts, and DevOps/QA
  responsibilities
- make it explicit how implementation-complete handoffs become QA review work
  on the GitHub PR surface
- keep GitHub operations subordinate to role authority and protocol state

## Sequencing

- define the portable repo-management canon first
- define the reusable GitHub-specific provider canon second
- define the Context Atlas GitHub binding third
- bind repo-management behavior back into the agentic workflow fourth

## Risks And Unknowns

- Repo-management guidance could accidentally leak provider-specific behavior
  into the portable layer if boundaries are weak.
- A GitHub binding could become too credential- or setup-specific and lose its
  value as governed project policy.
- Repo permissions may remain soft if authority is documented only in prompts
  instead of being reflected in scoped principals and branch policy.
- Audit identity may become noisy or inconsistent if agent/runtime identity is
  not separated cleanly from stable GitHub-visible principals.

## Exit Criteria

- Context Atlas has a documented RepoManagement layer distinct from the
  AgenticDevelopment canon
- the portable RepoManagement vocabulary is explicit
- reusable GitHub-specific guidance exists without being mistaken for project
  bindings
- Context Atlas has an explicit GitHub binding for principals, scopes, branch
  targets, and audit identity
- the agentic workflow now has a governed path for GitHub comments, reviews,
  pushes, merges, and related handoffs instead of treating them as ambient
  runtime powers

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- the RepoManagement layer stays distinct from both the portable
  AgenticDevelopment canon and the project-specific runtime-materialization
  docs
- `py -3 scripts/preflight.py` passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge
- the resulting Story is explicit enough that later validation/governance work
  can reason about repo principals, permissions, and audit identities without
  reconstructing them from PR folklore

## Related Artifacts

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 3 - Context Atlas Role Model](./story_3_context_atlas_role_model.md)
- [Story 5 - Protocol Model](./story_5_protocol_model.md)
- [Story 8 - Codex Materialization For Context Atlas](./story_8_codex_materialization_for_context_atlas.md)
- [Story 10 - Validation, Governance, And Drift Control](./story_10_validation_governance_and_drift_control.md)
- [Context Atlas Agentic Development Profile](../../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md)
- [Role Authority Matrix](../../../Authoritative/Identity/AgenticDevelopment/Role-Authority-Matrix.md)
- [Gate Review Pass Matrix](../../../Authoritative/Identity/AgenticDevelopment/Gate-Review-Pass-Matrix.md)
