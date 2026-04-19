"""Structured-record shaping and translation exports for Context Atlas.

This package intentionally exposes only the record-shaping boundary Atlas owns:
- validated record inputs
- mapping-to-input row mappers
- translation into canonical sources

Query execution and client lifecycles stay outside this package.
"""

from .mappers import StructuredRecordRowMapper
from .structured import (
    StructuredRecordInput,
    StructuredRecordPayload,
    StructuredRecordSourceAdapter,
)

__all__ = [
    "StructuredRecordInput",
    "StructuredRecordPayload",
    "StructuredRecordRowMapper",
    "StructuredRecordSourceAdapter",
]
