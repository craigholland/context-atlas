"""Tests for environment-backed assembly defaults and observability helpers."""

from __future__ import annotations

import io
import logging
import os
import unittest

from pydantic import ValidationError

from context_atlas.domain.errors import ConfigurationError, ContextAtlasError, ErrorCode
from context_atlas.domain.messages import LogMessage
from context_atlas.infrastructure.config import (
    ContextAtlasSettings,
    CompressionStrategy,
    load_settings_from_env,
)
from context_atlas.infrastructure.assembly import build_starter_context_assembly_service
from context_atlas.infrastructure.config.settings import (
    AssemblySettings,
    LoggingSettings,
    MemorySettings,
)
from context_atlas.infrastructure.logging import (
    configure_logger,
    log_assembly_stage_message,
)


class ConfigAndObservabilityTests(unittest.TestCase):
    """Verify the PR 2 config and observability backbone."""

    def test_load_settings_from_env_reads_assembly_defaults(self) -> None:
        with _temporary_environment(
            CONTEXT_ATLAS_LOGGER_NAME="atlas.observability.tests",
            CONTEXT_ATLAS_LOG_LEVEL="WARNING",
            CONTEXT_ATLAS_LOG_STRUCTURED_EVENTS="true",
            CONTEXT_ATLAS_DEFAULT_TOTAL_BUDGET="1024",
            CONTEXT_ATLAS_DEFAULT_MEMORY_BUDGET_FRACTION="0.4",
            CONTEXT_ATLAS_DEFAULT_RETRIEVAL_TOP_K="7",
            CONTEXT_ATLAS_DEFAULT_COMPRESSION_STRATEGY="sentence",
            CONTEXT_ATLAS_RANKING_MINIMUM_SCORE="0.15",
            CONTEXT_ATLAS_COMPRESSION_CHARS_PER_TOKEN="5",
            CONTEXT_ATLAS_COMPRESSION_MIN_CHUNK_CHARS="18",
            CONTEXT_ATLAS_MEMORY_SHORT_TERM_COUNT="6",
            CONTEXT_ATLAS_MEMORY_DECAY_RATE="0.0025",
            CONTEXT_ATLAS_MEMORY_DEDUP_THRESHOLD="0.81",
            CONTEXT_ATLAS_MEMORY_MIN_EFFECTIVE_SCORE="0.22",
            CONTEXT_ATLAS_MEMORY_QUERY_BOOST_WEIGHT="0.55",
        ):
            settings = load_settings_from_env()

        self.assertEqual(settings.logging.logger_name, "atlas.observability.tests")
        self.assertEqual(settings.logging.level, "WARNING")
        self.assertTrue(settings.logging.structured_events)
        self.assertEqual(settings.assembly.default_total_budget, 1024)
        self.assertAlmostEqual(settings.assembly.default_memory_budget_fraction, 0.4)
        self.assertEqual(settings.assembly.default_retrieval_top_k, 7)
        self.assertEqual(
            settings.assembly.default_compression_strategy,
            CompressionStrategy.SENTENCE,
        )
        self.assertAlmostEqual(settings.assembly.ranking_minimum_score, 0.15)
        self.assertEqual(settings.assembly.compression_chars_per_token, 5)
        self.assertEqual(settings.assembly.compression_min_chunk_chars, 18)
        self.assertEqual(
            settings.assembly.compression_token_estimator_name,
            "starter_heuristic",
        )
        self.assertEqual(settings.memory.short_term_count, 6)
        self.assertAlmostEqual(settings.memory.decay_rate, 0.0025)
        self.assertAlmostEqual(settings.memory.dedup_threshold, 0.81)
        self.assertAlmostEqual(settings.memory.min_effective_score, 0.22)
        self.assertAlmostEqual(settings.memory.query_boost_weight, 0.55)
        self.assertEqual(settings.last_loaded_message_name, "SETTINGS_LOADED")
        self.assertEqual(
            settings.last_loaded_message,
            "Settings loaded: logger_name=atlas.observability.tests, "
            "log_level=WARNING, default_total_budget=1024, "
            "default_memory_budget_fraction=0.4000, default_retrieval_top_k=7, "
            "default_compression_strategy=sentence, ranking_minimum_score=0.1500, "
            "compression_chars_per_token=5, compression_min_chunk_chars=18, "
            "memory_short_term_count=6, memory_decay_rate=0.0025, "
            "memory_dedup_threshold=0.81, memory_min_effective_score=0.2200, "
            "memory_query_boost_weight=0.5500",
        )

    def test_invalid_integer_settings_raise_configuration_error(self) -> None:
        with _temporary_environment(CONTEXT_ATLAS_DEFAULT_TOTAL_BUDGET="tiny"):
            with self.assertRaises(ConfigurationError) as context:
                load_settings_from_env()

        self.assertEqual(context.exception.code, ErrorCode.INVALID_CONFIGURATION)
        self.assertIn("DEFAULT_TOTAL_BUDGET", str(context.exception))

    def test_invalid_compression_strategy_raises_configuration_error(self) -> None:
        with _temporary_environment(CONTEXT_ATLAS_DEFAULT_COMPRESSION_STRATEGY="magic"):
            with self.assertRaises(ConfigurationError) as context:
                load_settings_from_env()

        self.assertEqual(context.exception.code, ErrorCode.INVALID_CONFIGURATION)
        self.assertIn("extractive", str(context.exception))

    def test_invalid_memory_threshold_raises_configuration_error(self) -> None:
        with _temporary_environment(CONTEXT_ATLAS_MEMORY_DEDUP_THRESHOLD="1.5"):
            with self.assertRaises(ConfigurationError) as context:
                load_settings_from_env()

        self.assertEqual(context.exception.code, ErrorCode.INVALID_CONFIGURATION)
        self.assertIn("MEMORY_DEDUP_THRESHOLD", str(context.exception))

    def test_invalid_extended_policy_setting_raises_configuration_error(self) -> None:
        with _temporary_environment(CONTEXT_ATLAS_RANKING_MINIMUM_SCORE="nan"):
            with self.assertRaises(ConfigurationError) as context:
                load_settings_from_env()

        self.assertEqual(context.exception.code, ErrorCode.INVALID_CONFIGURATION)
        self.assertIn("RANKING_MINIMUM_SCORE", str(context.exception))

    def test_invalid_memory_budget_fraction_raises_configuration_error(self) -> None:
        with _temporary_environment(CONTEXT_ATLAS_DEFAULT_MEMORY_BUDGET_FRACTION="1.5"):
            with self.assertRaises(ConfigurationError) as context:
                load_settings_from_env()

        self.assertEqual(context.exception.code, ErrorCode.INVALID_CONFIGURATION)
        self.assertIn("DEFAULT_MEMORY_BUDGET_FRACTION", str(context.exception))

    def test_configure_logger_uses_plain_formatter_when_structured_events_disabled(
        self,
    ) -> None:
        logger_name = "context_atlas.plain.tests"
        logger = logging.getLogger(logger_name)
        logger.handlers.clear()

        configured = configure_logger(
            LoggingSettings(
                logger_name=logger_name,
                level="INFO",
                structured_events=False,
            )
        )

        self.assertEqual(len(configured.handlers), 1)
        formatter = configured.handlers[0].formatter
        self.assertIsNotNone(formatter)
        assert formatter is not None
        self.assertNotIn("%(event)s", formatter._fmt)

    def test_log_assembly_stage_message_emits_structured_fields(self) -> None:
        logger_name = "context_atlas.assembly.tests"
        logger = logging.getLogger(logger_name)
        logger.handlers.clear()
        logger = configure_logger(
            LoggingSettings(
                logger_name=logger_name,
                level="INFO",
                structured_events=True,
            )
        )
        stream = io.StringIO()
        handler = logging.StreamHandler(stream)
        handler.setFormatter(
            logging.Formatter(
                "%(event)s|%(trace_id)s|%(candidate_count)s|%(strategy)s|%(message)s"
            )
        )
        logger.handlers = [handler]

        log_assembly_stage_message(
            logger,
            logging.INFO,
            LogMessage.CANDIDATES_GATHERED,
            trace_id="trace-2",
            message_args=("trace-2", 4),
            candidate_count=4,
            strategy=CompressionStrategy.EXTRACTIVE,
        )

        self.assertEqual(
            stream.getvalue().strip(),
            "candidates_gathered|trace-2|4|extractive|"
            "Candidates gathered: trace_id=trace-2, candidate_count=4",
        )

    def test_memory_settings_defaults_are_exposed_through_context_settings(
        self,
    ) -> None:
        settings = load_settings_from_env()

        self.assertEqual(settings.memory, MemorySettings())

    def test_with_assembly_overrides_revalidates_total_budget(self) -> None:
        settings = ContextAtlasSettings()

        updated = settings.with_assembly_overrides(default_total_budget=256)

        self.assertEqual(updated.assembly.default_total_budget, 256)
        self.assertEqual(settings.assembly.default_total_budget, 2048)

    def test_with_assembly_overrides_revalidates_memory_budget_fraction(self) -> None:
        settings = ContextAtlasSettings()

        updated = settings.with_assembly_overrides(default_memory_budget_fraction=0.4)

        self.assertAlmostEqual(updated.assembly.default_memory_budget_fraction, 0.4)
        self.assertAlmostEqual(
            settings.assembly.default_memory_budget_fraction,
            0.25,
        )

    def test_with_assembly_overrides_rejects_unsupported_total_budget(self) -> None:
        settings = ContextAtlasSettings(
            assembly=AssemblySettings(default_total_budget=128)
        )

        with self.assertRaises(ValidationError):
            settings.with_assembly_overrides(default_total_budget=32)

    def test_with_assembly_overrides_rejects_unsupported_memory_budget_fraction(
        self,
    ) -> None:
        settings = ContextAtlasSettings()

        with self.assertRaises(ValidationError):
            settings.with_assembly_overrides(default_memory_budget_fraction=1.0)

    def test_starter_assembly_accepts_custom_token_estimator_binding(self) -> None:
        def estimate_words(text: str) -> int:
            return len([token for token in text.split() if token])

        service = build_starter_context_assembly_service(
            retriever=_StubRetriever(),
            token_estimator=estimate_words,
            token_estimator_name="word_count",
        )

        self.assertIs(service._compression_policy.token_estimator, estimate_words)
        self.assertEqual(service._compression_policy.token_estimator_name, "word_count")

    def test_starter_assembly_defaults_to_starter_heuristic_without_binding(
        self,
    ) -> None:
        service = build_starter_context_assembly_service(
            retriever=_StubRetriever(),
        )

        self.assertIsNone(service._compression_policy.token_estimator)
        self.assertEqual(
            service._compression_policy.token_estimator_name,
            "starter_heuristic",
        )

    def test_starter_assembly_rejects_custom_estimator_label_without_binding(
        self,
    ) -> None:
        with self.assertRaises(ContextAtlasError) as context:
            build_starter_context_assembly_service(
                retriever=_StubRetriever(),
                token_estimator_name="word_count",
            )

        self.assertEqual(context.exception.code, ErrorCode.INVALID_ASSEMBLY_REQUEST)
        self.assertIn(
            "token_estimator_name requires token_estimator", str(context.exception)
        )


class _temporary_environment:
    """Temporarily set and later restore selected environment variables."""

    def __init__(self, **overrides: str) -> None:
        self._overrides = overrides
        self._previous: dict[str, str | None] = {}

    def __enter__(self) -> None:
        for key, value in self._overrides.items():
            self._previous[key] = os.environ.get(key)
            os.environ[key] = value

    def __exit__(self, *_: object) -> None:
        for key, previous in self._previous.items():
            if previous is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = previous


class _StubRetriever:
    """Minimal retriever stub for outward assembly wiring tests."""

    def retrieve(self, query: str, *, top_k: int = 5) -> tuple[object, ...]:
        return ()


if __name__ == "__main__":
    unittest.main()
