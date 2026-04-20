---
id: craig-discovery-model
title: Discovery Model
summary: Defines the portable discovery requirements a runtime materialization must satisfy before any environment-specific folder or filename conventions are chosen.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, discovery, materialization, portability]
related:
  - ./Platform-Materialization-Model.md
  - ./Template-Model.md
  - ./Materialization-Boundary-Model.md
supersedes: []
---

# Discovery Model

## Purpose

Define the portable discovery requirements that a runtime materialization must
satisfy before any environment-specific folder conventions, file names, or
indexing strategies are chosen.

## Scope

This document governs what a runtime needs to discover in order to use
materialized agentic-development assets.

It does not define how any specific environment performs that discovery.

## Binding Decisions

### 1. Discovery Starts From Asset Classes, Not File Layout

A discovery model should begin by identifying which classes of runtime-facing
assets a runtime needs to find, such as:

- parent-agent assets
- specialist-agent assets
- skill assets
- mode assets
- protocol assets
- runtime-guidance assets
- configuration assets

The portable discovery question is "what must be discoverable," not "which
folder is used."

### 2. Discovery Should Distinguish Required And Optional Surfaces

Some runtime-facing asset classes may be required for a usable materialization,
while others may be optional or supporting.

The portable layer should make that distinction explicit so downstream
bindings do not have to rediscover it from trial and error.

### 3. Discovery May Be Satisfied By More Than One Strategy

A runtime may satisfy discovery requirements through different downstream
strategies, such as:

- folder conventions
- manifests or registries
- explicit configuration references
- generated indexes
- mixed strategies

The portable discovery model should remain valid across those strategies.

### 4. Discovery Must Remain Traceable To Upstream Sources

A runtime-facing discovery surface should stay traceable to the canon,
application bindings, and template surfaces that authorize it.

Discovery should not become a separate place where new semantics are invented
without upstream authorization.

### 5. Folder Conventions Are Downstream Bindings Of Discovery Needs

Folder names, filenames, and other concrete discovery mechanics are downstream
binding decisions.

They may satisfy the discovery model, but they are not the portable discovery
model itself.

### 6. Downstream Bindings Should Document Their Discovery Mapping

When an environment chooses folder conventions, registries, manifests, or
other discovery mechanics, it should document how those concrete surfaces map
back to the portable discovery classes they satisfy.

That mapping belongs in the downstream binding or environment-materialization
layer rather than in the portable canon.

### 7. Discovery Mechanics Must Not Collapse Unrelated Asset Classes Casually

Downstream discovery mechanics may package multiple asset classes together, but
they should not do so in a way that erases meaningful distinctions inherited
from the canon, application bindings, or template contracts.

If a runtime needs a coarser discovery surface, that projection should be
documented as a downstream convenience rather than treated as the new portable
shape.

## Constraints

- Portable discovery rules must not hard-code one environment's folder layout.
- Discovery requirements should remain concept-shaped rather than directory-
  shaped.
- Discovery guidance must stay subordinate to the upstream canon and
  application-binding layers.
- Discovery abstractions should be portable across folder-based, manifest-
  based, configuration-based, or mixed discovery strategies.

## Non-Goals

- Define the folder conventions for a specific runtime.
- Define one platform's filename rules.
- Replace template or traceability guidance with discovery-only rules.

## Related Artifacts

- [Platform Materialization Model](./Platform-Materialization-Model.md)
- [Template Model](./Template-Model.md)
- [Materialization Boundary Model](./Materialization-Boundary-Model.md)
