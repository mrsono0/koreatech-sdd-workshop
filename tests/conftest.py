from pathlib import Path

import pytest

from todo_lib.storage import StorageContext, create_storage_context, initialize_database


@pytest.fixture()
def temp_data_dir(tmp_path: Path) -> Path:
    """테스트마다 독립적인 데이터 디렉터리를 제공한다."""

    data_dir = tmp_path / "data"
    data_dir.mkdir()
    return data_dir


@pytest.fixture()
def storage_context(temp_data_dir: Path) -> StorageContext:
    """임시 SQLite 저장소 컨텍스트를 생성한다."""

    context = create_storage_context(temp_data_dir)
    initialize_database(context)
    return context