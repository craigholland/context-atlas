---
template_id: base_metadata
template_kind: metadata
template_version: 1.0.0
status: active
supersedes: []
---

# Base Metadata

Every downstream Context Atlas document should start with a shared metadata block.

We prefer YAML front matter because it is readable in GitHub, works well in plain Markdown, and is easy for tooling to parse later.

## Template

```md
---
id: context-atlas-example
title: Example Title
summary: One sentence describing the document.
doc_class: authoritative
template_refs:
  metadata: base_metadata@1.0.0
  content: authoritative_content@1.0.0
status: active
created: 2026-04-16
last_reviewed: 2026-04-16
owners: [core]
tags: [example, ontology]
related: []
supersedes: []
---
```

## Field Guidance

- `id`: Stable identifier for the artifact. Prefer lowercase kebab-case.
- `title`: Human-readable document title.
- `summary`: Single-sentence description of what the document is for.
- `doc_class`: The document ontology class, such as `authoritative`, `planning`, `reviews`, `exploratory`, or `releases`.
- `template_refs`: The template artifacts and versions this document conforms to. At minimum, include `metadata` and `content`.
- `status`: Lifecycle state such as `draft`, `active`, `superseded`, or `archived`.
- `created`: Original creation date.
- `last_reviewed`: Most recent date the content was deliberately reviewed for accuracy.
- `owners`: Responsible maintainers or owning groups.
- `tags`: Short descriptive tags for search and grouping.
- `related`: Paths or links to nearby artifacts.
- `supersedes`: IDs or paths for artifacts this document replaces.

## Notes

- We use `last_reviewed` instead of `last_updated`. Git already records raw file changes, while review date better captures document trust.
- We use `template_refs` instead of a single `template_version` because metadata and content templates may evolve independently.
- This file is itself a versioned template artifact. Its own `template_version` appears in the front matter above, not inside the downstream document example block.
- The metadata block is governed content, not write-once boilerplate. When a document changes meaningfully, contributors should review whether `summary`, `last_reviewed`, `tags`, `related`, and when relevant `status` or `supersedes`, still describe the document honestly.
- `tags` should support discoverability and grouping of the document as it exists now, not only the concepts it had when first created.
- Documents that bind to neighboring authoritative surfaces, machine-readable artifacts, or runtime materializations should treat `related` and `summary` as part of the governance surface, not as optional decoration.
- When a document's boundary, neighboring canon, or validation/trust model changes, contributors should review whether `tags` and `related` still make that change discoverable to both humans and tooling.
- Additional fields may be added later once the project formalizes authority, safe-to-act-on semantics, and provenance requirements at the ontology level.
- The metadata block should stay compact. Fields should earn their place by supporting governance, review, or machine interpretation.
