# Context Atlas Skill: Review Findings Analysis

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for turning evidence into explicit findings, risk statements, and review outcomes.

## Parent Boundary

- Baseline for:
  - `parent-documentation-uat`
  - `parent-qa`
  - `specialist-review-readiness`
- Does not replace the underlying evidence-producing skills

## Workflow

1. Inspect the available evidence
2. Compare it to expected behavior or governing constraints
3. Classify the concern by kind, severity, and confidence
4. State the outcome or follow-up path explicitly

## Escalation Conditions

- Available evidence is too weak to support a responsible judgment
- The concern crosses into unsettled architecture, security, or product policy
- The required remedy would exceed the current review pass or role authority

## Return Contract

- findings summary
- acceptance or risk statement
- escalation or rework recommendation
- severity and confidence framing

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/review-findings-analysis.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
