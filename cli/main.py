"""Typer 기반 CLI 엔트리포인트."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Annotated, Literal

import typer

from todo_lib.models import TodoPriority
from todo_lib.services import (
    NotFoundError,
    ServiceContext,
    ValidationError,
    add_todo,
    complete_todo,
    delete_todo,
    list_todos,
)
from todo_lib.storage import (
    StorageContext,
    create_storage_context,
    healthcheck_database,
    initialize_database,
)


app = typer.Typer(help="개인 개발자를 위한 ToDo CLI")


def parse_due_date(raw_due: str | None) -> date | None:
    if raw_due is None:
        return None

    try:
        return date.fromisoformat(raw_due)
    except ValueError as exc:
        raise ValidationError("마감일은 YYYY-MM-DD 형식이어야 합니다.") from exc


def get_storage_context(ctx: typer.Context) -> StorageContext:
    storage_context = ctx.obj.get("storage_context")
    if storage_context is None:
        raise typer.Exit(code=1)
    return storage_context


def get_service_context(ctx: typer.Context) -> ServiceContext:
    return ServiceContext(session_factory=get_storage_context(ctx).session_factory)


@app.callback()
def main(
    ctx: typer.Context,
    data_dir: Annotated[Path, typer.Option(help="SQLite 파일을 저장할 데이터 디렉터리")] = Path(".todo-data"),
    reset_on_corruption: Annotated[
        bool,
        typer.Option(help="손상된 저장소를 백업 후 빈 저장소로 초기화합니다."),
    ] = False,
) -> None:
    """루트 명령에서 공통 저장소 컨텍스트를 준비한다."""

    storage_context = create_storage_context(data_dir, reset_on_corruption=reset_on_corruption)
    initialize_database(storage_context)
    healthcheck_database(storage_context)
    ctx.obj = {
        "storage_context": storage_context,
        "data_dir": data_dir,
        "reset_on_corruption": reset_on_corruption,
    }


@app.command("add")
def add_command(
    ctx: typer.Context,
    title: Annotated[str, typer.Argument(help="추가할 ToDo 제목")],
    due: Annotated[str | None, typer.Option("--due", help="마감일 (YYYY-MM-DD)")] = None,
    priority: Annotated[
        TodoPriority,
        typer.Option("--priority", case_sensitive=False, help="우선순위 (high|medium|low)"),
    ] = TodoPriority.MEDIUM,
) -> None:
    """새 ToDo 항목을 추가한다."""

    service_context = get_service_context(ctx)

    try:
        item = add_todo(
            service_context,
            title=title,
            due_date=parse_due_date(due),
            priority=priority,
        )
    except ValidationError as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=2) from exc

    summary = f"ID={item.id} 제목={item.title}"
    if item.due_date is not None:
        summary += f" 마감일={item.due_date.isoformat()}"
    summary += f" 우선순위={item.priority.value}"
    typer.echo(summary)


@app.command("list")
def list_command(
    ctx: typer.Context,
    filter_by: Annotated[
        Literal["done", "pending"] | None,
        typer.Option("--filter", help="상태 필터 (done|pending)"),
    ] = None,
    priority: Annotated[
        TodoPriority | None,
        typer.Option("--priority", case_sensitive=False, help="우선순위 필터 (high|medium|low)"),
    ] = None,
) -> None:
    """ToDo 목록을 조회한다."""

    items = list_todos(get_service_context(ctx), status_filter=filter_by, priority=priority)

    if not items:
        typer.echo("항목이 없습니다")
        return

    typer.echo("ID | 제목 | 마감일 | 우선순위 | 상태")
    for item in items:
        due_text = item.due_date.isoformat() if item.due_date else "-"
        status_text = "done" if item.is_done else "pending"
        typer.echo(
            f"{item.id} | {item.title} | {due_text} | {item.priority.value} | {status_text}"
        )


@app.command("done")
def done_command(
    ctx: typer.Context,
    todo_id: Annotated[int, typer.Argument(help="완료 처리할 ToDo ID")],
) -> None:
    """ToDo 항목을 완료 처리한다."""

    try:
        item, changed = complete_todo(get_service_context(ctx), todo_id)
    except (ValidationError, NotFoundError) as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=2) from exc

    if changed:
        typer.echo(f"ID={item.id} 항목을 완료 처리했습니다")
        return

    typer.echo("이미 완료된 항목입니다")


@app.command("delete")
def delete_command(
    ctx: typer.Context,
    todo_id: Annotated[int, typer.Argument(help="삭제할 ToDo ID")],
) -> None:
    """ToDo 항목을 삭제한다."""

    try:
        item = delete_todo(get_service_context(ctx), todo_id)
    except (ValidationError, NotFoundError) as exc:
        typer.echo(str(exc), err=True)
        raise typer.Exit(code=2) from exc

    typer.echo(f"ID={item.id} 항목을 삭제했습니다")


if __name__ == "__main__":
    app()