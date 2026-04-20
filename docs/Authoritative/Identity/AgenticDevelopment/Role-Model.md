---
id: context-atlas-role-model
title: Context Atlas Role Model
summary: Defines the initial top-level project roles that Context Atlas uses for agentic development and explains why those roles remain distinct accountabilities.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [context-atlas, agentic-development, identity, roles, accountability]
related:
  - ../Context-Atlas-Agentic-Development-Profile.md
  - ../Context-Atlas-System-Model.md
  - ./Role-Accountability-Matrix.md
  - ../../AgenticDevelopment/Agentic-Development-Glossary.md
  - ../../AgenticDevelopment/Agent-Authority-Model.md
  - ../../AgenticDevelopment/Agent-Composition-Model.md
supersedes: []
---

# Context Atlas Role Model

## Purpose

Define the initial project-specific role roster for Context Atlas agentic
development.

This document answers which top-level accountabilities Context Atlas recognizes
and why those accountabilities remain distinct instead of collapsing into one
generic implementation role.

## Scope

This document defines the top-level project roles only.

It does not define the full mode set, protocol catalog, runtime-materialization
files, or specialist roster.

It also does not replace the portable canon for what a role is. Instead, it
binds that canon to the project-specific roles Context Atlas chooses to use.

## Binding Decisions

### 1. Roles Are Project Accountabilities Embodied By Parent Agents

Within Context Atlas, a role is the project-level accountability concept.

The runtime or materialized actor that carries out that accountability is a
parent agent. Specialists may participate under that parent-owned
accountability, but they do not become a parallel role layer.

### 2. Context Atlas Uses Five Initial Top-Level Roles

The initial top-level role set for Context Atlas is:

- Planner/Decomp
- Backend
- Frontend
- QA
- DevOps

This roster is intentionally small enough to govern clearly while still
covering the distinct categories of planning, implementation, review, and
operational delivery that already exist in the repository.

### 3. Context Atlas Does Not Use A Generic Implementation Role

Context Atlas should not fall back to one generic implementation role for all
non-planning work.

The project has enough meaningful distinction between product-engine work,
user-facing surface work, review work, and operational delivery work that a
single implementation role would hide real accountability boundaries.

### 4. Each Role Exists Because It Represents A Real Repository Accountability

The current roles are grounded in repository work rather than aspirational job
titles:

- `Planner/Decomp`: owns decomposition quality, sequencing, planning artifacts,
  and dependency-aware delivery shape
- `Backend`: owns engine, model, service, adapter, and infrastructure-facing
  implementation work for the product core
- `Frontend`: owns user-facing interaction and presentation surfaces such as
  guides, examples, CLI-oriented experience, and future UI-facing product
  surfaces
- `QA`: owns governed validation, findings, acceptance analysis, and rework
  feedback loops
- `DevOps`: owns merge, release, workflow, and operational delivery surfaces
  that should not drift into ordinary implementation roles

### 5. The Role Set Is Intentionally Minimal At This Stage

Context Atlas should resist creating more top-level roles until there is a
persistent accountability difference that cannot be handled through skills,
specialists, or protocol participation.

This keeps the role model legible and prevents the parent-agent layer from
fragmenting too early.

### 6. Specialists Do Not Create A Shadow Role Roster

Specialists may exist under one or more parent-owned roles, but specialist
labels do not define top-level project accountability.

Any future specialist roster should therefore be interpreted as delegated
execution structure beneath these roles rather than as a competing role model.

### 7. Accountability And Ownership Are Defined Separately From Naming

The role roster answers which top-level accountabilities exist.

The accountability matrix answers what those roles directly own.

Context Atlas should keep those two surfaces separate so a short role roster
does not become overloaded with artifact-level ownership details.

## Constraints

- Role names should remain project accountabilities rather than vendor worker
  labels or tool-discovery names.
- The top-level role set should stay small enough that ownership boundaries are
  readable without cross-referencing runtime assets.
- New roles should justify themselves by durable accountability differences,
  not by one task, one tool, or one transient workflow preference.

## Non-Goals

- Define full artifact ownership or approval authority for each role.
- Define which modes each role may enter.
- Define the workflow protocols roles follow.
- Define runtime-specific files that materialize a role.

## Related Artifacts

- [Context Atlas Agentic Development Profile](../Context-Atlas-Agentic-Development-Profile.md)
- [Context Atlas System Model](../Context-Atlas-System-Model.md)
- [Context Atlas Role Accountability Matrix](./Role-Accountability-Matrix.md)
- [Agentic Development Glossary](../../AgenticDevelopment/Agentic-Development-Glossary.md)
- [Agent Authority Model](../../AgenticDevelopment/Agent-Authority-Model.md)
- [Agent Composition Model](../../AgenticDevelopment/Agent-Composition-Model.md)
