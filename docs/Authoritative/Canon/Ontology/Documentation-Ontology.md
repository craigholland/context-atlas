---
id: documentation-ontology
title: Documentation Ontology
summary: Defines the canonical document classes for Context Atlas, including their meanings, trust semantics, safe-use rules, and precedence relationships.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-17
last_reviewed: 2026-04-17
owners: [core]
tags: [ontology, documentation, authority, trust, provenance]
related:
  - ./README.md
  - ./base_metadata.md
  - ./authoritative_content.md
  - ./planning_content.md
  - ./general_content.md
  - ../Architecture/Craig-Architecture.md
  - ../../README.md
supersedes: []
---

# Documentation Ontology

## Purpose

This document defines the canonical document ontology for Context Atlas.

Its job is to say what the major document classes mean, how trustworthy they are, what they are safe to use for, and how they should interact when multiple artifacts disagree.

## Scope

This document applies to project artifacts that use the Context Atlas documentation ontology, especially documents under `docs/` that declare one of the canonical `doc_class` values.

It governs semantic meaning, not just file structure. The template files in this directory define how documents are shaped. This document defines what those document classes mean.

## Binding Decisions

### 1. The Ontology Is Semantic, Not Merely A Folder Convention

The documentation ontology is not just a directory layout.

The classes `authoritative`, `planning`, `reviews`, `exploratory`, and `releases` represent different kinds of project knowledge with different trust levels, intended uses, and safe-use boundaries.

Folder names such as `docs/Authoritative/` and `docs/Planning/` should align with those meanings, but the ontology itself is conceptual first.

### 2. `Authoritative` Means Binding Project Truth

`Authoritative` documents define the highest-trust project truth currently available for their scope.

They are the class intended for artifacts such as:

- canonical architecture decisions
- project charters
- ontology definitions
- binding interfaces or operating rules
- other artifacts that future contributors are expected to act on directly

Safe use:

- safe for direct action within their scope
- safe to use as the default source of truth when lower-trust documents disagree
- safe to use as binding input for implementation, review, and planning

Important limitation:

- authoritative scope still matters; a broad authoritative artifact does not automatically override a more specific authoritative artifact if the two can coexist without contradiction

### 3. `Planning` Means Forward-Looking Execution Intent

`Planning` documents describe intended work, sequencing, decomposition, or future direction.

They are the class intended for artifacts such as:

- roadmaps
- execution plans
- milestone plans
- implementation sequencing notes
- work decomposition documents

Safe use:

- safe to use for execution planning and prioritization
- conditionally safe to act on when consistent with authoritative truth
- useful for deciding what should happen next

Not safe for:

- overriding authoritative architecture or policy
- redefining canonical system meaning by implication

When planning disagrees with authoritative artifacts, authoritative artifacts govern.

### 4. `Reviews` Means Findings, Evidence, And Assessments

`Reviews` documents capture discovered issues, assessments, evidence, critiques, and other evaluative outputs.

They are the class intended for artifacts such as:

- code reviews
- architecture reviews
- audit findings
- evidence summaries
- defect assessments

Safe use:

- safe for surfacing risk
- safe for issue discovery
- safe for decision support and escalation
- safe for motivating changes to authoritative or planning artifacts

Not safe for:

- being treated as implementation truth by themselves
- silently overriding authoritative decisions

When a review conflicts with an authoritative artifact, the review should be treated as evidence that the authoritative truth may need correction, clarification, or exception handling. The review does not override the authoritative artifact on its own.

### 5. `Exploratory` Means Speculation, Investigation, And Prototype Thinking

`Exploratory` documents capture speculative investigation, loose research, prototypes, and other non-binding thought processes.

They are the class intended for artifacts such as:

- design sketches
- speculative research notes
- prototype writeups
- open-ended investigations

Safe use:

- safe for hypothesis generation
- safe for exploration and idea formation
- safe for identifying questions worth pursuing

Not safe for:

- direct implementation authority
- silent precedence over higher-trust artifacts
- defining canonical project policy by implication

Exploratory artifacts may inform later authoritative or planning artifacts, but they are not themselves binding.

### 6. `Releases` Means Operational And Project-History Context

`Releases` documents capture release-related, operational, or historical project context.

They are the class intended for artifacts such as:

- changelogs
- release notes
- deployment-history context
- versioned shipment summaries

Safe use:

- safe for understanding what shipped
- safe for operational or historical context
- safe for answering questions about release state or project history

Not safe for:

- defining current architectural truth when contradicted by authoritative artifacts
- being used as the primary authority for future intent

When release artifacts and planning artifacts disagree, release artifacts are the better source for what actually happened, while planning artifacts remain the source for what was intended to happen.

### 7. Default Precedence Depends On The Question Being Asked

The ontology is not a flat ranking system. Precedence depends partly on the kind of question being answered.

For current binding project truth:

- `authoritative` governs
- `planning`, `reviews`, `exploratory`, and `releases` do not override it

For future execution intent:

- `planning` is useful when consistent with `authoritative`
- `authoritative` still governs if the two conflict

For discovered issues or contradictory evidence:

- `reviews` are the relevant class
- they trigger investigation or canonical updates rather than silently replacing authoritative truth

For speculative ideas:

- `exploratory` is useful for hypothesis generation only

For historical shipment or operational history:

- `releases` are the relevant class unless a more specific authoritative historical artifact exists

### 8. Same-Class Conflicts Must Be Resolved Explicitly

When two artifacts of the same class conflict, precedence should be resolved with explicit signals rather than guesswork.

Preferred order:

- an artifact that explicitly `supersedes` another wins
- a more specific artifact may govern over a broader one within its narrower scope
- `last_reviewed` does not create automatic precedence by itself

If same-class conflict remains unresolved, contributors should create or update an authoritative artifact that makes the intended relationship explicit.

### 9. Safe Action Rules Must Follow Ontology Class

The ontology implies different safe-action boundaries:

- `authoritative`: safe to act on directly within scope
- `planning`: safe to use for execution intent when consistent with authority
- `reviews`: safe to use as evidence and escalation input
- `exploratory`: safe to use for hypothesis generation only
- `releases`: safe to use for historical and operational context

Contributors should not flatten all documents into "equally valid context."

### 10. `doc_class` Is Only The First Ontology Axis

For now, `doc_class` is the primary explicit ontology field.

In the future, the ontology may expand into additional explicit axes such as:

- authority level
- durability
- intended use
- safe-to-act-on semantics
- provenance
- override relationships

Until those fields are formalized, contributors should interpret document trust and safe-use primarily through the canonical class meanings in this document.

## Constraints

- The document ontology must not be treated as a flat retrieval taxonomy where all artifacts are interchangeable.
- Lower-trust classes must not silently override higher-trust classes.
- `Planning` and `Exploratory` artifacts must not be used as backdoor authority.
- `Reviews` must be treated as evidence and assessment, not automatic canonical truth.
- Folder placement and document metadata should agree whenever possible.

## Non-Goals

- This document does not define every possible metadata field the project may eventually use.
- This document does not yet create separate content templates for `reviews`, `exploratory`, or `releases`.
- This document does not replace project-specific artifacts that define more specific truth within a narrower scope.
- This document does not attempt to reduce all ontology reasoning to a purely mechanical ranking formula.

## Related Artifacts

- [Ontology Templates](./README.md)
- [Base Metadata](./base_metadata.md)
- [Authoritative Content](./authoritative_content.md)
- [Planning Content](./planning_content.md)
- [General Content](./general_content.md)
- [Craig Architecture](../Architecture/Craig-Architecture.md)
- [Documentation](../../README.md)
