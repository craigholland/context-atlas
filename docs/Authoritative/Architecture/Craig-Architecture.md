---
id: craig-architecture
title: Craig Architecture
summary: Defines the project-agnostic Craig Architecture applied philosophy, its architectural invariants, and its evolutionary model for human and AI contributors.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-16
last_reviewed: 2026-04-18
owners: [core]
tags: [architecture, philosophy, layering, clean-architecture, solid]
related:
  - ./Craig-Architecture-AI-Guidance.md
  - ./Craig-Architecture-__ai__-Template.md
  - ./Craig-Architecture-Python.md
  - ../Ontology/README.md
supersedes: []
---

# Craig Architecture

## Purpose

Craig Architecture is an AI-enabled applied architecture philosophy used across projects designed by Craig Holland. The goal is to provide a shared working structure - for both human engineers and AI contributors - for how a system should evolve over time toward a maintainable architecture.

A concise definition is:

> Craig Architecture is an AI-enabled applied architecture philosophy that operationalizes ideas from SOLID, Clean Architecture, and related design traditions into an evolvable, contract-aware working model.

Craig Architecture is best understood as a pragmatic blend of SOLID principles and Clean Architecture philosophy, adapted for real-world iterative development.

It is not intended to supersede or compete head-to-head with those underlying traditions as an independent grand theory of software architecture. Instead, it applies and operationalizes them in environments where iterative development, repository-local contracts, and AI collaboration all materially affect how systems are built.

Unlike many architectural documents that describe only the final structure of mature systems, Craig Architecture also attempts to describe how AI-assisted development can move a greenfield codebase toward that mature structure over time.

Modern software development increasingly involves collaboration between humans and AI coding agents. In that environment, architecture must do more than describe ideal layering - it must also provide clear intent signals that AI can follow during iterative development.

Craig Architecture therefore focuses on two complementary goals:

1. Defining the architectural end state a mature system should reach.
2. Providing AI-friendly guidance that allows early-stage code to evolve safely toward that structure.

Craig Architecture is not a rigid framework or a strict development rulebook. Instead, it describes an architectural end state that systems should gradually move toward as they mature. The intent of this document is to be pragmatic without being dogmatic; philosophical while still being actionable.

Craig Architecture holds that SOLID and Clean Architecture are often highly beneficial for mature codebases, but can inhibit development in young prototypes when applied too aggressively or too early. Prematurely forcing every abstraction, boundary, and dependency seam into existence can create infrastructure complexity that slows down discovery before the system understands itself.

For that reason, Craig Architecture explicitly allows systems to be intentionally dirty during exploration, but insists that they be dirty in a way that preserves future cleanup.

The guiding idea is:

> Build intentionally dirty in a clean way.

This means early code may temporarily place some responsibilities in less-than-ideal locations, but it should do so in forms that are easy to migrate later.

For example:

- domain-shaped data structures temporarily living in services may be acceptable if they are simple and easy to relocate
- stable business rules embedded into service orchestration are much more dangerous because they become harder to extract later

Craig Architecture therefore distinguishes between dirt that is migration-friendly and dirt that is migration-resistant.

Migration-friendly dirt usually involves code that is structurally easy to move later.

Migration-resistant dirt usually involves stable behavior becoming entangled with the dependencies of the wrong layer.

The central philosophy is:

> Build systems so that core business logic remains stable while infrastructure, interfaces, and storage mechanisms can evolve safely.

Craig Architecture draws inspiration from a number of well-known architectural traditions, including:

- SOLID principles
- Clean Architecture
- Ports and Adapters
- Event-oriented system design
- Long-term maintainability practices

However, it intentionally extends those ideas into the AI-assisted development era, where architecture must guide both humans and automated contributors.

## A Note about Philosophy vs Implementation

Craig Architecture is defined first and foremost as a philosophy. It expresses a set of beliefs about how software systems should be structured, how they should evolve over time, and how both human engineers and AI contributors should interact with that structure.

