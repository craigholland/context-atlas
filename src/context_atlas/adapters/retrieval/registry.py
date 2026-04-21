"""Registry surface for canonical in-memory retrieval sources."""

from __future__ import annotations

from collections.abc import Iterable
import logging

from ...domain.errors import ContextAtlasError, ErrorCode
from ...domain.messages import LogMessage
from ...domain.models import ContextSource

logger = logging.getLogger(__name__)


class InMemorySourceRegistry:
    """A small in-memory registry for canonical context sources from any family."""

    def __init__(self, sources: Iterable[ContextSource] = ()) -> None:
        self._sources: dict[str, ContextSource] = {}
        self._revision = 0
        self.add_sources(sources)

    @property
    def revision(self) -> int:
        """Return the current corpus revision for cache invalidation decisions."""

        return self._revision

    def add_source(self, source: ContextSource) -> None:
        """Register a canonical source by its stable identifier."""

        if source.source_id in self._sources:
            raise ContextAtlasError(
                code=ErrorCode.DUPLICATE_SOURCE_IDENTIFIER,
                message_args=(source.source_id,),
            )

        self._sources[source.source_id] = source
        self._revision += 1
        logger.info(
            LogMessage.SOURCE_REGISTERED,
            source.source_id,
            len(self._sources),
            extra={
                "event": LogMessage.SOURCE_REGISTERED.event_name,
                "source_id": source.source_id,
                "source_family": source.provenance.source_family,
                "total_sources": len(self._sources),
                "registry_revision": self._revision,
            },
        )

    def add_sources(self, sources: Iterable[ContextSource]) -> None:
        """Bulk-register canonical sources in insertion order."""

        for source in sources:
            self.add_source(source)

    def list_sources(self) -> tuple[ContextSource, ...]:
        """Return registered sources in insertion order."""

        return tuple(self._sources.values())

    def __len__(self) -> int:
        return len(self._sources)
