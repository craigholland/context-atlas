"""Centralized human-facing error messages for Context Atlas."""

from __future__ import annotations


class ErrorMessage:
    """Stable human-facing error messages and reusable detail fragments."""

    UNKNOWN = "Unknown Context Atlas error."
    DOCUMENT_NO_CONTENT = "Document '%s' has empty content."
    INVALID_CONFIGURATION = "Invalid configuration: %s"
    MISSING_REQUIRED_SETTING = "Required setting '%s' is missing."
    EMPTY_SOURCE_IDENTIFIER = "Context source identifier must not be empty."
    EMPTY_SOURCE_CONTENT = "Context source '%s' has empty content."
    INVALID_CANDIDATE_STATE = "Invalid context candidate state: %s"
    INVALID_BUDGET_TOTAL = "Invalid context budget total: %s"
    INVALID_BUDGET_SLOT = "Invalid context budget slot '%s': %s"
    DUPLICATE_BUDGET_SLOT_NAME = "Context budget slot '%s' is defined more than once."
    INVALID_ASSEMBLY_DECISION = "Invalid context assembly decision: %s"
    INVALID_TRACE_IDENTIFIER = "Context trace identifier must not be empty."
    INVALID_PACKET_IDENTIFIER = "Context packet identifier must not be empty."
    EMPTY_PACKET_QUERY = "Context packet query must not be empty."
    DUPLICATE_SOURCE_IDENTIFIER = "Context source '%s' is already registered."
    INVALID_ASSEMBLY_REQUEST = "Invalid assembly request: %s"
    INVALID_RETRIEVAL_REQUEST = "Invalid retrieval request: %s"
    INVALID_RANKING_REQUEST = "Invalid ranking request: %s"
    INVALID_BUDGET_ALLOCATION = "Invalid budget allocation: %s"
    INVALID_COMPRESSION_REQUEST = "Invalid compression request: %s"
    INVALID_MEMORY_ENTRY = "Invalid memory entry: %s"
    INVALID_MEMORY_SELECTION = "Invalid memory selection: %s"
    INVALID_SOURCE_ADAPTER_INPUT = "Invalid source adapter input: %s"
    UNSUPPORTED_DOCUMENT_CLASS = "Unsupported document class: %s"
    DEFAULT_TOP_K_MUST_BE_AT_LEAST_ONE = "default_top_k must be >= 1"
    DEFAULT_TOTAL_BUDGET_MUST_BE_AT_LEAST_ONE = "default_total_budget must be >= 1"
    QUERY_MUST_NOT_BE_EMPTY = "query must not be empty"
    TOP_K_MUST_BE_AT_LEAST_ONE = "top_k must be >= 1, got %s"
    CUSTOM_BUDGET_REQUIRES_DOCUMENTS_SLOT = "custom budgets must define a 'documents' slot or omit slots to use the starter defaults"
    FIELD_MUST_NOT_BE_BLANK_WHEN_PROVIDED = "%s must not be blank when provided"
    ENVIRONMENT_PREFIX_MUST_NOT_BE_EMPTY = "environment prefix must not be empty"
    ASSEMBLY_DECISION_SOURCE_ID_REQUIRED = "source_id must not be empty"
    ASSEMBLY_DECISION_REASON_CODES_REQUIRED = "at least one reason code is required"
    UNNAMED_BUDGET_SLOT = "<unnamed>"
    CANDIDATE_SCORE_MUST_BE_FINITE_WHEN_PROVIDED = (
        "candidate_score must be finite when provided"
    )
    POSITION_MUST_BE_AT_LEAST_ONE_WHEN_PROVIDED = "position must be >= 1 when provided"
    SLOT_NAME_MUST_NOT_BE_EMPTY = "slot name must not be empty"
    TOKEN_LIMIT_MUST_BE_NON_NEGATIVE = "token limit must be >= 0"
    PRIORITY_MUST_BE_NON_NEGATIVE = "priority must be >= 0"
    TOTAL_TOKENS_MUST_BE_AT_LEAST_ONE = "total tokens must be >= 1"
    FIXED_SLOT_RESERVATIONS_EXCEED_TOTAL = (
        "fixed slot reservations (%s) exceed total tokens (%s)"
    )
    ENTRY_ID_MUST_NOT_BE_EMPTY = "entry_id must not be empty"
    RECORDED_AT_EPOCH_SECONDS_MUST_BE_FINITE = (
        "recorded_at_epoch_seconds must be finite"
    )
    RECORDED_AT_EPOCH_SECONDS_MUST_BE_NON_NEGATIVE = (
        "recorded_at_epoch_seconds must be >= 0"
    )
    IMPORTANCE_MUST_BE_FINITE = "importance must be finite"
    IMPORTANCE_MUST_BE_NON_NEGATIVE = "importance must be >= 0"
    LAST_ACCESSED_AT_EPOCH_SECONDS_MUST_BE_FINITE = (
        "last_accessed_at_epoch_seconds must be finite"
    )
    LAST_ACCESSED_AT_EPOCH_SECONDS_MUST_BE_NON_NEGATIVE = (
        "last_accessed_at_epoch_seconds must be >= 0"
    )
    SCORE_MUST_BE_FINITE_WHEN_PROVIDED = "score must be finite when provided"
    RANK_MUST_BE_AT_LEAST_ONE_WHEN_PROVIDED = "rank must be >= 1 when provided"
    ORIGINAL_CHARS_MUST_BE_NON_NEGATIVE = "original_chars must be >= 0"
    COMPRESSED_CHARS_MUST_BE_NON_NEGATIVE = "compressed_chars must be >= 0"
    COMPRESSED_CHARS_MUST_NOT_EXCEED_ORIGINAL = (
        "compressed_chars must be <= original_chars for canonical compression results"
    )
    ESTIMATED_TOKENS_SAVED_MUST_BE_NON_NEGATIVE = "estimated_tokens_saved must be >= 0"
    REQUESTED_TOKENS_MUST_BE_NON_NEGATIVE = "requested_tokens for '%s' must be >= 0"
    ALLOCATED_TOKENS_MUST_BE_NON_NEGATIVE = "allocated_tokens for '%s' must be >= 0"
    ALLOCATED_TOKENS_MUST_NOT_EXCEED_REQUESTED = (
        "allocated_tokens for '%s' must be <= requested_tokens"
    )
    WAS_REDUCED_MUST_MATCH_ALLOCATION_DELTA = (
        "was_reduced for '%s' must match the allocation delta"
    )
    REMAINING_TOKENS_MUST_BE_NON_NEGATIVE = "remaining_tokens must be >= 0"
    DUPLICATE_BUDGET_REQUESTS_NOT_ALLOWED = (
        "duplicate budget requests for the same slot are not allowed"
    )
    UNKNOWN_BUDGET_SLOTS = "unknown budget slots: %s"
    CHARS_PER_TOKEN_MUST_BE_AT_LEAST_ONE = "chars_per_token must be >= 1"
    CHARS_PER_TOKEN_MUST_BE_AT_LEAST_ONE_GOT = "chars_per_token must be >= 1, got %s"
    MIN_CHUNK_CHARS_MUST_BE_AT_LEAST_ONE = "min_chunk_chars must be >= 1"
    MAX_TOKENS_MUST_BE_AT_LEAST_ONE = "max_tokens must be >= 1, got %s"
    SHORT_TERM_COUNT_MUST_BE_AT_LEAST_ONE = "short_term_count must be >= 1"
    DECAY_RATE_MUST_BE_FINITE_AND_NON_NEGATIVE = "decay_rate must be finite and >= 0"
    DEDUP_THRESHOLD_MUST_BE_WITHIN_UNIT_INTERVAL = (
        "dedup_threshold must be in [0.0, 1.0]"
    )
    MIN_EFFECTIVE_SCORE_MUST_BE_FINITE_AND_NON_NEGATIVE = (
        "min_effective_score must be finite and >= 0"
    )
    QUERY_BOOST_WEIGHT_MUST_BE_FINITE_AND_NON_NEGATIVE = (
        "query_boost_weight must be finite and >= 0"
    )
    NOW_EPOCH_SECONDS_MUST_BE_FINITE_AND_NON_NEGATIVE = (
        "now_epoch_seconds must be finite and >= 0"
    )
    MINIMUM_SCORE_MUST_BE_FINITE = "minimum_score must be finite"
    LIMIT_MUST_BE_AT_LEAST_ONE = "limit must be >= 1, got %s"
    ROOT_PATH_DOES_NOT_EXIST = "root path does not exist: %s"
    ROOT_PATH_IS_NOT_A_DIRECTORY = "root path is not a directory: %s"
    DOCUMENT_PATH_DOES_NOT_EXIST = "document path does not exist: %s"
    DOCUMENT_PATH_IS_NOT_A_FILE = "document path is not a file: %s"
    UNSUPPORTED_DOCUMENT_SUFFIX = "unsupported document suffix '%s' for %s"
    DOCUMENT_PATH_OUTSIDE_ADAPTER_ROOT = (
        "document path '%s' is outside adapter root '%s'"
    )
    INVALID_FRONT_MATTER_IN_DOCUMENT = "invalid front matter in '%s': %s"


__all__ = ["ErrorMessage"]
