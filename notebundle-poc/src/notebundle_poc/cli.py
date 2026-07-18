from __future__ import annotations

import argparse
from pathlib import Path

from notebundle_poc.operations import (
    validate,
    markdown_to_notebundle,
    notebundle_to_markdown,
    textbundle_to_notebundle,
    notebundle_to_textbundle,
)


def main(argv: list[str] | None = None) -> int:

    PROGRAM_NAME = "notebundle-poc"
    PROGRAM_DESCRIPTION = "Notebundle PoC"

    parser = argparse.ArgumentParser(prog=PROGRAM_NAME, description=PROGRAM_DESCRIPTION)
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ```
    # notebundle-poc validate example-files/notebundle-example.notebundle
    # ```
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("path", type=Path)

    # ```
    # notebundle-poc markdown-to-notebundle \
    #   example-files/markdown-example.md \
    #   output/notebundle-from-markdown.notebundle
    # ```
    m2n_parser = subparsers.add_parser("markdown-to-notebundle")
    m2n_parser.add_argument("source", type=Path)
    m2n_parser.add_argument("output", type=Path)

    # ```
    # notebundle-poc notebundle-to-markdown \
    #   example-files/notebundle-example.notebundle \
    #   output/markdown-dir-from-notebundle
    # ```
    n2m_parser = subparsers.add_parser("notebundle-to-markdown")
    n2m_parser.add_argument("source", type=Path)
    n2m_parser.add_argument("output", type=Path)

    # ```
    # notebundle-poc textbundle-to-notebundle \
    #   example-files/textbundle-example.textbundle \
    #   output/notebundle-from-textbundle.notebundle
    # ```
    t2n_parser = subparsers.add_parser("textbundle-to-notebundle")
    t2n_parser.add_argument("source", type=Path)
    t2n_parser.add_argument("output", type=Path)

    # ```
    # notebundle-poc notebundle-to-textbundle \
    #   example-files/notebundle-example.notebundle \
    #   output/textbundle-from-notebundle.textbundle
    # ```
    n2t_parser = subparsers.add_parser("notebundle-to-textbundle")
    n2t_parser.add_argument("source", type=Path)
    n2t_parser.add_argument("output", type=Path)

    args = parser.parse_args(argv)

    if args.command == "validate":
        result = validate.validate_notebundle(args.path)
        print(render_result(result))

        if result.is_valid:
            return 0

        return 1

    if args.command == "markdown-to-notebundle":
        result = markdown_to_notebundle.markdown_to_notebundle(args.source, args.output)
        print(render_result(result))

        if isinstance(result, Exception):
            return 1

        return 0

    if args.command == "notebundle-to-markdown":
        result = notebundle_to_markdown.notebundle_to_markdown(args.source, args.output)
        print(render_result(result))

        if isinstance(result, Exception):
            return 1

        return 0

    if args.command == "textbundle-to-notebundle":
        result = textbundle_to_notebundle.textbundle_to_notebundle(
            args.source,
            args.output,
        )
        print(render_result(result))

        if isinstance(result, Exception):
            return 1

        return 0

    if args.command == "notebundle-to-textbundle":
        result = notebundle_to_textbundle.notebundle_to_textbundle(
            args.source,
            args.output,
        )
        print(render_result(result))

        if isinstance(result, Exception):
            return 1

        return 0

    return 0


def render_result(result: object) -> str:
    if isinstance(result, Exception):
        return render_exception(result)

    if isinstance(result, validate.ValidationResult):
        return render_validation_result(result)

    if isinstance(result, markdown_to_notebundle.MarkdownToNotebundleResult):
        return render_markdown_to_notebundle_result(result)

    if isinstance(result, notebundle_to_markdown.NotebundleToMarkdownResult):
        return render_notebundle_to_markdown_result(result)

    if isinstance(result, textbundle_to_notebundle.TextbundleToNotebundleResult):
        return render_textbundle_to_notebundle_result(result)

    if isinstance(result, notebundle_to_textbundle.NotebundleToTextbundleResult):
        return render_notebundle_to_textbundle_result(result)

    return str(result)


