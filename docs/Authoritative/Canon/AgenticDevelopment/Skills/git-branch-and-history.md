---
id: craig-skill-git-branch-and-history
title: Git Branch And History
summary: Defines the portable skill for preparing, inspecting, and maintaining Git branch and commit history in a reviewable and low-drift way.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, skills, git, version-control]
related:
  - ./README.md
  - ./github-pr-review-and-handoff.md
  - ../RoleArchetypes/devops-engineer.md
supersedes: []
---

# Git Branch And History

## Purpose

Define the portable skill for managing Git history and branch state in support
of reviewable collaboration.

## Knowledge Scope

This skill should cover:

- branch state, ancestry, divergence, and integration readiness
- commit hygiene, commit grouping, and history readability
- merge, rebase, cherry-pick, and revert tradeoffs
- conflict handling and branch-stack maintenance
- tags and release-facing history interpretation

## Common Mode Affinity

- implementation
- operational_delivery
- recovery

## Common Role Affinity

- DevOps Engineer
- Backend Staff Engineer

## Common Inputs

- current branch topology and commit state
- target integration or release path
- repository branch policy and review model
- any unresolved conflicts or divergence

## Decision Heuristics

- preserve readable, attributable history over cleverness
- prefer non-destructive history operations unless a cleaner history is
  explicitly required and safe
- keep unrelated work separated into distinct commits or branches
- use reverts and explicit recovery when auditability matters more than a
  perfectly linear story
- escalate when the required history surgery could erase or obscure important
  collaboration context

## Execution Pattern

- inspect current branch and history state
- identify the intended integration target
- choose the smallest safe history or branch action
- confirm the resulting state is reviewable and attributable

## Expected Outputs

- branch-status summary
- commit preparation
- history or integration notes
- bounded conflict-resolution rationale

## Verification And Evidence

A well-used instance of this skill should usually leave behind:

- branch state that matches the intended review or integration path
- commit history that is understandable without hidden context
- explicit notes when unusual history operations were necessary

## Escalation Conditions

Escalate when:

- multiple collaborators' work would be rewritten or obscured
- the required integration path conflicts with branch governance rules
- conflict resolution cannot be done safely without product or implementation
  clarification
- the work appears to need provider-specific authority not owned by the actor

## Guardrails

- does not by itself grant merge authority
- should not normalize destructive history editing as a default
- does not replace provider-specific review and audit policy

## Related Artifacts

- [Skills](./README.md)
- [GitHub PR Review And Handoff](./github-pr-review-and-handoff.md)
- [DevOps Engineer](../RoleArchetypes/devops-engineer.md)
