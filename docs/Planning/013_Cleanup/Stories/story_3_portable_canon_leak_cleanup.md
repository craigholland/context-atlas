---
id: context-atlas-013-cleanup-story-3-portable-canon-leak-cleanup
title: Story 3 - Portable Canon Leak Cleanup
summary: Defines a bounded cleanup pass for the most obvious Context Atlas- and Codex-specific leaks inside Canon surfaces that are meant to be portable across projects.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-22
last_reviewed: 2026-04-23
owners: [core]
tags: [cleanup, story, canon, portability, examples, boundaries]
related:
  - ../013_cleanup_product_definition.md
  - ../../../Authoritative/Canon/AgenticDevelopment/README.md
  - ../../../Authoritative/Canon/Architecture/Craig-Architecture-Python.md
  - ../../../Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md
  - ../../../Authoritative/Canon/Ontology/Documentation-Ontology.md
  - ../../../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md
  - ../../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md
supersedes: []
---

# Story 3 - Portable Canon Leak Cleanup

## Objective

Remove the clearest avoidable Context Atlas- and Codex-specific leaks from
portable Canon surfaces so Canon reads more cleanly as reusable cross-project
guidance rather than as a thinly disguised project-local layer.

This Story is intentionally bounded to obvious leak cleanup. It is not the
Story that decides long-term runtime-policy placement, Canon admission rules,
or the full platform-binding architecture for future runtimes.

## Inputs

- [013 Cleanup Product Definition](../013_cleanup_product_definition.md)
- [AgenticDevelopment Canon README](../../../Authoritative/Canon/AgenticDevelopment/README.md)
- [Craig Architecture - Python](../../../Authoritative/Canon/Architecture/Craig-Architecture-Python.md)
- [Craig Architecture - AI Guidance](../../../Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md)
- [Documentation Ontology](../../../Authoritative/Canon/Ontology/Documentation-Ontology.md)
- [Codex Materialization README](../../../Authoritative/Identity/AgenticDevelopment/Materializations/Codex/README.md)
- [Context Atlas Agentic Development Profile](../../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md)

## Proposed Tasks

### Task 1: Leak Inventory And Classification

- identify which current Canon references are merely convenient local examples
  versus which ones incorrectly encode project-specific or platform-specific
  meaning into a portable surface
- classify each finding as:
  - replace with a project-neutral example
  - route to Identity or downstream materialization docs
  - or leave in place because the example is already truly portable

### Task 2: Portable Example Replacement And Rewording

Task 2 now settles the first concrete replacement pass for the Story:

- the portable AgenticDevelopment canon no longer relies on Context
  Atlas-specific framing or runtime-roster-flavored examples to teach the core
  model
- the portable Architecture canon no longer presents `.codex/`, `Codex
  guidance`, or `@codex review` as if they were universal Craig-style defaults
- Ontology branding examples remain explicitly classified work, not an implicit
  spillover from this task

- replace `.codex/`, `@codex review`, Context Atlas runtime IDs, and similar
  local examples where the surface is meant to describe a portable concept
- prefer project-neutral placeholders, generic platform language, or explicit
  downstream cross-links over local shorthand
- keep the replacement readable rather than abstract for its own sake

### Task 3: Boundary Cross-Link Reinforcement

Task 3 now settles the intended descent path once portable examples are
generalized:

- Canon entry surfaces may point readers to the current repository's Identity
  landing surfaces when concrete local detail is actually needed
- the first downstream stop is the Context Atlas Agentic Development Profile
  rather than a runtime-binding README
- the Codex binding README now explicitly declares itself downstream of the
  profile, manifest, and binding docs instead of acting like an alternate
  starting point for project structure

- ensure the Canon surfaces point readers toward the correct downstream
  Identity/materialization layer when a project-specific example is still
  needed
- avoid turning the Story into a broad directory reshuffle; the goal is to
  repair the boundary, not redesign the whole layout
- preserve the ability of later runtime-model work to move platform-binding
  guidance upward more deliberately if that becomes the chosen direction

### Task 4: Canon Readability And Reuse Check

Task 4 now settles the final readability boundary for Story 3:

- the portable AgenticDevelopment entry surfaces still read as learnable canon
  after the leak cleanup
- the reroute path now reads as canon first, then profile/binding detail, then
  current runtime binding
- the remaining ontology-branded examples are left only where they are
  intentionally classified or reserved for later Epics

- re-read the touched Canon entry surfaces as a newcomer who is not using
  Context Atlas specifically
- ensure the cleanup improves portability without making the prose vague or
  harder to learn from
- keep the final Canon shape useful as a case-study-derived canon rather than
  pretending it emerged from a second project that does not exist yet

## Current Bounded Leak Set

The current Story is intentionally bounded to the clearest review-backed leak
set rather than every project-local noun that appears anywhere in Canon.

The inventory currently in scope is:

- [AgenticDevelopment README](../../../Authoritative/Canon/AgenticDevelopment/README.md):
  the `Why This Matters Here` framing still talks directly about Context Atlas
  as the governed engine, which makes a portable canon entry surface read more
  project-local than necessary.
