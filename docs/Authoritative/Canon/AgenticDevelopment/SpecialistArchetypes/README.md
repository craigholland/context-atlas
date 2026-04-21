---
id: craig-specialist-archetypes-readme
title: Specialist Archetypes
summary: Introduces the portable specialist-archetype catalog used by downstream bindings to define bounded delegated actors from curated reusable skills.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-21
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, specialists, archetypes, canon, portability]
related:
  - ../Agent-Composition-Model.md
  - ../Delegation-Model.md
  - ../Skills/README.md
  - ../RoleArchetypes/README.md
supersedes: []
---

# Specialist Archetypes

## Purpose

This directory holds the portable specialist-archetype catalog for agentic
development.

These documents describe reusable delegated actor patterns that downstream
application bindings may instantiate when direct skill attachment to a parent
agent is no longer sufficient.

## Scope

Specialist archetypes describe things like:

- the bounded purpose of a delegated actor pattern
- the curated portable skills that commonly compose it
- the modes and workflows it commonly participates in
- the boundaries that keep it from becoming a second parent-agent layer

They do not define:

- whether a specific application instantiates the specialist
- what authority a specific project grants that specialist
- what runtime name or file path materializes that specialist
- which parent agent invokes it in a particular project

Those choices belong in the downstream identity and materialization layers.

## Current Archetypes

- [planning-and-change-specialist.md](./planning-and-change-specialist.md)
- [python-implementation-specialist.md](./python-implementation-specialist.md)
- [review-and-readiness-specialist.md](./review-and-readiness-specialist.md)
- [delivery-and-recovery-specialist.md](./delivery-and-recovery-specialist.md)

## How To Use This Set

The intended layering is:

1. read the portable composition and delegation docs
2. read the portable skill catalog
3. read the relevant specialist archetype documents in this directory
4. move to downstream bindings only when a project needs to decide whether any
   of these specialists should actually exist

Applications should treat these archetypes as reusable composition patterns,
not as mandatory runtime actors.

## Related Artifacts

- [Agent Composition Model](../Agent-Composition-Model.md)
- [Delegation Model](../Delegation-Model.md)
- [Skills](../Skills/README.md)
- [Role Archetypes](../RoleArchetypes/README.md)
