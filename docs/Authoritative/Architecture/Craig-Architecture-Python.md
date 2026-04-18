---
id: craig-architecture-python
title: Craig Architecture - Python
summary: Defines the Python-specific implementation guidance that supplements Craig Architecture, including package structure, ports, dependency wiring, circular-import management, and verification tooling.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-17
last_reviewed: 2026-04-18
owners: [core]
tags: [architecture, python, layering, dependency-injection, verification]
related:
  - ./Craig-Architecture.md
  - ./Craig-Architecture-AI-Guidance.md
  - ./Craig-Architecture-__ai__-Template.md
  - ../Ontology/README.md
supersedes: []
---

# Craig Architecture - Python

## Purpose

This document defines the Python-specific implementation guidance that supplements [Craig Architecture](./Craig-Architecture.md).

The main Craig Architecture document remains language-agnostic and philosophically primary. This document explains how those ideas are normally expressed in Python codebases, especially around package structure, ports/contracts, dependency wiring, circular imports, public surfaces, framework boundaries, and verification tooling.

## Scope

This document applies to Craig-style systems implemented primarily in Python.

It covers:

- Python package structure and layer packaging
- Python modeling choices by layer
- ports and contracts in Python
- dependency injection and composition in Python
- circular import risk management
- public surfaces via `__init__.py`
- framework leakage prevention
- testing and verification expectations
- folder cohesion, file size, and module-shape guidance

This document does not override the main Craig Architecture philosophy. It translates that philosophy into Python-specific defaults and guidance.

## Binding Decisions

### 1. This Document Is A Python Supplement

This document is subordinate to [Craig Architecture](./Craig-Architecture.md).

If this document appears to conflict with the main Craig Architecture document, the main document governs unless an explicit exception is documented.

### 2. Prefer A Clear Separation Between Repository Structure And Python Package Structure

Craig-style Python projects should usually separate repository-level project structure from Python package structure.

Two common repository shapes are acceptable.

Standalone package or library shape:

```text
project_name/
  docs/
  src/
    package_name/
      domain/
      services/
      ports/
      infrastructure/
      adapters/
      interface/
  tests/
  examples/
  scripts/
  .codex/
  .github/
  pyproject.toml
  .gitignore
```

Multi-app project shape:

```text
project_name/
  docs/
  apps/
    app_one/
      .env
      .venv/
      alembic/
      tests/
      src/
        domain/
        services/
        ports/
        infrastructure/
        adapters/
        interface/
      Dockerfile
      pyproject.toml
      alembic.ini
    app_two/
      .env
      tests/
      src/
        ...
      Dockerfile
      pyproject.toml
  scripts/
  .codex/
  .github/
  .gitignore
  docker-compose.yml
```

In either model:

- the repository root owns shared project concerns such as documentation, scripts, CI, Codex guidance, and packaging metadata appropriate to the repository shape
- the layer packages live inside a `src/` tree rather than directly at the repository root
- the package structure should make layer boundaries and dependency direction easier to see

In the standalone package shape:

- the repository typically represents one primary Python package
- `src/package_name/` owns the layer packages for that package
- repository-root `tests/` and `examples/` support the package without becoming part of its runtime namespace

In the multi-app shape:

- the `/apps` directory owns the individual deployable or runnable applications within the project
- each app owns its own Python packaging, tests, entrypoints, app-local environment configuration, and app-local `src/` tree
- the layer packages live inside each app's `src/` directory, not at the repository root

The `.github/` directory should remain at the repository root.

GitHub workflows, templates, and repository-governance files are repository-scoped by nature. In multi-app projects, those root workflows should become app-aware through path filters, app-specific jobs, and app-local scripts rather than by attempting to move `.github/` into individual app folders.

When a project uses both `adapters/` and `infrastructure/` inside the same app, the boundary should be explicit:

- `infrastructure/` owns persistence, storage, durable operational integrations, and other implementation details tied to systems of record or core technical capabilities
- `adapters/` owns translation-heavy integrations with external providers, protocols, payloads, or SDK-facing boundary code
- both remain outer-layer implementation details, and some smaller apps may reasonably collapse them together until the distinction becomes useful

Not every package or app needs every subdirectory immediately, and exact names may vary. Some projects may colocate ports with `domain/` or `services/` rather than introducing a separate `ports/` package early.

