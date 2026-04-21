---
id: craig-skill-git-branch-and-history
title: Git Branch And History
summary: Defines the portable skill for preparing, inspecting, and maintaining Git branch and commit history in a reviewable way.
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

## Common Mode Affinity

- implementation
- operational_delivery
- recovery

## Common Role Affinity

- DevOps Engineer
- Backend Staff Engineer

## Bounded Capability

- inspect branch state, commit history, and divergence
- prepare commits and branch structure for review or integration
- preserve readable, attributable history

## Common Outputs

- branch-status summary
- commit preparation
- history or integration notes

## Guardrails

- does not by itself grant merge authority
- should not normalize destructive history editing as a default
- does not replace provider-specific review and audit policy

## Related Artifacts

- [Skills](./README.md)
- [GitHub PR Review And Handoff](./github-pr-review-and-handoff.md)
- [DevOps Engineer](../RoleArchetypes/devops-engineer.md)
