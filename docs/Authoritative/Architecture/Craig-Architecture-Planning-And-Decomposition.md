---
id: craig-architecture-planning-and-decomposition
title: Craig Architecture - Planning And Decomposition
summary: Defines the canonical planning, decomposition, and code-shape governance model that supplements Craig Architecture and should guide project planning artifacts.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-18
last_reviewed: 2026-04-18
owners: [core]
tags: [architecture, planning, decomposition, delivery, governance]
related:
  - ./Craig-Architecture.md
  - ./Craig-Architecture-AI-Guidance.md
  - ./Craig-Architecture-Python.md
  - ./Craig-Architecture-__ai__-Template.md
  - ../Ontology/README.md
supersedes: []
---

# Craig Architecture - Planning And Decomposition

## Purpose

This document defines the detailed planning, decomposition, and code-shape guidance that supplements [Craig Architecture](./Craig-Architecture.md).

The main Craig Architecture document remains philosophically primary. This document expands the operational mechanics of how work should be decomposed from product intent into architecture-aware implementation slices.

It should also be treated as the authoritative planning-and-decomposition reference that project-specific planning documents derive from when a repository adopts Craig Architecture.

## Scope

This document applies to:

- decomposition of work from `Epic` to `Story` to `Task` to `Pull Request`
- planning-time expectations for guidance depth and code-touch scope
- sanity checks that should be performed before accepting a plan
- code-shape governance concerns that should influence planning before implementation starts

This document does not replace project-specific planning artifacts. It defines the canonical planning and decomposition model they should follow.

## Binding Decisions

### 1. This Document Is A Supplement To Craig Architecture

This document is subordinate to [Craig Architecture](./Craig-Architecture.md).

It expands the planning and decomposition mechanics that support the main philosophy. It does not redefine the architectural invariants or the target architectural model.

### 2. Planning And Decomposition Are Architectural Concerns

Craig Architecture treats decomposition as more than project-management convenience.

The way work is sliced affects:

- whether architecture remains legible
- whether local contracts remain governable
- whether PRs stay reviewable
- whether AI contributors can execute safely without causing structural drift

Decomposition quality is therefore treated as part of architectural quality.

### 3. Canonical Decomposition Ladder

Craig Architecture favors breaking large engineering efforts into small, understandable increments.

The numerical limits in this document are typical guidelines, not dogmatic truths.

The decomposition hierarchy is not only about size. It is also about meaning.

Typical hierarchy:

```text
Project
    Epics
        Stories
            Tasks
                Pull Requests
```

In general:

- `Epics` describe `Releases` and/or `Packages`
- `Stories` describe `Features` and/or `Modules`
- `Tasks` describe bounded implementation objectives
- `Pull Requests` describe reviewable delivery units

This hierarchy helps the system evolve in units that are both architecturally meaningful and practically reviewable.

### 4. Guidance Depth By Level

The decomposition hierarchy should also change the level of guidance as work moves closer to implementation.

- `Epics` should remain primarily product-level.
- `Stories` should translate product intent into architectural shape.
- `Tasks` should translate architectural intent into implementation plans.
- `Pull Requests` should translate task intent into concrete code changes.

In practical terms:

- `Epics` should usually define target users, desired outcomes, non-goals, and the major shared capabilities being pursued.
- `Stories` should usually define which layers, modules, bounded concerns, or architectural seams are expected to move.
- `Tasks` should usually define how that story will be implemented through sequenced PR slices while preserving architectural boundaries.
- `Pull Requests` should usually define the concrete code-facing scope, including expected new files, expected existing files updated, and the local contract files that must change with the slice.

If work is decomposed only by size and not by meaning, later implementation tends to become noisier, more brittle, and harder to govern.

### 5. Suggested Scale Guidelines

These are guidelines rather than rigid rules.

#### Pull Requests

- Preferably under about `500` lines of changed code
- Large changes should typically be split

The real objective is that a reviewer should be able to fully understand the PR within a short review window.

#### Tasks

Tasks represent bounded implementation objectives within a Story.

A Task should ideally be small enough that its initial implementation can be delivered in no more than about `5` planned PRs.

This guideline refers to the primary implementation PRs needed to build the Task, not later PRs for debugging, documentation, testing expansion, cleanup, or review-driven follow-up work.

If a Task reliably requires many follow-up PRs after implementation appears complete, that is still a useful signal that the Task may have been under-scoped, under-specified, or insufficiently decomposed.

#### Stories

Stories describe Features and/or Modules within an Epic.

A Story should usually describe a coherent functional capability or module-level increment that can be delivered through a small set of Tasks.

As a rough guideline, a Story should ideally stay within about `10` Tasks.

#### Epics

Epics describe Releases and/or Packages.

An Epic should usually define a major delivery surface, package boundary, or release-level objective that groups related Stories into a coherent milestone.

As a rough guideline, an Epic should ideally stay within about `5` Stories.

These limits encourage steady progress while preventing complexity from accumulating too quickly.

### 6. Branch Naming Should Reflect Decomposition

Craig Architecture prefers branch names that reflect the current decomposition level rather than vague work themes.

When work is being executed through a planned `Epic -> Story -> Task -> Pull Request` hierarchy:

- the long-lived feature branch should usually reflect the `Task`
- the short-lived implementation branch for each PR slice should usually reflect the `Task` plus the specific PR slice

Preferred feature-branch convention:

