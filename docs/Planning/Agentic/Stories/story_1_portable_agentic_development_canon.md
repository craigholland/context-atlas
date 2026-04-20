---
id: context-atlas-agentic-story-1-portable-agentic-development-canon
title: Story 1 - Portable Agentic Development Canon
summary: Defines the runtime-agnostic agentic-development vocabulary and invariant governance model that the rest of the Context Atlas agentic stack will build on.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, story, canon, glossary, governance]
related:
  - ../agentic_development_product_definition.md
  - ../../../Authoritative/Architecture/Craig-Architecture.md
  - ../../../Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md
  - ../../../Authoritative/Ontology/Documentation-Ontology.md
supersedes: []
---

# Story 1 - Portable Agentic Development Canon

## Objective

Define the portable, runtime-agnostic canon for agentic development so Context
Atlas has a stable vocabulary and rule set before it starts binding those
concepts to project-specific roles, modes, protocols, or any particular
runtime-materialization scheme.

## Inputs

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Craig Architecture](../../../Authoritative/Architecture/Craig-Architecture.md)
- [Craig Architecture - Planning And Decomposition](../../../Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md)
- [Documentation Ontology](../../../Authoritative/Ontology/Documentation-Ontology.md)
- [Agentic Development README](../../../Authoritative/AgenticDevelopment/README.md)
- [Agentic Development Glossary](../../../Authoritative/AgenticDevelopment/Agentic-Development-Glossary.md)
- [Agent Authority Model](../../../Authoritative/AgenticDevelopment/Agent-Authority-Model.md)
- [Boundary Model](../../../Authoritative/AgenticDevelopment/Boundary-Model.md)
- [Platform Materialization Model](../../../Authoritative/AgenticDevelopment/Platform-Materialization-Model.md)
- Current Craig Architecture split between portable canon, project-specific bindings, and executable surfaces

## Proposed Tasks

### Task 1: Core Terminology And Invariants

- define the portable meanings of agent, parent agent, specialist, role, mode,
  skill, protocol, handoff, escalation, delegation, runtime capacity, and
  materialization
- define the fundamental relationship chain explicitly:
  - a parent agent embodies a role
  - a parent agent follows protocols
  - a parent agent enters modes while executing a protocol
  - a parent or specialist uses skills to perform work
  - a parent agent may delegate bounded work to specialists
- capture the invariant rules that should hold across AI environments rather
  than tying those rules to one vendor's file layout
- keep the canon precise enough to guide later project bindings without
  prematurely hard-coding Context Atlas-specific choices

### Task 2: Authoritative Canon Surface

- define the authoritative folder shape under `docs/Authoritative/AgenticDevelopment/`
- identify which core documents belong in the initial canon versus which ones
  should wait for later stories
- ensure the new canon is clearly positioned alongside Craig Architecture
  rather than treated as a secondary prompt bundle

### Task 3: Portability And Boundary Rules

- define the boundary between portable canon, project-specific agentic profile,
  and runtime-specific materialization
- make it explicit that runtime files are derived operational artifacts rather
  than the source of truth
- prevent project-specific roles, workflow gates, or vendor-specific
  assumptions from leaking into the portable layer

### Task 4: Orientation And Cross-Linking

- make the canon readable to a human operator who has not memorized the later
  project-specific agentic docs
- cross-link the new canon with Craig Architecture, documentation ontology, and
  the Context Atlas system model where appropriate
- ensure later stories can build on the canon without redefining its terms

## Sequencing

- define the initial portable glossary and invariant rules
- shape the authoritative document set that should carry those concepts
- lock the portability boundaries before adding project-specific bindings
- add orientation and cross-links so the canon can serve as a real entrypoint

## Risks And Unknowns

- The canon could become too abstract to guide later stories if the definitions
  stay purely philosophical.
- The canon could become too concrete too early if it accidentally encodes
  Context Atlas-specific workflow habits as universal rules.
- If the boundary with project-specific bindings is weak, later stories will
  likely duplicate or redefine terms instead of building on the canon.

## Exit Criteria

- a portable agentic-development vocabulary exists and is internally coherent
- the parent agent -> role -> protocol -> mode -> skill -> specialist
  relationship model is stated explicitly in the canon
- invariant rules for portability, authority, and derived materialization are
  documented explicitly
- the initial `docs/Authoritative/AgenticDevelopment/` surface is defined
- later stories can reference the canon instead of restating its core terms

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- the new portable canon stays runtime-agnostic and does not silently absorb
  project-specific or platform-specific interpretation details
- `py -3 scripts/preflight.py` passes on the Story feature branch before review
- the Story feature PR receives `@codex review`, and any review findings are
  resolved on that same feature branch before human merge
- any new glossary or canon documents include enough cross-linking to be usable
  as a discoverable entrypoint rather than an isolated document set

## Related Artifacts

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Agentic Development README](../../../Authoritative/AgenticDevelopment/README.md)
- [Agentic Development Glossary](../../../Authoritative/AgenticDevelopment/Agentic-Development-Glossary.md)
- [Agent Authority Model](../../../Authoritative/AgenticDevelopment/Agent-Authority-Model.md)
- [Boundary Model](../../../Authoritative/AgenticDevelopment/Boundary-Model.md)
- [Platform Materialization Model](../../../Authoritative/AgenticDevelopment/Platform-Materialization-Model.md)
- [Craig Architecture](../../../Authoritative/Architecture/Craig-Architecture.md)
- [Craig Architecture - Planning And Decomposition](../../../Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md)
- [Documentation Ontology](../../../Authoritative/Ontology/Documentation-Ontology.md)
