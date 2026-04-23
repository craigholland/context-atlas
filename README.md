# Context Atlas

Context Atlas is a standalone context-governance and context-assembly engine
for Codex-powered systems and other provider-agnostic applications.

It exists to answer questions such as:

- What information should actually enter model context?
- Under what authority and trust rules should it be used?
- How should limited context budget be allocated?
- What should be retained, compressed, transformed, or excluded?
- How should inclusion decisions remain auditable and reproducible?

## Mental Model

Context Atlas takes one or more governed source inputs, applies authority,
retrieval, ranking, memory, budgeting, compression, and assembly rules, and
produces:

- a `ContextPacket`
- a `ContextTrace`
- derived rendered views over those artifacts

The goal is not just retrieval. The goal is governed, reproducible,
inspectable context decisions.

## Status

This repository has completed its initial architecture and governance bootstrap
and now carries an explicit `MVP Ready` recommendation in
[docs/Reviews/MVP/mvp_readiness_assessment.md](/context-atlas/docs/Reviews/MVP/mvp_readiness_assessment.md).

The `0.1.3` release packages the first post-hardening documentation and
runtime-governance refinement pass. It keeps the hardened shared-engine
contracts introduced in `0.1.2`, but makes the repository easier to approach
by separating the repo README's map from the deeper product tour and by
strengthening the manifest-driven Codex runtime materialization loop.

Important outward-facing truths that are now settled:

- repeated lexical retrieval reuses shared index state instead of rebuilding
  the whole TF-IDF picture on every query
- ranking and memory now share one bounded duplicate-handling baseline for
  Atlas-owned text
- starter token estimation is shape-aware by default instead of assuming one
  flat ratio for all content
- packet and trace inspection now prefer truthful budget and compression
  vocabulary
- the root README is now a layered entry surface, while the deeper walkthrough
  lives under `docs/Guides/context_atlas_tour.md`
- generated Codex runtime assets are now manifest-driven, regenerable, and
  drift-checked through preflight and CI

The in-repo release-history index lives at
[docs/Release/README.md](/context-atlas/docs/Release/README.md). The current
shipped release summary is
[docs/Release/release_0_1_3.md](/context-atlas/docs/Release/release_0_1_3.md).

## Start Here

Project Context Atlas is evolving along a few different fronts, which makes
this repository denser than a typical library repo. You do not need to absorb
all of them at once. Pick the path that matches what you care about most right
now:

This file is the repo map. If you want the documentation-only route splitter,
use [docs/README.md](/context-atlas/docs/README.md). If you already know you
want the product guide hub, use
[docs/Guides/README.md](/context-atlas/docs/Guides/README.md).

1. **The Context Atlas product itself**

   Use this route if you are here to evaluate Atlas as a library or try the
   current starter product path. You do not need `.codex/`,
   `.agents/skills/`, or `__ai__.md` to follow this route.

   Start with:
   - [docs/Guides/README.md](/context-atlas/docs/Guides/README.md)
   - [docs/Guides/getting_started.md](/context-atlas/docs/Guides/getting_started.md)
   - [docs/Guides/context_atlas_tour.md](/context-atlas/docs/Guides/context_atlas_tour.md)
   - [docs/Release/README.md](/context-atlas/docs/Release/README.md)

2. **The derived AgenticDevelopment components**

   Use this route if you want to inspect the repo's generated runtime surface
   and the upstream bindings that produce it.

   Start with:
   - [docs/Authoritative/Canon/AgenticDevelopment/README.md](/context-atlas/docs/Authoritative/Canon/AgenticDevelopment/README.md)
   - [docs/Authoritative/Identity/AgenticDevelopment/](/context-atlas/docs/Authoritative/Identity/AgenticDevelopment/)
   - [`.codex/`](/context-atlas/.codex/)
   - [`.agents/skills/`](/context-atlas/.agents/skills/)

3. **The Canon / Identity / operationalization architecture**

   Use this route if you want the project architecture and binding model rather
   than the product setup path.

   Start with:
   - [docs/README.md](/context-atlas/docs/README.md)
   - [docs/Authoritative/Canon/README.md](/context-atlas/docs/Authoritative/Canon/README.md)
   - [docs/Authoritative/Identity/](/context-atlas/docs/Authoritative/Identity/)
   - [Context Atlas Agentic Development Profile](/context-atlas/docs/Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md)

4. **The `__ai__.md` architectural governance and enforcement system**

   Use this route if you are here to understand or change the repo's
   contribution-governance model.

   Start with:
   - [`__ai__.md`](/context-atlas/__ai__.md)
   - [`__ai__.template.md`](/context-atlas/__ai__.template.md)
   - [`scripts/validate_ai_docs.py`](/context-atlas/scripts/validate_ai_docs.py)
   - [`scripts/check_ai_docs.py`](/context-atlas/scripts/check_ai_docs.py)
   - [`scripts/ai_verify_contracts.py`](/context-atlas/scripts/ai_verify_contracts.py)
   - [`.github/workflows/`](/context-atlas/.github/workflows/)

5. **I recently gave you a code review and you've come to rain down fiery vengeance upon me**

   Start with the area you disagree with most, then ask your AI client for the
   strongest honest critique it can make.

