"""Shared helpers for canonical domain models."""

from __future__ import annotations

from typing import NoReturn

from pydantic import BaseModel, ConfigDict


class FrozenStringMap(dict[str, str]):
    """A lightweight immutable string map for canonical model metadata."""

    def __readonly(self, *_args: object, **_kwargs: object) -> NoReturn:
        raise TypeError("FrozenStringMap is immutable.")

    __setitem__ = __readonly
    __delitem__ = __readonly
    clear = __readonly
    pop = __readonly
    popitem = __readonly
    setdefault = __readonly
    update = __readonly

    def copy(self) -> dict[str, str]:
        """Return a mutable copy for callers that need a plain dict."""

        return dict(self)


class CanonicalDomainModel(BaseModel):
    """Shared Pydantic configuration for canonical Context Atlas artifacts."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    @staticmethod
    def freeze_metadata(metadata: dict[str, str]) -> FrozenStringMap:
        """Return an immutable copy of metadata-like string maps."""

        return FrozenStringMap(dict(metadata))
