"""Filesystem adapter for turning documentation artifacts into Atlas sources."""

from __future__ import annotations

from collections.abc import Iterable
from datetime import UTC, datetime
import hashlib
import logging
from pathlib import Path
import re

from pydantic import (
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_validator,
)

from ...domain.errors import ContextAtlasError, ErrorCode
from ...domain.messages import ErrorMessage, LogMessage
from ...domain.models import (
    ContextSource,
    ContextSourceAuthority,
    ContextSourceClass,
    ContextSourceDurability,
    ContextSourceProvenance,
)

logger = logging.getLogger(__name__)

_SUPPORTED_SUFFIXES = (".md",)
_FRONT_MATTER_DELIMITER = "---"
_CLASS_SEGMENT_BY_NAME = {
    "authoritative": ContextSourceClass.AUTHORITATIVE,
    "planning": ContextSourceClass.PLANNING,
    "reviews": ContextSourceClass.REVIEWS,
    "exploratory": ContextSourceClass.EXPLORATORY,
    "releases": ContextSourceClass.RELEASES,
}


class _DocumentFrontMatter(BaseModel):
    """Validated subset of front matter relevant to source classification."""

    model_config = ConfigDict(
        extra="ignore",
        frozen=True,
        str_strip_whitespace=True,
    )

    title: str | None = None
    doc_class: str | None = None
    authority: ContextSourceAuthority | None = None
    durability: ContextSourceDurability | None = None
    tags: tuple[str, ...] = ()
    intended_uses: tuple[str, ...] = Field(
        default_factory=tuple,
        validation_alias=AliasChoices("intended_use", "intended_uses"),
    )

    @field_validator("doc_class")
    @classmethod
    def _normalize_doc_class(cls, value: str | None) -> str | None:
        if value is None:
            return None
        normalized = value.strip().lower()
        return normalized or None

    @field_validator("tags", "intended_uses", mode="before")
    @classmethod
    def _normalize_text_sequence(
        cls,
        value: object,
    ) -> tuple[str, ...]:
        if value is None:
            return ()
        if isinstance(value, str):
            normalized = _strip_quotes(value.strip())
            return () if not normalized else (normalized,)
        if isinstance(value, Iterable):
            normalized_items = [
                normalized
                for item in value
                if isinstance(item, str) and (normalized := _strip_quotes(item.strip()))
            ]
            return tuple(normalized_items)
        return ()


