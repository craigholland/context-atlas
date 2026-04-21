"""Shared lexical/structural duplicate-detection helpers for policy code.

The bounded baseline intentionally stays narrow:
- exact normalized text equality
- bounded leading front-matter stripping
- bounded shared-prefix discounting for pairwise comparison
- normalized containment
- token-overlap comparison

It does not attempt embeddings, semantic similarity, or provider-specific
matching.
"""

from __future__ import annotations

from dataclasses import dataclass
import re


_UNICODE_TOKEN_PATTERN = re.compile(r"[^\W_]+", flags=re.UNICODE)
_FRONT_MATTER_DELIMITER = "---"
_FRONT_MATTER_TERMINATORS = {"---", "..."}
_MAX_FRONT_MATTER_LINES = 40
_MAX_SHARED_PREFIX_LINES = 6
_MAX_SHARED_PREFIX_CHARS = 240
_MIN_SHARED_PREFIX_LINES = 2
_MIN_REMAINING_LINES_AFTER_PREFIX = 2


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

    return _join_normalized_lines(_normalized_content_lines(content))


def assess_duplicate_content(
    content_a: str,
    content_b: str,
    *,
    threshold: float,
) -> DuplicateContentAssessment:
    """Apply the bounded lexical/structural duplicate baseline."""

    left_lines = _normalized_content_lines(content_a)
    right_lines = _normalized_content_lines(content_b)
    left_key = _join_normalized_lines(left_lines)
    right_key = _join_normalized_lines(right_lines)
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

    effective_left_lines, effective_right_lines = _trim_shared_leading_prefix(
        left_lines,
        right_lines,
    )
    effective_left_key = _join_normalized_lines(effective_left_lines)
    effective_right_key = _join_normalized_lines(effective_right_lines)

    if (
        effective_left_key in effective_right_key
        or effective_right_key in effective_left_key
    ):
        return DuplicateContentAssessment(
            is_duplicate=True,
            match_kind="normalized_containment",
            overlap_ratio=1.0,
            left_key=effective_left_key,
            right_key=effective_right_key,
        )

    overlap_ratio = _jaccard_token_overlap(effective_left_key, effective_right_key)
    return DuplicateContentAssessment(
        is_duplicate=overlap_ratio >= threshold,
        match_kind="token_overlap" if overlap_ratio >= threshold else None,
        overlap_ratio=overlap_ratio,
        left_key=effective_left_key,
        right_key=effective_right_key,
    )


def _jaccard_token_overlap(left_key: str, right_key: str) -> float:
    """Return a simple lexical overlap ratio for normalized content."""

    tokens_a = set(_UNICODE_TOKEN_PATTERN.findall(left_key))
    tokens_b = set(_UNICODE_TOKEN_PATTERN.findall(right_key))
    union_size = len(tokens_a | tokens_b)
    if union_size == 0:
        return 0.0
    return len(tokens_a & tokens_b) / union_size


def _normalized_content_lines(content: str) -> tuple[str, ...]:
    """Return normalized non-empty lines after bounded front-matter stripping."""

    stripped_content = _strip_leading_front_matter(content)
    normalized_lines = [_normalize_line(line) for line in stripped_content.splitlines()]
    return tuple(line for line in normalized_lines if line)


def _strip_leading_front_matter(content: str) -> str:
    """Remove a small YAML-style front-matter block when it appears at the top."""

    lines = content.splitlines()
    if not lines or lines[0].strip() != _FRONT_MATTER_DELIMITER:
        return content

    search_limit = min(len(lines), _MAX_FRONT_MATTER_LINES)
    for index in range(1, search_limit):
        if lines[index].strip() in _FRONT_MATTER_TERMINATORS:
            remainder_lines = lines[index + 1 :]
            if not any(_normalize_line(line) for line in remainder_lines):
                return content
            remainder = "\n".join(remainder_lines)
            return remainder.lstrip()
    return content


def _trim_shared_leading_prefix(
    left_lines: tuple[str, ...],
    right_lines: tuple[str, ...],
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """Discount a bounded shared leading line prefix before fuzzy comparison."""

    shared_line_count = 0
    shared_char_count = 0

    for left_line, right_line in zip(left_lines, right_lines):
        if left_line != right_line:
            break
        if shared_line_count >= _MAX_SHARED_PREFIX_LINES:
            break
        prospective_char_count = shared_char_count + len(left_line)
        if prospective_char_count > _MAX_SHARED_PREFIX_CHARS:
            break
        shared_line_count += 1
        shared_char_count = prospective_char_count

    if shared_line_count < _MIN_SHARED_PREFIX_LINES:
        return left_lines, right_lines

    trimmed_left_lines = left_lines[shared_line_count:]
    trimmed_right_lines = right_lines[shared_line_count:]
    if (
        len(trimmed_left_lines) < _MIN_REMAINING_LINES_AFTER_PREFIX
        or len(trimmed_right_lines) < _MIN_REMAINING_LINES_AFTER_PREFIX
    ):
        return left_lines, right_lines
    return trimmed_left_lines, trimmed_right_lines


def _normalize_line(line: str) -> str:
    """Case-fold and collapse internal whitespace for one comparison line."""

    return " ".join(line.casefold().split())


def _join_normalized_lines(lines: tuple[str, ...]) -> str:
    """Join normalized lines into the canonical key shape used by comparisons."""

    return " ".join(lines)
