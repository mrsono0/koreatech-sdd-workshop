from typer.testing import CliRunner

from cli.main import app


runner = CliRunner()


def test_add_command_creates_todo_successfully(tmp_path):
    result = runner.invoke(
        app,
        ["--data-dir", str(tmp_path), "add", "회의록 작성"],
    )

    assert result.exit_code == 0
    assert "회의록 작성" in result.stdout
    assert "ID" in result.stdout


def test_add_command_requires_title(tmp_path):
    result = runner.invoke(
        app,
        ["--data-dir", str(tmp_path), "add"],
    )

    assert result.exit_code == 2
    assert "Usage" in result.output or "사용법" in result.output