class _DocumentOntologyProfile(BaseModel):
    """Canonical mapping profile from document class to Atlas source semantics."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    source_class: ContextSourceClass
    authority: ContextSourceAuthority
    durability: ContextSourceDurability
    intended_uses: tuple[str, ...] = ()


_PROFILE_BY_DOC_CLASS = {
    "authoritative": _DocumentOntologyProfile(
        source_class=ContextSourceClass.AUTHORITATIVE,
        authority=ContextSourceAuthority.BINDING,
        durability=ContextSourceDurability.DURABLE,
        intended_uses=("implementation", "review", "planning"),
    ),
    "planning": _DocumentOntologyProfile(
        source_class=ContextSourceClass.PLANNING,
        authority=ContextSourceAuthority.PREFERRED,
        durability=ContextSourceDurability.WORKING,
        intended_uses=("planning", "execution"),
    ),
    "reviews": _DocumentOntologyProfile(
        source_class=ContextSourceClass.REVIEWS,
        authority=ContextSourceAuthority.ADVISORY,
        durability=ContextSourceDurability.WORKING,
        intended_uses=("review", "evidence"),
    ),
    "exploratory": _DocumentOntologyProfile(
        source_class=ContextSourceClass.EXPLORATORY,
        authority=ContextSourceAuthority.SPECULATIVE,
        durability=ContextSourceDurability.WORKING,
        intended_uses=("hypothesis_generation", "exploration"),
    ),
    "releases": _DocumentOntologyProfile(
        source_class=ContextSourceClass.RELEASES,
        authority=ContextSourceAuthority.HISTORICAL,
        durability=ContextSourceDurability.ARCHIVAL,
        intended_uses=("history", "operations"),
    ),
}
_DEFAULT_PROFILE = _DocumentOntologyProfile(
    source_class=ContextSourceClass.OTHER,
    authority=ContextSourceAuthority.ADVISORY,
    durability=ContextSourceDurability.WORKING,
    intended_uses=(),
)


class FilesystemDocumentSourceAdapter:
    """Load markdown documentation files as ontology-aware Atlas sources."""

    def __init__(self, root_path: str | Path) -> None:
        root = Path(root_path).expanduser().resolve()
        if not root.exists():
            raise ContextAtlasError(
                code=ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
                message_args=(ErrorMessage.ROOT_PATH_DOES_NOT_EXIST % (root,),),
            )
        if not root.is_dir():
            raise ContextAtlasError(
                code=ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
                message_args=(ErrorMessage.ROOT_PATH_IS_NOT_A_DIRECTORY % (root,),),
            )
        self._root = root

    @property
    def root_path(self) -> Path:
        """Return the adapter's resolved filesystem root."""

        return self._root

    def load_sources(self) -> tuple[ContextSource, ...]:
        """Load all supported documents below the configured root."""

        document_paths = sorted(
            path
            for path in self._root.rglob("*")
            if path.is_file() and path.suffix.lower() in _SUPPORTED_SUFFIXES
        )
        return tuple(self.load_source(path) for path in document_paths)

    def load_source(self, path: str | Path) -> ContextSource:
        """Load one markdown document as a canonical Atlas source."""

        document_path = Path(path).expanduser().resolve()
        if not document_path.exists():
            raise ContextAtlasError(
                code=ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
                message_args=(
                    ErrorMessage.DOCUMENT_PATH_DOES_NOT_EXIST % (document_path,),
                ),
            )
        if not document_path.is_file():
            raise ContextAtlasError(
                code=ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
                message_args=(
                    ErrorMessage.DOCUMENT_PATH_IS_NOT_A_FILE % (document_path,),
                ),
            )
        if document_path.suffix.lower() not in _SUPPORTED_SUFFIXES:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
                message_args=(
                    ErrorMessage.UNSUPPORTED_DOCUMENT_SUFFIX
                    % (document_path.suffix, document_path),
                ),
            )

        try:
            relative_path = document_path.relative_to(self._root)
        except ValueError as error:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
                message_args=(
                    ErrorMessage.DOCUMENT_PATH_OUTSIDE_ADAPTER_ROOT
                    % (document_path, self._root),
                ),
            ) from error

        raw_text = document_path.read_text(encoding="utf-8")
        front_matter_raw, content = _split_front_matter(raw_text)
        front_matter = self._validate_front_matter(
            front_matter_raw,
            relative_path=relative_path,
        )
        classification = self._classify_document(
            relative_path=relative_path,
            front_matter=front_matter,
        )
        checksum = hashlib.sha256(document_path.read_bytes()).hexdigest()
        stat = document_path.stat()

        source = ContextSource(
            source_id=relative_path.as_posix(),
            content=content,
            title=front_matter.title or _extract_title(content, document_path),
            source_class=classification.source_class,
            authority=classification.authority,
            durability=classification.durability,
            provenance=ContextSourceProvenance(
                source_uri=document_path.as_uri(),
                collector="filesystem_document_source_adapter",
                captured_at_utc=datetime.fromtimestamp(
                    stat.st_mtime,
                    tz=UTC,
                )
                .replace(microsecond=0)
                .isoformat()
                .replace("+00:00", "Z"),
                checksum=checksum,
                metadata={
                    "classification_source": classification.classification_source,
                    "relative_path": relative_path.as_posix(),
                    "path_doc_class": classification.path_doc_class or "",
                    "frontmatter_doc_class": classification.frontmatter_doc_class or "",
                    "classification_mismatch": str(
                        classification.has_class_mismatch
                    ).lower(),
                },
            ),
            tags=_merge_unique_values(
                front_matter.tags,
                (
                    classification.source_class.value
                    if classification.source_class is not ContextSourceClass.OTHER
                    else "",
                ),
            ),
            intended_uses=_merge_unique_values(
                classification.profile.intended_uses,
                front_matter.intended_uses,
            ),
            metadata={
                "classification_source": classification.classification_source,
                "relative_path": relative_path.as_posix(),
                "doc_class": classification.source_class.value,
            },
        )
        self._emit_classification_log(source)
        return source

    def _validate_front_matter(
        self,
        raw_front_matter: dict[str, object],
        *,
        relative_path: Path,
    ) -> _DocumentFrontMatter:
        """Validate raw front matter into the subset relevant for Atlas."""

        try:
            return _DocumentFrontMatter.model_validate(raw_front_matter)
        except ValidationError as error:
            raise ContextAtlasError(
                code=ErrorCode.INVALID_SOURCE_ADAPTER_INPUT,
                message_args=(
                    ErrorMessage.INVALID_FRONT_MATTER_IN_DOCUMENT
                    % (relative_path.as_posix(), error),
                ),
            ) from error

    def _classify_document(
        self,
        *,
        relative_path: Path,
        front_matter: _DocumentFrontMatter,
    ) -> "_DocumentClassification":
        """Resolve classification from front matter first, then path, then default."""

        path_doc_class = _doc_class_from_path(relative_path)
        frontmatter_doc_class = front_matter.doc_class
        resolved_doc_class = frontmatter_doc_class or path_doc_class
        if resolved_doc_class is None:
            profile = _DEFAULT_PROFILE
            classification_source = "default"
        else:
            profile_candidate = _PROFILE_BY_DOC_CLASS.get(resolved_doc_class)
            if profile_candidate is None:
                raise ContextAtlasError(
                    code=ErrorCode.UNSUPPORTED_DOCUMENT_CLASS,
                    message_args=(resolved_doc_class,),
                )
            profile = profile_candidate
            classification_source = "frontmatter" if frontmatter_doc_class else "path"

        return _DocumentClassification(
            profile=profile,
            source_class=profile.source_class,
            authority=front_matter.authority or profile.authority,
            durability=front_matter.durability or profile.durability,
            classification_source=classification_source,
            path_doc_class=path_doc_class,
            frontmatter_doc_class=frontmatter_doc_class,
            has_class_mismatch=bool(
                frontmatter_doc_class
                and path_doc_class
                and frontmatter_doc_class != path_doc_class
            ),
        )

    def _emit_classification_log(self, source: ContextSource) -> None:
        """Emit one stable log line for each classified source."""

        logger.info(
            LogMessage.SOURCE_CLASSIFIED,
            source.source_id,
            source.source_class.value,
            extra={
                "event": LogMessage.SOURCE_CLASSIFIED.event_name,
                "source_id": source.source_id,
                "source_class": source.source_class.value,
                "authority": source.authority.value,
                "collector": source.provenance.collector,
            },
        )


