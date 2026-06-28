"""
Tests for the organizer module.

I'm using tmp_path (pytest's built-in fixture) so tests never touch
the real filesystem. Learned that the hard way years ago.
"""

import pytest
from pathlib import Path

from organize_files.organizer import organize
from organize_files.categories import get_category


# --- category mapping ---

def test_known_extension_returns_correct_category():
    assert get_category(".jpg") == "images"
    assert get_category(".mp4") == "videos"
    assert get_category(".pdf") == "docs"
    assert get_category(".zip") == "archives"
    assert get_category(".py") == "code"


def test_unknown_extension_returns_misc():
    assert get_category(".xyz") == "misc"
    assert get_category(".whatisthis") == "misc"


def test_extension_matching_is_case_insensitive():
    assert get_category(".JPG") == "images"
    assert get_category(".MP4") == "videos"


# --- organizer ---

def test_moves_files_into_correct_subfolders(tmp_path):
    (tmp_path / "photo.jpg").touch()
    (tmp_path / "report.pdf").touch()
    (tmp_path / "script.py").touch()

    result = organize(tmp_path)

    assert (tmp_path / "images" / "photo.jpg").exists()
    assert (tmp_path / "docs" / "report.pdf").exists()
    assert (tmp_path / "code" / "script.py").exists()
    assert len(result.moved) == 3
    assert len(result.errors) == 0


def test_dry_run_does_not_move_anything(tmp_path):
    (tmp_path / "photo.jpg").touch()
    (tmp_path / "report.pdf").touch()

    result = organize(tmp_path, dry_run=True)

    # files should still be in the original location
    assert (tmp_path / "photo.jpg").exists()
    assert (tmp_path / "report.pdf").exists()
    assert len(result.moved) == 2  # reported as "would move"


def test_skips_hidden_files_by_default(tmp_path):
    (tmp_path / ".DS_Store").touch()
    (tmp_path / "photo.jpg").touch()

    result = organize(tmp_path)

    assert (tmp_path / ".DS_Store").exists()  # should NOT have moved
    assert len(result.skipped) == 1
    assert len(result.moved) == 1


def test_include_hidden_moves_hidden_files(tmp_path):
    (tmp_path / ".DS_Store").touch()

    result = organize(tmp_path, skip_hidden=False)

    assert len(result.moved) == 1
    assert len(result.skipped) == 0


def test_conflict_resolution_does_not_overwrite(tmp_path):
    # put a file in place already
    (tmp_path / "images").mkdir()
    (tmp_path / "images" / "photo.jpg").write_text("original")

    # now try to move another file with the same name
    (tmp_path / "photo.jpg").write_text("new")

    result = organize(tmp_path)

    assert (tmp_path / "images" / "photo.jpg").read_text() == "original"
    assert (tmp_path / "images" / "photo (1).jpg").exists()
    assert len(result.moved) == 1


def test_raises_if_directory_does_not_exist():
    with pytest.raises(FileNotFoundError):
        organize(Path("/this/does/not/exist"))


def test_raises_if_path_is_a_file(tmp_path):
    f = tmp_path / "somefile.txt"
    f.touch()
    with pytest.raises(NotADirectoryError):
        organize(f)


def test_empty_directory_returns_empty_result(tmp_path):
    result = organize(tmp_path)
    assert result.total == 0
