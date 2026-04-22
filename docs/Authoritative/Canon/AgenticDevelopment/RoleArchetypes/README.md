---
id: craig-role-archetypes-readme
title: Role Archetypes
summary: Introduces the portable role-archetype catalog used by downstream applications to refine project-specific roles without redefining professional role patterns from scratch.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-21
owners: [core]
tags: [agentic-development, roles, archetypes, canon, portability]
related:
  - ../Agentic-Development-Glossary.md
  - ../Agent-Authority-Model.md
  - ../Agent-Composition-Model.md
  - ../Skills/README.md
supersedes: []
---

# Role Archetypes

## Purpose

This directory holds the portable role-archetype catalog for agentic
development.

These documents describe reusable professional role patterns that downstream
applications may refine into project-specific roles. They are portable
archetypes, not active project role rosters.

## Scope

Role archetypes describe things like:

- the common purpose of a role family
- the typical accountabilities that role family carries
- the common boundaries that keep the role from absorbing unrelated work
- the kinds of skills, protocols, or collaboration patterns that often attach
  to that role family

They do not define:

- which roles a specific application uses
- what artifacts a specific repository assigns to those roles
- what authority a specific project grants those roles
- how a specific runtime materializes those roles

Those choices belong in the downstream application-binding layer.

## Current Archetypes

- [planning-decomposition-lead.md](./planning-decomposition-lead.md)
- [backend-staff-engineer.md](./backend-staff-engineer.md)
- [technical-documentation-writer.md](./technical-documentation-writer.md)
- [user-acceptance-tester.md](./user-acceptance-tester.md)
- [quality-assurance-engineer.md](./quality-assurance-engineer.md)
- [devops-engineer.md](./devops-engineer.md)

## How To Use This Set

The intended layering is:

1. read the portable glossary so the role/archetype distinction is clear
2. read the relevant role archetype documents in this directory
3. read the portable skill catalog when you need reusable capabilities that
   often attach to those role families
4. move to the application-binding layer to see which archetypes a project
   refines and how it refines them

Applications should treat these archetypes as reusable starting points, not as
mandatory one-to-one role names.

## Related Artifacts

- [Agentic Development Glossary](../Agentic-Development-Glossary.md)
- [Agent Authority Model](../Agent-Authority-Model.md)
- [Agent Composition Model](../Agent-Composition-Model.md)
- [Skills](../Skills/README.md)
