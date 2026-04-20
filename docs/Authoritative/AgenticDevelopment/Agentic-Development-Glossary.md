---
id: craig-agentic-development-glossary
title: Agentic Development Glossary
summary: Defines the portable vocabulary for agentic-development concepts so downstream bindings and materializations can build on shared terms.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, glossary, canon, portability]
related:
  - ./Agent-Authority-Model.md
  - ./Mode-Model.md
  - ./Skill-Contract.md
  - ./Boundary-Model.md
  - ./Platform-Materialization-Model.md
  - ../Architecture/Craig-Architecture.md
  - ../Ontology/Documentation-Ontology.md
supersedes: []
---

# Agentic Development Glossary

## Purpose

Define the portable vocabulary for agentic development so downstream bindings
and materializations can build on one stable set of terms.

This glossary is intentionally environment-agnostic and application-agnostic. It
defines concepts, not any application's chosen instantiations of those
concepts.

## Scope

This document governs the meanings of the core agentic-development terms that
will recur across the wider `AgenticDevelopment` canon.

It covers the portable definitions for agents, roles, protocols, modes,
skills, delegation, handoff, escalation, execution capacity, and
materialization.

It does not choose any application's actual role set, mode set, protocol set,
or execution environment.

## Binding Decisions

- `Agent`: a defined actor in an agentic-development system.
- `Parent agent`: an accountable agent that embodies a role, follows
  protocols, enters modes while executing those protocols, and may delegate
  bounded work to specialists.
- `Specialist`: a focused agent with bounded authority and curated skills that
  performs a narrow delegated scope on behalf of a parent agent.
- `Role`: the accountability concept an agent embodies.
- `Protocol`: the workflow path that governs entry conditions, gates, required
  outputs, handoffs, and exit criteria.
- `Mode`: the execution state an agent is currently operating in while
  following a protocol.
- `Skill`: an atomic reusable capability unit used by a parent agent or
  specialist to perform bounded work.
- `Delegation`: the bounded assignment of work from one agent to another
  without automatically transferring overall accountability.
- `Handoff`: an explicit transfer of workflow ownership from one eligible actor
  to another according to a protocol.
- `Escalation`: the return of a decision, risk, exception, or blocked state to
  a broader authority boundary.
- `Execution capacity`: the planning-time description of how many independent
  execution slots are available to pick up work.
- `Application binding`: the layer that declares which portable concepts a
  specific application actually uses.
- `Execution environment`: the environment whose discovery rules and file
  conventions receive materialized assets.
- `Materialization`: the process of expressing portable and application-bound
  agentic definitions as environment-facing files, folders, prompts,
  templates, or other discoverable assets.
- `Materialized asset`: a concrete environment-facing artifact produced
  through materialization.

## Constraints

- Terms in this glossary should remain portable across execution environments
  rather than drifting toward one environment's file layout or discovery
  rules.
- Application-specific role names, current workflow gates, current capacity
  values, and environment-specific conventions do not belong in this glossary.
- Definitions here must distinguish accountability (`role`), workflow
  structure (`protocol`), execution state (`mode`), and reusable capability
  (`skill`) rather than allowing those concepts to collapse into one another.
- This glossary must not encode concrete role names, mode names, workflow
  gates, or environment conventions from any specific application.
- Materialized assets are not defined here as source-of-truth artifacts; they
  are downstream expressions of higher-level canon and bindings.

## Non-Goals

- Choose an application's initial role set or specialist roster.
- Define a specific application's current workflow protocol set.
- Pick an environment-specific folder layout or prompt format.
- Describe live execution scheduling, orchestration, or worker discovery.

## Related Artifacts

- [Agent-Authority-Model.md](./Agent-Authority-Model.md)
- [Craig-Architecture.md](../Architecture/Craig-Architecture.md)
- [Documentation-Ontology.md](../Ontology/Documentation-Ontology.md)
