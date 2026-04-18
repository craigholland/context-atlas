"""Centralized human-facing error messages for Context Atlas."""

from __future__ import annotations


class ErrorMessage:
    """Stable human-facing error messages grouped by their primary consumer."""

    # Error-code-aligned templates
    DOCUMENT_NO_CONTENT = "Document '%s' has empty content."
    DUPLICATE_BUDGET_SLOT_NAME = "Context budget slot '%s' is defined more than once."
    DUPLICATE_SOURCE_IDENTIFIER = "Context source '%s' is already registered."
    EMPTY_PACKET_QUERY = "Context packet query must not be empty."
    EMPTY_SOURCE_CONTENT = "Context source '%s' has empty content."
    EMPTY_SOURCE_IDENTIFIER = "Context source identifier must not be empty."
    INVALID_ASSEMBLY_DECISION = "Invalid context assembly decision: %s"
    INVALID_ASSEMBLY_REQUEST = "Invalid assembly request: %s"
    INVALID_BUDGET_ALLOCATION = "Invalid budget allocation: %s"
    INVALID_BUDGET_SLOT = "Invalid context budget slot '%s': %s"
    INVALID_BUDGET_TOTAL = "Invalid context budget total: %s"
    INVALID_CANDIDATE_STATE = "Invalid context candidate state: %s"
    INVALID_COMPRESSION_REQUEST = "Invalid compression request: %s"
    INVALID_CONFIGURATION = "Invalid configuration: %s"
    INVALID_MEMORY_ENTRY = "Invalid memory entry: %s"
    INVALID_MEMORY_SELECTION = "Invalid memory selection: %s"
    INVALID_PACKET_IDENTIFIER = "Context packet identifier must not be empty."
    INVALID_RANKING_REQUEST = "Invalid ranking request: %s"
    INVALID_RETRIEVAL_REQUEST = "Invalid retrieval request: %s"
    INVALID_SOURCE_ADAPTER_INPUT = "Invalid source adapter input: %s"
    INVALID_TRACE_IDENTIFIER = "Context trace identifier must not be empty."
    MISSING_REQUIRED_SETTING = "Required setting '%s' is missing."
    UNKNOWN = "Unknown Context Atlas error."
    UNSUPPORTED_DOCUMENT_CLASS = "Unsupported document class: %s"

    # services/assembly.py
    CUSTOM_BUDGET_REQUIRES_DOCUMENTS_SLOT = "custom budgets must define a 'documents' slot or omit slots to use the starter defaults"
    DEFAULT_TOP_K_MUST_BE_AT_LEAST_ONE = "default_top_k must be >= 1"
    DEFAULT_TOTAL_BUDGET_MUST_BE_AT_LEAST_ONE = "default_total_budget must be >= 1"
    FIELD_MUST_NOT_BE_BLANK_WHEN_PROVIDED = "%s must not be blank when provided"
    QUERY_MUST_NOT_BE_EMPTY = "query must not be empty"
    TOP_K_MUST_BE_AT_LEAST_ONE = "top_k must be >= 1, got %s"

    # infrastructure/config/environment.py
    ENVIRONMENT_PREFIX_MUST_NOT_BE_EMPTY = "environment prefix must not be empty"

    # domain/models/assembly.py
    ASSEMBLY_DECISION_REASON_CODES_REQUIRED = "at least one reason code is required"
    ASSEMBLY_DECISION_SOURCE_ID_REQUIRED = "source_id must not be empty"
    CANDIDATE_SCORE_MUST_BE_FINITE_WHEN_PROVIDED = (
        "candidate_score must be finite when provided"
    )
    POSITION_MUST_BE_AT_LEAST_ONE_WHEN_PROVIDED = "position must be >= 1 when provided"

    # domain/models/budget.py
    FIXED_SLOT_RESERVATIONS_EXCEED_TOTAL = (
        "fixed slot reservations (%s) exceed total tokens (%s)"
    )
    PRIORITY_MUST_BE_NON_NEGATIVE = "priority must be >= 0"
    SLOT_NAME_MUST_NOT_BE_EMPTY = "slot name must not be empty"
    TOKEN_LIMIT_MUST_BE_NON_NEGATIVE = "token limit must be >= 0"
    TOTAL_TOKENS_MUST_BE_AT_LEAST_ONE = "total tokens must be >= 1"
    UNNAMED_BUDGET_SLOT = "<unnamed>"

    # domain/models/memory.py
    ENTRY_ID_MUST_NOT_BE_EMPTY = "entry_id must not be empty"
    IMPORTANCE_MUST_BE_FINITE = "importance must be finite"
    IMPORTANCE_MUST_BE_NON_NEGATIVE = "importance must be >= 0"
    LAST_ACCESSED_AT_EPOCH_SECONDS_MUST_BE_FINITE = (
        "last_accessed_at_epoch_seconds must be finite"
    )
    LAST_ACCESSED_AT_EPOCH_SECONDS_MUST_BE_NON_NEGATIVE = (
        "last_accessed_at_epoch_seconds must be >= 0"
    )
    RECORDED_AT_EPOCH_SECONDS_MUST_BE_FINITE = (
        "recorded_at_epoch_seconds must be finite"
    )
    RECORDED_AT_EPOCH_SECONDS_MUST_BE_NON_NEGATIVE = (
        "recorded_at_epoch_seconds must be >= 0"
    )

    # domain/models/sources.py
    RANK_MUST_BE_AT_LEAST_ONE_WHEN_PROVIDED = "rank must be >= 1 when provided"
    SCORE_MUST_BE_FINITE_WHEN_PROVIDED = "score must be finite when provided"

    # domain/models/transformations.py
    COMPRESSED_CHARS_MUST_BE_NON_NEGATIVE = "compressed_chars must be >= 0"
    COMPRESSED_CHARS_MUST_NOT_EXCEED_ORIGINAL = (
        "compressed_chars must be <= original_chars for canonical compression results"
    )
    ESTIMATED_TOKENS_SAVED_MUST_BE_NON_NEGATIVE = "estimated_tokens_saved must be >= 0"
    ORIGINAL_CHARS_MUST_BE_NON_NEGATIVE = "original_chars must be >= 0"

    # domain/policies/budgeting.py
    ALLOCATED_TOKENS_MUST_BE_NON_NEGATIVE = "allocated_tokens for '%s' must be >= 0"
    ALLOCATED_TOKENS_MUST_NOT_EXCEED_REQUESTED = (
        "allocated_tokens for '%s' must be <= requested_tokens"
    )
    DUPLICATE_BUDGET_REQUESTS_NOT_ALLOWED = (
        "duplicate budget requests for the same slot are not allowed"
    )
    REMAINING_TOKENS_MUST_BE_NON_NEGATIVE = "remaining_tokens must be >= 0"
    REQUESTED_TOKENS_MUST_BE_NON_NEGATIVE = "requested_tokens for '%s' must be >= 0"
    UNKNOWN_BUDGET_SLOTS = "unknown budget slots: %s"
    WAS_REDUCED_MUST_MATCH_ALLOCATION_DELTA = (
        "was_reduced for '%s' must match the allocation delta"
    )

    # domain/policies/compression.py
    CHARS_PER_TOKEN_MUST_BE_AT_LEAST_ONE = "chars_per_token must be >= 1"
    CHARS_PER_TOKEN_MUST_BE_AT_LEAST_ONE_GOT = "chars_per_token must be >= 1, got %s"
    MAX_TOKENS_MUST_BE_AT_LEAST_ONE = "max_tokens must be >= 1, got %s"
    MIN_CHUNK_CHARS_MUST_BE_AT_LEAST_ONE = "min_chunk_chars must be >= 1"

    # domain/policies/memory.py
    DEDUP_THRESHOLD_MUST_BE_WITHIN_UNIT_INTERVAL = (
        "dedup_threshold must be in [0.0, 1.0]"
    )
    DECAY_RATE_MUST_BE_FINITE_AND_NON_NEGATIVE = "decay_rate must be finite and >= 0"
    MIN_EFFECTIVE_SCORE_MUST_BE_FINITE_AND_NON_NEGATIVE = (
        "min_effective_score must be finite and >= 0"
    )
    NOW_EPOCH_SECONDS_MUST_BE_FINITE_AND_NON_NEGATIVE = (
        "now_epoch_seconds must be finite and >= 0"
    )
    QUERY_BOOST_WEIGHT_MUST_BE_FINITE_AND_NON_NEGATIVE = (
        "query_boost_weight must be finite and >= 0"
    )
    SHORT_TERM_COUNT_MUST_BE_AT_LEAST_ONE = "short_term_count must be >= 1"

    # domain/policies/ranking.py
    LIMIT_MUST_BE_AT_LEAST_ONE = "limit must be >= 1, got %s"
    MINIMUM_SCORE_MUST_BE_FINITE = "minimum_score must be finite"

    # adapters/docs/filesystem.py
    DOCUMENT_PATH_DOES_NOT_EXIST = "document path does not exist: %s"
    DOCUMENT_PATH_IS_NOT_A_FILE = "document path is not a file: %s"
    DOCUMENT_PATH_OUTSIDE_ADAPTER_ROOT = (
        "document path '%s' is outside adapter root '%s'"
    )
    INVALID_FRONT_MATTER_IN_DOCUMENT = "invalid front matter in '%s': %s"
    ROOT_PATH_DOES_NOT_EXIST = "root path does not exist: %s"
    ROOT_PATH_IS_NOT_A_DIRECTORY = "root path is not a directory: %s"
    UNSUPPORTED_DOCUMENT_SUFFIX = "unsupported document suffix '%s' for %s"


__all__ = ["ErrorMessage"]
