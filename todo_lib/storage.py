from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from shutil import copy2

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from todo_lib.models import Base


DEFAULT_DB_FILENAME = "todo.db"


class StorageInitializationError(RuntimeError):
    """저장소 초기화 실패를 나타낸다."""


@dataclass(slots=True)
class StorageContext:
    database_path: Path
    engine: Engine
    session_factory: sessionmaker[Session]


def resolve_database_path(data_dir: Path, filename: str = DEFAULT_DB_FILENAME) -> Path:
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / filename


def backup_corrupt_database(database_path: Path) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    backup_path = database_path.with_suffix(f".corrupt.{timestamp}.bak")
    copy2(database_path, backup_path)
    return backup_path


def verify_or_recover_database(database_path: Path, reset_on_corruption: bool = False) -> Path | None:
    if not database_path.exists():
        return None

    try:
        connection = sqlite3.connect(database_path)
        cursor = connection.execute("PRAGMA integrity_check;")
        result = cursor.fetchone()
        connection.close()
    except sqlite3.DatabaseError as exc:
        backup_path = backup_corrupt_database(database_path)
        if reset_on_corruption:
            database_path.unlink(missing_ok=True)
            return backup_path
        raise StorageInitializationError(
            f"저장소가 손상되었습니다. 백업 파일: {backup_path}"
        ) from exc

    if result and result[0] == "ok":
        return None

    backup_path = backup_corrupt_database(database_path)
    if reset_on_corruption:
        database_path.unlink(missing_ok=True)
        return backup_path

    raise StorageInitializationError(f"저장소 무결성 검사 실패. 백업 파일: {backup_path}")


def create_storage_context(data_dir: Path, reset_on_corruption: bool = False) -> StorageContext:
    database_path = resolve_database_path(data_dir)
    verify_or_recover_database(database_path, reset_on_corruption=reset_on_corruption)

    engine = create_engine(f"sqlite+pysqlite:///{database_path}", future=True)
    session_factory = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False, future=True)
    return StorageContext(database_path=database_path, engine=engine, session_factory=session_factory)


def initialize_database(context: StorageContext) -> None:
    Base.metadata.create_all(context.engine)
    with context.engine.begin() as connection:
        connection.execute(text("PRAGMA foreign_keys = ON"))


def healthcheck_database(context: StorageContext) -> None:
    try:
        with context.engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError as exc:
        raise StorageInitializationError("저장소 연결 확인에 실패했습니다.") from exc