This core document defines those beliefs and invariants at a high level. It is intentionally language-agnostic and avoids prescribing one universal set of tools, file layouts, or enforcement mechanisms. Its purpose is to establish a shared understanding of good architectural direction, not to dictate one mandatory implementation for every repository.

The supplementary documents do not redefine the philosophy. They translate it into concrete working patterns such as AI collaboration guidance, local contract structure, language-specific implementation defaults, and example enforcement mechanisms. These are reference operationalizations of the philosophy, not the only valid ways it can be realized in practice.

Different implementations are possible, but the underlying expectation remains consistent: if the philosophy matters, it should become explicit, inspectable, and at least partly enforceable within the codebase rather than remaining implicit intent.

## Non-Negotiable Invariant

Craig Architecture allows provisional responsibility placement during exploration.

Craig Architecture does not allow broken dependency direction.

This is the rigid rule:

> Layer dependency cannot be broken.

Responsibilities may temporarily live in a less-than-ideal layer while the system is still being discovered. However, inner layers must not depend on outer implementation details. A system may be structurally unfinished without being architecturally reversed.

This means, for example:

- service modules may temporarily contain domain-shaped objects
- service modules may temporarily contain exploratory code that will later split apart
- outer composition boundaries may manually wire concrete adapters during exploration, so long as inner layers still depend on inward-owned contracts

But it does not mean:

- domain code may import service modules
- domain code may depend on ORM models, HTTP clients, UI request objects, or provider SDKs
- outer framework shapes may be allowed to define the core system model

Temporary mess is allowed inside the dependency rules, not across them.

## Explore vs Exploit

Craig Architecture treats system resources as living in one of two broad modes:

- `Explore`: the resource is still being discovered, refined, renamed, pressure-tested, or rethought
- `Exploit`: the resource is stable enough to canonize, depend on, build upon, and abstract

A resource may be:

- a domain object
- a policy module
- a service workflow
- an adapter contract
- a persistence model
- a documentation artifact

The purpose of this distinction is not to force a formal process. It is to improve judgment.

`Explore vs Exploit` is a conceptual judgment tool, not a deterministic scoring system.

It relies on architectural experience, project trajectory, surrounding context, expected stability, dependency surface, and the likely future role of the resource in the system.

It is meant to sharpen judgment, not replace it with a formula. Different experienced contributors may reasonably disagree at the margins about whether a resource is still exploratory or stable enough to exploit, and that is normal.

When a resource is in `Explore` mode:

- keep the structure as light as possible
- avoid premature abstraction
- minimize outward dependency surface
- prefer shapes that are easy to relocate or refactor
- avoid making the rest of the system depend too deeply on it

When a resource is in `Exploit` mode:

- canonize the naming and boundaries
- tighten invariants
- move stable rules inward
- strengthen tests and contracts
- allow broader reuse because the resource is now intended to be built upon

One practical implication is:

- exploratory data structures are often cheap to move
- exploratory business logic is often expensive to move

This is why temporary co-location of structures is usually safer than temporary co-location of stable behavior.

## AI Guidance Supplement

Craig Architecture is designed to guide both human and AI contributors.

The AI-specific operational guidance that supplements this document lives in [Craig Architecture - AI Guidance](./Craig-Architecture-AI-Guidance.md).

That companion document covers repository-level AI collaboration methodology, quick operational rules for AI contributors, and architecture drift signals for AI reviewers and automated tooling.

The standard structure for local repository guidance contracts lives in [Craig Architecture - __ai__.md Template](./Craig-Architecture-__ai__-Template.md).

## Language Supplements

Craig Architecture itself is language-agnostic.

Language-specific implementation guidance should live in companion documents rather than redefining the main philosophy. The current Python supplement is [Craig Architecture - Python](./Craig-Architecture-Python.md).

---

# Target Architectural Model

In its mature form, a Craig-style system should converge toward a stable core surrounded by replaceable outer layers.

A more explicit target model looks like this:

