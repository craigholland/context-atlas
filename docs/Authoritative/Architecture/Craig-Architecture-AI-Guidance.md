---
id: craig-architecture-ai-guidance
title: Craig Architecture - AI Guidance
summary: Defines the AI-specific operational guidance, local-contract workflow, and architectural review heuristics that supplement Craig Architecture.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-16
last_reviewed: 2026-04-18
owners: [core]
tags: [architecture, ai-guidance, ai-collaboration, repository-guidance]
related:
  - ./Craig-Architecture.md
  - ./Craig-Architecture-Planning-And-Decomposition.md
  - ./Craig-Architecture-__ai__-Template.md
  - ./Craig-Architecture-Python.md
  - ../Ontology/README.md
supersedes: []
---

# Craig Architecture - AI Guidance

## Purpose

This document defines the AI-specific operational guidance and local-contract workflow that supplement [Craig Architecture](./Craig-Architecture.md).

It focuses on how AI contributors, automated analysis tools, and repositories should collaborate within a Craig-style system. The main Craig Architecture document remains the canonical statement of the philosophy, target architecture, and architectural evolution model.

## Scope

This document applies to:

- AI coding agents
- automated analysis tools
- repository conventions intended to guide AI contributors
- operational heuristics for detecting architectural drift

This document does not replace the main Craig Architecture philosophy. It supplements it with practical guidance for AI-assisted development.

## Binding Decisions

### 1. AI Guidance Is A Supplement To Craig Architecture

This document is subordinate to [Craig Architecture](./Craig-Architecture.md).

It defines how AI contributors should operate inside Craig-style systems. It does not redefine the philosophy or relax the architectural invariants defined by the main architecture document.

### 2. Required Read Order For AI Contributors

Before modifying code in a Craig-style repository, AI contributors should orient in this order:

1. Read the relevant sections of [Craig Architecture](./Craig-Architecture.md), especially:
   - `Non-Negotiable Invariant`
   - `Explore vs Exploit`
   - `Target Architectural Model`
   - `Layer Responsibilities`
   - `Project Decomposition Strategy`
   - `Evolutionary Development Philosophy`
2. If the task involves planning, decomposition, or PR review, read [Craig Architecture - Planning And Decomposition](./Craig-Architecture-Planning-And-Decomposition.md).
3. Read the relevant language supplement when one exists for the code being changed, such as [Craig Architecture - Python](./Craig-Architecture-Python.md).
4. Read the nearest local `__ai__.md` file for the folder being changed, then read parent `__ai__.md` files as needed.
5. Read the local verification contract, if one exists.
6. Read only the local files needed to understand the subsystem and the planned change.

If local guidance is absent, the main [Craig Architecture](./Craig-Architecture.md) document, the planning/decomposition supplement when relevant, and any relevant language supplement govern.

### 3. Repository AI Guidance Files

Craig Architecture assumes that modern projects may involve multiple contributors including:

- human engineers
- AI coding agents
- automated analysis tools

To make this collaboration safe and predictable, Craig-style projects commonly use repository-local AI guidance contracts.

These files are typically named:

```md
__ai__.md
```

Each `__ai__.md` file provides a localized architectural contract for the directory in which it appears.

These files are still written in plain Markdown and should remain readable to humans, but they are not meant to be treated as casual notes. In Craig-style systems they are operational contract artifacts that communicate local architectural intent to both human and AI contributors.

Typical information contained in these files may include:

- the purpose of the module or subsystem
- architectural constraints
- allowed dependencies
- coding conventions specific to that area
- warnings about common mistakes
- Known Gaps / Future-State Notes describing where the current implementation intentionally falls short of the long-term architecture or where the subsystem is expected to evolve

Some projects may also provide a standard template for `__ai__.md` files so that AI contributors can generate consistent documentation for new folders. A template is not required for the methodology to work, but it can help ensure that architectural guidance remains structured and machine-readable across the repository.

When a repository maintains a standard local-guidance template, it should usually align with [Craig Architecture - __ai__.md Template](./Craig-Architecture-__ai__-Template.md). Repositories may refine that baseline, but should preserve the overall shape unless there is a clear reason to diverge.

This approach creates a form of distributed architectural documentation that AI agents can read before modifying code.

Instead of relying solely on large top-level design documents, architectural intent is embedded directly within the repository structure.

This methodology allows AI agents to make better development decisions while keeping human architectural oversight intact.

The combination of the main architecture canon, repository-local guidance, and small reviewable changes helps greenfield systems evolve toward the intended Craig Architecture end state.

#### File Index Sections

