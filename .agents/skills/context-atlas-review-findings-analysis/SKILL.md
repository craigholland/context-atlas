# Context Atlas Skill: Review Findings Analysis

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to turn evidence into explicit findings, risk statements, and
review outcomes that other actors can actually respond to.

## Parent Boundary

- Baseline for:
  - `parent-documentation-uat`
  - `parent-qa`
  - `specialist-review-readiness`
- This skill frames review observations. It does not replace the evidence-
  producing skills or turn review into implementation ownership.

## Workflow

1. Inspect the available evidence and governing expectations.
2. Distinguish observation, finding, risk, severity, and confidence clearly.
3. Write findings specific enough for rework or follow-up.
4. Return an explicit acceptance, hold, or escalation recommendation.

## Escalation Conditions

- Available evidence is too weak for a responsible judgment.
- The concern crosses into unsettled architecture, security, or product policy.
- The remedy exceeds the current review pass or role authority.

## Return Contract

- findings summary
- severity and confidence framing
- acceptance or risk statement
- rework or escalation recommendation

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/review-findings-analysis.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
