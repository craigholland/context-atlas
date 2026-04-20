---
id: context-atlas-charter
title: Context Atlas Charter
summary: Defines the mission, scope, non-goals, and strategic boundaries of Context Atlas as a standalone context-governance and context-assembly engine.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-17
last_reviewed: 2026-04-20
owners: [core]
tags: [charter, context-atlas, context-governance, architecture, scope]
related:
  - ./Context-Atlas-Agentic-Development-Profile.md
  - ./Context-Atlas-System-Model.md
  - ../Canon/Architecture/Craig-Architecture.md
  - ../Canon/Ontology/Documentation-Ontology.md
  - ../../README.md
supersedes: []
---

# Context Atlas Charter

## Purpose

This charter defines the mission, scope, non-goals, and strategic boundaries of Context Atlas.

Its job is to make the project's identity explicit before deeper package structure, implementation slices, and adapter work begin.

A concise project definition is:

> Context Atlas is a standalone context-governance and context-assembly engine that classifies, ranks, budgets, and assembles context into auditable packets.

## Scope

This document governs the identity and intended responsibility of the Context Atlas project.

It defines what Context Atlas is for, what kinds of systems it is intended to support, and what architectural boundaries future project artifacts should preserve.

This document does not define the final package layout, concrete APIs, storage schema, or detailed implementation plan. Those concerns should be handled by later authoritative or planning artifacts that remain consistent with this charter.

## Binding Decisions

### 1. Context Atlas Is A Standalone Product

Context Atlas is an independent library, package, SDK, and tool surface intended to support many context-sensitive systems.

It must not be defined conceptually as an internal module of one host application or be scoped primarily around the needs of one future consumer.

Future consumer systems may integrate Context Atlas, but no single downstream product defines the project's purpose, domain boundaries, or architectural center of gravity.

### 2. Context Atlas Exists To Solve Context Governance And Context Assembly

Context Atlas is not primarily a retrieval library.

It is not primarily a prompt utility.

It is not simply "RAG."

It is not only a memory store.

Its core job is to answer questions such as:

- given all possible information that could be included, what should actually enter model context
- in what order should context budget be allocated
- under what authority and trust hierarchy should candidate context be interpreted
- what should be retained, decayed, compressed, transformed, or excluded
- what representation should be treated as canonical
- how should inclusion and exclusion decisions remain inspectable and reproducible

### 3. Structured Context Packets Are Canonical; Prompt Rendering Is Derived

Context Atlas should preserve structured, inspectable context artifacts as its canonical outputs.

That means the project should center around concepts such as packets, decisions, provenance, lineage, reason codes, budget allocation, and transformations rather than collapsing everything prematurely into flat prompt text.

Prompt-ready rendering may exist as a useful derived output, but it is not the canonical representation of project truth.

### 4. Provider-Agnostic Is A Core Requirement

Context Atlas must remain provider-agnostic at its core.

It should support model-driven and agentic systems explicitly, but it must not become a brittle wrapper around one provider, runtime, or SDK vocabulary.

Provider-specific mechanics belong in adapters and integration layers rather than in the core project identity.

### 5. Context Governance Matters Wherever Model-Driven Workflows Exist

Modern model-driven and agentic systems increasingly rely on external capability bridges, memory surfaces, browser and computer-use tooling, and richer workflow orchestration.

That direction makes principled context governance more important, not less.

At the same time, Context Atlas should remain useful anywhere a system needs principled context classification, authority-aware selection, budgeting, memory policy, compression, and packet assembly.

### 6. Documentation Ontology And Authority Modeling Are First-Class Inputs

Context Atlas should treat documentation class, authority, trust level, intended use, durability, provenance, and safe-to-act-on semantics as meaningful signals rather than flattening all context into anonymous chunks plus similarity.

The project's documentation ontology is therefore not just a repository convention. It is an early expression of the broader contextual ontology the engine is expected to reason over.

### 7. Context Atlas Owns Governance, Not The Entire Runtime

The project should own responsibilities such as:

- source classification
- authority and trust modeling
- candidate selection, ranking, filtering, and deduplication
- context budgeting and slot allocation
- memory retention and decay policy
- compression and representation policy
- structured packet assembly
- provenance, lineage, and auditability

