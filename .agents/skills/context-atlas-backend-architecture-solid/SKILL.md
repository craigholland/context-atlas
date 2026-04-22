# Context Atlas Skill: Backend Architecture SOLID

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to evaluate backend design for cohesion, responsibility sizing,
interface quality, substitution safety, and useful dependency inversion.

## Parent Boundary

- Conditional for:
  - `parent-backend`
  - `parent-qa`
  - `specialist-python-implementation`
  - `specialist-review-readiness`
- This skill is a design-quality lens. It should stay tied to concrete design
  concerns rather than turning every change into an abstraction exercise.

## Workflow

1. Inspect the current responsibility and dependency shape.
2. Test whether abstractions match real seams and change pressure.
3. Identify cohesion, interface size, substitution, or inversion risks.
4. Return the narrowest design improvement that addresses the observed risk.

## Escalation Conditions

- The issue is really a higher-level architecture or ownership problem.
- Remediation would require broad public-interface change.
- The surrounding codebase lacks a stable design direction to anchor analysis.

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
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
