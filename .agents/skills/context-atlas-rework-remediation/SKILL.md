# Context Atlas Skill: Rework Remediation

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill for translating findings or clarified defects into bounded corrective changes.

## Parent Boundary

- Conditional for:
  - `parent-backend`
  - `parent-documentation-uat`
  - `specialist-python-implementation`
- Does not dismiss findings on its own authority

## Workflow

1. Restate the finding in corrective terms
2. Identify the minimum responsible change
3. Implement or document the correction
4. Gather bounded verification evidence
5. Respond back through the relevant handoff or review surface

## Escalation Conditions

- The finding implies broader redesign than the current actor may perform
- The evidence needed to defend or fix the finding is unavailable
- Multiple findings conflict and cannot be satisfied within one bounded change

## Return Contract

- targeted corrective diff
- response-to-finding notes
- bounded verification summary
- explicit statement of what was corrected or defended

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/rework-remediation.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution pattern and expected outputs
