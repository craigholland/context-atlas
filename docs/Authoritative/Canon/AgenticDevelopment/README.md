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

If you need the current repository's concrete application binding or runtime
target after learning the portable model, descend into the downstream Identity
layer rather than trying to infer those choices from the canon.

## Why This Matters Here

Projects that care about governed AI collaboration eventually run into the same
question: should roles, review gates, handoffs, and runtime-facing agent assets
be treated as ad hoc tool habits, or as concepts that can be defined and
reviewed upstream first?

This canon takes the second approach. Instead of treating those behaviors as
tool-specific prompt folklore, it makes them portable governed concepts that
can be reviewed before any one project or runtime binds them concretely.

## Start Here

If you are new to the agentic-development model, start with this README before
reading the individual canon documents.

The intended progression is:

1. understand what this directory is responsible for
2. build a quick mental picture of the main entities
3. learn the portable vocabulary
4. learn the invariant relationship and boundary rules
5. only then move into downstream binding or materialization guidance

If you want the shortest "Agentic Entities for Dummies" version first, read
[Quick-Mental-Model.md](./Quick-Mental-Model.md) before the glossary and the
deeper model docs.

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

- [Quick-Mental-Model.md](./Quick-Mental-Model.md)
- [Agentic-Development-Glossary.md](./Agentic-Development-Glossary.md)
- [RoleArchetypes/README.md](./RoleArchetypes/README.md)
- [Skills/README.md](./Skills/README.md)
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
- [SpecialistArchetypes/README.md](./SpecialistArchetypes/README.md)
- [Boundary-Model.md](./Boundary-Model.md)
- [Materialization-Boundary-Model.md](./Materialization-Boundary-Model.md)
- [Platform-Materialization-Model.md](./Platform-Materialization-Model.md)
- [Template-Model.md](./Template-Model.md)
- [Templates/README.md](./Templates/README.md)
- [Discovery-Model.md](./Discovery-Model.md)
- [Materialization-Traceability-Model.md](./Materialization-Traceability-Model.md)
- [Drift-Model.md](./Drift-Model.md)
- [Validation-Model.md](./Validation-Model.md)
- [Change-Management-Model.md](./Change-Management-Model.md)

## How To Read This Set

For most readers, the intended order is:

1. this README
2. [Quick-Mental-Model.md](./Quick-Mental-Model.md)
3. [Agentic-Development-Glossary.md](./Agentic-Development-Glossary.md)
4. [RoleArchetypes/README.md](./RoleArchetypes/README.md)
5. [Agent-Authority-Model.md](./Agent-Authority-Model.md)
6. [Delegation-Model.md](./Delegation-Model.md)
7. [Agent-Composition-Model.md](./Agent-Composition-Model.md)
8. [Mode-Model.md](./Mode-Model.md)
9. [Protocols/README.md](./Protocols/README.md)
10. [Runtime-Capacity-Model.md](./Runtime-Capacity-Model.md)
11. [Parallel-Decomposition-Model.md](./Parallel-Decomposition-Model.md)
12. [Skill-Contract.md](./Skill-Contract.md)
13. [Skills/README.md](./Skills/README.md)
14. [Skill-Attachment-Model.md](./Skill-Attachment-Model.md)
15. [Composition-Decision-Model.md](./Composition-Decision-Model.md)
16. [Escalation-Model.md](./Escalation-Model.md)
17. [SpecialistArchetypes/README.md](./SpecialistArchetypes/README.md)
18. [Boundary-Model.md](./Boundary-Model.md)
19. [Materialization-Boundary-Model.md](./Materialization-Boundary-Model.md)
20. [Platform-Materialization-Model.md](./Platform-Materialization-Model.md)
21. [Template-Model.md](./Template-Model.md)
22. [Templates/README.md](./Templates/README.md)
23. [Discovery-Model.md](./Discovery-Model.md)
24. [Materialization-Traceability-Model.md](./Materialization-Traceability-Model.md)
25. [Drift-Model.md](./Drift-Model.md)
26. [Validation-Model.md](./Validation-Model.md)
27. [Change-Management-Model.md](./Change-Management-Model.md)

This ordering is intentional:

- the README explains the purpose and scope of the canon surface
- the quick mental model gives new readers a short human-readable picture of
  the main entities before the deeper vocabulary and invariants begin
- the glossary defines the vocabulary
- the role-archetype catalog provides reusable professional role templates that
  downstream bindings may refine
- the skill contract defines what a portable skill is allowed to mean before
  any one project chooses a skill roster
- the skill catalog then provides reusable atomic capabilities that downstream
  bindings may adopt and attach without redefining those capabilities from
  scratch
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
- the later skill-attachment doc then refines how those skills attach to
  parent agents and specialists without becoming role or protocol surrogates
- the composition-decision and escalation docs define when work should stay
  parent-owned, become a skill addition, or justify a bounded specialist
- the specialist-archetype catalog then shows how curated delegated actors may
  be composed from portable skills without redefining specialist patterns
  project by project
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
- the drift, validation, and change-management docs then define how later
  bindings and runtime assets should be checked, reviewed, recovered, and
  evolved without inventing a second governance vocabulary elsewhere

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

## When To Leave Canon

Stay in this directory while you are still learning portable concepts such as
roles, parent agents, specialists, skills, modes, protocols, and
materialization boundaries.

Leave this directory when you need to answer project-specific questions such
as:

- which role roster a project actually chose
- which parent agents and specialists currently exist
- which modes and protocols that project bound
- which runtime environment the project currently materializes first

In this repository, the normal downstream path is:

1. [Context Atlas Agentic Development Profile](../../Identity/Context-Atlas-Agentic-Development-Profile.md)
2. the relevant Context Atlas binding docs and
   [`materialization_manifest.yaml`](../../Identity/AgenticDevelopment/materialization_manifest.yaml)
3. [Context Atlas Codex Binding](../../Identity/AgenticDevelopment/Materializations/Codex/README.md)

That path keeps the canon portable while still giving readers a clear route to
the current repository's concrete choices.

## Neighboring Canon

The most relevant adjacent authoritative surfaces are:

- [../Architecture/README.md](../Architecture/README.md): reusable architectural
  philosophy, planning/decomposition guidance, and AI-collaboration rules
- [../Ontology/README.md](../Ontology/README.md): metadata and document-class
  guidance for authoring authoritative artifacts

When deciding where to read next:

- stay in this directory if you are still learning the portable concepts
- move to a binding layer only when you need concrete application choices
- in this repository, start that descent with the
  [Context Atlas Agentic Development Profile](../../Identity/Context-Atlas-Agentic-Development-Profile.md)
  then use the relevant binding docs and
  [`materialization_manifest.yaml`](../../Identity/AgenticDevelopment/materialization_manifest.yaml)
  before reading the current
  [Codex binding](../../Identity/AgenticDevelopment/Materializations/Codex/README.md)
- move to planning only after the portable canon is clear enough that planning
  docs do not have to redefine it
