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
last_reviewed: 2026-04-19
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

### Epic Structure

This document should be treated as an MVP Epic.

The Epic consists of six Stories:

- Story 1: Engine To Product Surface
- Story 2: Shared Source Coverage
- Story 3: Codex Repository Workflow
- Story 4: Documents Plus Database Workflow
- Story 5: Low-Code Workflow
- Story 6: MVP Proof

Each Story should be implemented as a Craig-style increment:

- preserve inward dependency direction
- keep domain artifacts canonical and provider-agnostic
- use services for orchestration rather than policy ownership
- keep adapters responsible for external translation and source-specific mechanics
- keep prompt rendering and human-readable inspection as derived surfaces rather than canonical data

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

`Story 1: Engine To Product Surface`

- Goal: make the current starter implementation feel like an intentional product surface instead of a collection of internal components.
- Primary implementation areas:
  - package exports under `src/context_atlas/`
  - starter assembly entrypoints in `infrastructure/`
  - packet and trace inspection helpers in `rendering/`
  - example and setup guidance in `docs/` and `examples/`
- Architectural intent:
  - keep domain models canonical
  - keep orchestration in `services/`
  - keep human-readable packet and trace inspection in derived rendering surfaces
- Expected outcome: a new user can identify the supported entrypoint, the supported runtime knobs, and the primary inspection path without reverse-engineering the package.

`Story 2: Shared Source Coverage`

- Goal: prove that Atlas governs more than one source family while preserving one canonical source model.
- Primary implementation areas:
  - retain and refine the filesystem docs adapter
  - add a structured-record adapter shape for relational or vector-derived records
  - ensure provenance, authority, and intended-use mapping remain canonical in `domain`
- Architectural intent:
  - adapters translate source families into `ContextSource`
  - source-specific retrieval or parsing rules stay outward
  - shared semantics stay inward
- Expected outcome: documents and structured records can both become packet candidates through one common engine path.

`Story 3: Codex Repository Workflow`

- Goal: produce the flagship engineering workflow that shows Atlas improving repository-aware context for Codex.
- Primary implementation areas:
  - a concrete example flow for repo docs and related governed artifacts
  - a setup guide for engineering use
  - one realistic end-to-end example that outputs both rendered context and trace
- Architectural intent:
  - the workflow should consume the same core engine rather than a custom branch of logic
  - any repo-specific wiring should stay at the outer composition boundary
- Expected outcome: Context Atlas can be demonstrated as a useful Codex-facing pipeline component for real repository work.

`Story 4: Documents Plus Database Workflow`

- Goal: prove that Atlas can sit in front of a chatbot-style pipeline that uses both documents and database-backed information.
- Primary implementation areas:
  - a structured-record adapter or record-ingestion contract
  - one technical integration guide
  - one example that mixes docs plus record-backed context in one packet
- Architectural intent:
  - Atlas should not become a database client framework
  - database-specific access stays outward
  - Atlas should accept already-fetched record payloads or adapter-fed records and govern them consistently
- Expected outcome: a technical builder can understand how to use Atlas as a context-governance layer in a broader chatbot pipeline.

`Story 5: Low-Code Workflow`

- Goal: expose Atlas through a simplified configuration and preset path without creating a second engine.
- Primary implementation areas:
  - presets or profile-driven runtime configuration
  - a low-code setup path with minimal Python wiring
  - readable output that still preserves packet and trace inspection
- Architectural intent:
  - presets belong in outer configuration and composition surfaces, not in domain policy canon
  - the simplified path must still use the same packet, trace, and assembly contracts as the other workflows
- Expected outcome: a less-technical builder can reach a working Atlas flow through guided configuration rather than custom assembly code.

`Story 6: MVP Proof`

- Goal: produce evidence that Atlas is behaving like a real reusable product component rather than an architectural demo.
- Primary implementation areas:
  - one explicit evaluation rubric that defines what counts as acceptable MVP evidence
  - comparison workflows against naive context stuffing
  - artifact capture for packet and trace output
  - a documented assessment of usefulness, legibility, and correctness across at least two workflows
- Architectural intent:
  - proof should evaluate the shared engine, not bespoke demo logic
  - evidence artifacts should remain inspectable and reproducible
- Expected outcome: the project can make a grounded claim that Atlas has reached MVP status.

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
- [Story 1 - Engine To Product Surface](./Stories/story_1_engine_to_product_surface.md)
- [Story 2 - Shared Source Coverage](./Stories/story_2_shared_source_coverage.md)
- [Story 3 - Codex Repository Workflow](./Stories/story_3_codex_repository_workflow.md)
- [Story 4 - Documents Plus Database Workflow](./Stories/story_4_documents_plus_database_workflow.md)
- [Story 5 - Low-Code Workflow](./Stories/story_5_low_code_workflow.md)
- [Story 6 - MVP Proof](./Stories/story_6_mvp_proof.md)
