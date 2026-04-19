"""Tests for the structured-record source adapter."""

from __future__ import annotations

import unittest

from context_atlas.adapters import StructuredRecordInput, StructuredRecordSourceAdapter
from context_atlas.domain.errors import ContextAtlasError, ErrorCode
from context_atlas.domain.models import (
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceDurability,
    ContextSourceFamily,
)


class StructuredRecordSourceAdapterTests(unittest.TestCase):
    """Verify structured records become canonical Atlas sources."""

    def test_load_source_translates_record_input_to_canonical_source(self) -> None:
        adapter = StructuredRecordSourceAdapter()
        source = adapter.load_source(
            StructuredRecordInput(
                record_id="product-1",
                content="Structured product record content",
                title="Product 1",
                source_uri="records://products/1",
                source_class=ContextSourceClass.OTHER,
                authority=ContextSourceAuthority.PREFERRED,
                durability=ContextSourceDurability.WORKING,
                tags=("products",),
                intended_uses=("answering", "comparison"),
                metadata={"table": "products"},
                provenance_metadata={"database": "atlas_app"},
            )
        )

        self.assertEqual(source.source_id, "product-1")
        self.assertEqual(source.title, "Product 1")
        self.assertEqual(source.metadata["table"], "products")
        self.assertEqual(source.intended_uses, ("answering", "comparison"))
        self.assertEqual(
            source.provenance.source_family,
            ContextSourceFamily.STRUCTURED_RECORD,
        )
        self.assertEqual(
            source.provenance.collector,
            "structured_record_source_adapter",
        )
        self.assertEqual(source.provenance.metadata["record_id"], "product-1")
        self.assertEqual(source.provenance.metadata["database"], "atlas_app")

    def test_load_source_accepts_mapping_payloads(self) -> None:
        adapter = StructuredRecordSourceAdapter(collector_name="warehouse_records")
        source = adapter.load_source(
            {
                "record_id": "ticket-42",
                "content": "Ticket record content",
                "source_class": ContextSourceClass.REVIEWS,
                "intended_uses": ["triage"],
                "metadata": {"table": "tickets"},
            }
        )

        self.assertEqual(source.source_id, "ticket-42")
        self.assertEqual(source.provenance.collector, "warehouse_records")
        self.assertEqual(
            source.provenance.source_family, ContextSourceFamily.STRUCTURED_RECORD
        )
        self.assertEqual(source.metadata["table"], "tickets")
        self.assertEqual(source.intended_uses, ("triage",))

    def test_invalid_record_input_raises_coded_error(self) -> None:
        adapter = StructuredRecordSourceAdapter()

        with self.assertRaises(ContextAtlasError) as context:
            adapter.load_source({"record_id": "broken"})

        self.assertEqual(
            context.exception.code,
            ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
        )

    def test_blank_collector_name_raises_coded_error(self) -> None:
        with self.assertRaises(ContextAtlasError) as context:
            StructuredRecordSourceAdapter(collector_name="   ")

        self.assertEqual(
            context.exception.code,
            ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
        )


if __name__ == "__main__":
    unittest.main()
