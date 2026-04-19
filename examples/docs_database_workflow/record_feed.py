"""Outer-workflow helpers for the docs-plus-database example's record payloads.

These helpers stay outside Atlas adapters on purpose. They model one acceptable
integration pattern for loading already-fetched rows from a simple artifact
before those rows are reshaped and translated into canonical sources.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DEFAULT_RECORDS_FILE = Path(__file__).with_name("sample_records.json")


def resolve_records_file(records_file_arg: Path | None) -> Path:
    """Resolve the JSON payload file used by the runnable demo."""

    if records_file_arg is not None:
        return records_file_arg.resolve()
    return DEFAULT_RECORDS_FILE.resolve()


def load_record_rows(records_file: Path) -> tuple[dict[str, Any], ...]:
    """Load already-fetched record rows from a tracked JSON payload file."""

    payload = json.loads(records_file.read_text(encoding="utf-8"))
    return tuple(payload)
