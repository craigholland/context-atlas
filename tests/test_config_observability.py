"""Tests for environment-backed assembly defaults and observability helpers."""

from __future__ import annotations

import io
import logging
import os
import unittest

from context_atlas.domain.errors import ConfigurationError, ErrorCode
from context_atlas.domain.events import LogEvent
from context_atlas.infrastructure.config import (
    CompressionStrategy,
    load_settings_from_env,
)
from context_atlas.infrastructure.config.settings import LoggingSettings
from context_atlas.infrastructure.logging import (
    configure_logger,
    log_assembly_stage_event,
)


class ConfigAndObservabilityTests(unittest.TestCase):
    """Verify the PR 2 config and observability backbone."""

    def test_load_settings_from_env_reads_assembly_defaults(self) -> None:
        with _temporary_environment(
            CONTEXT_ATLAS_LOGGER_NAME="atlas.observability.tests",
            CONTEXT_ATLAS_LOG_LEVEL="WARNING",
            CONTEXT_ATLAS_LOG_STRUCTURED_EVENTS="true",
            CONTEXT_ATLAS_DEFAULT_TOTAL_BUDGET="1024",
            CONTEXT_ATLAS_DEFAULT_RETRIEVAL_TOP_K="7",
            CONTEXT_ATLAS_DEFAULT_COMPRESSION_STRATEGY="sentence",
        ):
            settings = load_settings_from_env()

        self.assertEqual(settings.logging.logger_name, "atlas.observability.tests")
        self.assertEqual(settings.logging.level, "WARNING")
        self.assertTrue(settings.logging.structured_events)
        self.assertEqual(settings.assembly.default_total_budget, 1024)
        self.assertEqual(settings.assembly.default_retrieval_top_k, 7)
        self.assertEqual(
            settings.assembly.default_compression_strategy,
            CompressionStrategy.SENTENCE,
        )
        self.assertEqual(settings.last_loaded_event, LogEvent.SETTINGS_LOADED)
        self.assertEqual(
            settings.last_loaded_message,
            "Settings loaded: logger_name=atlas.observability.tests, "
            "log_level=WARNING, default_total_budget=1024, "
            "default_retrieval_top_k=7, default_compression_strategy=sentence",
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

    def test_log_assembly_stage_event_emits_structured_fields(self) -> None:
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

        log_assembly_stage_event(
            logger,
            logging.INFO,
            LogEvent.CANDIDATES_GATHERED,
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


if __name__ == "__main__":
    unittest.main()