Many `__ai__.md` files include a File Index section that summarizes the responsibilities of important files in the folder. This section is particularly useful for AI contributors because it provides a quick structural overview without requiring the agent to read the entire directory first.

A typical file index entry may describe:

- the responsibility of the file
- important classes or functions defined within it
- major dependencies
- known downstream consumers
- invariants or important behavioral expectations

This allows AI agents to orient themselves within a subsystem quickly and reduces the likelihood that changes will violate architectural assumptions.

#### Verification Contracts

Some `__ai__.md` files also include a Verification Contract. These contracts define the automated checks that must pass before modifications to the folder are considered valid.

Verification contracts often reference repository tooling such as:

- linting rules
- type checking
- import sanity checks
- small test subsets

The purpose of these contracts is not to replace architectural judgment. It is to create machine-readable validation rules that AI agents can run after making changes and to make local repository expectations inspectable in CI.

In AI-assisted workflows this helps create a feedback loop where agents can verify that their modifications remain compatible with the project's technical constraints.

### 4. Failure Modes And Trust Limits

Craig-style AI collaboration should explicitly recognize a few common failure modes:

- stale local `__ai__.md` files that no longer match the code they govern
- ownerless governed folders where no local contract exists at all
- metadata-only updates that refresh `Last Verified (CI)` without meaningfully reviewing the surrounding guidance
- CI or local verification being bypassed while contributors still assume the contract system is protecting the architecture
- passing verification being mistaken for proof that the architecture is semantically correct

These are not reasons to abandon the contract model. They are reasons to treat the contract system as a real operational surface that needs review, ownership, and honest limits.

### 5. Operational Workflow For AI Contributors

This section translates the main Craig Architecture document into a practical working loop for AI contributors.

#### Before Making Changes

- Identify which layers are being touched.
- Decide which resources involved are in `Explore` mode and which are in `Exploit` mode.
- Determine whether the planned change is exploratory, exploitative, or a promotion from one to the other.
- Check that the planned change preserves inward dependency direction.
- Choose the smallest semantically meaningful slice that can carry the work forward.
- Inspect the target folder for cohesion or flatness risk before adding more files to it.
- Inspect likely target files for size and helper-sprawl risk before growing them further.

The minimum architectural questions are:

- What layer should own the stable reasoning?
- Is this resource still exploratory, or has it become stable enough to exploit?
- Am I moving code into the wrong home temporarily, or am I breaking dependency direction?
- What would make this change harder to clean up later?
- Is this plan creating future hotspot files or folders that will be harder to govern?

#### While Making Changes

- Preserve inward dependency direction even when responsibility placement is temporarily imperfect.
- Translate external representations at boundaries rather than leaking them inward.
- Prefer migration-friendly exploratory dirt over migration-resistant dirt.
- Keep stable business rules moving toward the domain rather than accumulating in services or adapters.
- If a resource is still exploratory, keep it easy to rename, relocate, split, or delete.

If a choice trades speed against future recoverability, prefer the option that preserves future cleanup.

#### After Making Changes

- Run the local verification contract.
- Check whether the change altered architectural meaning, not just implementation.
- Update local `__ai__.md` guidance when the architecture of a folder has materially changed.
- Surface architectural drift, ambiguity, or exceptions rather than leaving them implicit.
- If a temporary shortcut was taken, make the direction of future cleanup legible.

### 6. Derived Working Heuristics

The following heuristics are shorthand operational translations of the main architecture document. They are derivative guidance, not independent doctrine.

#### Protect Dependency Direction

- Never interpret exploratory freedom as permission to reverse layer dependency.
- Temporary wrong-home placement may be acceptable.
- Direct inward dependence on outer implementations is not.

See `Non-Negotiable Invariant` in [Craig Architecture](./Craig-Architecture.md).

#### Treat Resource Maturity Explicitly

- Decide whether a resource is being explored or exploited before choosing how much structure to impose.
- Treat `Explore vs Exploit` as qualitative architectural judgment, not as a pseudo-metric or scoring exercise.
- If a resource is still exploratory, keep it shallow and easy to move.
- If a resource is stable, tighten its boundary and let the rest of the system depend on it deliberately.
- If the judgment is genuinely ambiguous, surface the reasoning rather than pretending the answer is mechanically obvious.

See `Explore vs Exploit` and `Evolutionary Development Philosophy` in [Craig Architecture](./Craig-Architecture.md).

#### Place Code By Responsibility, Not Convenience

- Decide whether the code is translating, orchestrating, deciding, defining a contract, or implementing an external capability.
- Place code according to that responsibility, even if the final package shape is still immature.
- When placement is imperfect during exploration, preserve future migration.

