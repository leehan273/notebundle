from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path

from notebundle_poc.operations.validate import validate_notebundle


@dataclass(frozen=True, slots=True)
class NotebundleToTextbundleResult:
    source: Path
    output: Path
    text_file: Path
    assets_dir: Path | None
    info_json: Path


def notebundle_to_textbundle(
    source: Path,
    output: Path | None = None,
) -> NotebundleToTextbundleResult | Exception:
    if validate_notebundle(source).is_valid == False:
        return ValueError(f"Not valid source notebundle: {source}")

    destination = output

    if destination is None:
        destination = source.with_name(
            source.name.removesuffix(".notebundle") + ".textbundle"
        )

    if not destination.name.endswith(".textbundle"):
        return ValueError(f"Output must end with .textbundle: {destination}")

    if destination.exists():
        return FileExistsError(f"Destination already exists: {destination}")

    primary_note = find_primary_note(source)

    if primary_note is None:
        return ValueError(f"Primary note not found: {source}")

    if primary_note.suffix.lower() not in {".md", ".markdown"}:
        return ValueError(f"Primary note must be Markdown: {primary_note}")

    destination.mkdir(parents=True)

    text_file: Path = destination / "text.md"

    markdown = primary_note.read_text(encoding="utf-8")
    markdown = markdown.replace("attachments/", "assets/")
    text_file.write_text(markdown, encoding="utf-8")

    source_attachments: Path = source / "attachments"
    assets_dir: Path | None = None

    if source_attachments.exists():
        if not source_attachments.is_dir():
            return ValueError(
                f"Notebundle attachments must be a directory: {source_attachments}"
            )

        assets_dir = destination / "assets"
        shutil.copytree(source_attachments, assets_dir)

    info_json = destination / "info.json"
    info_json.write_text(
        json.dumps(
            {
                "version": 2,
                "type": "net.daringfireball.markdown",
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    return NotebundleToTextbundleResult(
        source=source,
        output=destination,
        text_file=text_file,
        assets_dir=assets_dir,
        info_json=info_json,
    )


def find_primary_note(source: Path) -> Path | None:
    bundle_name = source.name.removesuffix(".notebundle")

    candidates: list[Path] = []

    for entry in source.iterdir():
        if not entry.is_file():
            continue

        if entry.stem == bundle_name:
            candidates.append(entry)
            continue

        if entry.stem == "note":
            candidates.append(entry)
            continue

    if len(candidates) != 1:
        return None

    return candidates[0]