- [Quick Mental Model](../../../Authoritative/Canon/AgenticDevelopment/Quick-Mental-Model.md):
  the worked example uses runtime-facing names such as `parent-backend` and
  `specialist-python-implementation`, which are useful but currently read more
  like one project's materialized roster than a portable primer.
- [Craig Architecture - Python](../../../Authoritative/Canon/Architecture/Craig-Architecture-Python.md):
  the repository-shape examples still include `.codex/`, and one repository
  responsibility bullet still names `Codex guidance` directly rather than
  describing a generic runtime/governance surface.
- [Craig Architecture - AI Guidance](../../../Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md):
  the task-review-gate guidance still names `@codex review` directly instead of
  describing a portable automated review request pattern.
- [Documentation Ontology](../../../Authoritative/Canon/Ontology/Documentation-Ontology.md),
  [Ontology README](../../../Authoritative/Canon/Ontology/README.md), and
  [base_metadata.md](../../../Authoritative/Canon/Ontology/base_metadata.md):
  these surfaces still brand the ontology and metadata examples as Context
  Atlas-specific even where the surrounding guidance is otherwise reusable.

The inventory explicitly excludes:

- canonical Craig-style `__ai__.md` guidance, which is a portable Craig
  Architecture concept rather than a Context Atlas runtime leak
- downstream Identity and materialization docs, which belong to later tasks
  only when Canon needs a clearer place to point concrete project detail

## Classification Model

Story 3 should classify each inventory item into one of three dispositions:

1. `Generalize in Canon`
   Use when the current example is carrying a project-local or platform-local
   name but the surrounding concept is still portable. The preferred response
   is to replace the example with project-neutral wording, a generic runtime
   placeholder, or a broader case-study-safe example.
2. `Reroute downstream`
   Use when the portable canon should keep the concept but a concrete project
   binding or materialization detail still needs a home. The preferred response
   is to keep Canon conceptual and point readers toward the appropriate
   Identity or materialization entry surface.
3. `Keep intentionally`
   Use when the local example is still serving a real case-study purpose and
   its presence does not redefine a project-local runtime detail as universal
   law. If this disposition is chosen, the example should read as an explicit
   current proving-ground illustration rather than accidental residue.

The current expected classification is:

- AgenticDevelopment README framing: `generalize in Canon`
- Quick Mental Model runtime-facing roster example: `generalize in Canon`
- Craig Architecture - Python `.codex/` and `Codex guidance` examples:
  `generalize in Canon`
- Craig Architecture - AI Guidance `@codex review` example: `generalize in Canon`
- Ontology branding/examples: either `generalize in Canon` where the wording is
  only convenient branding, or `keep intentionally` where the text is
  explicitly describing the current project's proving-ground ontology

The current downstream-routing expectation is:

- Canon entry surfaces may link readers toward project-specific binding
  entrypoints when the portable explanation is no longer enough
- the Context Atlas Agentic Development Profile is the first project-specific
  landing surface after canon
- role, mode, protocol, and manifest bindings refine that profile
- the Codex binding README is downstream of that profile/binding layer rather
  than a substitute starting point

## Planned Task Decomposition

- [Task 3.1 - Leak Inventory And Classification](./Tasks/task_3_1_leak_inventory_and_classification.md)
- [Task 3.2 - Portable Example Replacement And Rewording](./Tasks/task_3_2_portable_example_replacement_and_rewording.md)
- [Task 3.3 - Boundary Cross-Link Reinforcement](./Tasks/task_3_3_boundary_cross_link_reinforcement.md)
- [Task 3.4 - Canon Readability And Reuse Check](./Tasks/task_3_4_canon_readability_and_reuse_check.md)

## Sequencing

- inventory and classify the leaks first
- replace or reword the clearest local assumptions next
- reinforce the Canon -> Identity boundary after the replacements are clear
- perform a final readability pass last so the cleanup improves portability
  without degrading approachability

## Risks And Unknowns

- The Story can become over-abstract if it strips away every concrete example.
- It can also accidentally absorb future runtime-policy work if contributors
  start debating where every platform-binding artifact should live long-term.
- Brand cleanup in ontology or canon docs can go too far if it erases the fact
  that Context Atlas is the current proving ground for the canon.

## Exit Criteria

- the clearest unnecessary Context Atlas- and Codex-specific Canon leaks are
  removed or re-routed
- portable Canon surfaces still read clearly to a human reader
- project-specific examples that remain in Canon are intentionally justified
  rather than left as accidental residue

Story 3 is allowed to end with a small remainder only when that remainder is
explicitly classified and does not silently redefine project-local details as
portable defaults.

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- Canon surfaces touched by this Story stay meaningfully portable and do not
  silently redefine project-local runtime details as universal rules
- The repository preflight command passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge

## Related Artifacts

- [013 Cleanup Product Definition](../013_cleanup_product_definition.md)
- [AgenticDevelopment Canon README](../../../Authoritative/Canon/AgenticDevelopment/README.md)
- [Craig Architecture - Python](../../../Authoritative/Canon/Architecture/Craig-Architecture-Python.md)
- [Craig Architecture - AI Guidance](../../../Authoritative/Canon/Architecture/Craig-Architecture-AI-Guidance.md)
- [Task docs](./Tasks/)
