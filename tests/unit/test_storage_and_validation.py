from pathlib import Path

import pytest

from todo_lib.services import ValidationError, normalize_title
from todo_lib.storage import StorageInitializationError, verify_or_recover_database


def test_normalize_title_strips_whitespace():
    assert normalize_title("  회의록 작성  ") == "회의록 작성"


def test_normalize_title_rejects_blank_value():
    with pytest.raises(ValidationError, match="제목은 비어 있을 수 없습니다"):
        normalize_title("   ")


def test_verify_or_recover_database_raises_and_keeps_backup(tmp_path):
    database_path = tmp_path / "todo.db"
    database_path.write_text("not-a-sqlite-db", encoding="utf-8")

    with pytest.raises(StorageInitializationError, match="손상"):
        verify_or_recover_database(database_path)

    backups = list(tmp_path.glob("todo.corrupt.*.bak"))
    assert len(backups) == 1
    assert database_path.exists()


def test_verify_or_recover_database_resets_on_corruption(tmp_path):
    database_path = tmp_path / "todo.db"
    database_path.write_text("not-a-sqlite-db", encoding="utf-8")

    backup_path = verify_or_recover_database(database_path, reset_on_corruption=True)

    assert isinstance(backup_path, Path)
    assert backup_path.exists()
    assert not database_path.exists()