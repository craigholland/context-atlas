---
id: craig-protocol-template
title: Protocol Template
summary: Defines the canonical structure that portable workflow protocol documents should follow so protocol guidance remains readable, comparable, and later machine-checkable.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, protocols, template, workflow, canon]
related:
  - ./README.md
  - ../Agentic-Development-Glossary.md
  - ../Boundary-Model.md
  - ../Mode-Model.md
supersedes: []
---

# Protocol Template

## Purpose

Define the canonical structure that protocol documents should follow inside the
portable protocol canon.

## Scope

This document governs the reusable shape of portable workflow protocol docs.

It does not define which specific protocols a project adopts, which roles
participate in them, or which runtime assets later materialize them.

## Binding Decisions

### 1. Protocol Docs Should Share One Core Shape

Portable protocol docs should remain consistent enough that readers and later
validation logic can compare them without reverse-engineering a new format each
time.

### 2. Required Core Sections

Every protocol document should include these sections:

- `Purpose`
- `Scope`
- `Actors`
- `Trigger / Entry Conditions`
- `Preconditions`
- `Allowed Mutations`
- `Required Inputs`
- `Required Outputs`
- `Exit Criteria`
- `Handoff Targets`
- `Escalation Conditions`
- `Constraints`
- `Non-Goals`
- `Related Artifacts`

### 3. Optional Review-Oriented Sections

When a protocol participates in review gating or review-state movement, the
document may additionally include:

- `Gate Context`
- `Review Pass Expectations`
- `Review Outcome States`

Those sections should be used when they clarify the workflow. They should not
be added mechanically to protocols that do not need them.

### 4. Contract-Carrying Protocols Must Name Contract State Explicitly

When a protocol consumes or emits structured state, the document should make
the expected contract content explicit.

That commonly includes fields such as:

- contract type
- source boundary
- target boundary
- scope level
- requested next action
- required review passes
- resulting review outcome
- blocked or escalated state

This does not mean the template defines one universal schema for every system.
It means protocol docs should reserve explicit space for those structured
states instead of hiding them in prose.

### 5. Protocol Docs Should Stay Workflow-Centered

Protocol docs should explain workflow progression, not become substitutes for:

- role-accountability matrices
- mode catalogs
- runtime prompt files
- environment-specific discovery conventions

### 6. Template Conformance Should Support Future Validation

The common shape should be explicit enough that downstream validation can later
check for missing sections, missing contract semantics, or missing review-pass
fields where those are required.

## Protocol Skeleton

```md
# <Protocol Name>

## Purpose

## Scope

## Actors

## Trigger / Entry Conditions

## Preconditions

## Allowed Mutations

## Required Inputs

## Required Outputs

## Exit Criteria

## Handoff Targets

## Escalation Conditions

## Constraints

## Non-Goals

## Related Artifacts
```

Optional additions:

```md
## Gate Context

## Review Pass Expectations

## Review Outcome States
```

## Constraints

- The template should stay readable enough for human operators, not just future
  validators.
- The template should stay general enough that multiple protocol families can
  use it without heavy customization.
- Template evolution should happen carefully so later protocol docs do not
  drift into incompatible local shapes.

## Non-Goals

- Define a project-specific protocol roster.
- Define one universal handoff schema for every system.
- Replace role, mode, or authority documents.

## Related Artifacts

- [Protocols README](./README.md)
- [Agentic Development Glossary](../Agentic-Development-Glossary.md)
- [Boundary Model](../Boundary-Model.md)
- [Mode Model](../Mode-Model.md)
