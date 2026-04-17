---
template_id: authoritative_content
template_kind: content
template_version: 1.0.0
status: active
supersedes: []
applies_to: [authoritative]
---

# Authoritative Content

Authoritative documents define binding project truth.

They should be written clearly enough that a future contributor or agent can safely act on them unless a newer authoritative artifact supersedes them.

## Template

Use this body template together with the shared metadata block from [base_metadata.md](./base_metadata.md).

Downstream authoritative documents should declare:

```md
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
```

```md
# Document Title

## Purpose

State what this document defines and why it exists.

## Scope

Define what is in scope and what is explicitly outside scope.

## Binding Decisions

List the decisions, rules, or definitions this document establishes.

## Constraints

Record hard constraints, invariants, or requirements that follow from the decisions above.

## Non-Goals

Clarify what this document does not attempt to decide or optimize.

## Related Artifacts

- [Related Document](./related-document.md)
```

## Expectations

- Authoritative documents should keep their `template_refs` aligned with the actual template versions they follow.
- Prefer explicit decisions over implied intent.
- Separate binding truth from examples and speculation.
- Avoid burying critical rules in long narrative sections.
- If the document replaces an older authoritative artifact, capture that in metadata and explain the change plainly.
