---
id: context-atlas-agentic-development-product-definition
title: Context Atlas Agentic Development Product Definition
summary: Defines the Context Atlas epic for establishing a portable agentic-development canon, project-specific bindings, and concrete runtime materialization paths.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, planning, product, protocols, automation]
related:
  - ../../Authoritative/Identity/Context-Atlas-Charter.md
  - ../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md
  - ../../Authoritative/Identity/AgenticDevelopment/Role-Model.md
  - ../../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../../Authoritative/Architecture/Craig-Architecture.md
  - ../../Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md
  - ../../Authoritative/Ontology/Documentation-Ontology.md
supersedes: []
---

# Context Atlas Agentic Development Product Definition

## Objective

Define a reusable agentic-development system for Context Atlas that is:

- portable in its core philosophy and governance model
- explicit about project-specific role, mode, skill, and protocol choices
- able to materialize into concrete AI-runtime assets without making the
  runtime-specific artifacts the source of truth

This epic is successful only if Context Atlas can describe agentic development
in three clear layers:

- portable, runtime-agnostic canon
- Context Atlas project-specific bindings
- runtime-specific materialization guidance and generated/discoverable assets

The goal is not just to create prompts or local AI helper files. The goal is to
establish agentic development as a governed product surface inside Context
Atlas.

## Inputs

- [Context Atlas Charter](../../Authoritative/Identity/Context-Atlas-Charter.md)
- [Context Atlas Agentic Development Profile](../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md)
- [Context Atlas Role Model](../../Authoritative/Identity/AgenticDevelopment/Role-Model.md)
- [Context Atlas System Model](../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../Authoritative/Architecture/Craig-Architecture.md)
- [Craig Architecture - Planning And Decomposition](../../Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md)
- [Documentation Ontology](../../Authoritative/Ontology/Documentation-Ontology.md)
- Current Context Atlas MVP planning and delivery patterns under `docs/Planning/MVP/`
- Current local experience with role-guided planning, execution slices,
  review gates, and AI-governed artifact ownership

## Proposed Work

### Product Thesis

Context Atlas should treat agentic development as a first-class governed system,
not as a collection of ad hoc prompt files.

That means the project should have:

- an authoritative, portable vocabulary for agents, specialists, modes, skills,
  protocols, handoffs, escalation, and runtime capacity
- a project-specific profile that says exactly which of those concepts Context
  Atlas uses
- platform-specific materialization rules that explain how those abstract
  concepts become real runtime files for a given AI environment

### Product Shape

The target product shape is:

- one runtime-agnostic `AgenticDevelopment` canon under
  `docs/Authoritative/AgenticDevelopment/`
- one Context Atlas project profile that binds the canon to this repository's
  real delivery model
- one or more platform materialization surfaces that can turn the abstract
  model into concrete runtime files and folders

The important rule is that Context Atlas should not confuse:

- the concept of a role
- the project's chosen roles
- the vendor/runtime-specific file format used to materialize that role
- the portable canon that defines those concepts in the first place

### Core Capability Areas

The epic should establish these capability areas:

- portable definitions for agents, parent agents, specialists, modes, skills,
  protocols, handoffs, escalation, and runtime capacity
- project-specific bindings that define what Context Atlas actually uses
- workflow protocols for planning, execution, review, rework, recovery,
  delegation, handoff, and escalation
- runtime-capacity planning inputs that let decomposition work reflect the
  number of independent AI runtimes currently available
- platform-specific materialization guidance so concrete runtime assets can be
  created consistently instead of ad hoc

### Epic Structure

This document should be treated as an Agentic Development Epic.

The Epic consists of nine Stories:

- Story 1: Portable Agentic Development Canon
- Story 2: Agent And Skill Structure
- Story 3: Context Atlas Role Model
- Story 4: Context Atlas Mode Model
- Story 5: Protocol Model
- Story 6: Runtime Capacity And Parallel Decomposition
- Story 7: Platform Materialization Model
- Story 8: Codex Materialization For Context Atlas
- Story 9: Validation, Governance, And Drift Control

Each Story should preserve Craig Architecture boundaries:

- portable canon should stay generic and runtime-agnostic
- project profile should stay project-specific without collapsing into
  vendor-specific implementation details
- runtime materialization should stay outward and derived from canon rather
  than becoming the source of truth
- later Stories should read as downstream bindings or materialization work, not
  as alternate canons that redefine Story 1 terms
- guidance should deepen progressively from:
  - product intent at the Epic layer
  - architectural shape at the Story layer
  - implementation sequencing at the Task layer
  - concrete file-touch expectations at the PR-plan layer

### Target Users

The first target users for this epic are internal to Context Atlas delivery.

`1. Planning And Decomposition Role`

- Primary job: break Epics, Stories, Tasks, and PR slices into a safe delivery
  shape
