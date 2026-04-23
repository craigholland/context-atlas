# Documentation

This directory holds the canonical project documentation for Context Atlas.

Use the entry surfaces intentionally:

- the root [README](../README.md) is the repo-wide map
- this file is the documentation route splitter
- [docs/Guides/README.md](./Guides/README.md) is the product guide hub

## Pick Your Route

If you are here to evaluate or set up Context Atlas as a product, start with
the product route first.

If you are here to contribute docs, inspect the Canon/Identity layers, or
understand the repo's runtime/governance model, use the contributor and
architecture routes further down this page.

## Product Route

User-facing setup and workflow help lives under
[docs/Guides/README.md](./Guides/README.md).

If you are trying to evaluate or wire Context Atlas into a workflow, start
there before reading deeper planning, canon, identity, or governance docs.
Use the root [README](../README.md) instead if you want the full repo map
before choosing a documentation route.

If you want runnable companion artifacts after the guide path, continue to
[examples/README.md](../examples/README.md).

## Release Notes

In-repo release summaries live under [docs/Release/README.md](./Release/README.md).

Those artifacts are the repository home for `releases`-class product summaries
such as shipped-version notes, operational release state, and versioned product
history. They are shipped-history context, not the main current setup route.

## Contributing Docs

If you are trying to add or update a document correctly, start with
[CONTRIBUTING.md](../CONTRIBUTING.md) and then continue into the ontology docs
linked below.

## Exploratory Notes

Non-binding investigations and speculative pickup points now live under
[docs/Exploratory/README.md](./Exploratory/README.md).

Use that surface when something is worth capturing so it is not lost, but is
not yet ready to become authoritative truth or forward-looking execution
planning.

The reusable top-tier canon is now grouped under
[docs/Authoritative/Canon/README.md](./Authoritative/Canon/README.md), while
Context Atlas-specific bindings remain under
[docs/Authoritative/Identity/](./Authoritative/Identity/).

## Contributor And Architecture Routes

If you are trying to inspect the repo's generated runtime surface or the
project-specific Codex binding, treat that as a contributor/architecture route
too. Those materials explain how this repository operationalizes its agentic
model; they are not required to evaluate Atlas as a library.

Use these links intentionally:

- portable agentic canon: [docs/Authoritative/Canon/AgenticDevelopment/README.md](./Authoritative/Canon/AgenticDevelopment/README.md)
- project-specific Codex binding: [docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md](./Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md)
- Codex refresh and drift-check workflow: [creation_guidance.md](./Authoritative/Identity/AgenticDevelopment/Materializations/Codex/creation_guidance.md) and [governance.md](./Authoritative/Identity/AgenticDevelopment/Materializations/Codex/governance.md)
- repo-governance entry surface: [README.md](../README.md) and [__ai__.md](../__ai__.md)

If you are changing generated Codex runtime inputs or the repo's governance
model, start from these contributor-owned surfaces instead of the product
guides or the root README's product route.

Before creating or editing project documents, start with [docs/Authoritative/Canon/Ontology/README.md](./Authoritative/Canon/Ontology/README.md). It contains the current guidance for how project documents should be structured, including the shared metadata template and the class-specific content templates.

The canonical semantic definitions for the document classes now live in [docs/Authoritative/Canon/Ontology/Documentation-Ontology.md](./Authoritative/Canon/Ontology/Documentation-Ontology.md). That document defines what `Authoritative`, `Planning`, `Reviews`, `Exploratory`, and `Releases` actually mean, what they are safe to use for, and how they should interact when they disagree.

The canonical definition of project mission, scope, and strategic boundaries now lives in [docs/Authoritative/Identity/Context-Atlas-Charter.md](./Authoritative/Identity/Context-Atlas-Charter.md). The project-specific operational model now lives in [docs/Authoritative/Identity/Context-Atlas-System-Model.md](./Authoritative/Identity/Context-Atlas-System-Model.md).

The reusable Craig Architecture canon now has its own directory index at [docs/Authoritative/Canon/Architecture/README.md](./Authoritative/Canon/Architecture/README.md). Contributors looking for the architecture set as a whole should start there before diving into individual supplements.

The reusable, runtime-agnostic agentic-development canon now has its own
directory index at [docs/Authoritative/Canon/AgenticDevelopment/README.md](./Authoritative/Canon/AgenticDevelopment/README.md).
Contributors working on roles, modes, skills, protocols, or runtime
materialization should start there before writing project-specific bindings or
runtime assets.

The project-specific Codex runtime binding lives under
[docs/Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md](./Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md).
Use that route if you intentionally want the generated-runtime and
materialization layer rather than the product setup path.

The reusable repo-management canon now has its own directory index at
[docs/Authoritative/Canon/RepoManagement/README.md](./Authoritative/Canon/RepoManagement/README.md).
Contributors working on repository principals, permissions, branch-target
policy, review surfaces, or audit identities should start there before writing
project-specific provider bindings.

That order matters:

- `AgenticDevelopment` defines portable concepts and boundaries
- `RepoManagement` defines portable repository-operation concepts and
  boundaries
- `Identity` defines what Context Atlas actually chooses to use from both
  portable surfaces
- `Planning` defines how we intend to deliver those choices

The canonical planning and decomposition reference now lives in [docs/Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md](./Authoritative/Canon/Architecture/Craig-Architecture-Planning-And-Decomposition.md). Project planning artifacts under [docs/Planning](./Planning/) should derive their decomposition model from that document, while completed planning stacks now live under [docs/Planning/completed](./Planning/completed/).

The intended documentation ontology is:

- `Authoritative` for binding project truth
- `Planning` for forward-looking execution intent
- `Reviews` for findings, evidence, and assessments
- `Exploratory` for speculative investigation and prototypes
- `Releases` for operational and release-history context

This file exists to separate the main documentation routes cleanly:

- product-facing setup and workflow help
- contributor-facing document authoring help
- Canon and Identity architecture reading
- exploratory, planning, and release-history support surfaces

