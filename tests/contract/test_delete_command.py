from typer.testing import CliRunner

from cli.main import app


runner = CliRunner()


def test_delete_command_removes_item(tmp_path):
    runner.invoke(app, ["--data-dir", str(tmp_path), "add", "삭제 대상"])

    result = runner.invoke(app, ["--data-dir", str(tmp_path), "delete", "1"])

    assert result.exit_code == 0
    assert "삭제" in result.stdout


def test_delete_command_fails_for_missing_id(tmp_path):
    result = runner.invoke(app, ["--data-dir", str(tmp_path), "delete", "999"])

    assert result.exit_code == 2
    assert "존재하지 않는 항목입니다" in result.output