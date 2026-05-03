from typer.testing import CliRunner

from cli.main import app


runner = CliRunner()


def test_list_command_shows_empty_state(tmp_path):
    result = runner.invoke(app, ["--data-dir", str(tmp_path), "list"])

    assert result.exit_code == 0
    assert "항목이 없습니다" in result.stdout


def test_list_command_filters_pending_items(tmp_path):
    runner.invoke(app, ["--data-dir", str(tmp_path), "add", "회의록 작성"])
    result = runner.invoke(app, ["--data-dir", str(tmp_path), "list", "--filter", "pending"])

    assert result.exit_code == 0
    assert "회의록 작성" in result.stdout