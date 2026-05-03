# Implementation Plan: CLI 기반 ToDo 관리 앱

**Branch**: `001-cli-todo-app` | **Date**: 2026-05-03 | **Spec**: `/specs/001-cli-todo-app/spec.md`
**Input**: Feature specification from `/specs/001-cli-todo-app/spec.md`

## Summary

터미널 사용자용 ToDo CLI를 구현한다. `todo add/list/done/delete` 명령을 제공하고,
비즈니스 로직은 `todo_lib/`에, CLI 파싱/출력은 `cli/`에 분리한다. 영속성은 로컬 SQLite 파일로 처리하며,
테스트는 `pytest` + `pytest-cov` 기반 Test-First로 진행한다.

## Technical Context

**Language/Version**: Python 3.12  
**Primary Dependencies**: typer, sqlalchemy  
**Storage**: SQLite (로컬 파일 기반, 서버 없음)  
**Testing**: pytest, pytest-cov  
**Target Platform**: macOS/Linux 터미널 환경
**Project Type**: CLI 애플리케이션 (단일 저장소)  
**Performance Goals**: add 3초 이내, list(50개 항목) 1초 이내  
**Constraints**: REST API/GUI/웹 범위 제외, 단일 사용자, 추가 패키지 금지  
**Scale/Scope**: 개인 개발자, 수십~수백 건 ToDo 항목

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Pre-Phase 0 Gate

- [x] Layer separation is explicit: `todo_lib/`(비즈니스)와 `cli/`(입출력) 분리.
- [x] Test-first approach is defined: 테스트 선작성 후 구현.
- [x] Every new dependency includes necessity and alternatives review: 지정된 4개 패키지만 사용.
- [x] Design avoids premature abstractions and justifies any added complexity: 추상 인터페이스 금지.
- [x] Scope is CLI-only; REST API, GUI, and web interface work are excluded.

### Post-Phase 1 Gate Re-check

- [x] `data-model.md`에서 도메인 규칙이 CLI와 분리되어 설계됨.
- [x] `contracts/cli-commands.md`는 CLI 계약만 정의하며 웹/API 계약 없음.
- [x] `quickstart.md`에서 테스트 우선 실행 절차를 강제함.
- [x] 의존성은 typer/sqlalchemy/pytest/pytest-cov로 제한됨.

## Project Structure

### Documentation (this feature)

```text
specs/001-cli-todo-app/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── cli-commands.md
└── tasks.md
```

### Source Code (repository root)

```text
todo_lib/
├── __init__.py
├── models.py
├── services.py
└── storage.py

cli/
└── main.py

tests/
├── contract/
├── integration/
└── unit/
```

**Structure Decision**: Constitution 원칙(레이어 분리, CLI 전용)에 맞춰
`todo_lib/`와 `cli/`를 분리하고, 테스트를 `tests/` 하위에 목적별로 분할한다.

## Phase 0 Research Outputs

- `/specs/001-cli-todo-app/research.md` 생성 완료
- 모호점(저장소 손상 대응, 날짜/우선순위 검증, ID 전략) 해소 완료

## Phase 1 Design Outputs

- `/specs/001-cli-todo-app/data-model.md` 생성 완료
- `/specs/001-cli-todo-app/contracts/cli-commands.md` 생성 완료
- `/specs/001-cli-todo-app/quickstart.md` 생성 완료
- `.github/copilot-instructions.md`의 SPECKIT 참조 경로 업데이트 완료

## Complexity Tracking

해당 없음. Constitution 위반 없이 단순 구현 경로를 선택했다.