The important rule is that Python package structure should make dependency direction easier to preserve, not harder to see.

If a layer does not yet have its own package, its responsibilities still exist and should be kept legible.

The `src/` layout is preferred in part because it helps prevent accidental imports of Python packages directly from the working tree without installation.

That makes local development, tests, packaging, and runtime imports behave more like the installed package or application rather than relying on repository-root path leakage. In practice, this catches missing packaging assumptions earlier and makes the architecture more legible to both humans and AI contributors.

### 3. Each Standalone Package Or App Owns Its Own `pyproject.toml`

Each standalone package or app should own its own `pyproject.toml`.

That file should define the package metadata, dependencies, developer tooling, entrypoints where relevant, and verification-tool configuration for that package or app.

Architecturally, `pyproject.toml` should usually describe:

- the package's or app's direct runtime dependencies
- the package's or app's development and verification tools
- the package/build settings
- the script or entrypoint definitions that belong to that package or app

Cross-app dependencies should usually be avoided by default.

If stable shared code emerges, the preferred move is to promote it into an explicit shared package with a clear ownership boundary rather than allowing one peer app to import another app's internals directly.

That means:

- do not treat `apps/app_a/src` as an implicit library for `apps/app_b`
- do not rely on ad hoc `PYTHONPATH` tricks or direct cross-app imports
- if shared code becomes worth exploiting, give it an explicit package boundary and depend on it deliberately

Editable installs or workspace-style package management may be acceptable for explicitly shared packages. They should not be used to hide accidental architectural coupling between peer apps.

### 4. Use `__init__.py` To Define Public Layer Surfaces

In Craig-style Python projects, `__init__.py` should usually define the intended public surface of a package or layer.

That means:

- re-export the stable names that outer consumers are meant to import
- keep the exported surface curated rather than accidental
- prefer explicit `__all__` when helpful
- keep `__init__.py` files thin and free of side effects

This helps make the public shape of a layer visible and reviewable.

However, there is an important distinction:

- outer consumers may import through the curated package surface
- internal implementation modules should often import concrete sibling modules directly instead of routing through package barrels

This reduces circular import risk and keeps `__init__.py` from becoming a dependency knot.

`__init__.py` should define the intended public surface of a layer, not become a second implementation module.

### 5. Model Types By Layer, Not By Convenience

Craig-style Python code should choose modeling tools based on layer responsibility.

Typical default stance:

- `domain/`: plain classes, `dataclasses`, `Enum`, and small pure helper types
- `services/`: request/response objects, orchestration inputs, temporary exploratory structures
- `interface/`: inbound delivery DTOs, request/response models, and transport-facing serialization
- `adapters/`: outbound provider DTOs, external payload mappers, and SDK-facing translation models
- `infrastructure/`: ORM models, persistence rows, storage-facing structures

The normal default for domain modeling is the Python standard library, not a framework.

That means:

- prefer `dataclasses` or plain classes for domain objects
- prefer `Enum` for stable symbolic categories
- prefer explicit validation logic over framework-driven model magic in the domain layer

`Pydantic` is usually best treated as a boundary technology:

- good for API request/response models
- good for external payload validation
- acceptable for temporary exploratory structures in services when easy migration is preserved
- not ideal as the long-term core vocabulary of the domain layer

Temporary dirt may still be acceptable here. A domain-shaped Pydantic model temporarily living in `services/` can be migration-friendly if it is simple, local, and not imported inward. A stable business concept coupled deeply to Pydantic and framework semantics is much harder to migrate later.

### 6. Prefer `Protocol` Over `ABC` For Most Ports And Contracts

Craig-style Python projects should generally prefer `typing.Protocol` for ports and contracts.

Why:

- `Protocol` is structurally typed
- it keeps contracts lightweight
- it avoids unnecessary inheritance pressure
- it works well for capability-oriented interfaces
- it tends to fit Python's modern type system better than heavy nominal hierarchies

Typical use cases for `Protocol`:

- repository contracts
- gateway contracts
- notifier contracts
- provider-neutral capability contracts
- small service-facing abstractions

When practical, these protocols should live in small inward-owned contract modules such as `ports.py`, `contracts.py`, or a narrow package dedicated to the consuming layer's boundary.

`ABC` is still appropriate when one or more of the following is true:

- shared base behavior actually belongs in the abstraction
- nominal identity is important
- registration hooks or base implementation logic are useful
- the abstraction is intentionally class-like rather than capability-like

