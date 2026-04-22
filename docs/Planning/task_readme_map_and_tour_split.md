---
id: context-atlas-task-readme-map-and-tour-split
title: Task - README Map And Tour Separation PR Plan
summary: Defines the small follow-up execution plan for turning the repo README into a clearer layered entry surface that stays the map, while moving deeper walkthrough content into linked guide material.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-22
owners: [core]
tags: [planning, task, readme, docs, onboarding, information-architecture]
related:
  - ./README.md
  - ../../README.md
  - ../Guides/README.md
  - ../Guides/getting_started.md
  - ../Guides/docs_database_workflow.md
  - ../Guides/low_code_workflow.md
  - ../Release/README.md
  - ../Reviews/MVP/mvp_readiness_assessment.md
  - ../../__ai__.md
supersedes: []
---

# Task - README Map And Tour Separation PR Plan

## Objective

Reframe the repo-level [README](../../README.md) so it behaves more clearly as
the repository's map:

- keep the high-level product framing
- keep the `Start Here` section and audience routing
- keep the AI-assisted review guidance
- keep a truthful but lighter current-state summary
- reduce the amount of deep workflow, adapter, and operational-tour content
  that a new reader is implicitly asked to digest before they know where to go

This Task is not a request to gut the README. The goal is to preserve its
strong voice, honesty, and differentiated framing while layering the material
more intentionally.

## Task Status

PLANNED

## Inputs

- the current repo-level [README](../../README.md)
- the current product-facing guide entrypoint at [docs/Guides/README.md](../Guides/README.md)
- the current getting-started path at [docs/Guides/getting_started.md](../Guides/getting_started.md)
- the current mixed-source and low-code guides:
  - [docs_database_workflow.md](../Guides/docs_database_workflow.md)
  - [low_code_workflow.md](../Guides/low_code_workflow.md)
- the current release-history surface at [docs/Release/README.md](../Release/README.md)
- the current MVP review anchor at [mvp_readiness_assessment.md](../Reviews/MVP/mvp_readiness_assessment.md)
- the repo-level owner contract at [__ai__.md](../../__ai__.md)

## Proposed Work

### PR - A: Layer The README As A True Entry Surface

- add one short explicit `Mental Model` section near the top so new readers can
  understand Atlas in one minute before encountering denser workflow detail
- compress the `Status` section so it tells the truth about current state
  without front-loading too much hardening-specific implementation detail
- keep `Start Here` intact as the multi-audience routing surface, with only the
  minimum edits needed for clarity, pacing, and consistency
- keep the `AI-Assisted Review` section, but make sure it still reads as a
  helper for focused critique rather than a second large documentation layer
- define, in README structure and nearby owner guidance, that the root README
  is the map and entry surface rather than the place to carry every walkthrough
  in full

#### Expected New Files

- none expected

#### Expected Existing Files Updated

- `README.md`
- `__ai__.md`

#### Update AI files

- `.`

### PR - B: Move Tour-Level Depth Into Linked Guide Material

- identify the README sections that are functioning more like a tour than a
  map, especially the deeper workflow, source-family, packet/trace, and
  runtime-orientation sections
- move or consolidate that deeper explanation into one or more guide surfaces
  under `docs/Guides/`, favoring a small number of strong linked docs over many
  thin fragments
- replace the README's deepest tour-style sections with shorter summaries plus
  links out to the guide material that now owns the walkthrough
- make sure the final split is durable:
  - README explains what Atlas is, who it is for, what is currently true, and
    where to go next
  - guide material explains how the current workflows, source families, and
    inspection paths actually behave

#### Expected New Files

- `docs/Guides/context_atlas_tour.md` only if one consolidated tour document is
  needed instead of expanding existing guides

#### Expected Existing Files Updated

- `README.md`
- `docs/Guides/README.md`
- `docs/Guides/getting_started.md` only if link routing or overlap cleanup is
  needed
- `docs/Guides/docs_database_workflow.md` only if README-owned mixed-source
  explanation is pushed down there
- `docs/Guides/low_code_workflow.md` only if README-owned low-code explanation
  is pushed down there
- `__ai__.md`

#### Update AI files

- `.`

## Sequencing

- layer the README first so the target role of the file is explicit before any
  content is moved around
- extract or consolidate tour-style material second, with README summaries and
  guide links updated in the same slice so readers are not left with broken or
  incomplete routing

## Risks And Unknowns

- Over-compression could make the README cleaner but less truthful if too much
  current-state detail is stripped away from the top-level surface.
- Tour extraction can create duplication drift if the moved content is copied
  into guides without a clear ownership split.
- A new tour guide can become a dumping ground if it is not kept focused on
  product/system walkthrough material rather than every architectural detail in
  the repo.
- If the `Start Here` and `AI-Assisted Review` sections grow further while the
  deeper walkthrough remains nearby, the README can still feel like both a map
  and a tour even after this Task.

## Exit Criteria

- the top section of `README.md` gives a new reader a short mental model plus a
  clear path into the right surface without forcing them through deep workflow
  explanation first
- `README.md` still keeps the product framing, `Start Here`, and
  AI-assisted-review guidance that make the repo distinctive
- deeper workflow and tour-level material is linked from the README rather than
  carried there in full
- the split between entry surface and walkthrough surface is clear enough that
  future README edits can preserve it intentionally

## Final Handoff State

- completing this Task should leave the repo README acting more clearly as the
  map and truth-framing surface for Context Atlas
- guide material under `docs/Guides/` should own more of the walkthrough load
  without losing discoverability from the root
- future README growth should be easier to resist because the map-versus-tour
  boundary is now explicit

## Related Artifacts

- [Planning README](./README.md)
- [Repo README](../../README.md)
- [Guides README](../Guides/README.md)
- [Getting Started Guide](../Guides/getting_started.md)
- [Docs + Database Workflow Guide](../Guides/docs_database_workflow.md)
- [Low-Code Workflow Guide](../Guides/low_code_workflow.md)
- [Release README](../Release/README.md)
- [MVP Readiness Assessment](../Reviews/MVP/mvp_readiness_assessment.md)
