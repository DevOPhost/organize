import shutil
from dataclasses import dataclass, field
from pathlib import Path

from .categories import get_category


@dataclass
class MoveResult:
    moved: list[tuple[Path, Path]] = field(default_factory=list)
    skipped: list[Path] = field(default_factory=list)
    errors: list[tuple[Path, str]] = field(default_factory=list)

    @property
    def total(self) -> int:
        return len(self.moved) + len(self.skipped) + len(self.errors)


def organize(
    source: Path,
    dry_run: bool = False,
    skip_hidden: bool = True,
) -> MoveResult:
    """
    Walk through `source` and move files into subfolders by extension.

    I'm intentionally not making this recursive by default — organizing
    nested directories without asking first felt too aggressive.
    """
    if not source.exists():
        raise FileNotFoundError(f"Directory not found: {source}")
    if not source.is_dir():
        raise NotADirectoryError(f"Not a directory: {source}")

    result = MoveResult()

    files = [f for f in source.iterdir() if f.is_file()]

    for file in files:
        # skip hidden files like .DS_Store, .gitkeep, etc.
        if skip_hidden and file.name.startswith("."):
            result.skipped.append(file)
            continue

        category = get_category(file.suffix)
        destination_dir = source / category
        destination = destination_dir / file.name

        # if a file with the same name already exists, append a counter
        # rather than silently overwriting — that would be bad
        if destination.exists():
            destination = _resolve_conflict(destination)

        if dry_run:
            result.moved.append((file, destination))
            continue

        try:
            destination_dir.mkdir(exist_ok=True)
            shutil.move(str(file), str(destination))
            result.moved.append((file, destination))
        except Exception as exc:
            result.errors.append((file, str(exc)))

    return result


def _resolve_conflict(path: Path) -> Path:
    """Append (1), (2), etc. until we find a free name."""
    counter = 1
    stem = path.stem
    suffix = path.suffix
    parent = path.parent

    while True:
        candidate = parent / f"{stem} ({counter}){suffix}"
        if not candidate.exists():
            return candidate
        counter += 1
