from datetime import date

from typer.testing import CliRunner

from cli.main import app
from todo_lib.models import TodoPriority
from todo_lib.services import ServiceContext, add_todo
from todo_lib.storage import create_storage_context, initialize_database


runner = CliRunner()


def test_list_command_orders_and_filters_by_priority(tmp_path):
    context = create_storage_context(tmp_path)
    initialize_database(context)
    service_context = ServiceContext(session_factory=context.session_factory)

    add_todo(service_context, "낮은 우선순위", priority=TodoPriority.LOW)
    add_todo(service_context, "높은 우선순위", due_date=date(2026, 5, 10), priority=TodoPriority.HIGH)

    result = runner.invoke(app, ["--data-dir", str(tmp_path), "list", "--priority", "high"])

    assert result.exit_code == 0
    assert "높은 우선순위" in result.stdout
    assert "2026-05-10" in result.stdout
    assert "낮은 우선순위" not in result.stdout