```text
External Actors / Systems
        ->
Interface / Delivery Adapters
        ->
Application / Service Layer
        ->
Domain Layer

Inner-owned capability contracts:
Application / Service Layer and/or Domain Layer
        ->
Ports / Contracts
        ->
Infrastructure / Provider Adapters
```

Typical examples of each part:

- `Interface / Delivery Adapters`: HTTP endpoints, CLI commands, event consumers, job runners, UI controllers
- `Application / Service Layer`: use-case orchestration, workflow sequencing, transaction boundaries, coordination across multiple domain behaviors
- `Domain Layer`: entities, value objects, policies, invariants, state transitions, deterministic rules
- `Ports / Contracts`: repository interfaces, gateways, provider contracts, publish/subscribe contracts, storage abstractions owned by the inner layer that needs them
- `Infrastructure / Provider Adapters`: databases, ORM repositories, filesystems, queues, search systems, third-party APIs, model providers

The exact package or folder names may vary by project. Some systems expose `ports` as a distinct package, while others colocate the contracts with the domain or application layer. Craig Architecture is not rigid about folder naming. It is strict about responsibility placement and dependency direction.

The `Ports / Contracts` path is not a claim that the domain must always talk to infrastructure directly. It expresses the rule that when inner layers need external capabilities, they should depend on inward-owned contracts rather than outer implementations.

These layers describe the target mature structure of the system. They are not a claim that every early prototype will start perfectly separated.

## Architectural Center Of Gravity

The conceptual center of a Craig-style system is the domain layer.

This means:

- the domain should define the most stable concepts in the system
- the domain should own the rules the system is trying to preserve over time
- outer layers should be easier to replace than the domain
- system understanding should improve when moving inward, not become more ad hoc

If replacing a database, transport, framework, or provider forces a rewrite of the system's core logic, the architectural center of gravity is probably in the wrong place.

## Preferred Dependency Direction

The preferred dependency direction is inward:

```text
interfaces -> services -> domain
inner layers (services and/or domain) -> inward-owned ports -> infrastructure adapters
infrastructure adapters -> domain types only at mapping boundaries
```

These arrows describe allowed dependency direction, not necessarily a literal runtime call stack in every code path.

The important rule is:

- inner layers should not depend on outer implementation details
- outer layers may depend on inner abstractions

In practical terms, the following dependencies are usually signs of architectural drift:

- domain code importing ORM models
- domain code calling HTTP clients directly
- domain code depending on UI or transport request objects
- service code becoming coupled to one provider's SDK shape
- interfaces reaching directly into persistence logic without going through application behavior

## Boundary Translation Rules

Craig Architecture expects translation to happen at boundaries rather than leaking external representations inward.

Examples:

- transport payloads should be translated at the interface boundary
- ORM rows and persistence models should be translated at the infrastructure boundary
- provider-specific request and response shapes should be translated at the adapter boundary
- domain objects should not simply be thin wrappers around external schemas

This matters because systems become brittle when framework shapes, provider payloads, or storage layouts become the accidental domain model.

## Ports Belong To The Core, Not The Adapters

Ports and contracts should be owned by the inner layers that need the capability, not by the infrastructure that happens to implement it.

For example:

- if the domain needs persistence, the repository contract should be defined inward
- if a service needs to send notifications, the notification contract should be defined inward
- if the system needs model inference, the contract should be expressed in system terms rather than mirroring a vendor SDK

Adapters should implement these contracts.

This keeps the core in control of its own vocabulary and prevents third-party APIs from quietly defining the architecture.

## Not Every Project Needs Every Layer As A Separate Package

Craig Architecture describes responsibilities first and package structure second.

That means:

- a small project may have no UI layer at all
- a library may have a very thin interface boundary
- a purely in-memory system may have minimal infrastructure code
- a prototype may temporarily combine service and domain logic

What must remain clear is that missing packages do not imply missing responsibilities. If a project has no dedicated `infrastructure/` folder yet, infrastructure concerns still exist. If a project has no explicit `ports/` package, the contracts still need a clear owner.

