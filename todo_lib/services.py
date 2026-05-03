from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Literal

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from todo_lib.models import ToDoItem, TodoPriority


class ValidationError(ValueError):
    """입력 검증 실패를 나타낸다."""


class NotFoundError(ValueError):
    """조회 대상이 없을 때 발생한다."""


@dataclass(slots=True)
class ServiceContext:
    """비즈니스 서비스에서 공통으로 사용하는 의존성 묶음."""

    session_factory: sessionmaker[Session]


def normalize_title(title: str) -> str:
    normalized = title.strip()
    if not normalized:
        raise ValidationError("제목은 비어 있을 수 없습니다.")
    if len(normalized) > 200:
        raise ValidationError("제목은 200자를 초과할 수 없습니다.")
    return normalized


def add_todo(
    context: ServiceContext,
    title: str,
    due_date: date | None = None,
    priority: TodoPriority = TodoPriority.MEDIUM,
) -> ToDoItem:
    normalized_title = normalize_title(title)

    item = ToDoItem(
        title=normalized_title,
        due_date=due_date,
        priority=priority,
    )

    with context.session_factory() as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item


def list_todos(
    context: ServiceContext,
    status_filter: Literal["done", "pending"] | None = None,
    priority: TodoPriority | None = None,
) -> list[ToDoItem]:
    statement = select(ToDoItem)

    if status_filter == "done":
        statement = statement.where(ToDoItem.is_done.is_(True))
    elif status_filter == "pending":
        statement = statement.where(ToDoItem.is_done.is_(False))

    if priority is not None:
        statement = statement.where(ToDoItem.priority == priority)

    statement = statement.order_by(ToDoItem.created_at.desc())

    with context.session_factory() as session:
        return list(session.scalars(statement))


def complete_todo(context: ServiceContext, todo_id: int) -> tuple[ToDoItem, bool]:
    if todo_id <= 0:
        raise ValidationError("ID는 1 이상의 정수여야 합니다.")

    with context.session_factory() as session:
        item = session.get(ToDoItem, todo_id)
        if item is None:
            raise NotFoundError("존재하지 않는 항목입니다.")

        if item.is_done:
            return item, False

        item.is_done = True
        session.commit()
        session.refresh(item)
        return item, True


def delete_todo(context: ServiceContext, todo_id: int) -> ToDoItem:
    if todo_id <= 0:
        raise ValidationError("ID는 1 이상의 정수여야 합니다.")

    with context.session_factory() as session:
        item = session.get(ToDoItem, todo_id)
        if item is None:
            raise NotFoundError("존재하지 않는 항목입니다.")

        session.delete(item)
        session.commit()
        return item