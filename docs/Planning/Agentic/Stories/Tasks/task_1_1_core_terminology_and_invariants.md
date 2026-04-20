---
id: context-atlas-agentic-task-1-1-core-terminology-and-invariants
title: Task 1.1 - Core Terminology And Invariants PR Plan
summary: Defines the PR sequence for establishing the portable agentic-development glossary and invariant relationship model.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, task, pr-plan, canon, glossary]
related:
  - ../story_1_portable_agentic_development_canon.md
  - ../../agentic_development_product_definition.md
  - ../../../../Authoritative/Canon/Architecture/Craig-Architecture.md
supersedes: []
---

# Task 1.1 - Core Terminology And Invariants PR Plan

## Objective

Define the portable vocabulary and invariant relationship model for agentic
development before project-specific bindings or runtime materialization are introduced.

## Task Status

IMPLEMENTED

## Inputs

- [Story 1 - Portable Agentic Development Canon](../story_1_portable_agentic_development_canon.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
- [Craig Architecture](../../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- current repo patterns for roles, modes, skills, protocols, and task review gates

## Proposed Work

### PR - A: Portable Glossary Inventory And Term Boundaries

- inventory the agentic concepts that need portable definitions
- define boundary lines between overlapping terms such as role, parent agent,
  specialist, mode, protocol, and skill
- identify terms that should remain outside the initial canon until later Stories

#### Expected New Files
- `docs/Authoritative/Canon/AgenticDevelopment/Agentic-Development-Glossary.md`

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_1_portable_agentic_development_canon.md`

#### Update AI files
- `.`

### PR - B: Invariant Relationship Model

- document the stable relationship chain between parent agents, roles,
  protocols, modes, skills, and specialist delegation
- keep the model runtime-agnostic and free of project-specific role names
- reinforce the distinction between accountability, workflow state, and reusable capability

#### Expected New Files
- `docs/Authoritative/Canon/AgenticDevelopment/Agent-Authority-Model.md`

#### Expected Existing Files Updated
- `docs/Authoritative/Canon/AgenticDevelopment/Agentic-Development-Glossary.md`
- `docs/Planning/Agentic/Stories/story_1_portable_agentic_development_canon.md`

#### Update AI files
- `.`

### PR - C: Canon Reinforcement And Cross-Linking

- connect the glossary and invariant model back to Craig Architecture and the
  wider agentic canon surface
- tighten wording so later Story docs can reference the canon without redefining it
- verify that the portable layer still reads as vendor-agnostic and project-agnostic

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Authoritative/Canon/AgenticDevelopment/README.md`
- `docs/Authoritative/Canon/AgenticDevelopment/Agentic-Development-Glossary.md`
- `docs/Authoritative/Canon/AgenticDevelopment/Agent-Authority-Model.md`
- `docs/Planning/Agentic/Stories/story_1_portable_agentic_development_canon.md`

#### Update AI files
- `.`

## Sequencing

- inventory terms first
- define invariant relationships second
- reinforce the canon surface and cross-links third

## Risks And Unknowns

- Definitions may become too abstract if they are not tied to clear term boundaries.
- Relationship rules may become too concrete if they accidentally assume a single runtime.
- Later Stories may still redefine terms if the portable vocabulary is not crisp enough.

## Exit Criteria

- the portable glossary exists
- the invariant relationship model is explicit
- later Stories can reference the canon without redefining its terms

## Related Artifacts

- [Story 1 - Portable Agentic Development Canon](../story_1_portable_agentic_development_canon.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)

