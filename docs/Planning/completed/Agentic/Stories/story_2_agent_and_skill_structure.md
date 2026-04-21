---
id: context-atlas-agentic-story-2-agent-and-skill-structure
title: Story 2 - Agent And Skill Structure
summary: Defines how Context Atlas composes parent agents, specialist agents, and skills without yet collapsing those structural concepts into project roles or runtime modes.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: active
created: 2026-04-19
last_reviewed: 2026-04-20
owners: [core]
tags: [agentic-development, story, agents, specialists, skills]
related:
  - ../agentic_development_product_definition.md
  - ./story_1_portable_agentic_development_canon.md
  - ../../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Delegation-Model.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Agent-Composition-Model.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Skill-Contract.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Skill-Attachment-Model.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Composition-Decision-Model.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Escalation-Model.md
  - ../../../Authoritative/Canon/AgenticDevelopment/Agent-Authority-Model.md
  - ../../../Authoritative/Canon/Architecture/Craig-Architecture.md
supersedes: []
---

# Story 2 - Agent And Skill Structure

## Objective

Define the structural model that Context Atlas will use for parent agents,
specialist agents, and skills so the repository has one governed pattern for
layering atomic skills into focused specialists and broader parent agents
before project roles and runtime-specific files are introduced.

## Inputs

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](./story_1_portable_agentic_development_canon.md)
- [Skill Contract](../../../Authoritative/Canon/AgenticDevelopment/Skill-Contract.md)
- [Agent Authority Model](../../../Authoritative/Canon/AgenticDevelopment/Agent-Authority-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)
- Current repo experience with reusable prompts, bounded execution surfaces, and specialist-style sub-work

## Proposed Tasks

### Task 1: Parent And Specialist Composition

- define why Context Atlas uses parent agents plus specialist agents rather than
  a flat list of peer workers
- capture the authority difference between a parent that owns workflow state
  and a specialist that performs bounded delegated work
- make the structural asymmetry explicit enough that later role and protocol
  docs inherit it rather than rediscovering it
- prevent specialists from quietly accumulating lifecycle authority that should
  stay with the parent layer

### Task 2: Skill Contract And Attachment Model

- define what a skill is responsible for versus what an agent definition is
  responsible for
- define skills as the atomic reusable units that parents and specialists
  consume rather than as alternate role or workflow definitions
- establish how skills attach to parents or specialists without becoming a
  second copy of the role, mode, or protocol model
- define a portable attachment vocabulary that distinguishes baseline and
  conditional skill use without turning attachment into workflow logic
- keep skills focused on reusable work procedures instead of letting them turn
  into ad hoc role definitions

### Task 3: Composition And Escalation Rules

- define when a new need should be handled by:
  - adding a skill to an existing parent or specialist
  - introducing a new specialist with a curated skill set and bounded authority
  - keeping responsibility parent-owned rather than delegating it
- document the decision rules that prevent the project from solving every new
  need by creating another specialist
- establish the initial structural constraints for:
  - parent agents with direct skills and delegation rights
  - specialist agents with focused scope, curated skills, and return contracts
  - skills as reusable atomic capabilities rather than standalone workflow
    owners

### Task 4: Context Atlas Structural Binding

- bind the portable structure model to Context Atlas's intended agentic shape
  without yet naming the full project role set
- make the structural pattern understandable before roles, modes, or protocols
  add more workflow detail
- keep the Story focused on how parents, specialists, and skills compose rather
  than on operational sequencing

## Sequencing

- define the parent-versus-specialist boundary first
- define the skill contract and attachment model next
- lock the composition and escalation rules
- bind the structure model to Context Atlas at a project-architecture level

## Risks And Unknowns

- The Story could blur into the role model if it starts assigning full project
  responsibilities too early.
- Skills could become a dumping ground for role instructions if the boundary is
  not kept tight.
- Specialists could multiply quickly if the decision rules are not explicit
  enough to discourage shallow capability splits.

## Exit Criteria

- Context Atlas has one documented structural model for parent agents,
  specialists, and skills
- the boundary between skill definition and agent definition is explicit
- the boundary between parent-agent and specialist-agent contract shapes is
  explicit
- skills are explicitly treated as atomic reusable units
- specialists are explicitly treated as focused agents built from curated
  skills plus bounded authority
- parent agents are explicitly treated as broader accountable actors that may
  both use direct skills and delegate to specialists
- there are clear decision rules for when a new need should be handled by
  adding a skill, introducing a specialist, or keeping responsibility
  parent-owned
- escalation and return-contract constraints reinforce those structural
  decisions instead of leaving them implicit
- later role and mode stories can build on this structure without redefining it

## Definition Of Done

- the Story's scoped Tasks are either completed or intentionally deferred with
  the reason documented
- all merged PR slices for the Story update the relevant local `__ai__.md`
  files in the same slice
- the Story preserves the distinction between structural composition, role
  accountability, and mode governance
- The repository preflight command passes on the Story feature branch before review
- the Story feature PR receives the QA Architecture Pass and Security Pass
  required for the `Story -> Epic` gate, and any findings are resolved on that
  same feature branch before human merge
- any structural templates or examples introduced by the Story remain derived
  from the canon rather than becoming a competing source of truth

## Related Artifacts

- [Context Atlas Agentic Development Product Definition](../agentic_development_product_definition.md)
- [Story 1 - Portable Agentic Development Canon](./story_1_portable_agentic_development_canon.md)
- [Context Atlas Agentic Development Profile](../../../Authoritative/Identity/Context-Atlas-Agentic-Development-Profile.md)
- [Delegation Model](../../../Authoritative/Canon/AgenticDevelopment/Delegation-Model.md)
- [Agent Composition Model](../../../Authoritative/Canon/AgenticDevelopment/Agent-Composition-Model.md)
- [Skill Attachment Model](../../../Authoritative/Canon/AgenticDevelopment/Skill-Attachment-Model.md)
- [Composition Decision Model](../../../Authoritative/Canon/AgenticDevelopment/Composition-Decision-Model.md)
- [Escalation Model](../../../Authoritative/Canon/AgenticDevelopment/Escalation-Model.md)
- [Craig Architecture](../../../Authoritative/Canon/Architecture/Craig-Architecture.md)

