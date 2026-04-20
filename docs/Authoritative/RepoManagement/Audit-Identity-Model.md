---
id: repo-audit-identity-model
title: Audit Identity Model
summary: Defines the portable audit-identity model for separating stable visible principals from transient runtime identities while keeping repository history readable.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [repo-management, audit, identities, traceability]
related:
  - ./README.md
  - ./Principal-Model.md
  - ./Operation-Model.md
supersedes: []
---

# Audit Identity Model

## Purpose

Define the portable audit-identity model for repository actions.

## Scope

This document governs how stable visible principals, runtime instances, and
structured action records should relate to one another.

It does not choose one project's bot names or provider event format.

## Binding Decisions

### 1. Visible Principal Identity Must Stay Stable

Repository history should expose stable visible principals so humans can read a
PR, review, or merge record and understand which governed actor family was
responsible.

### 2. Runtime Instance Identity Must Stay Separate

The transient runtime instance that executed work should remain separately
recorded rather than being embedded directly in the visible principal name.

### 3. Structured Action Records Should Carry The Extra Detail

When deeper traceability is needed, bindings should carry structured action
records that capture fields such as:

- provider
- visible principal
- project role
- runtime instance identifier
- protocol
- mode
- action
- scope level
- source and target refs
- work item identifier

### 4. Audit Identity Should Explain Who Acted And Why They Were Allowed

Good audit identity is not only "who clicked the button."

It should also let a reviewer understand which workflow state or governed
authority made that action legitimate.

## Example Shape

```yaml
repo_action_event:
  repo_provider: <provider>
  visible_principal: <stable-principal-name>
  project_role: <role>
  runtime_instance_id: <runtime-id>
  protocol: <protocol-id>
  mode: <mode-id>
  action: <operation-id>
  scope_level: <task|story|epic|release>
  source_ref: <source-branch-or-ref>
  target_ref: <target-branch-or-ref>
  work_item_ref: <provider-item-reference>
```

## Constraints

- Visible principal names should stay human-readable.
- Runtime instance identifiers should stay structured, not improvised inside
  visible actor names.
- Provider or project bindings should refine this model without collapsing the
  distinction between stable identity and transient execution context.

## Non-Goals

- Define one provider's event schema.
- Define one project's final principal names.
