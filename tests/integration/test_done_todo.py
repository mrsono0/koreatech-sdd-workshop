from typer.testing import CliRunner

from cli.main import app
from todo_lib.models import ToDoItem
from todo_lib.storage import create_storage_context, initialize_database


runner = CliRunner()


def test_done_command_persists_completion_state(tmp_path):
    result_add = runner.invoke(app, ["--data-dir", str(tmp_path), "add", "테스트 완료"])
    assert result_add.exit_code == 0

    result_done = runner.invoke(app, ["--data-dir", str(tmp_path), "done", "1"])
    assert result_done.exit_code == 0

    context = create_storage_context(tmp_path)
    initialize_database(context)

    with context.session_factory() as session:
        item = session.get(ToDoItem, 1)

    assert item is not None
    assert item.is_done is True