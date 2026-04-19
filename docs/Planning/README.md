# Planning

This directory holds forward-looking execution intent for Context Atlas.

Planning artifacts here should derive their decomposition model from [Craig Architecture - Planning And Decomposition](../Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md).

The expected planning stack is:

- `Epic` documents for major product or delivery surfaces
- `Story` documents for architectural increments inside an Epic
- `Task` documents for implementation-ready decomposition of a Story, including a basic `Task Status` field (`PLANNED`, `WORKING`, or `IMPLEMENTED`)
- task-level PR-plan documents for bounded reviewable slices

The current MVP planning stack lives under [MVP](./MVP/):

- [MVP Product Definition](./MVP/mvp_product_defintiion.md)
- [Story docs](./MVP/Stories/)
- [Task PR plans](./MVP/Stories/Tasks/)

Contributors should prefer planning artifacts that move from:

- product-level intent at the Epic layer
- architectural shape at the Story layer
- implementation sequencing at the Task layer
- concrete code-touch expectations at the PR-plan layer

Planning documents are not authoritative project truth in the same sense as the `Authoritative` docs. They describe intended work, sequencing, and decomposition, and they must yield to the authoritative canon when conflicts appear.
