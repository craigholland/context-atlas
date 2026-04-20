# Agentic Development

This directory holds the portable, runtime-agnostic agentic-development canon
for Context Atlas.

These documents are intentionally more general than the project-specific
artifacts that will later bind the canon to Context Atlas's chosen roles,
modes, protocols, runtime-capacity inputs, and platform materializations.

This set should be read alongside the reusable Craig Architecture canon, not as
an isolated prompt bundle or runtime-specific helper surface.

The portable canon ends where project-specific bindings begin. This directory
defines portable terms and invariants, not Context Atlas's chosen role roster,
workflow gates, runtime-capacity values, or vendor-specific layouts.

## What Lives Here

This surface should define portable concepts and invariant rules such as:

- core terminology for agents, roles, specialists, modes, skills, protocols,
  delegation, handoff, escalation, runtime capacity, and materialization
- stable authority and relationship rules
- portable mode semantics
- portable skill semantics
- portable boundary rules between canon, project bindings, and runtime assets
- portable materialization concepts that remain valid across AI environments

The initial Story 1 surface is centered on:

- [Agentic-Development-Glossary.md](./Agentic-Development-Glossary.md)
- [Agent-Authority-Model.md](./Agent-Authority-Model.md)
- [Mode-Model.md](./Mode-Model.md)
- [Skill-Contract.md](./Skill-Contract.md)
- [Boundary-Model.md](./Boundary-Model.md)
- [Platform-Materialization-Model.md](./Platform-Materialization-Model.md)

## How To Read This Set

For most readers, the intended order is:

1. this README
2. [Agentic-Development-Glossary.md](./Agentic-Development-Glossary.md)
3. [Agent-Authority-Model.md](./Agent-Authority-Model.md)
4. [Mode-Model.md](./Mode-Model.md)
5. [Skill-Contract.md](./Skill-Contract.md)
6. [Boundary-Model.md](./Boundary-Model.md)
7. [Platform-Materialization-Model.md](./Platform-Materialization-Model.md)

This ordering is intentional:

- the README explains the purpose and scope of the canon surface
- the glossary defines the vocabulary
- the authority model defines the invariant relationship chain built on that
  vocabulary
- the later supplements refine adjacent concerns without replacing those
  foundations

## What Does Not Live Here

This directory should not be used for:

- Context Atlas's chosen role roster
- Context Atlas's chosen mode set
- Context Atlas's chosen protocol set
- current runtime-capacity numbers for this repo
- vendor-specific discovery folders, prompts, config files, or platform naming
  conventions

Those concerns belong in downstream project-specific bindings and
runtime-specific materialization guidance, not in the portable canon.

## Neighboring Canon

The most relevant adjacent authoritative surfaces are:

- [../Architecture/README.md](../Architecture/README.md): reusable architectural
  philosophy, planning/decomposition guidance, and AI-collaboration rules
- [../Identity/Context-Atlas-System-Model.md](../Identity/Context-Atlas-System-Model.md):
  the project-specific operational model for Context Atlas, including
  downstream project choices that do not belong in the portable canon
- [../Ontology/README.md](../Ontology/README.md): metadata and document-class
  guidance for authoring authoritative artifacts