See `Target Architectural Model` and `Layer Responsibilities` in [Craig Architecture](./Craig-Architecture.md).

#### Translate At Boundaries

- Transport, persistence, and provider shapes should be translated at boundaries.
- Do not let framework DTOs, ORM rows, or vendor payloads quietly become the core system model.

See `Boundary Translation Rules` in [Craig Architecture](./Craig-Architecture.md).

#### Prefer Canonical Over Convenient

- Treat canonical state as the source of truth.
- Treat caches, indexes, summaries, and similar projections as derived.
- Avoid changes that make derived artifacts harder to rebuild or reason about.

See `Canonical vs Derived Data` in [Craig Architecture](./Craig-Architecture.md).

#### Decompose Work Semantically

- Keep changes small enough to review.
- Decompose work using the semantic hierarchy in the main document rather than arbitrary ticket slicing.
- Prefer a bounded task over a sprawling implementation batch.

When planning work at the PR level, include:

- expected new files
- expected existing files updated
- the local `__ai__.md` files that should be updated with the same slice

When reviewing a Task or PR plan, inspect for:

- duplicate planned file creation
- future hotspot files touched by too many slices
- folder flatness risk
- large-file risk
- junk-drawer helper-sprawl risk

See [Craig Architecture - Planning And Decomposition](./Craig-Architecture-Planning-And-Decomposition.md).

#### Respect Local Guidance

- Always read the nearest relevant `__ai__.md`.
- Prefer the more local rule when it tightens the main architecture contract for a subsystem.
- Surface explicit conflicts rather than resolving them silently.
- If a folder has become too broad for one useful local contract file, treat folder splitting as a valid architectural response rather than only updating prose.

### 7. Architecture Review Signals For AI Contributors And Tools

These signals are not independent architectural law. They are review prompts derived from the Craig Architecture canonical doc set, especially [Craig Architecture](./Craig-Architecture.md) and [Craig Architecture - Planning And Decomposition](./Craig-Architecture-Planning-And-Decomposition.md).

When these signals appear, AI contributors and automated reviewers should slow down, inspect boundary placement, and decide whether a small refactor or a documented exception is needed.

#### Service Layer Growing Unbounded

If service classes begin accumulating large amounts of unrelated logic, this may indicate that domain behavior has not yet been extracted into domain modules.

Possible action:

- Identify deterministic rules that could move into the domain layer.
- Introduce domain objects or modules that encapsulate that logic.

Relevant main-doc anchors:

- `Layer Responsibilities -> Application / Service Layer`
- `Layer Responsibilities -> Domain Layer`

#### APIs Containing Workflow Logic

Interface layers should generally translate requests and responses rather than coordinate system workflows.

Possible action:

- Move orchestration behavior into the service layer.
- Keep interface layers focused on transport concerns.

Relevant main-doc anchors:

- `Layer Responsibilities -> Interface / Delivery Layer`
- `Layer Responsibilities -> Application / Service Layer`

#### ORM Models Containing Business Logic

Persistence models should primarily represent stored data rather than business behavior.

Possible action:

- Move domain rules into domain modules or services.
- Keep persistence models focused on storage representation.

Relevant main-doc anchors:

- `Layer Responsibilities -> Domain Layer`
- `Layer Responsibilities -> Infrastructure / Provider Adapters`

#### Infrastructure Dependencies Appearing In Domain Code

Domain modules ideally avoid direct references to databases, frameworks, or external services.

Possible action:

- Introduce inward-owned ports in the appropriate inner layer.
- Move concrete implementations to the infrastructure layer.

Relevant main-doc anchors:

- `Non-Negotiable Invariant`
- `Preferred Dependency Direction`
- `Ports Belong To The Core, Not The Adapters`

#### Derived Data Treated As Canonical Truth

Caches, indexes, embeddings, or summaries should not become the primary source of truth.

Possible action:

- Ensure canonical state remains stored in durable systems.
- Treat projections as rebuildable artifacts.

Relevant main-doc anchors:

- `Canonical vs Derived Data`
- `Layer Responsibilities -> Infrastructure / Provider Adapters`

#### Exploratory Resources Becoming Quietly Canonical

An exploratory object, policy, contract, or adapter may no longer be truly exploratory if multiple callers depend on it, naming has stabilized, or cleanup keeps getting deferred.

Possible action:

- Promote the resource into a clearer architectural home.
- Tighten its contract and tests.
- Stop treating it as a disposable shortcut once the rest of the system depends on it.

Relevant main-doc anchors:

- `Explore vs Exploit`
- `Evolutionary Development Philosophy`

#### Large Or Unreviewable Pull Requests

