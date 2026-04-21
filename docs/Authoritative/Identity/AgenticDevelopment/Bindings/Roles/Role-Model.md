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
  - ../../../Context-Atlas-Agentic-Development-Profile.md
  - ../../../Context-Atlas-System-Model.md
  - ./Role-Accountability-Matrix.md
  - ../../../../Canon/AgenticDevelopment/RoleArchetypes/README.md
  - ../../../../Canon/AgenticDevelopment/RoleArchetypes/planning-decomposition-lead.md
  - ../../../../Canon/AgenticDevelopment/RoleArchetypes/backend-staff-engineer.md
  - ../../../../Canon/AgenticDevelopment/RoleArchetypes/technical-documentation-writer.md
  - ../../../../Canon/AgenticDevelopment/RoleArchetypes/user-acceptance-tester.md
  - ../../../../Canon/AgenticDevelopment/RoleArchetypes/quality-assurance-engineer.md
  - ../../../../Canon/AgenticDevelopment/RoleArchetypes/devops-engineer.md
  - ../../../../Canon/AgenticDevelopment/Agentic-Development-Glossary.md
  - ../../../../Canon/AgenticDevelopment/Agent-Authority-Model.md
  - ../../../../Canon/AgenticDevelopment/Agent-Composition-Model.md
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

This means the project role model is downstream of the portable role-archetype
catalog under `docs/Authoritative/Canon/AgenticDevelopment/RoleArchetypes/`.

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
- Documentation/UAT
- QA
- DevOps

This roster is intentionally small enough to govern clearly while still
covering the distinct categories of planning, implementation, review, and
operational delivery that already exist in the repository.

### 2a. The Project Role Roster Refines Portable Role Archetypes

The initial Context Atlas role roster refines the following portable role
archetypes:

- `Planner/Decomp` refines
  [Planning And Decomposition Lead](../../../../Canon/AgenticDevelopment/RoleArchetypes/planning-decomposition-lead.md)
- `Backend` refines
  [Backend Staff Engineer](../../../../Canon/AgenticDevelopment/RoleArchetypes/backend-staff-engineer.md)
- `Documentation/UAT` refines both
  [Technical Documentation Writer](../../../../Canon/AgenticDevelopment/RoleArchetypes/technical-documentation-writer.md)
  and
  [User Acceptance Tester](../../../../Canon/AgenticDevelopment/RoleArchetypes/user-acceptance-tester.md)
- `QA` refines
  [Quality Assurance Engineer](../../../../Canon/AgenticDevelopment/RoleArchetypes/quality-assurance-engineer.md)
- `DevOps` refines
  [DevOps Engineer](../../../../Canon/AgenticDevelopment/RoleArchetypes/devops-engineer.md)

The project role roster is therefore a refinement layer, not a replacement for
the portable catalog.

### 3. Context Atlas Does Not Use A Generic Implementation Role

Context Atlas should not fall back to one generic implementation role for all
non-planning work.

The project has enough meaningful distinction between product-engine work,
user-facing documentation and evaluation work, review work, and operational
delivery work that a single implementation role would hide real accountability
boundaries.

### 4. Each Role Exists Because It Represents A Real Repository Accountability

The current roles are grounded in repository work rather than aspirational job
titles:

- `Planner/Decomp`: owns decomposition quality, sequencing, planning artifacts,
  and dependency-aware delivery shape
- `Backend`: owns engine, model, service, adapter, and infrastructure-facing
  implementation work for the product core
- `Documentation/UAT`: owns user-facing documentation, runnable example
  experience, guided evaluation surfaces, and user-acceptance-oriented product
  walkthroughs for the current repository
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

If Context Atlas later grows a bona fide frontend application surface, that may
justify introducing a separate frontend role in a future revision. The current
repository does not justify that split yet.

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

- [Context Atlas Agentic Development Profile](../../../Context-Atlas-Agentic-Development-Profile.md)
- [Context Atlas System Model](../../../Context-Atlas-System-Model.md)
- [Context Atlas Role Accountability Matrix](./Role-Accountability-Matrix.md)
- [Role Archetypes](../../../../Canon/AgenticDevelopment/RoleArchetypes/README.md)
- [Agentic Development Glossary](../../../../Canon/AgenticDevelopment/Agentic-Development-Glossary.md)
- [Agent Authority Model](../../../../Canon/AgenticDevelopment/Agent-Authority-Model.md)
- [Agent Composition Model](../../../../Canon/AgenticDevelopment/Agent-Composition-Model.md)



