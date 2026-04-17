---
template_id: general_content
template_kind: content
template_version: 1.0.0
status: active
supersedes: []
applies_to: [reviews, exploratory, releases]
---

# General Content

General content is the fallback body template for document classes that do not yet have a dedicated structure.

This currently applies to Reviews, Exploratory, and Releases documents unless a more specific ontology template is added later.

## Template

Use this body template together with the shared metadata block from [base_metadata.md](./base_metadata.md).

Downstream documents using this fallback should declare:

```md
template_refs:
  metadata: base_metadata@1.0.0
  content: general_content@1.0.0
```

```md
# Document Title

## Context

Briefly explain what this document is about and why it exists.

## Content

Write the main body here.

## Notes Or Findings

Capture the most important observations, implications, or takeaways.

## Related Artifacts

- [Related Document](./related-document.md)
```

## Expectations

- Documents using this fallback template should keep their `template_refs` aligned with the actual template versions they follow.
- Use this template when a document needs structure but does not yet warrant a class-specific schema.
- Keep the body honest about whether it is descriptive, evaluative, or speculative.
- If a recurring document class starts stretching this template too far, that is a signal to create a dedicated content template for it.