class _DocumentClassification(BaseModel):
    """Resolved classification outcome for one document."""

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    profile: _DocumentOntologyProfile
    source_class: ContextSourceClass
    authority: ContextSourceAuthority
    durability: ContextSourceDurability
    classification_source: str
    path_doc_class: str | None = None
    frontmatter_doc_class: str | None = None
    has_class_mismatch: bool = False


def _split_front_matter(text: str) -> tuple[dict[str, object], str]:
    """Split leading front matter from markdown content when present."""

    if not text.startswith(f"{_FRONT_MATTER_DELIMITER}\n") and not text.startswith(
        f"{_FRONT_MATTER_DELIMITER}\r\n"
    ):
        return {}, text.strip()

    lines = text.splitlines()
    if not lines or lines[0].strip() != _FRONT_MATTER_DELIMITER:
        return {}, text.strip()

    front_matter_lines: list[str] = []
    closing_index: int | None = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == _FRONT_MATTER_DELIMITER:
            closing_index = index
            break
        front_matter_lines.append(line)

    if closing_index is None:
        return {}, text.strip()

    body = "\n".join(lines[closing_index + 1 :]).strip()
    return _parse_front_matter(front_matter_lines), body


def _parse_front_matter(lines: list[str]) -> dict[str, object]:
    """Parse the simple front matter shapes Atlas currently cares about."""

    parsed: dict[str, object] = {}
    active_list_key: str | None = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            active_list_key = None
            continue

        if active_list_key is not None and stripped.startswith("- "):
            values = parsed.setdefault(active_list_key, [])
            if isinstance(values, list):
                values.append(_strip_quotes(stripped[2:].strip()))
            continue

        active_list_key = None
        match = re.match(r"^(?P<key>[A-Za-z0-9_-]+)\s*:\s*(?P<value>.*)$", stripped)
        if match is None:
            continue

        key = match.group("key")
        raw_value = match.group("value").strip()
        if not raw_value:
            active_list_key = key
            parsed[key] = []
            continue

        parsed[key] = _parse_scalar_or_list(raw_value)

    return parsed


def _parse_scalar_or_list(raw_value: str) -> object:
    """Parse a scalar string or a simple inline list from front matter."""

    if raw_value.startswith("[") and raw_value.endswith("]"):
        inner = raw_value[1:-1].strip()
        if not inner:
            return []
        return [
            _strip_quotes(part.strip()) for part in inner.split(",") if part.strip()
        ]
    return _strip_quotes(raw_value)


def _strip_quotes(value: str) -> str:
    """Strip one layer of matching quotes from a scalar front matter value."""

    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _doc_class_from_path(relative_path: Path) -> str | None:
    """Infer a document class from known ontology path segments."""

    for part in relative_path.parts:
        normalized = part.strip().lower()
        if normalized in _CLASS_SEGMENT_BY_NAME:
            return normalized
    return None


def _extract_title(content: str, document_path: Path) -> str:
    """Infer a human-readable title from the first heading or file stem."""

    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return document_path.stem.replace("-", " ").replace("_", " ").strip()


def _merge_unique_values(*groups: Iterable[str]) -> tuple[str, ...]:
    """Merge text groups while preserving first-seen order."""

    ordered: list[str] = []
    seen: set[str] = set()
    for group in groups:
        for item in group:
            normalized = item.strip()
            if not normalized or normalized in seen:
                continue
            ordered.append(normalized)
            seen.add(normalized)
    return tuple(ordered)


__all__ = ["FilesystemDocumentSourceAdapter"]