The project should not attempt to own the entire agent runtime, orchestration platform, model execution surface, or provider ecosystem around it.

### 8. Context Atlas Is Intended To Serve Multiple Consumer Classes

The project should be usable by more than one application family.

Intended consumers include:

- planning assistants
- review systems
- engineering copilots
- release assistants
- repo-aware reasoning systems
- agentic tools and workflows
- other systems that need principled context selection under trust and budget constraints

### 9. Relationship Boundaries Must Stay Explicit

The intended responsibility split is:

- model-facing systems own model execution, agent runtime behavior, and end-user interaction surfaces
- integration layers own external capability surfaces and environment access
- Context Atlas owns context governance, authority-aware selection, budgeting, assembly, and traceability
- downstream applications own their own workflow-specific orchestration and product behavior

These boundaries may be refined later, but Context Atlas should not quietly expand into the responsibilities of adjacent systems by default.

### 10. Reference Implementations Are Inspiration, Not Foundation

Prototype implementations, design specimens, and external examples may surface useful conceptual decompositions such as reranking, memory policy, compression, budgeting, and packet assembly.

Context Atlas should preserve those lessons where they are sound.

Context Atlas should not copy a prototype structure blindly, inherit its incidental limitations, or depend on any one specimen as the architectural foundation of this project.

### 11. Craig Architecture Applies From Day One

Context Atlas should be built under Craig Architecture from its first implementation slices.

That means:

- deterministic policy belongs in the domain over time
- orchestration belongs in services
- persistence belongs in infrastructure
- provider and environment specifics belong in adapters
- canonical data and derived representations must remain distinguishable
- small, reviewable increments are preferred over monolithic implementation drops

The project may explore intentionally dirty implementations during early discovery, but it must still protect dependency direction and future cleanup.

### 12. Early Project Work Should Prefer Canonical Docs And Thin Slices Over Feature Breadth

The project's early phase should prioritize:

- canonical architecture and ontology artifacts
- explicit project identity and boundary definitions
- a clean package and repository spine
- thin implementation slices that validate the architecture

The project should not chase broad feature coverage before those foundations exist.

### 13. Governed Agentic Development Should Preserve The Same Structural Boundaries

When Context Atlas formalizes its own agentic-development system, it should use
the same kind of explicit structural boundaries it expects elsewhere:

- top-level accountable actors should stay distinct from bounded delegates
- bounded delegates should stay distinct from atomic reusable capabilities
- project-specific bindings should stay distinct from environment-specific
  materialization

That keeps the internal agentic-development surface aligned with the same
governance values the product is trying to embody.

## Constraints

- Context Atlas must remain conceptually and architecturally standalone from any one downstream consumer.
- Core project concepts must remain provider-agnostic even when specific adapters support model-oriented or agentic workflows.
- Canonical project outputs should preserve provenance, reasoning, and inspectable transformation history where practical.
- Prompt rendering should remain a derived view over richer structured artifacts.
- Documentation ontology and authority hierarchy should remain available as first-class signals rather than being discarded during early retrieval or assembly steps.
- The architecture should favor reusable library and SDK patterns over app-specific assumptions baked into the core.

## Non-Goals

- Context Atlas is not intended to be a general agent runtime or orchestration framework.
- Context Atlas is not intended to be merely a vector-search or retrieval wrapper.
- Context Atlas is not intended to be merely a prompt templating utility.
- Context Atlas is not intended to be only a transcript or memory store.
- Context Atlas is not intended to define any one downstream application or product.
- Context Atlas is not intended to be a direct port of any prototype or reference implementation.
- This charter does not yet canonize the full domain model, package structure, or public API surface of the project.

## Related Artifacts

- [Context Atlas System Model](./Context-Atlas-System-Model.md)
- [Context Atlas Agentic Development Profile](./Context-Atlas-Agentic-Development-Profile.md)
- [Craig Architecture](../Canon/Architecture/Craig-Architecture.md)
- [Documentation Ontology](../Canon/Ontology/Documentation-Ontology.md)
- [Documentation](../../README.md)