### AI-Assisted Review

If you want an AI client to help you review this repo honestly, use:

- the [latest GitHub release](https://github.com/craigholland/context-atlas/releases/latest)
  if you want to critique shipped behavior rather than in-progress branch work
- your current checkout of `development` if you want to critique the latest
  evolving product, canon, runtime, or governance work

Then point the AI at the specific surface you care about instead of asking it
to summarize the whole repository at once.

Suggested prompts:

- **Product**
  ```text
  Review this repository as a product evaluator. Focus on the user-facing setup path,
  guides, examples, and release notes. Be critical and honest. Tell me what is clear,
  what is confusing, and what would block adoption.
  ```
- **AgenticDevelopment**
  ```text
  Review the agentic-development layer in this repository. Focus on roles, modes,
  protocols, skills, specialists, manifest-driven materialization, and generated
  Codex runtime assets. Be critical and tell me where the model is strong,
  under-specified, or over-engineered.
  ```
- **Canon / Identity / operationalization**
  ```text
  Review how this repository separates portable canon, Context Atlas-specific
  identity bindings, and runtime operationalization/materialization. Be skeptical
  and tell me where the boundaries are clean versus where they still leak.
  ```
- **`__ai__` governance**
  ```text
  Review the `__ai__.md` governance system in this repository. Focus on owner-file
  scope, freshness checks, verification contracts, and CI enforcement. Be honest
  about whether it improves governance or creates unnecessary process overhead.
  ```
- **Fiery vengeance**
  ```text
  My own project got a critically-poignant review from this repo's author. Do
  a full, brutally honest audit and highlight any areas that are misguided,
  brittle, overstated, incomplete or evidence that this guy is a complete
  fraud.
  ```

## Guides And Contributing

The guides remain the primary user-facing help surface for product evaluation.
The `examples/` directory contains runnable companion artifacts, sample
payloads, and proof inputs that support the guides rather than replacing them.

If you are evaluating Atlas as a product or library, you can stop at the guide
and example surfaces. The generated Codex runtime and the repo's `__ai__.md`
governance model are contributor-facing layers, not prerequisites for the
product path.

If you are contributing documentation or authoritative canon, start with
[CONTRIBUTING.md](/context-atlas/CONTRIBUTING.md) before authoring a new file.

If you change Codex materialization inputs under the authoritative canon or
Identity bindings, refresh the generated runtime surface with
`py -3 scripts/materialize_codex_runtime.py --write` and verify it with
`py -3 scripts/check_codex_materialization.py` before pushing.

## Principles

- Standalone and reusable
- Provider-agnostic, while explicitly supporting Codex-powered systems
- Craig Architecture from day one
- Canonical structured packets before prompt rendering
- Authority-aware context governance, not just retrieval

## Initial Repository Layout

- `docs/` for project documentation, product-facing guides, and documentation
  ontology
- `src/context_atlas/` for the package source
- `tests/` for automated tests
- `examples/` for runnable companion artifacts, sample payloads, and
  demonstrations

## Current Product Surface

The current product-facing surface is intentionally narrow and explicit:

- a package-facing starter path through
  `context-atlas-starter` and
  [docs/Guides/getting_started.md](/context-atlas/docs/Guides/getting_started.md)
- two currently supported source families:
  - governed filesystem documents
  - already-fetched structured records
- three supported workflow surfaces:
  - [Codex Repository Workflow](/context-atlas/docs/Guides/codex_repository_workflow.md)
  - [Documents Plus Database Workflow](/context-atlas/docs/Guides/docs_database_workflow.md)
  - [Low-Code Workflow](/context-atlas/docs/Guides/low_code_workflow.md)
- canonical outputs:
  - `ContextPacket`
  - `ContextTrace`
  - rendered context, packet inspection, and trace inspection views

## Atlas Boundaries

Atlas currently owns:

- canonical source shaping and translation into `ContextSource`
- retrieval, ranking, budgeting, compression, and memory policies
- packet assembly and trace production
- derived inspection views over canonical packet and trace artifacts

Atlas currently does **not** own:

- database connections, queries, vector-store clients, or ORM sessions
- general-purpose connectors or connector lifecycle management
- git history ingestion, issue-system integration, or broad code crawling
- a visual builder or broad no-code orchestration surface

Those boundaries are part of the product truth, not temporary hand-waving.

## Tour And Workflow Guides

This README is the map. If you want the tour, start with:

- [Context Atlas Tour](/context-atlas/docs/Guides/context_atlas_tour.md)

Then drop into the workflow guide that matches the path you care about:

- [Getting Started](/context-atlas/docs/Guides/getting_started.md)
- [Codex Repository Workflow](/context-atlas/docs/Guides/codex_repository_workflow.md)
- [Documents Plus Database Workflow](/context-atlas/docs/Guides/docs_database_workflow.md)
- [Low-Code Workflow](/context-atlas/docs/Guides/low_code_workflow.md)

For proof and review surfaces, start with:

- [docs/Reviews/MVP/mvp_readiness_assessment.md](/context-atlas/docs/Reviews/MVP/mvp_readiness_assessment.md)
- [examples/mvp_proof/README.md](/context-atlas/examples/mvp_proof/README.md)

## License

MPL-2.0