## Mature-State Shape

In a mature Craig-style system:

- interfaces are thin and mostly translate inputs and outputs
- services read like use-case orchestration rather than policy engines
- domain code carries the stable reasoning and invariants
- infrastructure can be swapped or refactored without redefining the system's core behavior
- canonical state and derived projections are clearly distinguished

This is the architectural end state contributors should move toward.

## Early-Stage Deviations

Early-stage systems are allowed to fall short of this target model while the domain is still being discovered.

Common temporary deviations include:

- services temporarily hosting domain-shaped data structures that are still being explored
- interfaces performing light orchestration before service boundaries stabilize
- manual outer-boundary wiring of concrete adapters before more formal dependency setup becomes worthwhile
- a single module temporarily containing multiple responsibilities during early exploration

Common dangerous deviations include:

- stable business rules being embedded into service orchestration
- invariants being enforced only by persistence models or framework objects
- provider-specific SDK shapes becoming the effective application contract
- domain code taking dependencies on outer layers because it is convenient in the moment

These shortcuts are acceptable only if they are treated as transitional. The direction of travel should remain clear:

- stable rules move inward
- framework and provider specifics stay outward
- contracts become clearer over time
- boundaries become more explicit as understanding improves
- exploratory resources are either retired or promoted into canonized forms

One useful test is:

- if the code is easy to move later, it may be acceptable exploratory dirt
- if the code is becoming harder to move every week, it is probably the wrong kind of dirt

---

# Layer Responsibilities

The target model only becomes useful when each layer has a clear job.

These responsibilities are about architectural ownership, not folder naming. A project may package them in different ways, but the responsibilities themselves should remain distinct.

When placement is unclear, ask:

- which layer should own the stable reasoning?
- which layer is only translating?
- which layer is only coordinating?
- which layer is only implementing an external capability?

## Interface / Delivery Layer

Primary role:

- receive input from external actors
- validate transport shape
- translate external requests into application-level requests
- translate application results into outward-facing responses

Allowed work:

- HTTP / gRPC endpoints
- CLI commands
- UI controllers and presentation boundaries
- event consumers and job entry points
- authentication or session handling tied to delivery mechanics
- transport-level validation
- response serialization, status code selection, exit code selection, and presentation concerns

Not allowed:

- stable business rules
- domain invariants that are enforced only here
- direct ownership of workflow orchestration that belongs in services
- direct coupling to persistence details as a substitute for application behavior
- treating transport DTOs as the system's core model

Temporary but acceptable:

- light orchestration while service boundaries are still stabilizing
- exploratory request-shaping code that is easy to move into services later
- temporary co-location of simple request or response objects during early discovery

Danger signals:

- controllers or endpoints deciding business outcomes
- UI or transport payload shapes becoming the effective domain model
- interface code bypassing services to reach directly into persistence or provider code

## Application / Service Layer

Primary role:

- orchestrate use cases and workflows
- coordinate multiple domain behaviors
- define transaction or unit-of-work boundaries
- coordinate repositories, gateways, and external capabilities through inward-owned contracts

Services should answer questions such as:

- what sequence of operations should occur?
- which domain behaviors must run together?
- when should data be loaded, persisted, published, or retried?
- what belongs inside one application action versus another?

Allowed work:

- workflow sequencing
- transaction management
- coordination across repositories or external gateways
- invoking domain policies and state transitions
- assembling inputs needed for domain decisions
- handling application-level errors, retries, and idempotency concerns

Not allowed:

- becoming the long-term home of stable business policy
- embedding invariants that clearly belong to the core system model
- allowing provider SDK shapes or transport objects to define application contracts
- becoming a giant grab-bag for any code that lacks a better home

Temporary but acceptable:

- hosting domain-shaped data structures that are still exploratory and easy to relocate
- containing short-lived exploratory behavior before the stable core model is understood
- relying on simple manual wiring at an outer composition boundary before formal dependency setup becomes worthwhile, so long as the service module itself still depends on an inward-owned contract

