from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class TextbundleToNotebundleResult:
    source: Path
    output: Path
    primary_note: Path
    attachments_dir: Path | None


def textbundle_to_notebundle(
    source: Path,
    output: Path | None = None,
) -> TextbundleToNotebundleResult | Exception:
    if not source.is_dir():
        return ValueError(f"Source must be a TextBundle directory: {source}")

    if not source.name.endswith(".textbundle"):
        return ValueError(f"Source must end with .textbundle: {source}")

    # The TextBundle specification itself allows `text.*` without restricting the extension,
    # but this PoC project limits it for convenience.

    md_source_text = source / "text.md"
    markdown_source_text = source / "text.markdown"

    source_text = (
        md_source_text if md_source_text.is_file() == True else markdown_source_text
    )

    if source_text.is_file() == False:
        return ValueError(
            f"Source TextBundle must contain text.md or text.markdown. (This PoC only supports Markdown TextBundle files, although the TextBundle specification allows `text.*`."
        )

    destination = output

    if destination is None:
        destination = source.with_name(
            source.name.removesuffix(".textbundle") + ".notebundle"
        )

    if not destination.name.endswith(".notebundle"):
        return ValueError(f"Output must end with .notebundle: {destination}")

    if destination.exists():
        return FileExistsError(f"Destination already exists: {destination}")

    destination.mkdir(parents=True)

    bundle_name = destination.name.removesuffix(".notebundle")
    primary_note = destination / f"{bundle_name}.md"

    markdown = source_text.read_text(encoding="utf-8")

    markdown = markdown.replace("assets/", "attachments/")  # Just replace

    primary_note.write_text(markdown, encoding="utf-8")

    source_assets = source / "assets"
    attachments_dir: Path | None = None

    if source_assets.exists():
        if not source_assets.is_dir():
            return ValueError(f"TextBundle assets must be a directory: {source_assets}")

        attachments_dir = destination / "attachments"
        shutil.copytree(source_assets, attachments_dir)

    return TextbundleToNotebundleResult(
        source=source,
        output=destination,
        primary_note=primary_note,
        attachments_dir=attachments_dir,
    )
