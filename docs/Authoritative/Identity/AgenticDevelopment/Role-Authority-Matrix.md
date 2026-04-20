---
id: context-atlas-role-authority-matrix
title: Context Atlas Role Authority Matrix
summary: Defines what each Context Atlas role may authorize, approve, mutate, delegate, or escalate so ownership does not drift into implicit authority.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, roles, authority, approvals]
related:
  - ./Role-Model.md
  - ./Role-Accountability-Matrix.md
  - ../Context-Atlas-Agentic-Development-Profile.md
  - ../../AgenticDevelopment/Escalation-Model.md
supersedes: []
---

# Context Atlas Role Authority Matrix

## Purpose

Define what each Context Atlas role may authorize, approve, mutate, delegate,
or escalate so role ownership does not collapse into implied authority.

This matrix is intentionally separate from the accountability matrix:

- the accountability matrix answers who owns a surface
- the authority matrix answers what that role may actually do with the surface

## Scope

This document defines:

- authority to decompose work
- authority to implement or mutate owned surfaces
- authority to request or perform review
- authority to approve merge or release actions
- authority to change repository operational workflows
- escalation expectations where authority should stop rather than drift

It does not define full protocol sequencing. Those workflow sequences belong in
the protocol story.

## Authority Matrix

### Planner/Decomp

#### May

- decompose Epics, Stories, Tasks, and PR slices
- update planning artifacts under `docs/Planning/`
- request review of planning changes
- delegate bounded planning analysis while retaining planning authority
- escalate when planning conflicts require ownership, review, or operational
  clarification

#### May Not

- self-approve merge or release actions solely by virtue of owning planning
- silently assume backend, documentation/UAT, QA, or DevOps authority without an
  explicit role handoff
- treat a decomposition proposal as equivalent to implementation approval

### Backend

#### May

- implement and mutate backend-owned product surfaces
- request review of backend changes
- delegate bounded backend implementation work to specialists under
  parent-owned authority
- escalate architectural, ownership, or review blockers that prevent delivery

#### May Not

- treat implementation ownership as final QA acceptance
- approve merges or releases as a default part of backend work
- mutate repository workflow or release surfaces unless explicitly operating
  under DevOps authority

### Documentation/UAT

#### May

- implement and mutate documentation/UAT-owned user-facing product surfaces
- request review of documentation, example, or evaluator-facing changes
- delegate bounded documentation/UAT work to specialists under parent-owned
  authority
- escalate user-facing or evaluation-surface blockers that need review or
  operational resolution

#### May Not

- treat documentation or evaluator-surface ownership as final QA acceptance
- approve merges or releases as a default part of documentation/UAT work
- mutate repository workflow or release surfaces unless explicitly operating
  under DevOps authority

### QA

#### May

- perform governed review
- record findings, acceptance analysis, and rework requests
- request additional evidence or validation work before recommending readiness
- escalate when review results conflict with claimed readiness or ownership

#### May Not

- silently inherit implementation ownership while performing review
- approve merges or releases as a substitute for DevOps authority
- convert review participation into a general right to rewrite owned product
  surfaces without explicit reassignment

### DevOps

#### May

- approve or execute merge actions once required planning, implementation, and
  QA expectations are satisfied
- prepare and execute release-oriented actions
- mutate operational workflow surfaces such as CI and release automation
- escalate when merge or release readiness is incomplete or contractually
  blocked

#### May Not

- bypass required planning, implementation, or QA gates merely because DevOps
  owns the operational action
- rewrite product implementation ownership as part of operational authority
- treat workflow ownership as authority over all repository content

## Cross-Role Constraints

- Specialists inherit delegated authority from a parent-owned role; they do not
  define an alternate approval surface.
- Escalation should preserve ownership context instead of silently transferring
  authority.
- Merge and release authority are distinct from implementation authority even
  when the same human or runtime may temporarily embody multiple roles.

## Constraints

- Authority boundaries should stay explicit before protocol sequencing deepens.
- Approval surfaces should remain narrow enough that merges and releases do not
  become implicit side effects of ordinary implementation work.
- The matrix should not drift into a role-by-role protocol narrative.

## Non-Goals

- Define every workflow transition.
- Replace the accountability matrix.
- Define runtime-specific approval files or bot behavior.

## Related Artifacts

- [Context Atlas Role Model](./Role-Model.md)
- [Context Atlas Role Accountability Matrix](./Role-Accountability-Matrix.md)
- [Context Atlas Agentic Development Profile](../Context-Atlas-Agentic-Development-Profile.md)
- [Escalation Model](../../AgenticDevelopment/Escalation-Model.md)
