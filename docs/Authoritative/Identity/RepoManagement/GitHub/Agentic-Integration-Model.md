---
id: context-atlas-github-agentic-integration-model
title: Agentic Integration Model
summary: Defines how the Context Atlas GitHub binding integrates with role authority, structured handoff contracts, QA review intake, and DevOps-controlled merges.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, repo-management, github, agentic-development, handoffs]
related:
  - ./README.md
  - ./Operation-Matrix.md
  - ./Branch-Target-Policy.md
  - ../../AgenticDevelopment/Bindings/Roles/Role-Authority-Matrix.md
  - ../../AgenticDevelopment/Bindings/Protocols/Gate-Review-Pass-Matrix.md
  - ../../../Canon/AgenticDevelopment/Protocols/Handoff-Protocol.md
  - ../../../Canon/AgenticDevelopment/Protocols/Review-Protocol.md
supersedes: []
---

# Agentic Integration Model

## Purpose

Define how the Context Atlas GitHub binding integrates with role authority,
structured handoff contracts, QA review intake, and DevOps-controlled merges.

## Binding Decisions

### 1. GitHub Operations Are Downstream Of Role Authority And Protocol State

Context Atlas should treat GitHub operations as governed effects of:

- role authority
- structured handoff or review state
- branch-target policy

GitHub actions are not ambient runtime powers.

### 2. `implementation_complete` Starts The QA Intake Path

When Backend or Documentation/UAT completes work, the normal downstream intake
for QA review is an `implementation_complete` contract scoped to the current
gate level.

The GitHub PR becomes the active review surface for that intake.

### 3. QA Performs Review Directly On The GitHub PR Surface

QA should publish findings and review outcomes directly on the active GitHub PR
surface through:

- PR review submissions
- inline findings where needed
- review-summary commentary where needed

The canonical trigger is the structured intake contract, not an ad hoc tool
invocation comment.

### 4. Implementation Roles Respond Through Patch Or Rationale

When QA raises findings, the implementation role should either:

- patch the branch
- or respond with a technical rationale on the PR surface

QA then decides whether the finding is cleared or remains open.

### 5. DevOps Merges Only After Required Review State Exists

The appropriate DevOps merge principal may merge only after:

- the branch-target policy for the target tier is satisfied
- the required review passes for that gate are complete
- unresolved findings no longer block the gate

### 6. Structured Contracts Stay Machine-Readable

The expected project-facing shapes remain machine-readable, for example:

```yaml
handoff:
  contract_type: implementation_complete
  scope_level: task
  target_role: qa
  required_review_passes:
    - code
  pr_number: <pr-number>
  source_ref: <source-branch>
  target_ref: <target-branch>
```

```yaml
review_outcome:
  scope_level: task
  review_passes_completed:
    - code
  outcome: changes_required
  blocking_findings: 2
  pr_number: <pr-number>
```

## Constraints

- GitHub PR behavior should remain aligned with the upstream role-authority and
  gate-review-pass surfaces.
- QA review should stay role-owned rather than collapsing back into a
  tool-trigger pattern.
- Merge execution should stay DevOps-owned rather than drifting into
  implementation or QA participation.


