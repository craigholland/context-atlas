---
id: context-atlas-mvp-product-definition
title: Context Atlas MVP Product Definition
summary: Defines the MVP product shape for Context Atlas as one reusable engine demonstrated through three reference workflows.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [mvp, product, planning, codex, chatbot]
related:
  - ../../Authoritative/Identity/Context-Atlas-Charter.md
  - ../../Authoritative/Identity/Context-Atlas-System-Model.md
  - ../../Authoritative/Architecture/Craig-Architecture.md
  - ../../Authoritative/Ontology/Documentation-Ontology.md
supersedes: []
---

# Context Atlas MVP Product Definition

## Objective

Define a practical MVP for Context Atlas that proves it is a real context-governance pipeline component rather than a single-purpose integration.

The MVP should present one shared engine and three credible reference experiences:

- a software engineer using Codex on a repository
- a technical builder creating a chatbot over documents plus database-backed records
- a low-code chatbot builder using presets and guided configuration instead of custom Python wiring

The MVP is successful only if all three experiences clearly rely on the same Atlas core concepts, packet model, and governance behavior.

## Inputs

- [Context Atlas Charter](../../Authoritative/Identity/Context-Atlas-Charter.md)
- [Context Atlas System Model](../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../Authoritative/Architecture/Craig-Architecture.md)
- [Documentation Ontology](../../Authoritative/Ontology/Documentation-Ontology.md)
- Current starter implementation in `src/context_atlas/`
- Current review feedback that Atlas is closer to a core engine than an adoptable MVP product

## Proposed Work

### MVP Thesis

Context Atlas MVP should be:

- one reusable context-governance engine
- one canonical packet and trace model
- one Python-first product surface
- three reference workflows that prove the engine can sit in multiple AI pipelines

The MVP should not feel like:

- a Codex-only helper
- a docs-only retriever
- a prototype hidden behind architecture documents

### Target Users

The MVP should intentionally support three target users.

`1. Engineer using Codex on a repository`

- Primary job: ask Codex to understand or change a real codebase
- Atlas value: curate repo-aware context from docs, reviews, planning notes, selected code surfaces, and retained memory
- Required output: a Codex-ready rendered packet plus readable trace

`2. Technical builder creating a chatbot over documents plus database-backed records`

- Primary job: build a useful assistant on top of a docs corpus and structured data
- Atlas value: normalize heterogeneous sources, apply authority and budget policy, and produce inspectable context packets before model invocation
- Required output: a Python-integrated assembly flow that can work with documents plus relational or vector-derived records

`3. Low-code chatbot builder`

- Primary job: assemble a useful chatbot without writing much application code
- Atlas value: expose the same engine through presets, declarative configuration, and a guided setup path
- Required output: a simplified product surface that does not require deep familiarity with Atlas internals

### Shared Core Capabilities

The MVP should prove the following shared capabilities across all three target users:

- source normalization into canonical `ContextSource` artifacts
- source classification by class, authority, durability, provenance, and intended use
- reusable candidate retrieval and ranking
- explicit budgeting and slot allocation
- compression under budget pressure
- memory retention and demotion behavior
- canonical `ContextPacket` generation
- canonical `ContextTrace` generation
- prompt-ready rendering as a derived surface rather than the canonical artifact

### Required Product Surfaces

The MVP should include these shared product surfaces:

- a stable Python package API
- a golden-path setup guide
- a packet inspection surface
- a trace inspection surface
- a clear environment and configuration story
- at least one preset-driven path that reduces required code for the low-code builder

### Required Reference Workflows

The MVP should ship with three concrete reference workflows.

`Codex Repository Workflow`

- ingest repo docs and other governed artifacts
- assemble a packet for an engineering task
- render model-facing context for Codex
- expose the trace so a human can inspect why sources were included or excluded

`Docs Plus Database Workflow`

- ingest documents from the filesystem
- ingest structured records from a database-facing adapter or adapter-ready record feed
- assemble a packet for a chatbot query
- show that Atlas treats both source families under one governance model

`Low-Code Workflow`

- configure source roots and runtime knobs without requiring custom Python composition for every step
- choose or inherit a preset
- generate a packet and readable result from a guided setup path
- keep the underlying packet and trace inspectable even when the setup experience is simplified

### Required MVP Deliverables

- one polished golden-path guide for the Codex repository workflow
- one technical integration guide for the documents plus database workflow
- one simplified preset-driven guide for the low-code workflow
- one packet and trace inspection story that works across all three
- one evidence-oriented comparison showing Atlas-governed context versus naive context stuffing for at least two workflows

### Non-Goals For This MVP

- a hosted SaaS platform
- enterprise multi-tenant management
- exhaustive provider integrations
- advanced vector-database ecosystem coverage
- production-grade UI for every workflow
- full autonomy or agent orchestration

## Sequencing

`Phase 1: Engine To Product Surface`

- stabilize public package exports
- tighten the assembly entrypoints
- produce a clear packet and trace inspection surface
- harden examples so they feel like supported usage rather than exploratory snippets

`Phase 2: Shared Source Coverage`

- keep the filesystem docs adapter as a first-class source path
- add a structured-record adapter shape for relational or vector-derived records
- ensure both source families converge into the same canonical source model

`Phase 3: Reference Workflow 1`

- build the flagship Codex-on-a-repository workflow
- write the setup guide
- produce at least one realistic end-to-end example

`Phase 4: Reference Workflow 2`

- build the technical chatbot-over-docs-plus-db workflow
- validate mixed-source packet assembly
- document the integration path clearly

`Phase 5: Reference Workflow 3`

- create a low-code or low-configuration path
- introduce presets or a simplified wrapper only after the shared engine and workflows are legible
- keep the low-code surface honest about what Atlas is doing underneath

`Phase 6: MVP Proof`

- compare Atlas-guided context versus naive baseline context
- record packet differences, trace clarity, and practical usefulness
- use those results to decide whether Atlas is ready to be presented as an MVP product

## Risks And Unknowns

- The low-code workflow may tempt the project into building a separate product surface too early.
- Database-backed source ingestion is not yet concretely defined in the current implementation.
- The current starter implementation is stronger on engine behavior than on product legibility.
- If the three workflows diverge too much, Atlas may accidentally become three partial products rather than one reusable component.
- The project still needs clear criteria for what counts as a "good enough" packet and trace experience for external users.
- Presets may be useful, but introducing them too early could freeze weak abstractions.

## Exit Criteria

This MVP definition is ready to guide implementation when:

- the three target users are accepted as the intended MVP personas
- the project agrees that the MVP is one engine with three reference workflows
- the required shared capabilities and required product surfaces are accepted
- the sequencing is accepted as the near-term productization order
- follow-on planning can break this definition into concrete workstreams or PR slices without redefining the MVP itself

The broader MVP effort is complete when:

- all three reference workflows are demonstrably functional
- they all rely on the same Atlas packet and trace model
- the setup path for each workflow is documented and reproducible
- Atlas can be shown as a reusable context-governance component rather than a one-off integration

## Related Artifacts

- [Context Atlas Charter](../../Authoritative/Identity/Context-Atlas-Charter.md)
- [Context Atlas System Model](../../Authoritative/Identity/Context-Atlas-System-Model.md)
- [Craig Architecture](../../Authoritative/Architecture/Craig-Architecture.md)
- [Documentation Ontology](../../Authoritative/Ontology/Documentation-Ontology.md)
