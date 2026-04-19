"""Tests for the structured-record row-mapping pattern."""

from __future__ import annotations

import unittest

from context_atlas.adapters import (
    StructuredRecordRowMapper,
    StructuredRecordSourceAdapter,
)
from context_atlas.domain.errors import ContextAtlasError, ErrorCode
from context_atlas.domain.models import (
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceDurability,
)


class StructuredRecordRowMapperTests(unittest.TestCase):
    """Verify row-shaping helpers stay narrow and adapter-facing."""

    def test_row_mapper_produces_validated_record_inputs(self) -> None:
        mapper = StructuredRecordRowMapper(
            record_id_field="ticket_id",
            content_field="summary",
            title_field="title",
            source_uri_field="uri",
            tags_field="labels",
            intended_uses_field="uses",
            metadata_fields=("team", "table"),
            provenance_fields=("database",),
            source_class=ContextSourceClass.REVIEWS,
            authority=ContextSourceAuthority.ADVISORY,
            durability=ContextSourceDurability.WORKING,
            fixed_tags=("support",),
            fixed_intended_uses=("triage",),
        )

        record_input = mapper.to_record_input(
            {
                "ticket_id": "ticket-44",
                "summary": "Retry escalation details for a support record.",
                "title": "Ticket 44",
                "uri": "records://tickets/44",
                "labels": ["urgent", "retries"],
                "uses": ["evidence"],
                "team": "support",
                "table": "tickets",
                "database": "warehouse",
            }
        )
        source = StructuredRecordSourceAdapter().load_source(record_input)

        self.assertEqual(record_input.record_id, "ticket-44")
        self.assertEqual(record_input.tags, ("support", "urgent", "retries"))
        self.assertEqual(record_input.intended_uses, ("triage", "evidence"))
        self.assertEqual(record_input.metadata["team"], "support")
        self.assertEqual(record_input.provenance_metadata["database"], "warehouse")
        self.assertEqual(source.source_id, "ticket-44")
        self.assertEqual(source.metadata["table"], "tickets")
        self.assertEqual(source.provenance.metadata["database"], "warehouse")

    def test_row_mapper_supports_batch_translation(self) -> None:
        mapper = StructuredRecordRowMapper(
            record_id_field="id",
            content_field="body",
            source_class=ContextSourceClass.OTHER,
        )

        record_inputs = mapper.to_record_inputs(
            (
                {"id": "row-1", "body": "Row one content"},
                {"id": "row-2", "body": "Row two content"},
            )
        )

        self.assertEqual(
            tuple(record.record_id for record in record_inputs),
            ("row-1", "row-2"),
        )

    def test_missing_required_row_field_raises_coded_error(self) -> None:
        mapper = StructuredRecordRowMapper(
            record_id_field="ticket_id",
            content_field="summary",
        )

        with self.assertRaises(ContextAtlasError) as context:
            mapper.to_record_input({"ticket_id": "ticket-45"})

        self.assertEqual(context.exception.code, ErrorCode.INVALID_SOURCE_ADAPTER_INPUT)


if __name__ == "__main__":
    unittest.main()
