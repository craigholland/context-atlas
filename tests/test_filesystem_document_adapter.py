"""Tests for the ontology-aware filesystem document adapter."""

from __future__ import annotations

import logging
from pathlib import Path
from tempfile import TemporaryDirectory
import textwrap
import unittest

from context_atlas.adapters import (
    FilesystemDocumentSourceAdapter,
    InMemorySourceRegistry,
    LexicalRetrievalMode,
    LexicalRetriever,
)
from context_atlas.domain.errors import ContextAtlasError, ErrorCode
from context_atlas.domain.models import (
    AuthorityPrecedenceReasonCode,
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceDurability,
    InclusionReasonCode,
)
from context_atlas.infrastructure.assembly import build_starter_context_assembly_service
from context_atlas.infrastructure.config import (
    AssemblySettings,
    ContextAtlasSettings,
    LoggingSettings,
    MemorySettings,
)


class FilesystemDocumentSourceAdapterTests(unittest.TestCase):
    """Verify filesystem documentation becomes ontology-aware Atlas sources."""

    def test_load_sources_classifies_docs_from_path_segments(self) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            self._write_doc(
                docs_root / "Authoritative" / "Architecture" / "Craig-Architecture.md",
                """
                # Craig Architecture

                Clean architecture is the mature destination.
                """,
            )
            self._write_doc(
                docs_root / "Planning" / "Roadmap.md",
                """
                # Roadmap

                Planning notes describe future execution intent.
                """,
            )
            self._write_doc(
                docs_root / "Releases" / "v0.1.0.md",
                """
                # Release 0.1.0

                Release notes describe what shipped.
                """,
            )

            sources = FilesystemDocumentSourceAdapter(docs_root).load_sources()
            source_by_id = {source.source_id: source for source in sources}

            authoritative = source_by_id[
                "Authoritative/Architecture/Craig-Architecture.md"
            ]
            planning = source_by_id["Planning/Roadmap.md"]
            release = source_by_id["Releases/v0.1.0.md"]

            self.assertEqual(
                authoritative.source_class, ContextSourceClass.AUTHORITATIVE
            )
            self.assertEqual(authoritative.authority, ContextSourceAuthority.BINDING)
            self.assertEqual(authoritative.durability, ContextSourceDurability.DURABLE)
            self.assertEqual(
                authoritative.provenance.collector,
                "filesystem_document_source_adapter",
            )
            self.assertEqual(
                authoritative.provenance.metadata["classification_source"],
                "path",
            )
            self.assertIn("authoritative", authoritative.tags)
            self.assertEqual(planning.source_class, ContextSourceClass.PLANNING)
            self.assertEqual(planning.authority, ContextSourceAuthority.PREFERRED)
            self.assertEqual(release.source_class, ContextSourceClass.RELEASES)
            self.assertEqual(release.authority, ContextSourceAuthority.HISTORICAL)
            self.assertEqual(release.durability, ContextSourceDurability.ARCHIVAL)

    def test_frontmatter_can_override_path_and_supply_metadata(self) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            self._write_doc(
                docs_root / "Reviews" / "Speculative-Finding.md",
                """
                ---
                title: "Exploratory Review"
                doc_class: exploratory
                tags: [prototype, ontology]
                intended_use:
                  - hypothesis_generation
                  - exploration
                ---

                # Ignored Title

                Exploratory notes should remain non-binding.
                """,
            )

            source = FilesystemDocumentSourceAdapter(docs_root).load_source(
                docs_root / "Reviews" / "Speculative-Finding.md"
            )

            self.assertEqual(source.title, "Exploratory Review")
            self.assertEqual(source.source_class, ContextSourceClass.EXPLORATORY)
            self.assertEqual(source.authority, ContextSourceAuthority.SPECULATIVE)
            self.assertEqual(
                source.provenance.metadata["classification_source"],
                "frontmatter",
            )
            self.assertEqual(
                source.provenance.metadata["classification_mismatch"],
                "true",
            )
            self.assertIn("prototype", source.tags)
            self.assertIn("exploration", source.intended_uses)

    def test_unsupported_doc_class_raises_coded_error(self) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            bad_doc = docs_root / "Misc" / "Bad.md"
            self._write_doc(
                bad_doc,
                """
                ---
                doc_class: impossible
                ---

                # Bad

                Impossible document class.
                """,
            )

            adapter = FilesystemDocumentSourceAdapter(docs_root)

            with self.assertRaises(ContextAtlasError) as context:
                adapter.load_source(bad_doc)

            self.assertEqual(
                context.exception.code, ErrorCode.UNSUPPORTED_DOCUMENT_CLASS
            )

    def test_classified_docs_flow_into_ranking_and_service_trace(self) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            self._write_doc(
                docs_root / "Authoritative" / "Architecture" / "Canon.md",
                """
                # Canon

                Context authority and packet assembly should remain explicit and auditable.
                """,
            )
            self._write_doc(
                docs_root / "Exploratory" / "Ideas" / "Canon-Idea.md",
                """
                # Idea

                Context authority and packet assembly should remain explicit and auditable.
                """,
            )

            sources = FilesystemDocumentSourceAdapter(docs_root).load_sources()
            service = build_starter_context_assembly_service(
                retriever=LexicalRetriever(
                    InMemorySourceRegistry(sources),
                    mode=LexicalRetrievalMode.KEYWORD,
                ),
                settings=ContextAtlasSettings(
                    logging=LoggingSettings(
                        logger_name="context_atlas.tests.filesystem_docs"
                    ),
                    assembly=AssemblySettings(
                        default_total_budget=128,
                        default_retrieval_top_k=2,
                    ),
                    memory=MemorySettings(),
                ),
            )

            packet = service.assemble(
                query="context authority packet assembly explicit auditable"
            )
            authoritative_source_id = "Authoritative/Architecture/Canon.md"
            authoritative_decision = next(
                decision
                for decision in packet.trace.decisions
                if decision.source_id == authoritative_source_id
            )

            self.assertEqual(
                packet.selected_candidates[0].source.source_id,
                authoritative_source_id,
            )
            self.assertEqual(
                packet.selected_candidates[0].source.source_class,
                ContextSourceClass.AUTHORITATIVE,
            )
            self.assertIn(
                AuthorityPrecedenceReasonCode.HIGHER_AUTHORITY_PREFERRED,
                authoritative_decision.reason_codes,
            )
            self.assertIn(
                InclusionReasonCode.AUTHORITY_PRIORITY,
                authoritative_decision.reason_codes,
            )
            self.assertIn(
                "authoritative",
                packet.trace.metadata["selected_source_classes"],
            )
            self.assertEqual(
                packet.trace.metadata["selected_source_collectors"],
                "filesystem_document_source_adapter",
            )

    def test_source_classification_logs_use_stable_messages(self) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            self._write_doc(
                docs_root / "Authoritative" / "Charter.md",
                """
                # Charter

                Context Atlas is a standalone context-governance engine.
                """,
            )

            adapter = FilesystemDocumentSourceAdapter(docs_root)

            with self.assertLogs(
                "context_atlas.adapters.docs.filesystem",
                level=logging.INFO,
            ) as captured:
                adapter.load_sources()

            self.assertTrue(
                any("Source classified" in message for message in captured.output)
            )

    def test_adapter_outputs_immutable_canonical_source_metadata(self) -> None:
        with TemporaryDirectory() as temp_dir:
            docs_root = Path(temp_dir)
            self._write_doc(
                docs_root / "Authoritative" / "Charter.md",
                """
                # Charter

                Context Atlas is a standalone context-governance engine.
                """,
            )

            source = FilesystemDocumentSourceAdapter(docs_root).load_sources()[0]

            with self.assertRaises(TypeError):
                source.metadata["scope"] = "identity"

            with self.assertRaises(TypeError):
                source.provenance.metadata["collector"] = "override"

    def _write_doc(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
