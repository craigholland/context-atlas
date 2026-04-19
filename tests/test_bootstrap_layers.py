"""Bootstrap tests for the initial Context Atlas package spine."""

from __future__ import annotations

import io
import logging
import os
import unittest

from context_atlas import api
from context_atlas.adapters import StructuredRecordInput
from context_atlas.domain.errors import ConfigurationError, ContextAtlasError, ErrorCode
from context_atlas.domain.models import ContextSourceClass
from context_atlas.domain.messages import ErrorMessage, LogMessage
from context_atlas.infrastructure import build_starter_context_assembly_service
from context_atlas.infrastructure.config import load_settings_from_env
from context_atlas.infrastructure.config.settings import LoggingSettings
from context_atlas.infrastructure.logging import configure_logger, log_message
from context_atlas.rendering import render_packet_inspection, render_trace_inspection


class BootstrapLayerTests(unittest.TestCase):
    """Verify the initial shared contracts and infrastructure bootstrap."""

    def test_curated_api_exposes_supported_starter_surface(self) -> None:
        self.assertTrue(hasattr(api, "FilesystemDocumentSourceAdapter"))
        self.assertTrue(hasattr(api, "LexicalRetriever"))
        self.assertTrue(hasattr(api, "load_settings_from_env"))
        self.assertTrue(hasattr(api, "render_packet_context"))
        self.assertIs(
            api.build_starter_context_assembly_service,
            build_starter_context_assembly_service,
        )

    def test_getting_started_import_surfaces_exist(self) -> None:
        self.assertTrue(callable(api.render_packet_context))
        self.assertTrue(callable(render_packet_inspection))
        self.assertTrue(callable(render_trace_inspection))

    def test_structured_record_input_validates_minimum_adapter_shape(self) -> None:
        record = StructuredRecordInput(
            record_id="product-1",
            content="Structured product record content",
            source_class=ContextSourceClass.OTHER,
            tags=("products",),
            intended_uses=("answering",),
            metadata={"table": "products"},
        )

        self.assertEqual(record.record_id, "product-1")
        self.assertEqual(record.tags, ("products",))
        self.assertEqual(record.metadata["table"], "products")

    def test_error_messages_are_centralized_and_formatted(self) -> None:
        message = ErrorMessage.DOCUMENT_NO_CONTENT % ("notes.md",)

        self.assertEqual(message, "Document 'notes.md' has empty content.")

    def test_context_atlas_error_uses_registered_template(self) -> None:
        error = ContextAtlasError(
            code=ErrorCode.DOCUMENT_NO_CONTENT,
            message_args=["notes.md"],
        )

        self.assertEqual(str(error), "Document 'notes.md' has empty content.")
        self.assertEqual(
            error.model_dump(),
            {
                "code": ErrorCode.DOCUMENT_NO_CONTENT,
                "message_args": ("notes.md",),
            },
        )

    def test_load_settings_from_env_reads_expected_variables(self) -> None:
        with _temporary_environment(
            CONTEXT_ATLAS_LOGGER_NAME="atlas.tests",
            CONTEXT_ATLAS_LOG_LEVEL="DEBUG",
            CONTEXT_ATLAS_LOG_STRUCTURED_EVENTS="false",
        ):
            settings = load_settings_from_env()

        self.assertEqual(settings.logging.logger_name, "atlas.tests")
        self.assertEqual(settings.logging.level, "DEBUG")
        self.assertFalse(settings.logging.structured_events)
        self.assertEqual(settings.last_loaded_message_name, "SETTINGS_LOADED")

    def test_invalid_boolean_configuration_raises_configuration_error(self) -> None:
        with _temporary_environment(CONTEXT_ATLAS_LOG_STRUCTURED_EVENTS="sometimes"):
            with self.assertRaises(ConfigurationError) as context:
                load_settings_from_env()

        self.assertEqual(context.exception.code, ErrorCode.INVALID_CONFIGURATION)

    def test_structured_log_events_use_stable_event_names(self) -> None:
        logger = configure_logger(
            LoggingSettings(logger_name="context_atlas.tests", level="INFO")
        )
        stream = io.StringIO()
        handler = logging.StreamHandler(stream)
        handler.setFormatter(logging.Formatter("%(event)s|%(message)s"))
        logger.handlers = [handler]

        log_message(
            logger,
            logging.INFO,
            LogMessage.COMPONENT_INITIALIZED,
            "bootstrap",
        )

        output = stream.getvalue().strip()
        self.assertEqual(
            output,
            "component_initialized|Component initialized: name=bootstrap",
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
