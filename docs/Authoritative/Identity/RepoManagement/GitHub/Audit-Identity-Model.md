---
id: context-atlas-github-audit-identity-model
title: Audit Identity Model
summary: Defines the Context Atlas GitHub naming and structured traceability model so closed PR history remains readable while runtime-level detail stays machine-readable.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, repo-management, github, audit, identities]
related:
  - ./Principal-Binding-Model.md
  - ./Agentic-Integration-Model.md
  - ../../../RepoManagement/Audit-Identity-Model.md
supersedes: []
---

# Audit Identity Model

## Purpose

Define the Context Atlas GitHub naming and traceability model.

## Binding Decisions

### 1. GitHub-Visible Names Stay Stable

The GitHub-visible principal names defined in the principal binding model are
the stable names that should appear in PR comments, reviews, and merge history.

### 2. Runtime Detail Stays Structured

Runtime-specific detail such as worker identity or execution instance should be
carried through structured event payloads rather than hidden in GitHub-visible
names.

### 3. PR History Should Reveal The Main Actor Changes

Closed PR history should let a human reader quickly answer:

- who implemented
- who reviewed
- who merged

### 4. Structured Event Payloads Carry The Deeper Contract State

When deeper traceability is needed, the expected shape is:

```yaml
repo_action_event:
  repo_provider: github
  github_principal: <context-atlas-principal>
  project_role: <planner|backend|documentation_uat|qa|devops>
  runtime_instance_id: <runtime-id>
  protocol: <protocol-id>
  mode: <mode-id>
  action: <operation-id>
  scope_level: <task|story|epic>
  source_ref: <source-branch>
  target_ref: <target-branch>
  pr_number: <pr-number>
```

### 5. Role Identity And Runtime Identity Stay Separate

The GitHub principal name should communicate the governed actor family.

The runtime instance identifier should communicate which specific execution
instance participated.

## Constraints

- Visible names should remain human-readable in PR history.
- Structured event data should remain machine-readable and easy to parse.
- The audit model should remain aligned with the portable audit-identity
  model.
