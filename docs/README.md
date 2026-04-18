# Documentation

This directory will hold the canonical project documentation for Context Atlas.

Before creating or editing project documents, start with [docs/Authoritative/Ontology/README.md](./Authoritative/Ontology/README.md). It contains the current guidance for how project documents should be structured, including the shared metadata template and the class-specific content templates.

The canonical semantic definitions for the document classes now live in [docs/Authoritative/Ontology/Documentation-Ontology.md](./Authoritative/Ontology/Documentation-Ontology.md). That document defines what `Authoritative`, `Planning`, `Reviews`, `Exploratory`, and `Releases` actually mean, what they are safe to use for, and how they should interact when they disagree.

The canonical definition of project mission, scope, and strategic boundaries now lives in [docs/Authoritative/Identity/Context-Atlas-Charter.md](./Authoritative/Identity/Context-Atlas-Charter.md). The project-specific operational model now lives in [docs/Authoritative/Identity/Context-Atlas-System-Model.md](./Authoritative/Identity/Context-Atlas-System-Model.md).

The canonical planning and decomposition reference now lives in [docs/Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md](./Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md). Project planning artifacts under [docs/Planning](./Planning/) should derive their decomposition model from that document.

The intended documentation ontology is:

- `Authoritative` for binding project truth
- `Planning` for forward-looking execution intent
- `Reviews` for findings, evidence, and assessments
- `Exploratory` for speculative investigation and prototypes
- `Releases` for operational and release-history context

This file exists to orient contributors toward the ontology and template canon before they author new project artifacts.
