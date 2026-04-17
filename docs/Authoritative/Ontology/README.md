# Ontology Templates

This directory defines the initial document template model for Context Atlas.

The goal is to keep project artifacts lightweight enough to author quickly while still making them structured enough for review, reuse, and future machine interpretation.

The canonical semantic meaning of the document classes themselves now lives in [Documentation-Ontology.md](./Documentation-Ontology.md).

## Composition Model

All downstream project documents should begin with the shared metadata block defined in [base_metadata.md](./base_metadata.md).

Document classes then add a content template appropriate to their role:

- Authoritative docs use [base_metadata.md](./base_metadata.md) plus [authoritative_content.md](./authoritative_content.md).
- Planning docs use [base_metadata.md](./base_metadata.md) plus [planning_content.md](./planning_content.md).
- Reviews, Exploratory, and Releases docs currently use [base_metadata.md](./base_metadata.md) plus [general_content.md](./general_content.md) unless a more specific class template is later introduced.

This gives the project one shared metadata vocabulary while still allowing different document classes to carry different body shapes and levels of binding force.

## Independent Template Versioning

Each template file is its own versioned artifact.

That means:

- [base_metadata.md](./base_metadata.md) has its own `template_id` and `template_version`
- [authoritative_content.md](./authoritative_content.md) has its own `template_id` and `template_version`
- [planning_content.md](./planning_content.md) has its own `template_id` and `template_version`
- [general_content.md](./general_content.md) has its own `template_id` and `template_version`

This is important because the shared metadata template and the various content templates may evolve independently.

For example, it should be possible to change `planning_content` from `1.0.0` to `1.1.0` without also forcing a version change to `authoritative_content` or `base_metadata`.

## Downstream Document Conformance

Downstream project documents should not use a single scalar `template_version`.

Instead, they should declare which template versions they conform to by using `template_refs` in their metadata.

Example:

```md
---
id: context-atlas-charter
title: Context Atlas Charter
summary: Defines the mission, scope, and non-goals of Context Atlas.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-16
last_reviewed: 2026-04-16
owners: [core]
tags: [charter, architecture]
related: []
supersedes: []
---
```

This allows a future document to declare, for example:

```md
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.1.0
```

## Why This Split Exists

We do not want every project artifact to collapse into a generic "note."

Different document classes serve different purposes:

- Authoritative documents define binding truth and safe-to-act-on project understanding.
- Planning documents describe intended work and sequencing, but do not override authoritative decisions.
- General content provides a safe fallback for document classes that are useful but not yet formalized into stricter body schemas.

The shared metadata layer helps future humans and tools understand what a document is, how trustworthy it is, and how it should be used.

This template directory handles structure. [Documentation-Ontology.md](./Documentation-Ontology.md) handles class meaning, trust, precedence, and safe-use semantics.

## Initial File Set

- [Documentation-Ontology.md](./Documentation-Ontology.md): canonical semantic meanings for the document classes
- [base_metadata.md](./base_metadata.md): shared front matter contract for all documents
- [authoritative_content.md](./authoritative_content.md): body template for binding documents
- [planning_content.md](./planning_content.md): body template for forward-looking execution documents
- [general_content.md](./general_content.md): fallback body template for other document classes

## Template Versioning

The current active template set is:

- `base_metadata@1.0.0`
- `authoritative_content@1.0.0`
- `planning_content@1.0.0`
- `general_content@1.0.0`

In the future, we expect to add `docs/Authoritative/Ontology/versioned/` to preserve older template revisions. The likely structure is one directory per template artifact, with versioned files beneath it.

Example:

```text
docs/Authoritative/Ontology/versioned/
  base_metadata/
    1.0.0.md
  authoritative_content/
    1.0.0.md
  planning_content/
    1.0.0.md
  general_content/
    1.0.0.md
```

## Versioning Rules

We should treat template versions as semver-like:

- Major: incompatible structural or semantic change
- Minor: compatible extension or additional required guidance
- Patch: clarifications, examples, or editorial cleanup without schema impact

## Current Scope

These templates remain part of the ontology scaffold, not the entire ontology by themselves.

The canonical class semantics are now defined in [Documentation-Ontology.md](./Documentation-Ontology.md). We should still expect to refine the templates further as the project charter and future class-specific document patterns are written.
