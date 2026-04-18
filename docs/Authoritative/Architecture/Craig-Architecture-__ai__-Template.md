---
id: craig-architecture-ai-template
title: Craig Architecture - __ai__.md Template
summary: Defines the standard structure and baseline content expectations for repository-local `__ai__.md` contract files in Craig-style systems.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-17
last_reviewed: 2026-04-18
owners: [core]
tags: [architecture, ai-guidance, template, local-guidance]
related:
  - ./Craig-Architecture.md
  - ./Craig-Architecture-Planning-And-Decomposition.md
  - ./Craig-Architecture-AI-Guidance.md
  - ./Craig-Architecture-Python.md
  - ../Ontology/README.md
supersedes: []
---

# Craig Architecture - __ai__.md Template

## Purpose

This document defines the standard structure and baseline content expectations for repository-local `__ai__.md` contract files in Craig-style systems.

It exists so that local AI guidance remains consistent, machine-readable, and operationally useful across repositories, folders, and future AI contributors.

## Scope

This document applies to:

- root-level `__ai__.template.md` files used to standardize local guidance across a repository
- folder-level `__ai__.md` files that provide localized architectural and verification guidance
- AI contributors and repository tooling that read, validate, or generate those files

This document does not replace [Craig Architecture](./Craig-Architecture.md) or [Craig Architecture - AI Guidance](./Craig-Architecture-AI-Guidance.md). It defines the expected structure for one specific kind of local operational artifact.

In Craig-style systems, these files are not merely convenience documentation. They are repository-local contract artifacts that encode folder-level architectural intent in a form that humans, AI agents, and CI workflows can all inspect.

## Binding Decisions

### 1. `__ai__.md` Is The Standard Local Contract Filename

Craig-style repositories should use `__ai__.md` as the standard filename for folder-level AI contract files.

When a repository wants a reusable authoring template, it should usually place that template at the repository root as `__ai__.template.md`.

### 2. Local Contract Files Should Follow A Standard Section Shape

The baseline section structure for a local `__ai__.md` file is:

- `Last Verified (CI)`
- `Scope`
- `Purpose`
- `Architectural Rules`
- `Allowed Dependencies`
- `Public API / Key Exports`
- `File Index`
- `Known Gaps / Future-State Notes`
- `Cross-Folder Contracts`
- `Verification Contract`

Repositories may refine this structure, but they should do so conservatively. The goal is predictable local contract structure, not endless local variation.

### 3. `Last Verified (CI)` Describes Technical Verification, Not Human Approval

The `Last Verified (CI)` block exists to record the most recent automated verification state for the scope governed by the file.

It should communicate at least:

- the commit that was verified
- the verification timestamp
- the verifying actor, typically `ci`
- a note clarifying that verification means the declared checks passed, not that a human performed architectural review

This distinction matters because AI contributors should not confuse passing automation with human sign-off.

### 4. `Scope` Must Make Folder Ownership Explicit

Each `__ai__.md` file should clearly define:

- the folder it governs
- what file patterns are included
- what file patterns are excluded

This helps both humans and AI tools understand what guidance applies where, especially in larger repositories with multiple apps or nested guidance files.

### 5. Local Contract Files Must Express Real Architectural Constraints

Local `__ai__.md` files should not be vague summaries.

They should capture the real operational rules for the folder, including:

- what the folder is for
- what it is allowed to do
- what it must not do
- what dependencies are permitted or forbidden
- what invariants or runtime constraints matter in practice

If the folder intentionally falls short of the long-term architecture, that should be stated explicitly in `Known Gaps / Future-State Notes`.

### 6. `File Index` Should Be Selective, Useful, And Maintained

The `File Index` section should help contributors orient quickly without reading the entire folder first.

It should focus on important files rather than trying to mechanically catalog every file in a directory.

Useful entries may include:

- the file's responsibility
- key classes or functions it defines
- major dependencies
- important downstream consumers
- invariants
- known footguns

When relevant, the `File Index` should also surface code-shape warnings such as:

- files that are already unusually large
- modules that are at risk of becoming junk drawers
- files that are likely hotspot files for future work

### 7. Folder Scope Should Stay Cohesive Enough To Govern

If a folder becomes too flat or mixes too many unrelated concerns, one local `__ai__.md` file often becomes broad, vague, and hard to maintain.

Craig-style repositories should prefer splitting a folder by bounded concern before the local contract file becomes a sprawling exception list.

Useful local notes may include:

- folder split signals
- known hotspot files
- sub-concerns that should become subpackages later

### 8. `Verification Contract` Must Be Runnable And Local To The Scope

The `Verification Contract` section should describe executable checks that are meaningful for the governed folder.

These checks should usually be:

- runnable by contributors locally
- automatable in CI
- scoped enough to provide fast feedback
- aligned with the repository's actual toolchain

A verification contract is not a wish list. It should describe commands or scripts that the project actually expects contributors to run.

The YAML step format used in the template is intentionally CI-like because it is familiar, easy to parse, and easy to translate into automation. It resembles GitHub Actions step syntax on purpose, but it is not a requirement that repositories use GitHub Actions literally as the execution engine.

### 9. `Cross-Folder Contracts` Should Capture Real Boundary Assumptions