Danger signals:

- services start reading like policy engines rather than orchestration flows
- stable business rules accumulate here because extraction feels increasingly expensive
- services become tightly coupled to one database model, framework object, or provider SDK
- a service must be understood in full before the system's core rules make sense

## Domain Layer

Primary role:

- own the stable conceptual model of the system
- define deterministic business rules
- hold explicit state transitions, policies, and invariants
- represent the reasoning the system is trying to preserve over time

Allowed work:

- entities
- value objects
- enums
- pure domain services
- policies and rule modules
- explicit state transition logic
- reason codes and invariant enforcement

Domain logic should ideally:

- run and be testable without frameworks, databases, or network access
- remain deterministic where practical
- express system meaning in system terms rather than provider or framework terms

Not allowed:

- direct dependencies on service modules
- direct dependencies on transport, UI, ORM, or provider SDK shapes
- hidden side effects that rely on infrastructure to complete their meaning
- using outer-layer convenience objects as the core system vocabulary

Temporary but acceptable:

- incomplete decomposition inside the domain while stable concepts are still emerging
- simple, pure structures and rules that may later split into finer-grained modules
- a smaller-than-ideal domain layer during early discovery, as long as outward dependencies remain forbidden

Danger signals:

- the domain imports ORM models, HTTP clients, UI requests, or provider SDKs
- the domain becomes a mirror of database schema or transport payload shape
- core rules live elsewhere because the domain is treated as an afterthought
- moving the domain to a different framework would require redefining the concepts themselves

## Ports / Contracts Layer

Primary role:

- define the capabilities the inner system requires from outer layers
- preserve core vocabulary at system boundaries
- let the core ask for what it needs without adopting the implementation's language

Allowed work:

- repository interfaces
- gateway contracts
- notification or publishing contracts
- storage abstractions
- provider-neutral inference or execution contracts
- clock, identity, or other external capability contracts when useful

Not allowed:

- mirroring a vendor SDK so closely that the vendor becomes the architecture
- placing stable business policy inside the contract definition
- allowing infrastructure-specific error or data shapes to define the core boundary
- hiding architectural uncertainty behind unnecessary abstraction theater

Temporary but acceptable:

- colocating ports with the domain or service layer rather than giving them a dedicated package
- using simple protocols, abstract base classes, or lightweight interfaces during early exploration
- delaying formal port extraction until a capability is clearly worth abstracting

Danger signals:

- contracts live only in infrastructure code
- the rest of the system must speak adapter language instead of system language
- provider-specific terms define the public meaning of the boundary
- ports proliferate before the system knows which capabilities are stable enough to exploit

## Infrastructure / Provider Adapters

Primary role:

- implement the capabilities requested through ports
- persist canonical state and maintain derived projections
- integrate with external systems, providers, and operational tooling

Allowed work:

- ORM models and repositories
- filesystem access
- queue, cache, and search integrations
- HTTP clients and external service SDK wiring
- provider adapters
- serialization, persistence mapping, and operational retry mechanics

Not allowed:

- becoming the primary home of business policy
- being the only place where core invariants are enforced
- defining canonical system meaning through storage layout or provider schema
- leaking infrastructure data shapes inward as if they were domain objects

Temporary but acceptable:

- narrow exploratory adapters with limited local scope
- manual outer-boundary wiring of concrete adapters before more formal dependency setup becomes worthwhile
- implementation-first experimentation when the external capability itself is still being explored

Danger signals:

- database schema or provider payloads define the core model more than the domain does
- adapter code contains stable decision-making that the rest of the system depends on
- switching infrastructure would require rethinking the business model instead of just changing implementation
- derived systems such as caches or indexes quietly become canonical truth

---

# Core System Principles

Several system-level principles appear repeatedly in Craig-style systems. These principles help ensure that systems remain predictable, maintainable, and evolvable as they grow.

## Canonical vs Derived Data

Craig Architecture distinguishes between canonical state and derived projections.

