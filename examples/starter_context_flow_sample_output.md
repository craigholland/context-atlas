# Starter Context Flow Sample Output

This file shows one bounded successful run from the current getting-started
path.

It was captured from:

```bash
python examples/starter_context_flow.py examples/codex_repository_workflow/sample_repo/docs "How should planning docs be treated?"
```

The `packet_id` and `trace_id` values below are normalized because those
identifiers vary from run to run. The rest of the output comes from a real run
against the checked-in sample repository docs.

## Rendered Context

```text
# Repository Guidance

Repository architecture guidance is authoritative for contributors working in
this sample repository.

When planning notes, draft reviews, or exploratory documents discuss the same
repository process, engineers should follow this architecture guidance first and
then update lower-authority documents so they remain aligned.

For repository planning docs specifically:

- keep the authoritative architecture guidance as the binding reference
- update planning docs to reflect that guidance rather than replacing it
- keep owner files and review notes aligned in the same implementation slice

# Current Work

The current implementation plan proposes changes to repository planning docs,
task review cadence, and contributor guidance.

These notes are useful for sequencing work, but they should not override the
authoritative repository guidance when both discuss the same process.

If planning documents drift away from the authoritative architecture guidance,
the planning docs should be updated so the two remain consistent.

# Review Notes

Review findings for this sample repository note that contributors sometimes
edit planning docs first and only later realign architecture guidance.

Those findings are useful as lower-authority evidence and follow-up input, but
they should remain subordinate to the authoritative repository guidance when an
engineer is deciding which repository process to follow.
```

## Packet Inspection

```text
Packet
- packet_id: packet_<sample>
- query: How should planning docs be treated?
- selected_candidates: 3
- selected_memory_entries: 0
- total_items: 3
- compression_applied: no
- trace_attached: yes

Budget
- total_tokens: 2048
- fixed_reserved_tokens: 512
- unreserved_tokens: 1536
- unallocated_tokens: 1572
- slots:
  - memory: limit=512, mode=fixed, priority=0
  - documents: limit=2048, mode=elastic, priority=10

Selected Sources
- Authoritative/Canon/Architecture/Repo-Guidance.md: title=Repository Guidance; class=authoritative; authority=binding; rank=1; score=0.2518
- Planning/Current-Work.md: title=Current Work; class=planning; authority=preferred; rank=2; score=0.2348
- Reviews/Review-Notes.md: title=Review Notes; class=reviews; authority=advisory; rank=3; score=0.0763

Retained Memory
- none

Compression
- effective_strategy: extractive
- was_applied: no
- original_chars: 1430
- compressed_chars: 1430
- compression_ratio: 1.0
- estimated_tokens_saved: 0
- source_ids: Authoritative/Canon/Architecture/Repo-Guidance.md, Planning/Current-Work.md, Reviews/Review-Notes.md
```

## Trace Inspection

```text
Trace
- trace_id: trace_<sample>
- decision_count: 6
- included_count: 5
- excluded_count: 0
- transformed_count: 0
- deferred_count: 1
- budget_total_tokens: 2048
- budget_fixed_reserved_tokens: 512
- budget_unreserved_tokens: 1536
- budget_unallocated_tokens: 1572
- compression_strategy: extractive

Included Decisions
- [1] Authoritative/Canon/Architecture/Repo-Guidance.md; action=included; reasons=direct_match,higher_authority_preferred,authority_priority; score=0.2518
- [2] Planning/Current-Work.md; action=included; reasons=direct_match,higher_authority_preferred,authority_priority; score=0.2348
- [3] Reviews/Review-Notes.md; action=included; reasons=direct_match; score=0.0763
- [5] budget:documents; action=included; reasons=budget_available; score=476.0000
- [6] compression; action=included; reasons=budget_available; score=476.0000

Excluded Decisions
- none

Transformed Decisions
- none

Deferred Decisions
- [4] budget:memory; action=deferred; reasons=slot_exhausted; score=0.0000; why=No tokens were requested for this slot.

Trace Metadata
- budget_allocated_tokens: 476
- budget_budget_total_tokens: 2048
- budget_fixed_reserved_tokens: 512
- budget_slot_count: 2
- budget_total_tokens: 2048
- budget_unallocated_tokens: 1572
- budget_unreserved_tokens: 1536
- compression_applied: false
- compression_compression_strategy: extractive
- compression_max_tokens: 476
- compression_present: true
- compression_source_count: 3
- compression_strategy: extractive
- compression_token_estimator: starter_heuristic
- memory_input_entry_count: 0
- memory_memory_policy: starter_memory_retention_policy
- memory_selected_entry_count: 0
- ranked_candidate_count: 3
- ranking_dedup_threshold: 0.72
- ranking_deduplicated_candidate_count: 0
- ranking_excluded_candidate_count: 0
- ranking_included_candidate_count: 3
- ranking_input_candidate_count: 3
- ranking_ranking_policy: starter_candidate_ranking_policy
- retrieved_candidate_count: 3
- selected_memory_collectors:
- selected_memory_count: 0
- selected_memory_source_classes:
- selected_memory_source_families:
- selected_source_classes: authoritative,planning,reviews
- selected_source_collector_counts: filesystem_document_source_adapter=3
- selected_source_collectors: filesystem_document_source_adapter
- selected_source_families: document
- selected_source_family_counts: document=3
- service: context_assembly_service
```