The `Cross-Folder Contracts` section should record important assumptions that one folder makes about another folder's behavior or boundary shape.

Useful entries are concrete rather than generic.

Examples:

- `services/`: domain objects passed across this boundary must be plain domain types or dataclasses, not ORM models
- `adapters/`: external payloads must be translated before crossing into services
- `tests/`: integration tests may rely on bootstrap helpers, but should not import private infrastructure internals as a substitute for real contracts

This section exists to make inter-folder assumptions reviewable before they silently turn into accidental architecture.

### 10. Local Contracts May Tighten Global Guidance But Must Not Contradict It

Local `__ai__.md` files may refine or tighten guidance for a subsystem.

They must not contradict:

- [Craig Architecture](./Craig-Architecture.md)
- [Craig Architecture - AI Guidance](./Craig-Architecture-AI-Guidance.md)
- relevant language supplements such as [Craig Architecture - Python](./Craig-Architecture-Python.md)

If a subsystem needs an exception, that exception should be made explicit rather than implied by drift.

### 11. Standard Baseline Template

The following is the baseline template Craig-style repositories should start from when creating a root `__ai__.template.md` or a new folder-level `__ai__.md` file:

````md
# __ai__.md - Folder Summary

## Last Verified (CI)
- commit: <FILL_IN_SHA>
- timestamp_utc: <FILL_IN_UTC_ISO8601>
- verified_by: ci
- notes: Verified means "all commands in Verification Contract passed" (not a human review).

## Scope
- folder: <RELATIVE/POSIX/PATH/TO/FOLDER>
- included:
  - <glob patterns, e.g. "*.py", "**/*.py">
- excluded:
  - <glob patterns, e.g. "__pycache__/**", "**/migrations/**">

## Purpose
- <1-3 bullets describing what this folder provides and why it exists>

## Architectural Rules
- <what this folder is allowed to do>
- <what this folder must not do>
- <important runtime / transaction / import-safety rules>
- <important layering constraints>

## Allowed Dependencies
- may depend on:
  - <important allowed upstream modules/packages>
- must not depend on:
  - <important forbidden modules/packages>

## Public API / Key Exports
- <module>:
  - <symbol>: <what it is + why it matters>
  - <symbol>: <what it is + why it matters>

## File Index
- <file>:
  - responsibility: <short>
  - defines:
    - <class/function>: <inputs/outputs + notes>
  - depends_on:
    - <important imports / upstream modules>
  - used_by:
    - <known downstream modules (optional)>
  - invariants:
    - <rules that should always hold>
  - footguns:
    - <common pitfalls / gotchas>
  - size_warning:
    - <use when the file is approaching local complexity limits>
  - shape_risks:
    - <use when helper-sprawl, mixed responsibilities, or hotspot risk is emerging>

## Known Gaps / Future-State Notes
- <intentional simplification in current implementation>
- <future direction that is relevant to reading current code>
- <areas where current runtime slice is narrower than the long-term architecture>
- <folder split signals if this scope is becoming too broad to govern well with one local contract>

## Cross-Folder Contracts
- services/: domain objects passed across this boundary must be plain domain types or dataclasses, not ORM models
- <folder or module>: <assumption this folder relies on>
- <folder or module>: <boundary or behavioral expectation>

## Verification Contract
```yaml
steps:
  - name: lint
    run: |
      cd <APP_OR_WORKDIR>
      <LINT_COMMAND_FOR_SCOPE>

  - name: typecheck
    run: |
      cd <APP_OR_WORKDIR>
      <TYPECHECK_COMMAND_FOR_SCOPE>

  - name: import_sanity
    run: |
      cd <APP_OR_WORKDIR>
      <IMPORT_SANITY_COMMAND_FOR_SCOPE>
```
````

## Constraints

- This document must not be interpreted as overriding the main Craig Architecture canon.
- Local `__ai__.md` files must stay concise enough to be operationally useful.
- The template should support machine readability and human fast-scan readability at the same time.
- Repository-specific refinements should preserve the recognizable section structure unless there is a clear reason to diverge.
- Local `__ai__.md` files should be updated when a folder's responsibilities, dependency rules, public API, verification contract, or cross-folder assumptions have materially changed.
- Stale local contract files should be treated as a failure state for the contract system, not as harmless documentation drift.
- If one local contract file is becoming broad, exception-heavy, or vague because the folder is too flat, the preferred response is usually to split the folder rather than only enlarging the prose.

## Non-Goals

- This document does not require every folder in every repository to have a `__ai__.md` file immediately.
- This document does not require the `File Index` to become a mechanically exhaustive inventory.
- This document does not replace project-specific architectural judgment.
- This document does not imply that passing the `Verification Contract` is equivalent to architectural correctness.

## Related Artifacts

- [Craig Architecture](./Craig-Architecture.md)
- [Craig Architecture - Planning And Decomposition](./Craig-Architecture-Planning-And-Decomposition.md)
- [Craig Architecture - AI Guidance](./Craig-Architecture-AI-Guidance.md)
- [Craig Architecture - Python](./Craig-Architecture-Python.md)
- [Ontology Templates](../Ontology/README.md)
