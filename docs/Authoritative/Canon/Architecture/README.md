# Architecture

This directory holds the reusable Craig Architecture canon for Context Atlas.

These documents are intentionally more general than the project-specific artifacts under [`docs/Authoritative/Identity`](../../Identity/). They define the architectural philosophy, implementation guidance, AI-collaboration rules, planning/decomposition model, and local `__ai__.md` contract shape that downstream projects can copy and adapt.

The neighboring runtime-agnostic agentic-development canon lives under
[`docs/Authoritative/Canon/AgenticDevelopment`](../AgenticDevelopment/README.md).
When a change concerns agent roles, modes, skills, protocols, or runtime
materialization concepts, contributors should read that set alongside Craig
Architecture rather than forcing those concepts into the architecture docs.

In practice:

- Craig Architecture explains reusable architectural philosophy and delivery
  governance
- AgenticDevelopment explains reusable agentic vocabulary, authority,
  boundaries, and materialization concepts

## What Lives Here

- [Craig-Architecture.md](./Craig-Architecture.md): the core language-agnostic Craig Architecture philosophy
- [Craig-Architecture-Planning-And-Decomposition.md](./Craig-Architecture-Planning-And-Decomposition.md): the canonical planning and decomposition supplement for `Epic -> Story -> Task -> PR`
- [Craig-Architecture-Python.md](./Craig-Architecture-Python.md): the Python-specific implementation companion
- [Craig-Architecture-AI-Guidance.md](./Craig-Architecture-AI-Guidance.md): the operational supplement for AI contributors and reviewers
- [Craig-Architecture-__ai__-Template.md](./Craig-Architecture-__ai__-Template.md): the canonical local `__ai__.md` template guidance
- [example_ci_scripts](./example_ci_scripts/README.md): example enforcement scripts and workflow patterns for `__ai__.md` governance

## How To Read This Set

For most contributors, the recommended order is:

1. [Craig-Architecture.md](./Craig-Architecture.md)
2. [Craig-Architecture-Planning-And-Decomposition.md](./Craig-Architecture-Planning-And-Decomposition.md)
3. [Craig-Architecture-AI-Guidance.md](./Craig-Architecture-AI-Guidance.md)
4. the relevant language supplement, such as [Craig-Architecture-Python.md](./Craig-Architecture-Python.md)
5. [Craig-Architecture-__ai__-Template.md](./Craig-Architecture-__ai__-Template.md) when authoring or reviewing local owner files

## What Does Not Live Here

This directory should stay focused on reusable architectural canon.

Project-specific identity, mission, scope, and first-class system definition belong under [`docs/Authoritative/Identity`](../../Identity/). Forward-looking work decomposition belongs under [`docs/Planning`](../../../Planning/), but should derive its shape from [Craig-Architecture-Planning-And-Decomposition.md](./Craig-Architecture-Planning-And-Decomposition.md).