The default should be:

- `Protocol` for narrow ports/contracts
- `ABC` only when you really need base behavior or nominal semantics

`@runtime_checkable` should be used only when runtime protocol checks are genuinely needed. The default assumption should be static typing, not runtime interface inspection.

In either case, keep contracts small and focused. Craig Architecture does not benefit from giant interfaces that bundle unrelated capabilities together.

### 7. Use Explicit Dependency Wiring Before Reaching For A Container

The Python expression of Craig-style dependency injection should usually start with explicit manual composition.

Typical composition boundaries:

- `main.py`
- CLI entrypoints
- ASGI / WSGI app factories
- worker bootstrap modules
- task runner bootstrap code
- integration test setup

Preferred Python patterns include:

- constructor injection
- function-parameter injection
- small builder or bootstrap functions
- explicit top-level wiring modules

This is usually enough for exploratory and early exploitative systems.

A DI container is not forbidden, but it is not the default.

Craig-style Python projects should reach for a container only when:

- wiring is repeated across many entrypoints
- object lifetimes become non-trivial
- environment-dependent composition becomes hard to manage manually
- the relevant seams are stable enough to exploit

Even then, the container remains an outer implementation detail. Domain and service modules should not depend on the container's APIs, decorators, or runtime lookup model.

### 8. Treat Circular Imports As A Structural Warning Sign

Circular imports are a real Python hazard and often signal architectural or ownership confusion.

Craig-style Python projects should manage circular import risk intentionally.

Preferred techniques:

- organize packages so dependency direction is visible in the file tree
- keep contracts in inward-owned contract modules instead of hiding them in implementations
- avoid mutual imports between sibling modules when one shared concept can be moved inward
- keep `__init__.py` files thin
- use `from __future__ import annotations` where helpful
- use `typing.TYPE_CHECKING` for type-only imports when appropriate
- import concrete submodules directly inside a layer instead of routing every internal import through package barrels
- avoid treating package-level re-export surfaces as the default internal import path
- prefer splitting shared types or contracts into a smaller inward module instead of leaving them in mutually dependent implementations

The right response to a circular import is usually not "get clever with Python import tricks."

The right response is usually one of:

- move a shared concept to a more inward home
- split responsibilities more clearly
- extract a contract
- reduce accidental bidirectional knowledge between modules

Python workarounds can sometimes unblock a local problem, but they should not be used to hide structural drift.

Local imports inside functions may be acceptable at outer composition boundaries, plugin loading seams, or other clearly infrastructure-facing code paths. They should not become the default method for hiding core-layer dependency problems.

### 9. Keep Frameworks At The Boundary

Craig-style Python systems should keep framework-specific constructs from defining the core model.

Examples:

- FastAPI request objects, `Depends`, and route decorators belong at the interface boundary
- SQLAlchemy models and sessions belong in infrastructure
- Celery task wrappers and runtime context belong in delivery/infrastructure boundaries
- Pydantic transport models belong at boundaries unless they are clearly temporary exploratory structures

Domain and service code should not require framework runtime objects in order to make sense.

Boundary translation remains important in Python because frameworks often encourage convenient leakage.

### 10. Testing Should Follow The Wiring Model

Craig-style Python tests should reinforce explicit dependencies rather than hide them.

Tests should normally live in the app-level `tests/` directory, not inside `src/`.

This keeps production packages and verification suites distinct, and it reinforces the same installed-package import discipline encouraged by the `src/` layout.

Preferred patterns:

- test domain code directly with no framework setup
- pass fakes and stubs explicitly into services
- use hand-wired bootstrap helpers in tests when useful
- keep infrastructure-heavy tests separate from pure domain tests

Test suites should usually remain distinguishable by architectural scope, even if they are all run through `pytest`.

Typical distinctions include:

- domain tests for pure rules, value objects, policies, and deterministic state changes
- service tests for orchestration behavior with fakes, stubs, or narrow test doubles
- adapter or infrastructure tests for persistence, provider integrations, translation boundaries, and other external capabilities

The goal is not to create ceremony for its own sake. The goal is to avoid one undifferentiated test pile where architectural drift becomes hard to detect and slow feedback loops become the default.

`monkeypatch` and runtime patching are sometimes useful, but they should not become the primary architectural strategy for substituting dependencies.