```text
Canonical State
    authoritative system truth

Derived Projections
    caches
    summaries
    search indexes
    embeddings
```

Derived data should always be rebuildable from canonical sources.

This distinction improves reliability and simplifies recovery.

---

## Ports and Adapters Philosophy

Where practical, core logic should depend on interfaces rather than concrete infrastructure.

Example structure:

```text
domain/repos
    MemoryRepo

infrastructure/database/repos
    SqlMemoryRepo
```

This allows infrastructure implementations to change without altering business logic.

During early development it is acceptable for concrete adapters to be wired manually at outer composition boundaries until more formal dependency setup becomes worthwhile, so long as inner layers still depend on inward-owned contracts rather than importing adapter implementations directly.

---

## Dependency Injection And Composition Boundaries

Craig Architecture treats dependency injection primarily as a way to preserve dependency direction.

It does not require a framework, container, or elaborate infrastructure by default.

In Craig-style systems, proper dependency injection means:

- inner layers define or depend on inward-owned contracts
- outer layers choose concrete implementations
- concrete implementations are wired at an outer composition boundary
- inner layers receive dependencies explicitly rather than discovering them through hidden global lookup

Acceptable composition boundaries may include:

- application startup
- CLI entrypoints
- worker bootstrap code
- HTTP server setup
- job runners
- test setup

The specific injection mechanism may vary by project. Constructor injection, function-parameter injection, explicit factory wiring, and small builder/composer modules are all acceptable if they keep dependency direction clear and make the dependency graph understandable.

Craig Architecture does not treat dependency injection as synonymous with a DI container.

In many young systems, manual outer-boundary wiring is preferable because:

- the dependency graph is still exploratory
- object lifetimes are still simple
- introducing a container too early can create infrastructure complexity before the system understands its own stable seams

This is one place where Craig Architecture applies the idea of building intentionally dirty in a clean way.

### Proper DI In A Mature System

In a mature Craig-style system:

- contracts are defined inward
- concrete adapters are selected outward
- the composition boundary assembles the graph
- inner layers receive only the capabilities they need
- tests can substitute fakes or stubs without changing core logic

The goal is not to make dependency injection feel sophisticated. The goal is to keep core logic independent from outer implementation details.

### Intentionally Dirty But Acceptable Wiring

During exploration, the following may be acceptable:

- manual construction of concrete adapters in startup or entrypoint code
- repeated wiring across a small number of entrypoints while the graph is still unstable
- small local factories or builder functions near the outer boundary
- hand-wired test setup without a formal container

These forms of dirt are acceptable because they are usually easy to clean up later.

They preserve the core rule that inner layers still depend on inward-owned contracts rather than importing concrete outer implementations directly.

### Not Acceptable, Even During Exploration

The following are not acceptable forms of temporary dirt:

- domain or service modules importing concrete adapter implementations directly
- inner layers reaching into global registries or service locators to discover dependencies
- framework-specific DI annotations or container APIs leaking into core domain logic
- allowing the container's lookup model to become the real architecture instead of explicit contracts

These patterns are migration-resistant because they hide dependency direction and make cleanup harder over time.

### When To Formalize Wiring

Teams should consider moving from manual composition toward more formal wiring when:

- the same wiring is repeated across many entrypoints
- object lifetime management becomes non-trivial
- environment-specific composition starts to branch significantly
- test setup becomes noisy or repetitive
- the relevant contracts and resource boundaries are stable enough to exploit rather than still being explored

At that point, a more structured composition mechanism may be justified.

Even then, the container or framework remains an outer-layer implementation detail. It should not become the vocabulary of the core system.

### Service Locator Warning

Craig Architecture strongly disfavors service locator patterns in inner layers.

If a module must reach into a runtime registry to find what it needs, the dependency relationship has become hidden. Hidden dependency direction is one of the easiest ways for a codebase to look architecturally clean on the surface while drifting structurally underneath.

Explicit dependencies are preferred even when they feel temporarily repetitive.

