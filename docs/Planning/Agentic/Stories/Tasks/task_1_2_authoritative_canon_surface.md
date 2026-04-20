---
id: context-atlas-agentic-task-1-2-authoritative-canon-surface
title: Task 1.2 - Authoritative Canon Surface PR Plan
summary: Defines the PR sequence for shaping the initial authoritative AgenticDevelopment doc set and its internal document boundaries.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, task, pr-plan, canon, docs]
related:
  - ../story_1_portable_agentic_development_canon.md
  - ../../agentic_development_product_definition.md
  - ../../../../Authoritative/Ontology/Documentation-Ontology.md
supersedes: []
---

# Task 1.2 - Authoritative Canon Surface PR Plan

## Objective

Define the initial authoritative document surface under `docs/Authoritative/AgenticDevelopment/` so the canon has a stable home before project-specific bindings are added.

## Task Status

PLANNED

## Inputs

- [Story 1 - Portable Agentic Development Canon](../story_1_portable_agentic_development_canon.md)
- [Context Atlas Agentic Development Product Definition](../../agentic_development_product_definition.md)
- [Documentation Ontology](../../../../Authoritative/Ontology/Documentation-Ontology.md)
- current authoritative-doc structure under `docs/Authoritative/Architecture/`

## Proposed Work

### PR - A: Canon Surface Layout Decision

- decide which top-level agentic canon documents should exist immediately
- define the initial folder shape and reading order
- keep the initial surface small enough to govern clearly

#### Expected New Files
- `docs/Authoritative/AgenticDevelopment/README.md`

#### Expected Existing Files Updated
- `docs/Planning/Agentic/Stories/story_1_portable_agentic_development_canon.md`

#### Update AI files
- `.`

### PR - B: Core Canon Document Set

- add the first core canon documents that Story 1 needs
- separate glossary, authority, mode, skill, protocol, and materialization
  concepts into clear document boundaries
- align the new documents with the documentation ontology and authoritative-doc conventions

#### Expected New Files
- `docs/Authoritative/AgenticDevelopment/Mode-Model.md`
- `docs/Authoritative/AgenticDevelopment/Skill-Contract.md`
- `docs/Authoritative/AgenticDevelopment/Platform-Materialization-Model.md`

#### Expected Existing Files Updated
- `docs/Authoritative/AgenticDevelopment/README.md`
- `docs/Authoritative/AgenticDevelopment/Agentic-Development-Glossary.md`
- `docs/Authoritative/AgenticDevelopment/Agent-Authority-Model.md`

#### Update AI files
- `.`

### PR - C: Canon Navigation And Metadata Reinforcement

- align metadata, related links, and reading-order guidance across the new canon
- make the AgenticDevelopment surface discoverable from broader authoritative indexes
- confirm the canon reads as one coherent document set rather than isolated files

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/README.md`
- `docs/Authoritative/Architecture/README.md`
- `docs/Authoritative/AgenticDevelopment/README.md`
- `docs/Planning/README.md`

#### Update AI files
- `.`

## Sequencing

- decide the document surface first
- add the core document set second
- reinforce navigation and metadata third

## Risks And Unknowns

- The canon may become too fragmented if too many documents are created too early.
- The surface may become hard to discover if reading order and related links are weak.
- Ontology drift may appear if metadata and doc classes are inconsistent.

## Exit Criteria

- the AgenticDevelopment authoritative surface is defined
- the initial canon document set exists with clear boundaries
- the canon is discoverable from the broader authoritative-doc system

## Related Artifacts

- [Story 1 - Portable Agentic Development Canon](../story_1_portable_agentic_development_canon.md)
- [Documentation Ontology](../../../../Authoritative/Ontology/Documentation-Ontology.md)
