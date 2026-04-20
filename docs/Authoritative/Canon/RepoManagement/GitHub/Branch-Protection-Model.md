---
id: github-branch-protection-model
title: Branch Protection Model
summary: Defines reusable GitHub guidance for expressing branch-target policy through branch protection, rulesets, and merge restrictions.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [repo-management, github, branch-protection, rulesets, merges]
related:
  - ./README.md
  - ../Branch-Target-Policy-Model.md
  - ../Authorization-Model.md
supersedes: []
---

# Branch Protection Model

## Purpose

Define reusable GitHub guidance for expressing branch-target policy through
GitHub's branch protection and ruleset surfaces.

## Scope

This document governs reusable GitHub-side enforcement ideas for protected
branches, merge restrictions, and required checks.

It does not define one project's exact protected-branch roster.

## Binding Decisions

### 1. Branch-Target Policy Should Be Reflected In GitHub Enforcement

If a project claims that certain principals may merge only into certain target
branch classes, GitHub-side enforcement should reflect that policy rather than
leaving it only in prose.

### 2. Higher-Tier Targets Should Usually Have Stronger Protection

As target branches move toward integration or release significance, GitHub
protection should usually become stricter rather than looser.

### 3. Required Reviews And Checks Should Match The Claimed Gate Model

If a project defines review gates or required evidence, the GitHub side should
make those requirements visible through required reviews, required status
checks, or equivalent ruleset enforcement where practical.

### 4. Direct Push Rights And Merge Rights Should Stay Distinct

GitHub configuration should preserve the distinction between:

- pushing directly to a branch
- opening PRs against a branch
- merging into a branch

### 5. Emergency Override Paths Should Be Explicit

If emergency human overrides exist, they should be explicit and exceptional,
not the default path hiding behind broad admin access.

## Constraints

- Reusable GitHub guidance should describe policy intent, not one repo's exact
  click path.
- Project bindings should own the final protected-branch mapping.
- Branch protection should remain downstream of the portable branch-target
  policy model.

## Non-Goals

- Define one project's exact ruleset configuration.
- Define one provider-neutral protection syntax.