---

## Deterministic System Behavior

Craig Architecture favors deterministic behavior when possible.

Systems designed under this philosophy often make state transitions explicit rather than hiding them behind side effects. Explicit transitions make it easier to reason about system behavior, debug issues, and reproduce outcomes during testing or simulation.

Given the same inputs, the system should ideally produce the same outputs.

Benefits include:

- easier debugging
- reproducible simulations
- reliable automated testing

This principle is particularly valuable in simulation-driven systems.

---

# Project Decomposition Strategy

Craig Architecture also emphasizes breaking large engineering efforts into small, understandable increments.

The numerical limits in this section are typical guidelines, not dogmatic truths.

The decomposition hierarchy is not only about size. It is also about meaning.

Typical hierarchy:

```text
Project
    Epics
        Stories
            Tasks
                Pull Requests
```

This structure helps ensure that development remains reviewable and understandable.

In general:

- `Epics` describe `Releases` and/or `Packages`
- `Stories` describe `Features` and/or `Modules`
- `Tasks` describe bounded implementation objectives
- `Pull Requests` describe reviewable delivery units

This hierarchy helps the system evolve in units that are both architecturally meaningful and practically reviewable.

## Guidance Depth By Level

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

## Suggested Scale Guidelines

These are guidelines rather than rigid rules.

### Pull Requests

- Preferably under ~500 lines of changed code
- Large changes should typically be split

The real objective is that a reviewer should be able to fully understand the PR within a short review window.

### Tasks

Tasks represent bounded implementation objectives within a Story.

A Task should ideally be small enough that its initial implementation can be delivered in no more than about 5 planned PRs.

This guideline refers to the primary implementation PRs needed to build the Task, not later PRs for debugging, documentation, testing expansion, cleanup, or review-driven follow-up work.

If a Task reliably requires many follow-up PRs after implementation appears complete, that is still a useful signal that the Task may have been under-scoped, under-specified, or insufficiently decomposed.

### Stories

Stories describe Features and/or Modules within an Epic.

A Story should usually describe a coherent functional capability or module-level increment that can be delivered through a small set of Tasks.

As a rough guideline, a Story should ideally stay within about 10 Tasks.

### Epics

Epics describe Releases and/or Packages.

An Epic should usually define a major delivery surface, package boundary, or release-level objective that groups related Stories into a coherent milestone.

As a rough guideline, an Epic should ideally stay within about 5 Stories.

These limits encourage steady progress while preventing complexity from accumulating too quickly.

## Decomposition Sanity Checks

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

## Code Shape Governance

Craig Architecture treats code shape as an architectural concern rather than a mere style preference.

Three recurring risks are especially important:

- folders that become too flat and broad to govern well
- files that become too large to understand in one focused pass
- modules that devolve into junk drawers of loosely related helper functions

### Folder Cohesion

Folders should stay cohesive enough that a nearby local contract file can describe the folder's purpose, key files, and boundary rules without becoming vague or encyclopedic.

If a folder starts mixing multiple sub-concerns, accumulating too many unrelated files, or requiring a sprawling local contract file full of exceptions, that is usually a signal that the folder should split.

### File Reviewability

Files should stay small enough to be reviewed, reasoned about, and evolved without forcing contributors to keep too much unrelated logic in working memory at once.

Language supplements may define more concrete thresholds, but the philosophy-level rule is simple:

- if a file is becoming hard to read in one focused review pass, it is probably becoming too large

### Module Shape And Helper-Sprawl

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

---

# Evolutionary Development Philosophy

Craig Architecture assumes systems evolve through stages.

Typical lifecycle:

```text
Prototype
    ->
Working System
    ->
Structured Architecture
```

Early versions may temporarily violate ideal layering. As the system stabilizes, refactoring moves responsibilities toward their proper architectural locations.

The goal is eventual clarity, not premature rigidity.

The important qualifier is that exploratory systems should not accumulate irreversible mess.

