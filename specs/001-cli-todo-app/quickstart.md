# Quickstart: CLI 기반 ToDo 관리 앱

## 1) 환경 준비

```bash
uv python install 3.12
uv venv
source .venv/bin/activate
uv pip install typer sqlalchemy pytest pytest-cov
```

## 2) 테스트 우선 흐름 (Red -> Green -> Refactor)

```bash
# Story별 테스트 먼저 작성 후 실패 확인
uv run pytest tests/contract tests/integration -q

# 전체 회귀 검증
uv run pytest
```

## 3) 애플리케이션 실행

```bash
# 예시: Typer 엔트리포인트 기준
uv run python -m cli.main --help

# 수동 검증용 데이터 디렉터리 지정
uv run python -m cli.main --data-dir .todo-data add "회의록 작성"
```

## 4) CLI 명령 예시

```bash
uv run python -m cli.main --data-dir .todo-data add "회의록 작성"
uv run python -m cli.main --data-dir .todo-data add "보고서 제출" --due 2026-05-10 --priority high
uv run python -m cli.main --data-dir .todo-data list
uv run python -m cli.main --data-dir .todo-data list --filter pending
uv run python -m cli.main --data-dir .todo-data list --priority high
uv run python -m cli.main --data-dir .todo-data done 1
uv run python -m cli.main --data-dir .todo-data delete 1
```

## 5) 커버리지 측정

```bash
uv run pytest --cov=todo_lib --cov=cli --cov-report=term-missing
```

## 6) 품질 게이트
- 테스트 실패 상태에서는 구현 커밋 금지
- 지정 패키지 외 신규 의존성 추가 금지
- CLI 외 인터페이스(REST API/GUI/웹) 구현 금지
- 목록 조회 옵션은 `--filter`, `--priority`만 사용한다