def render_exception(error: Exception) -> str:
    lines: list[str] = [
        "",
        "Error",
        "",
        f"Type: {type(error).__name__}",
        f"Message: {error}",
        "",
    ]

    return "\n".join(lines)


def render_validation_result(result: validate.ValidationResult) -> str:
    lines: list[str] = [
        "",
        "Validation Result",
        "",
        f"Valid: {result.is_valid}",
        "",
    ]

    lines.extend(render_path_tree(result.path, title="Path"))
    lines.append("")
    lines.append("")

    if len(result.issues) > 0:
        lines.append("Issues")
        lines.append("------")

        for issue in result.issues:
            lines.extend(render_issue_lines(issue))

        lines.append("")

    return "\n".join(lines)


def render_markdown_to_notebundle_result(
    result: markdown_to_notebundle.MarkdownToNotebundleResult,
) -> str:
    lines: list[str] = [
        "",
        "Markdown to Notebundle Result",
        "",
    ]

    lines.extend(render_path_tree(result.source, title="Source"))
    lines.append("")
    lines.append("")
    lines.extend(render_path_tree(result.output, title="Output"))
    lines.append("")
    lines.append("")
    lines.append(f"Primary note: {result.primary_note}")
    lines.append("")

    return "\n".join(lines)


def render_notebundle_to_markdown_result(
    result: notebundle_to_markdown.NotebundleToMarkdownResult,
) -> str:
    lines: list[str] = [
        "",
        "Notebundle to Markdown Result",
        "",
    ]

    lines.extend(render_path_tree(result.source, title="Source"))
    lines.append("")
    lines.append("")
    lines.extend(render_path_tree(result.output, title="Output"))
    lines.append("")
    lines.append("")

    return "\n".join(lines)


def render_textbundle_to_notebundle_result(
    result: textbundle_to_notebundle.TextbundleToNotebundleResult,
) -> str:
    lines: list[str] = [
        "",
        "TextBundle to Notebundle Result",
        "",
    ]

    lines.extend(render_path_tree(result.source, title="Source"))
    lines.append("")
    lines.append("")
    lines.extend(render_path_tree(result.output, title="Output"))
    lines.append("")
    lines.append("")
    lines.append(f"Primary note: {result.primary_note}")
    lines.append(f"Attachments dir: {format_optional_path(result.attachments_dir)}")
    lines.append("")

    return "\n".join(lines)


def render_notebundle_to_textbundle_result(
    result: notebundle_to_textbundle.NotebundleToTextbundleResult,
) -> str:
    lines: list[str] = [
        "",
        "Notebundle to TextBundle Result",
        "",
    ]

    lines.extend(render_path_tree(result.source, title="Source"))
    lines.append("")
    lines.append("")
    lines.extend(render_path_tree(result.output, title="Output"))
    lines.append("")
    lines.append("")
    lines.append(f"Text file: {result.text_file}")
    lines.append(f"Assets dir: {format_optional_path(result.assets_dir)}")
    lines.append(f"Info JSON: {result.info_json}")
    lines.append("")

    return "\n".join(lines)


def render_issue_lines(issue: object) -> list[str]:
    level = getattr(issue, "level", "unknown")
    title = getattr(issue, "title", "")
    description = getattr(issue, "description", "")

    lines: list[str] = [
        f"- [{level}] {title}",
    ]

    if description:
        lines.append(f"  {description}")

    return lines


def format_optional_path(path: Path | None) -> str:
    if path is None:
        return "-"

    return str(path)


def render_path_tree(path: Path, *, title: str) -> list[str]:
    lines: list[str] = [
        f"{title}: {path}",
        "-" * len(f"{title}: {path}"),
    ]

    if not path.exists():
        lines.append(f"{path.name}")
        lines.append("  <does not exist>")
        return lines

    lines.append(path.name)

    if path.is_file():
        return lines

    for item in sorted(path.rglob("*")):
        relative = item.relative_to(path)
        depth = len(relative.parts)

        indent = "  " * depth
        lines.append(f"{indent}- {item.name}")

    return lines


if __name__ == "__main__":
    raise SystemExit(main())
