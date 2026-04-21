---
id: context-atlas-hardening-task-2-2-boilerplate-and-front-matter-handling
title: Task 2.2 - Boilerplate And Front-Matter Handling PR Plan
summary: Defines the PR sequence for making duplicate detection less sensitive to repeated boilerplate, front matter, and template prefixes.
doc_class: planning
template_refs:
  metadata: base_metadata@1.0.0
  content: planning_content@1.0.0
status: implemented
created: 2026-04-20
last_reviewed: 2026-04-20
owners: [core]
tags: [hardening, task, pr-plan, deduplication, boilerplate, front-matter]
related:
  - ../story_2_duplicate_detection_and_similarity_quality.md
  - ../../context_assembly_hardening_product_definition.md
supersedes: []
---

# Task 2.2 - Boilerplate And Front-Matter Handling PR Plan

## Objective

Improve duplicate detection so shared headers, governed document front matter,
and repeated template prefixes do not overwhelm the near-duplicate baseline.

## Task Status

IMPLEMENTED

## Inputs

- [Story 2 - Duplicate Detection And Similarity Quality](../story_2_duplicate_detection_and_similarity_quality.md)
- shared duplicate surface defined in Task 2.1
- current false-positive examples from memory and ranking behavior

## Proposed Work

### PR - A: Normalization Boundary

- define what boilerplate or front-matter normalization happens before
  duplicate comparison
- keep the normalization bounded and generic rather than document-type
  encyclopedic
- make the normalization compatible with the shared duplicate surface instead
  of becoming a parallel path

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `src/context_atlas/domain/policies/memory.py`
- `src/context_atlas/domain/policies/ranking.py`

#### Update AI files
- `src/context_atlas/domain/`

### PR - B: Prefix-Heavy False-Positive Coverage

- add regressions that cover shared headers with divergent document bodies
- prove that boilerplate similarity alone no longer drives duplicate outcomes
- keep tests centered on governed Atlas-style text rather than generic NLP
  corpora

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `tests/test_candidate_ranking.py`
- `tests/test_memory_policy.py`

#### Update AI files
- `tests/`

### PR - C: Story Reinforcement

- align Story 2 with the chosen normalization boundary
- document any intentionally unsupported edge cases so later Tasks do not keep
  expanding the baseline

#### Expected New Files
- none expected

#### Expected Existing Files Updated
- `docs/Planning/Hardening/Stories/story_2_duplicate_detection_and_similarity_quality.md`

#### Update AI files
- `.`

## Sequencing

- define normalization boundary first
- prove prefix-heavy false positives are addressed second
- reinforce scope and remaining edges last

## Risks And Unknowns

- Normalization can become too clever if it starts encoding content-type
  special cases that should remain outside the baseline.
- False-positive tests can still be too narrow if they only use one boilerplate
  pattern.

## Exit Criteria

- boilerplate and front matter are handled explicitly in duplicate detection
- shared prefixes alone no longer dominate duplicate outcomes
- Story 2 keeps a bounded normalization story instead of widening scope
- the supported normalization boundary is explicit: strip bounded top-of-file
  front matter and discount a bounded shared leading line prefix only when both
  sides still retain meaningful body content

## Related Artifacts

- [Story 2 - Duplicate Detection And Similarity Quality](../story_2_duplicate_detection_and_similarity_quality.md)