- Value from this epic: knows what runtime capacity exists, what protocols
  govern planning, and which role/mode boundaries apply

`2. Backend Role`

- Primary job: execute backend-oriented implementation work without losing
  workflow discipline
- Value from this epic: knows what role it occupies, what modes it can enter,
  what artifacts it can mutate, and how to hand work off correctly

`3. Documentation/UAT Role`

- Primary job: own user-facing documentation, guided evaluation surfaces, and
  user-acceptance-oriented walkthroughs without losing workflow discipline
- Value from this epic: knows what role it occupies, what modes it can enter,
  what artifacts it can mutate, and how to hand work off correctly

`4. QA Role`

- Primary job: validate, critique, and return work through governed review and
  rework loops
- Value from this epic: uses the same shared protocols and project profile
  instead of a separate ad hoc review prompt stack

`5. DevOps Role`

- Primary job: own governed merge, release, workflow, and operational delivery
  actions that should not drift into ordinary implementation roles
- Value from this epic: has a clear authority boundary for merges, workflows,
  versioning, and release-oriented handoffs instead of inheriting those actions
  implicitly

`6. Human Operator`

- Primary job: understand, configure, and trust the agentic-development system
- Value from this epic: can inspect portable canon, project bindings, runtime
  capacity, and materialization rules without reverse-engineering live runtime
  files

## Deliverables

This epic should ultimately produce:

- a new authoritative `docs/Authoritative/AgenticDevelopment/` canon
- a project-specific Context Atlas agentic-development profile
- a project-specific role model that explicitly defines:
  - Planner/Decomp
  - Backend
  - Documentation/UAT
  - QA
  - DevOps
- a project-specific mode model that defines which execution states Context
  Atlas actually uses
- a project-specific runtime-capacity artifact for decomposition planning
- a protocol set that covers agent execution and inter-agent handoffs
- one or more platform materialization guides and templates
- generated or governed runtime-specific assets that are explicitly tied back
  to the canon and project profile

At the product level, the deliverable is not just documentation. It is a
governed system that can drive how agentic work is decomposed, executed,
reviewed, and resumed.

## Boundaries And Non-Goals

This epic is not trying to:

- create a generic multi-agent orchestration platform
- create live runtime scheduling or worker discovery infrastructure
- force all future AI environments into one vendor-shaped file layout
- treat runtime-specific prompt files as the authoritative model
- replace project architecture or documentation ontology with agentic rules
- define every possible future role, specialist, or lifecycle state up front

Near-term scope should stay focused on governance, decomposition, protocols,
and materialization rules for Context Atlas development itself.

## Risks And Unknowns

- The portable canon may become too concrete too early and accidentally bake in
  one runtime's assumptions.
- The project profile may blur into runtime-specific details if the boundaries
  are not kept explicit.
- Protocol docs may drift into role-specific duplication rather than shared
  workflow definitions with project-specific bindings.
- Runtime-capacity configuration may be confused with live runtime allocation if
  the model does not distinguish planning capacity from current operational
  availability.
- Materialization guidance may become write-only if the generated/live runtime
  assets are not kept clearly traceable back to the authoritative docs.
- The system may overfit to current delivery habits instead of staying flexible
  enough for future AI environments.

## Exit Criteria

This Epic definition is ready to guide implementation when:

- the three-layer model is accepted:
  - portable canon
  - Context Atlas project profile
  - runtime-specific materialization
- the split between:
  - agent/skill structure
  - role model
  - mode model
  is accepted as the near-term decomposition path
- the role of protocols, handoffs, and runtime-capacity planning is accepted as
  part of the product surface
- the initial Context Atlas top-level role set is accepted:
  - Planner/Decomp
  - Backend
  - Documentation/UAT
  - QA
  - DevOps

The broader epic is complete when:

- Context Atlas has an authoritative agentic-development canon
- the repository has a project-specific profile that declares what it uses
- the repository has an explicit role model and explicit mode model rather than
  blending those concepts into one layer
- runtime-capacity planning is machine-readable and usable during decomposition
- shared workflow protocols define not only task execution but inter-agent
  handoff and escalation
- at least one runtime materialization path is concretely supported without
  becoming the source of truth
- the resulting runtime assets are discoverable, governed, and resistant to
  drift

## Related Artifacts

- [Context Atlas Charter](../../Authoritative/Identity/Context-Atlas-Charter.md)
- [Context Atlas Agentic Development Profile](../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md)
- [Context Atlas Role Model](../../Authoritative/Identity/AgenticDevelopment/Role-Model.md)
- [Context Atlas System Model](../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../Authoritative/Architecture/Craig-Architecture.md)
- [Craig Architecture - Planning And Decomposition](../../Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md)
- [Documentation Ontology](../../Authoritative/Ontology/Documentation-Ontology.md)
- [MVP Product Definition](../MVP/mvp_product_defintiion.md)
