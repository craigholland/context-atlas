"""Tests for shared source semantics across supported source families."""

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


class SourceSemanticsTests(unittest.TestCase):
    """Verify supported source families share one canonical semantic model."""

    def test_documents_and_records_share_review_defaults(self) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            self._write_doc(
                docs_root / "Reviews" / "Review-Notes.md",
                """
                # Review Notes

                Review notes should stay advisory but useful as evidence.
                """,
            )

            document_source = FilesystemDocumentSourceAdapter(docs_root).load_sources()[
                0
            ]
            record_source = StructuredRecordSourceAdapter().load_source(
                StructuredRecordInput(
                    record_id="review-1",
                    content="Review evidence from a structured record.",
                    source_class=ContextSourceClass.REVIEWS,
                )
            )

            self.assertEqual(document_source.source_class, ContextSourceClass.REVIEWS)
            self.assertEqual(record_source.source_class, ContextSourceClass.REVIEWS)
            self.assertEqual(document_source.authority, record_source.authority)
            self.assertEqual(document_source.durability, record_source.durability)
            self.assertEqual(document_source.intended_uses, record_source.intended_uses)
            self.assertEqual(document_source.authority, ContextSourceAuthority.ADVISORY)
            self.assertEqual(
                document_source.durability,
                ContextSourceDurability.WORKING,
            )
            self.assertEqual(document_source.intended_uses, ("review", "evidence"))

    def test_documents_and_records_share_override_merge_behavior(self) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            self._write_doc(
                docs_root / "Reviews" / "Triaged-Review.md",
                """
                ---
                intended_use:
                  - triage
                ---

                # Triaged Review

                Review notes with a triage focus.
                """,
            )

            document_source = FilesystemDocumentSourceAdapter(docs_root).load_sources()[
                0
            ]
            record_source = StructuredRecordSourceAdapter().load_source(
                StructuredRecordInput(
                    record_id="review-2",
                    content="Structured review notes with a triage focus.",
                    source_class=ContextSourceClass.REVIEWS,
                    intended_uses=("triage",),
                )
            )

            self.assertEqual(
                document_source.intended_uses,
                ("review", "evidence", "triage"),
            )
            self.assertEqual(document_source.intended_uses, record_source.intended_uses)

    def test_mixed_source_packets_keep_family_specific_provenance_but_shared_semantics(
        self,
    ) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            self._write_doc(
                docs_root / "Reviews" / "Mixed-Review.md",
                """
                ---
                intended_use:
                  - triage
                ---

                # Mixed Review

                Shared review evidence should stay canonical across source families.
                """,
            )

            document_sources = FilesystemDocumentSourceAdapter(docs_root).load_sources()
            record_sources = StructuredRecordSourceAdapter().load_sources(
                (
                    StructuredRecordInput(
                        record_id="review-3",
                        content=(
                            "Shared review evidence should stay canonical across "
                            "source families."
                        ),
                        source_class=ContextSourceClass.REVIEWS,
                        intended_uses=("triage",),
                    ),
                )
            )

            packet = build_starter_context_assembly_service(
                retriever=LexicalRetriever(
                    InMemorySourceRegistry((*document_sources, *record_sources)),
                    mode=LexicalRetrievalMode.KEYWORD,
                ),
                settings=ContextAtlasSettings(
                    logging=LoggingSettings(
                        logger_name="context_atlas.tests.source_semantics"
                    ),
                    assembly=AssemblySettings(
                        default_total_budget=256,
                        default_retrieval_top_k=4,
                    ),
                    memory=MemorySettings(),
                ),
            ).assemble(query="shared review evidence canonical triage")

            review_candidates = [
                candidate
                for candidate in packet.selected_candidates
                if candidate.source.source_class is ContextSourceClass.REVIEWS
            ]
            families = {
                candidate.source.provenance.source_family
                for candidate in review_candidates
            }
            semantic_tuples = {
                (
                    candidate.source.authority,
                    candidate.source.durability,
                    candidate.source.intended_uses,
                )
                for candidate in review_candidates
            }

            self.assertEqual(
                families,
                {
                    ContextSourceFamily.DOCUMENT,
                    ContextSourceFamily.STRUCTURED_RECORD,
                },
            )
            self.assertEqual(
                semantic_tuples,
                {
                    (
                        ContextSourceAuthority.ADVISORY,
                        ContextSourceDurability.WORKING,
                        ("review", "evidence", "triage"),
                    )
                },
            )
            self.assertIn(
                "reviews",
                packet.trace.metadata["selected_source_classes"],
            )
            self.assertIn(
                "filesystem_document_source_adapter",
                packet.trace.metadata["selected_source_collectors"],
            )
            self.assertIn(
                "structured_record_source_adapter",
                packet.trace.metadata["selected_source_collectors"],
            )
            self.assertIn(
                "document",
                packet.trace.metadata["selected_source_families"],
            )
            self.assertIn(
                "structured_record",
                packet.trace.metadata["selected_source_families"],
            )

    def _write_doc(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
