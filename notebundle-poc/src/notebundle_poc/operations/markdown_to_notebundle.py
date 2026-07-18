from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class MarkdownToNotebundleResult:
    source: Path
    output: Path
    primary_note: Path


def markdown_to_notebundle(
    source: Path,
    output: Path | None = None,
) -> MarkdownToNotebundleResult | Exception:
    if not source.is_file():
        return ValueError(f"Source must be a Markdown file: {source}")

    if source.suffix.lower() not in {".md", ".markdown"}:
        return ValueError(f"Source must have .md or .markdown extension: {source}")

    destination = output

    if destination is None:
        destination = source.with_name(f"{source.stem}.notebundle")

    if not destination.name.endswith(".notebundle"):
        return ValueError(f"Output must end with .notebundle: {destination}")

    if destination.exists():
        return FileExistsError(f"Destination already exists: {destination}")

    destination.mkdir(parents=True)

    bundle_name = destination.name.removesuffix(".notebundle")
    primary_note = destination / f"{bundle_name}.md"

    shutil.copy2(source, primary_note)

    return MarkdownToNotebundleResult(
        source=source,
        output=destination,
        primary_note=primary_note,
    )
