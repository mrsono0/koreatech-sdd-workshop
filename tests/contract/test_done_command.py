from typer.testing import CliRunner

from cli.main import app


runner = CliRunner()


def test_done_command_marks_item_completed(tmp_path):
    runner.invoke(app, ["--data-dir", str(tmp_path), "add", "문서 정리"])

    result = runner.invoke(app, ["--data-dir", str(tmp_path), "done", "1"])

    assert result.exit_code == 0
    assert "완료 처리" in result.stdout


def test_done_command_is_idempotent_for_completed_item(tmp_path):
    runner.invoke(app, ["--data-dir", str(tmp_path), "add", "문서 정리"])
    runner.invoke(app, ["--data-dir", str(tmp_path), "done", "1"])

    result = runner.invoke(app, ["--data-dir", str(tmp_path), "done", "1"])

    assert result.exit_code == 0
    assert "이미 완료된 항목입니다" in result.stdout


def test_done_command_fails_for_missing_id(tmp_path):
    result = runner.invoke(app, ["--data-dir", str(tmp_path), "done", "999"])

    assert result.exit_code == 2
    assert "존재하지 않는 항목입니다" in result.output