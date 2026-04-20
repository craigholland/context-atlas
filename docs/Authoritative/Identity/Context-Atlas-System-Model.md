---
id: context-atlas-system-model
title: Context Atlas System Model
summary: Defines the project-specific operational model for Context Atlas, including its first-class component families, canonical artifacts, and initial package architecture.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-17
last_reviewed: 2026-04-20
owners: [core]
tags: [system-model, context-atlas, domain, package-architecture, components]
related:
  - ./Context-Atlas-Agentic-Development-Profile.md
  - ./Context-Atlas-Charter.md
  - ../Architecture/Craig-Architecture.md
  - ../Ontology/Documentation-Ontology.md
  - ../../README.md
supersedes: []
---

# Context Atlas System Model

## Purpose

This document defines the initial project-specific operational model for Context Atlas.

Its job is to translate the charter and Craig Architecture into an explicit view of the system's expected first-class component families, canonical artifacts, and initial package boundaries.

This is the document that answers questions such as:

- what major component families Context Atlas is expected to have
- what artifacts should be treated as canonical rather than incidental
- what belongs in the core domain versus services, infrastructure, adapters, and rendering
- which candidate concepts are central enough to deserve early package and model attention

## Scope

This document applies to the initial architectural shape of the `context_atlas` package and to the first thin implementation slices built from it.

It defines the expected system model and package direction for Context Atlas as a product-specific system.

It does not yet define the complete public API, final storage schema, every adapter contract, or every concrete type name that may eventually exist. Some vocabulary remains intentionally provisional while the project is still exploring its most stable seams.

## Binding Decisions

### 1. This Document Is The Project-Specific Bridge Between Charter And Architecture

The Context Atlas charter defines project identity and strategic scope.

Craig Architecture defines the reusable architectural philosophy and layering discipline used across projects.

This document instantiates those two artifacts for Context Atlas specifically by defining the expected first-class system components and the initial package architecture that should house them.

### 2. Context Atlas Has Eight First-Class Capability Families

The initial system model for Context Atlas should treat the following capability families as first-class:

1. source classification
2. authority and trust modeling
3. context assembly
4. memory policy
5. compression and transformation policy
6. budgeting and slot allocation
7. structured packet generation
8. provenance, lineage, and auditability

These are not optional side features. They describe the primary operational surface of the product.

Future implementations may add supporting capabilities, but these families define the first architectural center of gravity.

### 3. Source Classification Is A First-Class Domain Concern

Context Atlas should reason about sources as more than chunks of text.

The system model should preserve source-related information such as:

- source type
- source class
- authority and trust
- durability
- provenance
- intended use
- safe-to-act-on semantics

Classification should be treated as a domain-level concern because later selection, budgeting, memory, compression, and packet assembly decisions all depend on it.

### 4. Authority Modeling Is A First-Class Domain Concern

Context Atlas should explicitly represent how trust, precedence, override rules, and safe-use boundaries affect context selection.

This means the domain should be able to express ideas such as:

- authoritative sources should generally outrank lower-trust materials for binding questions
- exploratory materials may inform hypothesis generation without silently overriding higher-trust sources
- reviews should act as evidence and escalation input rather than automatic canonical truth
- release history is useful for historical questions without automatically defining current architecture truth

Authority modeling should not be left as an incidental scoring heuristic hidden inside one retriever or reranker implementation.

### 5. Context Assembly Is A First-Class Service Family

Context Atlas should treat context assembly as an explicit orchestration responsibility rather than as a thin wrapper around retrieval.

The assembly flow is expected to include capabilities such as:

- gathering candidate context
- scoring, reranking, filtering, and deduplication
- applying authority-aware selection rules
- allocating budget across classes or slots
- requesting compression or transformation where needed
- producing structured canonical packet outputs

The exact sequence may evolve, but context assembly itself is a first-class system concern.

### 6. Memory, Compression, And Budgeting Are Policy Families, Not Incidental Utilities

Memory retention and decay, compression and transformation, and budget allocation should all be treated as policy families with explicit ownership in the system model.

They should not be treated merely as helper utilities scattered across services.

This implies that Context Atlas should evolve toward explicit policy concepts for:

- what stays relevant over time
- what decays or is demoted
- what can be compressed safely under budget pressure
- how fixed and elastic budget slots are allocated
- how policy differs by source class, workflow, or role

### 7. Structured Packets, Decisions, And Traces Are Canonical Artifacts

The following artifact families should be treated as canonical or near-canonical outputs of the system:

- a structured context packet
- assembly decisions explaining inclusion, exclusion, ranking, or transformation outcomes
- lineage or trace artifacts that explain how a packet was assembled
- budget allocation records and transformation results where relevant

Prompt-ready text may be generated from these artifacts, but prompt text is derived rather than canonical.

