# Canon

This directory holds the reusable, cross-project canon for Context Atlas.

It is intentionally separate from [../Identity/](../Identity/):

- `Canon/` defines portable meaning, boundaries, models, and reusable guidance
- `Identity/` defines how Context Atlas binds and applies that canon in this
  repository

## What Lives Here

- [Architecture](./Architecture/README.md): reusable Craig Architecture canon
- [AgenticDevelopment](./AgenticDevelopment/README.md): portable
  agentic-development canon for roles, skills, modes, protocols, materialization,
  validation, and drift control
- [RepoManagement](./RepoManagement/README.md): portable repo-management canon
  for principals, authorization, operations, branch-target policy, and audit
  identity
- [Ontology](./Ontology/README.md): reusable documentation ontology and metadata
  canon

## Reading Order

For most contributors:

1. [Ontology](./Ontology/README.md)
2. the relevant domain canon:
   - [Architecture](./Architecture/README.md)
   - [AgenticDevelopment](./AgenticDevelopment/README.md)
   - [RepoManagement](./RepoManagement/README.md)
3. the project-specific bindings under [../Identity/](../Identity/)
4. the forward-looking delivery surfaces under [../../Planning/](../../Planning/)

## Boundary Rule

Do not place Context Atlas-specific operational bindings, chosen role rosters,
provider selections, or runtime policy here unless the portable canon is what is
actually changing. Those project-specific choices belong under
[../Identity/](../Identity/).
