from typer.testing import CliRunner

from cli.main import app
from todo_lib.models import ToDoItem
from todo_lib.storage import create_storage_context, initialize_database


runner = CliRunner()


def test_delete_command_persists_removal(tmp_path):
    result_add = runner.invoke(app, ["--data-dir", str(tmp_path), "add", "삭제 테스트"])
    assert result_add.exit_code == 0

    result_delete = runner.invoke(app, ["--data-dir", str(tmp_path), "delete", "1"])
    assert result_delete.exit_code == 0

    context = create_storage_context(tmp_path)
    initialize_database(context)

    with context.session_factory() as session:
        item = session.get(ToDoItem, 1)

    assert item is None