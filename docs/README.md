# Documentation

This directory holds the canonical project documentation for Context Atlas.

## Guides

User-facing setup and workflow help now lives under
[docs/Guides/README.md](./Guides/README.md).

If you are trying to evaluate or set up Context Atlas as a product, start there
before reading `examples/` or the deeper architecture/planning canon.

Before creating or editing project documents, start with [docs/Authoritative/Ontology/README.md](./Authoritative/Ontology/README.md). It contains the current guidance for how project documents should be structured, including the shared metadata template and the class-specific content templates.

The canonical semantic definitions for the document classes now live in [docs/Authoritative/Ontology/Documentation-Ontology.md](./Authoritative/Ontology/Documentation-Ontology.md). That document defines what `Authoritative`, `Planning`, `Reviews`, `Exploratory`, and `Releases` actually mean, what they are safe to use for, and how they should interact when they disagree.

The canonical definition of project mission, scope, and strategic boundaries now lives in [docs/Authoritative/Identity/Context-Atlas-Charter.md](./Authoritative/Identity/Context-Atlas-Charter.md). The project-specific operational model now lives in [docs/Authoritative/Identity/Context-Atlas-System-Model.md](./Authoritative/Identity/Context-Atlas-System-Model.md).

The reusable Craig Architecture canon now has its own directory index at [docs/Authoritative/Architecture/README.md](./Authoritative/Architecture/README.md). Contributors looking for the architecture set as a whole should start there before diving into individual supplements.

The canonical planning and decomposition reference now lives in [docs/Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md](./Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md). Project planning artifacts under [docs/Planning](./Planning/) should derive their decomposition model from that document.

The intended documentation ontology is:

- `Authoritative` for binding project truth
- `Planning` for forward-looking execution intent
- `Reviews` for findings, evidence, and assessments
- `Exploratory` for speculative investigation and prototypes
- `Releases` for operational and release-history context

This file exists to orient contributors toward the ontology and template canon before they author new project artifacts.