Pull requests that are difficult to understand or contain many unrelated changes may indicate that work has not been decomposed properly.

Possible action:

- Break the change into smaller PRs aligned with a single task.

The goal of these signals is not to block development but to provide early warnings that architectural drift may be occurring. When such signals appear, contributors should consider whether a small refactor or restructuring step would help the system continue evolving toward the Craig Architecture end state.

#### Folder Becoming Too Flat To Govern Locally

If one folder begins accumulating many unrelated files or mixed concerns, the nearest `__ai__.md` often becomes broad, exception-heavy, or vague.

Possible action:

- split the folder by bounded concern
- keep the local contract scoped to one coherent area

Relevant planning/decomposition anchors:

- `Code Shape Governance -> Folder Cohesion` in [Craig Architecture - Planning And Decomposition](./Craig-Architecture-Planning-And-Decomposition.md)
- `Project Decomposition Strategy` in [Craig Architecture](./Craig-Architecture.md)

#### File Growing Beyond Reviewable Size

If a file is becoming hard to understand in one focused pass, future changes to it become riskier for both humans and AI contributors.

Possible action:

- split the file by responsibility
- extract a concept, submodule, or object before adding more behavior

Relevant planning/decomposition anchors:

- `Code Shape Governance -> File Reviewability` in [Craig Architecture - Planning And Decomposition](./Craig-Architecture-Planning-And-Decomposition.md)
- `Project Decomposition Strategy` in [Craig Architecture](./Craig-Architecture.md)

#### Helper-Chain / Junk-Drawer Module

If a module's behavior is spread across many unbound helpers, especially nested helpers or deep helper-call chains, the module may be missing clearer architectural concepts.

Possible action:

- introduce a value object, policy object, service object, or submodule
- reduce helper depth and make responsibilities more explicit

Relevant planning/decomposition anchors:

- `Code Shape Governance -> Module Shape And Helper-Sprawl` in [Craig Architecture - Planning And Decomposition](./Craig-Architecture-Planning-And-Decomposition.md)
- `Layer Responsibilities` in [Craig Architecture](./Craig-Architecture.md)

#### PR Plans Missing Code-Touch And Contract Expectations

If a Task or PR plan does not identify which files are expected to be created, which files are expected to change, and which local `__ai__.md` files must be updated, the plan is often too vague for reliable execution.

Possible action:

- refine the plan to include code-touch scope and local contract updates before implementation starts

Relevant planning/decomposition anchors:

- `Guidance Depth By Level` in [Craig Architecture - Planning And Decomposition](./Craig-Architecture-Planning-And-Decomposition.md)
- `Decomposition Sanity Checks` in [Craig Architecture - Planning And Decomposition](./Craig-Architecture-Planning-And-Decomposition.md)

#### Task Feature PR Missing A Review Gate

If a Task is being executed through multiple PR slices but there is no task-level feature PR, no `@codex review` request, or no pause before the next Task starts, contributors can lose the intended review boundary and drift into unsupervised multi-task accumulation.

Possible action:

- open or update the task-level feature PR
- request `@codex review` once the Task's planned slices are complete
- resolve review findings on the same feature branch before recommending human merge
- avoid moving to the next Task until the current Task has been reviewed and handed off, unless explicit parallelization was chosen

Relevant planning/decomposition anchors:

- `Task Execution Workflow Should Use The Feature PR As The Review Gate` in [Craig Architecture - Planning And Decomposition](./Craig-Architecture-Planning-And-Decomposition.md)
- `Branch Naming Should Reflect Decomposition` in [Craig Architecture - Planning And Decomposition](./Craig-Architecture-Planning-And-Decomposition.md)

## Constraints

- This document must not be interpreted as overriding the architectural invariants in [Craig Architecture](./Craig-Architecture.md).
- AI-operational convenience must not be used to justify broken dependency direction or architectural reversal.
- Local `__ai__.md` guidance may refine this document for a subsystem, but it must not contradict the main Craig Architecture document unless an explicit exception is documented.
- Passing local verification steps must not be treated as proof that the governed architecture is semantically correct.

## Non-Goals

- This document does not redefine the core Craig Architecture philosophy.
- This document does not turn AI heuristics into rigid truths detached from context and judgment.
- This document does not replace subsystem-specific local guidance.

## Related Artifacts

- [Craig Architecture](./Craig-Architecture.md)
- [Craig Architecture - Planning And Decomposition](./Craig-Architecture-Planning-And-Decomposition.md)
- [Craig Architecture - __ai__.md Template](./Craig-Architecture-__ai__-Template.md)
- [Ontology Templates](../Ontology/README.md)
