# Agentic Development

This directory holds the portable, environment-agnostic agentic-development canon.

These documents are intentionally more general than the binding-layer artifacts
that later choose concrete roles, modes, protocols, capacity inputs, and
environment materializations.

This set should be read alongside the reusable Craig Architecture canon, not as
an isolated prompt bundle or environment-specific helper surface.

The portable canon ends where binding-layer documents begin. This directory
defines portable terms and invariants, not an application's chosen role
roster, workflow gates, capacity values, or environment-specific layouts.

## Start Here

If you are new to the agentic-development model, start with this README before
reading the individual canon documents.

The intended progression is:

1. understand what this directory is responsible for
2. learn the portable vocabulary
3. learn the invariant relationship and boundary rules
4. only then move into downstream binding or materialization guidance

## What Lives Here

This surface should define portable concepts and invariant rules such as:

- core terminology for agents, roles, specialists, modes, skills, protocols,
  delegation, handoff, escalation, execution capacity, and materialization
- stable authority and relationship rules
- portable mode semantics
- portable protocol semantics and reusable protocol shapes
- portable skill semantics
- portable boundary rules between canon, application bindings, and materialized
  assets
- portable materialization concepts that remain valid across execution
  environments

The initial canon surface is centered on:

- [Agentic-Development-Glossary.md](./Agentic-Development-Glossary.md)
- [RoleArchetypes/README.md](./RoleArchetypes/README.md)
- [Agent-Authority-Model.md](./Agent-Authority-Model.md)
- [Delegation-Model.md](./Delegation-Model.md)
- [Agent-Composition-Model.md](./Agent-Composition-Model.md)
- [Mode-Model.md](./Mode-Model.md)
- [Protocols/README.md](./Protocols/README.md)
- [Runtime-Capacity-Model.md](./Runtime-Capacity-Model.md)
- [Parallel-Decomposition-Model.md](./Parallel-Decomposition-Model.md)
- [Skill-Contract.md](./Skill-Contract.md)
- [Skill-Attachment-Model.md](./Skill-Attachment-Model.md)
- [Composition-Decision-Model.md](./Composition-Decision-Model.md)
- [Escalation-Model.md](./Escalation-Model.md)
- [Boundary-Model.md](./Boundary-Model.md)
- [Materialization-Boundary-Model.md](./Materialization-Boundary-Model.md)
- [Platform-Materialization-Model.md](./Platform-Materialization-Model.md)
- [Template-Model.md](./Template-Model.md)
- [Templates/README.md](./Templates/README.md)
- [Discovery-Model.md](./Discovery-Model.md)
- [Materialization-Traceability-Model.md](./Materialization-Traceability-Model.md)

## How To Read This Set

For most readers, the intended order is:

1. this README
2. [Agentic-Development-Glossary.md](./Agentic-Development-Glossary.md)
3. [RoleArchetypes/README.md](./RoleArchetypes/README.md)
4. [Agent-Authority-Model.md](./Agent-Authority-Model.md)
5. [Delegation-Model.md](./Delegation-Model.md)
6. [Agent-Composition-Model.md](./Agent-Composition-Model.md)
7. [Mode-Model.md](./Mode-Model.md)
8. [Protocols/README.md](./Protocols/README.md)
9. [Runtime-Capacity-Model.md](./Runtime-Capacity-Model.md)
10. [Parallel-Decomposition-Model.md](./Parallel-Decomposition-Model.md)
11. [Skill-Contract.md](./Skill-Contract.md)
12. [Skill-Attachment-Model.md](./Skill-Attachment-Model.md)
13. [Composition-Decision-Model.md](./Composition-Decision-Model.md)
14. [Escalation-Model.md](./Escalation-Model.md)
15. [Boundary-Model.md](./Boundary-Model.md)
16. [Materialization-Boundary-Model.md](./Materialization-Boundary-Model.md)
17. [Platform-Materialization-Model.md](./Platform-Materialization-Model.md)
18. [Template-Model.md](./Template-Model.md)
19. [Templates/README.md](./Templates/README.md)
20. [Discovery-Model.md](./Discovery-Model.md)
21. [Materialization-Traceability-Model.md](./Materialization-Traceability-Model.md)

This ordering is intentional:

- the README explains the purpose and scope of the canon surface
- the glossary defines the vocabulary
- the role-archetype catalog provides reusable professional role templates that
  downstream bindings may refine
- the authority model defines the invariant relationship chain built on that
  vocabulary
- the delegation and composition docs refine how parent agents and specialists
  stay structurally distinct inside that relationship chain
- the mode and protocol docs define portable execution-state and workflow-path
  semantics before any downstream application binds them to concrete roles,
  gates, or runtime assets
- the runtime-capacity and parallel-decomposition docs define how bounded
  planning capacity should influence safe decomposition before any project or
  environment binding chooses concrete values
- the skill docs refine what a skill may contain and how skills attach to
  parent agents and specialists without becoming role or protocol surrogates
- the composition-decision and escalation docs define when work should stay
  parent-owned, become a skill addition, or justify a bounded specialist
- the later supplements refine adjacent concerns without replacing those
  foundations
- the materialization-boundary and platform-materialization docs then define
  how later runtime-facing assets stay downstream of canon and project
  bindings
- the template model and template-contract surface then define what kinds of
  runtime-facing projections later environments are allowed to use
- the discovery model then defines what later runtime bindings must make
  discoverable before any environment chooses concrete folder conventions or
  indexing strategies
- the traceability model then defines how later runtime assets remain reviewable
  against the canon, bindings, and template surfaces that authorize them

## Why This Surface Comes First

Later binding-layer docs may choose:

- concrete roles
- concrete modes
- concrete protocols
- concrete capacity inputs
- concrete environment materializations

Those later documents should bind to this canon, not redefine it. If a reader
cannot understand the portable layer from this directory alone, later planning
and environment-facing docs will start carrying canon concepts they should be
inheriting instead.

## What Does Not Live Here

This directory should not be used for:

- an application's chosen role roster
- an application's chosen mode set
- an application's chosen protocol set
- current capacity numbers for a specific system
- environment-specific discovery folders, prompts, config files, or naming
  conventions

Those concerns belong in downstream binding-layer docs and
environment-specific materialization guidance, not in the portable canon.

## Neighboring Canon

The most relevant adjacent authoritative surfaces are:

- [../Architecture/README.md](../Architecture/README.md): reusable architectural
  philosophy, planning/decomposition guidance, and AI-collaboration rules
- [../Ontology/README.md](../Ontology/README.md): metadata and document-class
  guidance for authoring authoritative artifacts

When deciding where to read next:

- stay in this directory if you are still learning the portable concepts
- move to a binding layer only when you need concrete application choices
- move to planning only after the portable canon is clear enough that planning
  docs do not have to redefine it
