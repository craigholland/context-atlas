# Context Atlas Skill: Rework Remediation

> Generated surface notice
> This file is generated or regenerated from the authoritative Canon and Identity docs.
> Local edits may be overwritten by later regeneration. Durable semantic changes belong upstream in `docs/Authoritative/Canon/` or `docs/Authoritative/Identity/`.

## Purpose

Use this skill to translate accepted findings or clarified defects into bounded
corrective work with traceable intent.

## Parent Boundary

- Conditional for:
  - `parent-backend`
  - `parent-documentation-uat`
  - `specialist-python-implementation`
- This skill answers returned findings. It does not dismiss them on its own
  authority or turn rework into a stealth redesign.

## Workflow

1. Restate the finding in corrective terms.
2. Choose the narrowest responsible fix or rationale response.
3. Implement or document the correction and gather bounded evidence.
4. Return a response that maps the original finding to the resulting action.

## Escalation Conditions

- The finding implies redesign beyond the actor's allowed scope.
- The evidence needed to defend or fix the finding is unavailable.
- Multiple findings conflict and cannot be satisfied inside one bounded change.

## Return Contract

- targeted corrective diff or rationale response
- mapping from finding to correction
- bounded verification summary
- explicit note of what was corrected or defended

## Traceability

- Maintenance mode: `generated`
- Canon source:
  - `docs/Authoritative/Canon/AgenticDevelopment/Skills/rework-remediation.md`
- Identity binding source:
  - `docs/Authoritative/Identity/AgenticDevelopment/materialization_manifest.yaml`
- Adaptation note:
  - workflow and return contract are adapted from the canon skill's execution
    pattern and expected outputs
