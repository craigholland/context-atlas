# Context Atlas Skill: Backend Architecture SOLID

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for reasoning about backend design through cohesion, responsibility, substitution, interface, and dependency-inversion concerns commonly associated with SOLID analysis.

## Parent Boundary

- Conditional for:
  - `parent-backend`
  - `parent-qa`
  - `specialist-python-implementation`
  - `specialist-review-readiness`
- Does not replace full system-architecture reasoning

## Workflow

1. Inspect the current responsibility and dependency shape
2. Test whether the abstraction surface matches real change and substitution pressure
3. Surface findings about cohesion, interface size, and inversion strategy
4. Propose the narrowest design improvement that addresses the risk

## Escalation Conditions

- The design issue is really a higher-level architecture or ownership issue
- Remediation would require broad public-interface changes
- The current codebase lacks a stable design direction to anchor the analysis

## Return Contract

- design-quality notes
- abstraction or cohesion findings
- focused refactoring guidance

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/backend-architecture-solid.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
