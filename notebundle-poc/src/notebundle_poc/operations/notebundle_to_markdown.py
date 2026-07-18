from __future__ import annotations

import shutil
from pathlib import Path
from dataclasses import dataclass


from notebundle_poc.operations.validate import validate_notebundle


@dataclass(frozen=True, slots=True)
class NotebundleToMarkdownResult:
    source: Path
    output: Path


def notebundle_to_markdown(
    source: Path,
    output: Path | None = None,
) -> NotebundleToMarkdownResult | Exception:
    if validate_notebundle(source).is_valid == False:
        return ValueError(f"Not valid source notebundle: {source}")

    destination = output

    if destination is None:
        destination = source.with_name(source.name.removesuffix(".notebundle"))

    if destination.exists():
        return FileExistsError(f"Destination already exists: {destination}")

    shutil.copytree(source, destination)

    return NotebundleToMarkdownResult(source=source, output=destination)