If a dependency is difficult to replace in tests, that is often evidence that the production wiring is too implicit.

### 11. Split Folders Before Local Governance Becomes Vague

Craig-style Python packages should keep folders cohesive enough that a nearby `__ai__.md` file can describe the folder's purpose, major files, and boundary rules without turning into a broad essay.

Useful warning signs include:

- a folder mixes multiple sub-concerns that would be easier to understand as subpackages
- the local `File Index` is becoming mechanically exhaustive rather than selectively useful
- the local `__ai__.md` needs many exceptions or special cases to describe one folder's behavior honestly
- contributors regularly touch many unrelated files in the same folder because the folder has become a catch-all

As a rough Python-specific heuristic, once a governed folder has around `7-10` real implementation files or starts mixing clearly different responsibilities, contributors should at least consider splitting it.

This is a heuristic rather than a law. The important principle is that folder structure should remain governable and locally legible.

### 12. Treat Large Files And Helper-Sprawl As Design Smells

Craig-style Python code should prefer files that remain understandable in one focused pass.

As rough Python-specific guidance:

- `200-400` lines is usually healthy
- `400-600` lines should trigger scrutiny
- above roughly `600` lines should normally trigger deliberate decomposition unless there is a strong countervailing reason

Line count alone is not the only signal. Shape matters too.

Particularly important warning signs include:

- many top-level private helper functions in one module
- nested local helper functions that are doing more than one tightly local algorithm
- helper chains where one unbound function mainly orchestrates more unbound functions deeper and deeper
- modules whose real behavior is spread across a brittle private call graph rather than expressed through cohesive objects or submodules

When these signs appear, the usual preferred response is to introduce a clearer concept:

- a value object
- a policy object
- a focused service object
- a smaller submodule

Deep helper stacks are often a sign that the code is resisting its current file and module shape.

### 13. Verification Contracts Should Default To Ruff, MyPy, Pytest, And CI Contract Checks

The baseline Python verification contract for Craig-style repositories should usually include:

- `ruff` for linting and import hygiene
- `mypy` for static typing checks
- `pytest` for automated tests
- CI workflow scripts that validate repository AI guidance contracts such as `__ai__.md` expectations

Typical baseline commands:

```text
ruff check .
mypy src
pytest
```

Projects may also add:

- `ruff format --check .`
- targeted test subsets
- import-shape validation scripts
- custom CI checks for folder-level `__ai__.md`, File Index, or Verification Contract expectations

Typical `__ai__.md` contract automation may include:

- checking that required `__ai__.md` files exist in governed folders
- checking that required sections such as File Index or Verification Contract are present when the repository expects them
- checking that referenced verification commands or scripts remain valid
- checking that local guidance stays aligned with repository conventions

When a repository standardizes local guidance files, those checks should usually align with [Craig Architecture - __ai__.md Template](./Craig-Architecture-__ai__-Template.md) or a clearly documented repository-specific refinement of it.

The goal of these tools is not to replace architectural judgment. The goal is to make structural drift and contract breakage visible early.

The preferred posture is:

- verification should be runnable locally by contributors
- the same core checks should run in CI
- repository-specific AI contract checks should be treated as part of the real verification surface, not optional documentation lint

## Constraints

- This document must not be read as permission to let Python convenience override Craig Architecture dependency direction.
- `__init__.py` files must not become side-effect-heavy import hubs.
- Framework-specific models and runtime objects must not become the default domain vocabulary.
- DI containers, if used, must remain outer-layer implementation details.
- Circular import workarounds must not be used to hide unresolved ownership problems.
- Folder structure must not become so flat that local governance files become broad and vague.
- Large files and helper-sprawl must not be normalized as harmless style issues when they are really structural warnings.

## Non-Goals

- This document does not require every Python project to adopt the exact same package names.
- This document does not ban `ABC`, `Pydantic`, or DI containers outright.
- This document does not require zero circular-import mitigation techniques in all cases.
- This document does not replace project-specific local Python guidance in `__ai__.md` files.

## Related Artifacts

- [Craig Architecture](./Craig-Architecture.md)
- [Craig Architecture - AI Guidance](./Craig-Architecture-AI-Guidance.md)
- [Craig Architecture - __ai__.md Template](./Craig-Architecture-__ai__-Template.md)
- [Ontology Templates](../Ontology/README.md)
