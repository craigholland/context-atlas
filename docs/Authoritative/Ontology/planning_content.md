---
template_id: planning_content
template_kind: content
template_version: 1.0.0
status: active
supersedes: []
applies_to: [planning]
---

# Planning Content

Planning documents describe intended work, sequencing, and execution shape.

They are useful guides for implementation, but they do not override authoritative documents when the two conflict.

## Template

Use this body template together with the shared metadata block from [base_metadata.md](./base_metadata.md).

Downstream planning documents should declare:

```md
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
```

```md
# Document Title

## Objective

Describe the work this plan is trying to achieve.

## Inputs

List the authoritative documents, assumptions, and dependencies this plan relies on.

## Proposed Work

Describe the planned slices, milestones, or workstreams.

## Sequencing

Explain the intended order of work and any gating dependencies.

## Risks And Unknowns

Call out unresolved questions, uncertainties, and external dependencies.

## Exit Criteria

Define what would make this plan complete or good enough to supersede.

## Related Artifacts

- [Related Document](./related-document.md)
```

## Expectations

- Planning documents should keep their `template_refs` aligned with the actual template versions they follow.
- Plans should cite the authoritative sources they derive from.
- Plans may propose work, but they should not redefine architecture or policy without an accompanying authoritative change.
- Unknowns should be surfaced directly instead of being hidden inside roadmap prose.
