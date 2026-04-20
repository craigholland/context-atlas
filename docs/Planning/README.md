# Planning

This directory holds forward-looking execution intent for Context Atlas.

Planning artifacts here should derive their decomposition model from [Craig Architecture - Planning And Decomposition](../Authoritative/Architecture/Craig-Architecture-Planning-And-Decomposition.md).

The expected planning stack is:

- `Epic` documents for major product or delivery surfaces
- `Story` documents for architectural increments inside an Epic
- `Task` documents for implementation-ready decomposition of a Story, including a basic `Task Status` field (`PLANNED`, `WORKING`, or `IMPLEMENTED`)
- task-level PR-plan documents for bounded reviewable slices

The expected execution loop for a Task is:

- open the task-level feature branch and feature PR early
- mark the Task `WORKING`
- implement bounded PR slices on short-lived slice branches and merge them back into the task feature branch
- when the Task's planned slices are complete, mark it `IMPLEMENTED`
- run local preflight on the feature branch, request `@codex review`, and resolve findings there
- hand the clean feature PR to a human reviewer before starting the next Task unless an explicit parallelization decision has been made

The current MVP planning stack lives under [MVP](./MVP/):

- [MVP Product Definition](./MVP/mvp_product_defintiion.md)
- [Story docs](./MVP/Stories/)
- [Task PR plans](./MVP/Stories/Tasks/)

The current agentic-development planning surface lives under [Agentic](./Agentic/):

- [Agentic Development Product Definition](./Agentic/agentic_development_product_definition.md)
- [Story docs](./Agentic/Stories/)
- [Task PR plans](./Agentic/Stories/Tasks/)

Those planning artifacts should derive their portable vocabulary and boundary
rules from [docs/Authoritative/AgenticDevelopment/README.md](../Authoritative/AgenticDevelopment/README.md)
and its neighboring canon docs instead of redefining those concepts at the
planning layer.

Contributors should prefer planning artifacts that move from:

- product-level intent at the Epic layer
- architectural shape at the Story layer
- implementation sequencing at the Task layer
- concrete code-touch expectations at the PR-plan layer

Planning documents are not authoritative project truth in the same sense as the `Authoritative` docs. They describe intended work, sequencing, and decomposition, and they must yield to the authoritative canon when conflicts appear.
