from sqlalchemy import select
from typer.testing import CliRunner

from cli.main import app
from todo_lib.models import ToDoItem, TodoPriority
from todo_lib.storage import create_storage_context


runner = CliRunner()


def test_add_command_persists_due_date_and_priority(tmp_path):
    result = runner.invoke(
        app,
        [
            "--data-dir",
            str(tmp_path),
            "add",
            "보고서 제출",
            "--due",
            "2026-05-10",
            "--priority",
            "high",
        ],
    )

    assert result.exit_code == 0

    context = create_storage_context(tmp_path)
    with context.session_factory() as session:
        item = session.scalar(select(ToDoItem).where(ToDoItem.title == "보고서 제출"))

    assert item is not None
    assert item.priority == TodoPriority.HIGH
    assert str(item.due_date) == "2026-05-10"