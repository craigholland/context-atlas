"""Tests for the structured-record source adapter."""

from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import textwrap
import unittest

from context_atlas.adapters import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetrievalMode,
    LexicalRetriever,
    StructuredRecordInput,
    StructuredRecordSourceAdapter,
)
from context_atlas.domain.errors import ContextAtlasError, ErrorCode
from context_atlas.domain.models import (
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceDurability,
    ContextSourceFamily,
)
from context_atlas.infrastructure.assembly import build_starter_context_assembly_service
from context_atlas.infrastructure.config import (
    AssemblySettings,
    ContextAtlasSettings,
    LoggingSettings,
    MemorySettings,
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

    def test_canonical_record_id_overrides_provenance_metadata(self) -> None:
        adapter = StructuredRecordSourceAdapter()
        source = adapter.load_source(
            StructuredRecordInput(
                record_id="product-2",
                content="Structured product record content",
                provenance_metadata={
                    "record_id": "spoofed-id",
                    "database": "atlas_app",
                },
            )
        )

        self.assertEqual(source.source_id, "product-2")
        self.assertEqual(source.provenance.metadata["record_id"], "product-2")
        self.assertEqual(source.provenance.metadata["database"], "atlas_app")

    def test_invalid_record_input_raises_coded_error(self) -> None:
        adapter = StructuredRecordSourceAdapter()

        with self.assertRaises(ContextAtlasError) as context:
            adapter.load_source({"record_id": "broken"})

        self.assertEqual(
            context.exception.code,
            ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
        )

    def test_mapping_tags_input_raises_coded_error(self) -> None:
        adapter = StructuredRecordSourceAdapter()

        with self.assertRaises(ContextAtlasError) as context:
            adapter.load_source(
                {
                    "record_id": "ticket-43",
                    "content": "Ticket record content",
                    "tags": {"primary": "triage"},
                }
            )

        self.assertEqual(
            context.exception.code,
            ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
        )
        self.assertIn("must not be a mapping", str(context.exception))

    def test_blank_collector_name_raises_coded_error(self) -> None:
        with self.assertRaises(ContextAtlasError) as context:
            StructuredRecordSourceAdapter(collector_name="   ")

        self.assertEqual(
            context.exception.code,
            ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
        )

    def test_documents_and_records_coexist_in_shared_registry_and_packet_flow(
        self,
    ) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            self._write_doc(
                docs_root / "Authoritative" / "Architecture" / "Mixed-Sources.md",
                """
                # Mixed Sources

                Authoritative documentation explains packet budgeting and retries.
                """,
            )

            document_sources = FilesystemDocumentSourceAdapter(docs_root).load_sources()
            record_sources = StructuredRecordSourceAdapter().load_sources(
                (
                    StructuredRecordInput(
                        record_id="ticket-42",
                        content="Structured support record covers retries and escalation.",
                        title="Ticket 42",
                        source_class=ContextSourceClass.REVIEWS,
                        authority=ContextSourceAuthority.ADVISORY,
                        durability=ContextSourceDurability.WORKING,
                        intended_uses=("triage",),
                    ),
                )
            )
            service = build_starter_context_assembly_service(
                retriever=LexicalRetriever(
                    InMemorySourceRegistry((*document_sources, *record_sources)),
                    mode=LexicalRetrievalMode.KEYWORD,
                ),
                settings=ContextAtlasSettings(
                    logging=LoggingSettings(
                        logger_name="context_atlas.tests.mixed_sources"
                    ),
                    assembly=AssemblySettings(
                        default_total_budget=160,
                        default_retrieval_top_k=4,
                    ),
                    memory=MemorySettings(),
                ),
            )

            packet = service.assemble(query="retries packet budgeting escalation")
            source_families = {
                candidate.source.provenance.source_family
                for candidate in packet.selected_candidates
            }

            self.assertEqual(
                source_families,
                {
                    ContextSourceFamily.DOCUMENT,
                    ContextSourceFamily.STRUCTURED_RECORD,
                },
            )
            self.assertIn(
                "filesystem_document_source_adapter",
                packet.trace.metadata["selected_source_collectors"],
            )
            self.assertIn(
                "structured_record_source_adapter",
                packet.trace.metadata["selected_source_collectors"],
            )

    def _write_doc(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