### 8. Initial Domain Vocabulary Should Be Explicit, But Some Names Remain Provisional

The project should begin with explicit domain vocabulary rather than hiding everything behind generic dictionaries or anonymous payloads.

Candidate first-wave concepts include:

- `ContextSource`
- `ContextSourceClass`
- `ContextSourceAuthority`
- `ContextSourceDurability`
- `ContextSourceProvenance`
- `ContextEvidence`
- `ContextMemoryEntry`
- `ContextBudget`
- `ContextBudgetSlot`
- `ContextAssemblyDecision`
- `ContextPacket`
- `ContextPolicy`
- `ContextTransformation`
- `CompressionResult`
- `ContextTrace`

These concept families are in scope for early modeling.

The exact type names and final decomposition may evolve, but contributors should treat the underlying concepts as first-class rather than optional implementation details.

### 9. The Initial Package Architecture Should Reflect The System Model

For Context Atlas specifically, the current repository is a standalone package-style bootstrap rather than a multi-app repository.

That means the Craig-style layers should initially live inside the package namespace under `src/context_atlas/`.

The initial package direction should therefore be:

```text
project_root/
  docs/
  src/
    context_atlas/
      domain/
      services/
      infrastructure/
      adapters/
      rendering/
  tests/
  examples/
```

The intended responsibilities are:

- `domain/`: canonical models, enums, value objects, policy contracts, reason codes, and deterministic rules
- `services/`: context assembly orchestration, candidate flow coordination, packet creation workflow, persistence coordination
- `infrastructure/`: persistence backends, audit stores, memory stores, lineage storage, and other durable operational implementations
- `adapters/`: filesystem, repository, ticketing, tokenizer, embedding, model-facing, and other external integration adapters
- `rendering/`: derived output renderers such as prompt-ready packet views, reports, or exports

This is the standalone package variant of the Python layout described in [Craig Architecture - Python](../Architecture/Craig-Architecture-Python.md), adapted to Context Atlas as a single primary package.

### 10. Canonical And Derived Data Must Stay Distinguishable

Within Context Atlas, contributors should distinguish clearly between:

- canonical source and packet artifacts
- derived renderings
- derived indexes, embeddings, caches, and projections
- audit and lineage records derived from canonical assembly activity

Derived artifacts may be operationally important, but they must not quietly replace canonical system meaning.

### 11. Adapters Must Not Define The Core Ontology

Filesystem layouts, tokenizer APIs, embedding provider schemas, model-provider request shapes, and similar adapter details must not define the core Context Atlas ontology.

Those details may influence adapter contracts and translation boundaries, but the core vocabulary of the product should remain centered on context governance concepts rather than on the incidental vocabulary of one integration.

### 12. Early Implementation Slices Should Validate The System Model Incrementally

The first implementation slices should validate the architectural shape with minimal but meaningful end-to-end flows.

Good early slices are likely to include:

- source classification over a small authoritative document set
- authority-aware candidate selection under a simple budget
- structured packet generation with derived rendering
- traceable inclusion and exclusion decisions

Early slices should prefer architectural proof over breadth of integrations.

### 13. The Project-Specific Agentic Development Binding Lives In Identity

Context Atlas's own agentic-development structure is also part of the
project-specific operational model.

That binding should live in the Identity layer as a project profile that says:

- the project uses parent agents as top-level accountable actors
- the project uses specialists as bounded delegates rather than a second role
  layer
- the project uses skills as atomic reusable capabilities attached to those
  actors

Later role, mode, protocol, and environment-materialization artifacts should
bind through that project profile rather than skipping directly from portable
canon to concrete runtime assets.

## Constraints

- The system model must remain consistent with the Context Atlas charter.
- The package model must remain consistent with Craig Architecture dependency direction.
- First-class component families should not be collapsed prematurely into one monolithic service.
- Canonical packet, decision, and trace artifacts should remain visible in the architecture rather than hidden behind prompt rendering.
- Domain vocabulary should become more explicit over time, not less.
- Exploratory implementations may keep some names or boundaries provisional, but they must preserve future migration toward clearer first-class components.

## Non-Goals

- This document does not yet freeze every concrete class name or module path.
- This document does not define every adapter Context Atlas may eventually support.
- This document does not yet define the final persistence model for audit, memory, or packet lineage storage.
- This document does not replace future planning artifacts that sequence implementation slices.
- This document does not require every first-class concept to be implemented immediately before thin validation slices begin.

## Related Artifacts

- [Context Atlas Charter](./Context-Atlas-Charter.md)
- [Context Atlas Agentic Development Profile](./Context-Atlas-Agentic-Development-Profile.md)
- [Craig Architecture](../Architecture/Craig-Architecture.md)
- [Documentation Ontology](../Ontology/Documentation-Ontology.md)
- [Documentation](../../README.md)
