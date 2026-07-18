from __future__ import annotations

from pathlib import Path

from dataclasses import dataclass

from typing import Literal


@dataclass(frozen=True, slots=True)
class Issue:
    level: Literal["error", "warning"]
    title: str
    description: str


@dataclass(frozen=True, slots=True)
class ValidationResult:
    path: Path
    issues: list[Issue]

    @property
    def is_valid(self) -> bool:
        return not any(issue.level == "error" for issue in self.issues)


def validate_notebundle(path: Path) -> ValidationResult:

    # If not directory, can't progress more.
    if path.is_dir() == False:
        return ValidationResult(
            path=path,
            issues=[
                Issue(
                    level="error",
                    title="Notebundle must be a directory.",
                    description=f"`{path}` is not a directory.",
                )
            ],
        )

    issues: list[Issue] = []

    has_notebundle_suffix: bool = path.name.endswith(".notebundle")

    bundle_name: str = (
        path.name.removesuffix(".notebundle") if has_notebundle_suffix else path.name
    )

    if has_notebundle_suffix == False:
        issues.append(
            Issue(
                level="error",
                title="Notebundle directory must end with `.notebundle`.",
                description=f"`{path.name}` does not have the `.notebundle` suffix.",
            )
        )

    def get_primary_note_candidates(target_name_list: list[str]) -> list[Path]:

        candidates: list[Path] = []

        for entry in path.iterdir():
            if entry.is_file() == False:
                continue

            for target_name in target_name_list:
                if entry.name.startswith(f"{target_name}."):
                    candidates.append(entry)

        temp_set_for_remove_duplicate = set(candidates)

        return list(temp_set_for_remove_duplicate)

    expected_primary_note_name_case_list = [bundle_name, "note"]

    primary_note_candidates: list[Path] = get_primary_note_candidates(
        expected_primary_note_name_case_list
    )

    is_primary_note_detectable: bool = (
        True if len(primary_note_candidates) == 1 else False
    )

    if is_primary_note_detectable == False:
        primary_note_candidates_number = len(primary_note_candidates)

        if primary_note_candidates_number == 0:
            issues.append(
                Issue(
                    level="error",
                    title="Primary note is missing.",
                    description=(
                        "A Notebundle must contain exactly one root-level primary note named "
                        f"`{bundle_name}.*` or `note.*`."
                    ),
                )
            )
        if primary_note_candidates_number >= 2:
            issues.append(
                Issue(
                    level="error",
                    title="Primary note is unclear.",
                    description=(
                        "Multiple primary note candidates were found: "
                        f"{primary_note_candidates}. "
                        "A Notebundle must have exactly one primary note."
                    ),
                )
            )

    attachments_directory_path = path / "attachments"

    if attachments_directory_path.exists():
        if attachments_directory_path.is_dir() == False:
            issues.append(
                Issue(
                    level="error",
                    title="`attachments` must be a directory.",
                    description=(
                        f"`{attachments_directory_path}` exists, "
                        "but it is not a directory."
                    ),
                )
            )

    return ValidationResult(
        path=path,
        issues=issues,
    )
