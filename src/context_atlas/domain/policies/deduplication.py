"""Shared lexical/structural duplicate-detection helpers for policy code."""

from __future__ import annotations

from dataclasses import dataclass
import re


@dataclass(frozen=True, slots=True)
class DuplicateContentAssessment:
    """Structured result of comparing two content strings for duplication."""

    is_duplicate: bool
    match_kind: str | None
    overlap_ratio: float
    left_key: str
    right_key: str


def build_duplicate_content_key(content: str) -> str:
    """Return the normalized text key used by shared duplicate handling."""

    return " ".join(content.casefold().split())


def assess_duplicate_content(
    content_a: str,
    content_b: str,
    *,
    threshold: float,
) -> DuplicateContentAssessment:
    """Apply the bounded lexical/structural duplicate baseline."""

    left_key = build_duplicate_content_key(content_a)
    right_key = build_duplicate_content_key(content_b)
    if not left_key or not right_key:
        return DuplicateContentAssessment(
            is_duplicate=False,
            match_kind=None,
            overlap_ratio=0.0,
            left_key=left_key,
            right_key=right_key,
        )

    if left_key == right_key:
        return DuplicateContentAssessment(
            is_duplicate=True,
            match_kind="exact_key_match",
            overlap_ratio=1.0,
            left_key=left_key,
            right_key=right_key,
        )

    if left_key in right_key or right_key in left_key:
        return DuplicateContentAssessment(
            is_duplicate=True,
            match_kind="normalized_containment",
            overlap_ratio=1.0,
            left_key=left_key,
            right_key=right_key,
        )

    overlap_ratio = _jaccard_token_overlap(left_key, right_key)
    return DuplicateContentAssessment(
        is_duplicate=overlap_ratio >= threshold,
        match_kind="token_overlap" if overlap_ratio >= threshold else None,
        overlap_ratio=overlap_ratio,
        left_key=left_key,
        right_key=right_key,
    )


def _jaccard_token_overlap(left_key: str, right_key: str) -> float:
    """Return a simple lexical overlap ratio for normalized content."""

    tokens_a = set(re.findall(r"[a-z0-9]+", left_key))
    tokens_b = set(re.findall(r"[a-z0-9]+", right_key))
    union_size = len(tokens_a | tokens_b)
    if union_size == 0:
        return 0.0
    return len(tokens_a & tokens_b) / union_size