```text
feature/<Epic name>/<Story #>_<Task #>_<Task description>
```

Preferred PR-slice branch convention when branching from that feature branch:

```text
codex/<Story #>_<Task #><PR Char>_<PR description>
```

Examples:

- `feature/mvp/3_2_product_surface`
- `codex/3_2A_public_api_exports`
- `codex/3_2B_trace_rendering`

These names should stay concise, lowercase where practical, and formatted safely for shell, Git, and GitHub usage. Descriptions should communicate bounded intent rather than broad themes.

The goal is not naming ceremony for its own sake.

The goal is that a contributor should be able to infer:

- which task a branch belongs to
- whether a branch is the long-lived task branch or a short-lived PR slice
- what bounded delivery unit the branch is meant to contain

### 7. Task Execution Workflow Should Use The Feature PR As The Review Gate

When work is being executed through a planned `Epic -> Story -> Task -> Pull Request` hierarchy, Craig Architecture prefers the `Task` feature PR to be the main review and handoff boundary rather than treating every PR slice as an independent human-review checkpoint.

The usual workflow is:

- create the task-level feature branch and open its feature PR early
- mark the Task as `WORKING`
- implement bounded PR slices on short-lived slice branches and merge them back into the task feature branch
- keep the feature PR body aligned with the Task goals and current slice status
- when all planned slices for the Task are complete, mark the Task as `IMPLEMENTED`
- run the full local preflight on the feature branch
- request `@codex review` on the feature PR
- resolve review findings on the same feature branch and rerun preflight
- hand the feature PR to a human reviewer once the task branch is review-clean
- avoid starting the next Task until the current task feature PR has been reviewed, fixed if needed, and merged, unless an explicit parallelization decision has been made

This workflow preserves two useful properties at once:

- contributors can move quickly within a Task without pausing for human review on every slice
- humans still review work at a meaningful architectural boundary rather than only after many Tasks have accumulated

The goal is not process ceremony for its own sake.

The goal is that decomposition should also define the review cadence and handoff shape, especially when AI contributors are executing many small slices quickly.

### 8. Decomposition Sanity Checks

Before accepting a Story, Task, or PR plan, contributors should inspect the plan for shape risks rather than only counting how many slices exist.

Useful checks include:

- whether the same file is being planned as a new creation in more than one PR
- whether too many future PRs converge on one file, creating an obvious hotspot
- whether the planned folder structure is becoming too flat for one useful local contract file
- whether a planned change is likely to push a file toward an unreviewable size
- whether a plan relies on growing helper chains instead of introducing missing concepts, objects, policies, or submodules
- whether each planned PR identifies the local `__ai__.md` files that should be updated as part of the same slice

These checks are not intended to create planning ceremony for its own sake.

They exist because brittle implementation plans often reveal themselves before coding starts, especially when work is being decomposed for AI-assisted execution.

### 9. Code Shape Governance

Craig Architecture treats code shape as an architectural concern rather than a mere style preference.

Three recurring risks are especially important:

- folders that become too flat and broad to govern well
- files that become too large to understand in one focused pass
- modules that devolve into junk drawers of loosely related helper functions

#### Folder Cohesion

Folders should stay cohesive enough that a nearby local contract file can describe the folder's purpose, key files, and boundary rules without becoming vague or encyclopedic.

If a folder starts mixing multiple sub-concerns, accumulating too many unrelated files, or requiring a sprawling local contract file full of exceptions, that is usually a signal that the folder should split.

#### File Reviewability

Files should stay small enough to be reviewed, reasoned about, and evolved without forcing contributors to keep too much unrelated logic in working memory at once.

Language supplements may define more concrete thresholds, but the philosophy-level rule is simple:

- if a file is becoming hard to read in one focused review pass, it is probably becoming too large

#### Module Shape And Helper-Sprawl

Craig Architecture strongly disfavors modules that become procedural junk drawers.

Small pure helpers can be useful. The risk appears when:

- a file accumulates many unbound helper functions with weak shared cohesion
- nested helpers are used to hide complexity rather than express a genuinely local algorithm
- top-level helpers call more helpers which call more helpers, creating a brittle private call graph

When this happens, the usual architectural diagnosis is not "write better helper names."

The more common diagnosis is that a missing concept should be introduced, such as:

- a value object
- a policy object
- a service object
- a submodule with a clearer bounded concern

Code that is difficult to govern structurally is usually also difficult to evolve safely.

## Constraints

- This document must not be interpreted as replacing the main Craig Architecture philosophy.
- Numeric planning guidelines in this document must not be enforced as dogmatic truths detached from context.
- Planning detail must not become ceremony for its own sake.
- Code-shape guardrails must not be dismissed as mere style preferences when they are actually structural warnings.

## Non-Goals

- This document does not prescribe one project-management tool, issue tracker, or PR platform.
- This document does not require all projects to decompose work into identical counts or identical document structures.
- This document does not eliminate the need for architectural judgment when sizing or sequencing work.

## Related Artifacts

- [Craig Architecture](./Craig-Architecture.md)
- [Craig Architecture - AI Guidance](./Craig-Architecture-AI-Guidance.md)
- [Craig Architecture - Python](./Craig-Architecture-Python.md)
- [Craig Architecture - __ai__.md Template](./Craig-Architecture-__ai__-Template.md)
- [Ontology Templates](../Ontology/README.md)