Craig Architecture encourages fast early development, but prefers forms of speed that preserve future architectural exploitation. Exploration is not an excuse to make the core of the system depend on the wrong things.

The preferred progression is:

- explore lightly
- identify what is stabilizing
- promote stable resources into clearer architectural homes
- exploit the canonized forms as the foundation for later work

---

# Common Failure Patterns Craig Architecture Tries to Avoid

The philosophy attempts to reduce several common architectural problems:

- large monolithic services accumulating unrelated logic
- overly flat folders whose local contracts become broad and vague
- large files that become difficult to review or refactor safely
- junk-drawer modules built from deep helper chains instead of cohesive concepts
- tight coupling between APIs and persistence layers
- embedding business rules directly inside ORM models
- infrastructure concerns leaking into core business logic
- stale local guidance being treated as authoritative after the code has materially changed
- verification metadata being mistaken for semantic review
- CI or local contract checks being bypassed while contributors still assume the architecture is being enforced
- undocumented local exceptions or hidden boundary violations accumulating outside the visible contract system

Gradual separation of concerns helps prevent these issues.

---

# Architecture Anti-Goals

Craig Architecture also clarifies what it does not attempt to optimize for. These anti-goals help prevent contributors from over-applying architectural patterns in ways that slow down development or create unnecessary complexity.

Craig Architecture intentionally does not prioritize:

### Premature Perfect Layering

Early-stage systems are allowed to place logic in imperfect locations while the product is still evolving. The architecture expects gradual refactoring toward the target structure rather than perfect layering from the beginning.

### Premature Infrastructure Complexity

The architecture does not encourage introducing heavy dependency injection systems, excessive adapter scaffolding, or elaborate abstraction layers before the system has identified which resources are actually stable enough to exploit.

### Maximum Abstraction

The architecture does not encourage adding interfaces or abstractions until they provide clear value. Simpler implementations are often preferred early in development.

### Framework-Centric Design

Frameworks, ORMs, and infrastructure tools should support the system rather than define its structure. Core system concepts should not be tightly coupled to specific frameworks.

### Large, Multi-Feature Changes

Large changes that combine many responsibilities are discouraged. Incremental, reviewable changes are preferred so that the system can evolve safely.

### Cleverness Over Clarity

Highly clever implementations that are difficult to understand are avoided. Code should favor readability and maintainability over clever techniques.

These anti-goals reinforce the central philosophy of Craig Architecture: systems should evolve toward clarity and maintainability through steady, understandable progress.

---

# Summary

Craig Architecture is an AI-enabled applied architecture philosophy focused on:

- long-term maintainability
- separation of responsibilities
- deterministic behavior where possible
- canonical vs derived data modeling
- machine-readable local contracts that help align human and AI contributors
- small, reviewable development increments

It shares important ground with SOLID principles and Clean Architecture, but it is not merely a generic restatement of either.

It is not intended as a replacement for SOLID, Clean Architecture, DDD, or other established design traditions. It is an applied working model for using ideas from those traditions in repositories where architecture must be understandable, evolvable, and legible to both humans and AI systems.

What distinguishes Craig Architecture is:

- clean boundaries are treated as the target mature state, not the mandatory starting posture for early prototypes
- `Explore vs Exploit` is used as a judgment model for deciding when resources should remain light and exploratory versus when they should be canonized and built upon
- systems may be intentionally dirty during exploration, but only in forms that preserve future cleanup
- dependency direction remains rigid even when responsibility placement is temporarily imperfect
- local `__ai__.md` contracts and verification workflows make architectural intent more legible and enforceable in AI-assisted development
- folder structure, file size, and module shape are treated as architectural concerns rather than merely stylistic concerns
- architecture is expected to evolve as stable concepts emerge, clarify, and move into more appropriate homes over time

It is not a strict framework but rather a target structure that systems should evolve toward deliberately.

Projects developed under this philosophy typically begin with flexible implementations, protect inward dependency direction from day one, and gradually mature into well-layered systems whose stable concepts are increasingly explicit and reusable.
