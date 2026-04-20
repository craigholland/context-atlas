---
id: craig-template-model
title: Template Model
summary: Defines the portable template surfaces used to project agentic-development semantics into runtime-facing assets before any platform-specific file conventions are chosen.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, templates, materialization, portability]
related:
  - ./Platform-Materialization-Model.md
  - ./Materialization-Boundary-Model.md
  - ./RoleArchetypes/README.md
  - ./Protocols/README.md
supersedes: []
---

# Template Model

## Purpose

Define the portable template surfaces used to project agentic-development
semantics into runtime-facing assets.

## Scope

This document governs which generic template surfaces exist before any
platform-specific file naming or folder conventions are chosen.

It does not define one platform's final file layout.

## Binding Decisions

### 1. Templates Are Generic Materialization Surfaces

Templates are generic materialization surfaces that describe how authoritative
semantics may be shaped into runtime-facing assets.

They are not the authoritative source of the semantics they carry.

### 2. Template Surfaces Should Track Distinct Concept Families

The generic template layer should distinguish at least these surfaces:

- parent-agent templates
- specialist-agent templates
- skill templates
- role-projection templates when a runtime needs explicit role-facing surfaces
- mode templates
- protocol templates
- runtime-guidance templates for surrounding operational instructions
- configuration templates when a runtime needs structured non-behavioral
  settings

Projects may refine which of those surfaces are needed, but they should avoid
collapsing unrelated concepts into one catch-all template type too early.

### 3. Templates Must Stay Platform-Agnostic

The generic template layer should describe what kind of projection exists, not
which platform-specific filename or folder shape later hosts it.

That means a template type should remain valid even if two environments
materialize it very differently.

### 4. Templates Sit Between Authoritative Meaning And Runtime Files

Templates belong conceptually between:

- authoritative semantics
- concrete runtime-facing assets

They are the layer where a system says, "This class of runtime-facing artifact
should exist," before saying, "Here is where platform X stores it."

### 5. Templates Should Remain Traceable To Upstream Layers

A reviewer should be able to tell:

- which authoritative source a template draws from
- whether the template expresses portable canon, project binding, or both
- which later runtime asset type the template is meant to support

### 6. Template Types Should Carry Explicit Information Contracts

Each generic template type should define what information it must carry before
that template is projected into a platform-specific file layout.

Those contracts belong in a portable template-contract surface rather than
being rediscovered independently by each platform binding.

### 7. Template Types Stay Upstream Of Discovery Mechanics

Template types should remain defined in terms of the concept family they
project, not in terms of the folder, filename, or registry mechanism that a
later environment uses to discover them.

Downstream bindings may map one or more template types into concrete discovery
surfaces, but that mapping should not replace the upstream template
vocabulary.

## Constraints

- Templates must not replace authoritative canon or bindings.
- Template types should remain broad enough to map to multiple environments.
- Template inventory should stay concept-shaped rather than folder-shaped.
- Template definitions should remain valid even when later environments satisfy
  discovery through manifests, indexes, or mixed layouts instead of folders.

## Non-Goals

- Define per-platform filenames or directories.
- Define traceability metadata in full.
- Define regeneration behavior in full.

## Related Artifacts

- [Platform Materialization Model](./Platform-Materialization-Model.md)
- [Materialization Boundary Model](./Materialization-Boundary-Model.md)
- [Generic Template Contracts](./Templates/README.md)
- [Role Archetypes README](./RoleArchetypes/README.md)
- [Protocols README](./Protocols/README.md)
