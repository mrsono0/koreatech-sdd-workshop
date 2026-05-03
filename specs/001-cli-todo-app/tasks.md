# Tasks: CLI 기반 ToDo 관리 앱

**Input**: Design documents from `/specs/001-cli-todo-app/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, quickstart.md, contracts/cli-commands.md

**Tests**: 모든 사용자 스토리는 테스트 선작성과 실패 확인이 필수다.

**Organization**: 태스크는 사용자 스토리별로 정리되며, 각 태스크는 하나의 커밋 단위가 되도록 분해한다.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: 병렬 실행 가능 (서로 다른 파일, 선행 의존성 없음)
- **[Story]**: 사용자 스토리 라벨 (`[US1]`, `[US2]`, `[US3]`, `[US4]`)
- 모든 태스크는 정확한 파일 경로를 포함한다.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Python/uv 기반 CLI 프로젝트 골격과 공통 개발 환경 준비

- [X] T001 Create Python 3.12 uv project config and locked dependency list in pyproject.toml
- [X] T002 Create package skeleton for todo_lib and cli entrypoint in todo_lib/__init__.py, cli/__init__.py, cli/main.py
- [X] T003 [P] Configure pytest and pytest-cov defaults in pyproject.toml
- [X] T004 [P] Create initial test directory scaffold and shared markers in tests/conftest.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: 모든 사용자 스토리에서 공통으로 사용하는 저장소, 모델, 배선 준비

**⚠️ CRITICAL**: 이 단계가 완료되기 전에는 어떤 사용자 스토리도 구현하지 않는다.

- [X] T005 Define SQLAlchemy engine, session factory, and SQLite file path management in todo_lib/storage.py
- [X] T006 [P] Implement ToDoItem ORM model and enum fields in todo_lib/models.py
- [X] T007 [P] Add temporary SQLite fixture and database bootstrap helpers in tests/conftest.py
- [X] T008 Wire Typer root app and shared command dependency bootstrap in cli/main.py
- [X] T009 Add corruption backup and recovery bootstrap path in todo_lib/storage.py

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - ToDo 항목 추가 (Priority: P1) 🎯 MVP

**Goal**: 제목 필수, 마감일/우선순위 선택 입력으로 새 ToDo 항목을 저장한다.

**Independent Test**: `todo add "회의록 작성"` 및 옵션 조합 명령을 실행해 항목이 저장되고 성공/오류 메시지가 명세대로 출력되면 완료.

### Tests for User Story 1 (MANDATORY) ⚠️

- [X] T010 [P] [US1] Add CLI contract tests for `todo add` success and validation errors in tests/contract/test_add_command.py
- [X] T011 [P] [US1] Add integration tests for persisted todo creation with due date and priority in tests/integration/test_add_todo.py

### Implementation for User Story 1

- [X] T012 [US1] Implement add-todo service with title, due-date, and priority validation in todo_lib/services.py
- [X] T013 [US1] Implement `todo add` command output and error handling in cli/main.py

**Checkpoint**: User Story 1 is independently functional and testable.

---

## Phase 4: User Story 2 - 전체 목록 조회 (Priority: P2)

**Goal**: 저장된 ToDo 목록을 전체/상태/우선순위 기준으로 조회한다.

**Independent Test**: 데이터가 있는 상태에서 `todo list`, `todo list --filter pending`, `todo list --priority high`가 각각 올바른 결과를 출력하면 완료.

### Tests for User Story 2 (MANDATORY) ⚠️

- [X] T014 [P] [US2] Add CLI contract tests for `todo list` filters and empty-state output in tests/contract/test_list_command.py
- [X] T015 [P] [US2] Add integration tests for list ordering and filter queries in tests/integration/test_list_todos.py

### Implementation for User Story 2

- [X] T016 [US2] Implement list query service with done/pending and priority filtering in todo_lib/services.py
- [X] T017 [US2] Implement `todo list` table rendering and filter option parsing in cli/main.py

**Checkpoint**: User Stories 1 and 2 both work independently.

---

## Phase 5: User Story 3 - 항목 완료 처리 (Priority: P3)

**Goal**: ID 기반으로 항목을 완료 상태로 전환하고 멱등 메시지를 제공한다.

**Independent Test**: `todo done <id>` 실행 후 완료 상태가 영속 저장되고, 중복 완료 시 안내 메시지가 출력되면 완료.

### Tests for User Story 3 (MANDATORY) ⚠️

- [X] T018 [P] [US3] Add CLI contract tests for `todo done` success, already-done, and missing-id cases in tests/contract/test_done_command.py
- [X] T019 [P] [US3] Add integration tests for completion state persistence in tests/integration/test_done_todo.py

### Implementation for User Story 3

- [X] T020 [US3] Implement complete-todo service with missing-id and idempotent handling in todo_lib/services.py
- [X] T021 [US3] Implement `todo done` command messaging in cli/main.py

**Checkpoint**: User Stories 1-3 all work independently.

---

## Phase 6: User Story 4 - 항목 삭제 (Priority: P4)

**Goal**: ID 기반으로 항목을 영구 삭제한다.

**Independent Test**: `todo delete <id>` 실행 후 목록에서 항목이 사라지고, 없는 ID는 오류 메시지를 반환하면 완료.

### Tests for User Story 4 (MANDATORY) ⚠️

- [X] T022 [P] [US4] Add CLI contract tests for `todo delete` success and missing-id errors in tests/contract/test_delete_command.py
- [X] T023 [P] [US4] Add integration tests for deletion persistence in tests/integration/test_delete_todo.py

### Implementation for User Story 4

- [X] T024 [US4] Implement delete-todo service with missing-id handling in todo_lib/services.py
- [X] T025 [US4] Implement `todo delete` command messaging in cli/main.py

**Checkpoint**: All user stories are independently functional.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: 회귀 방지, 문서 보강, 범위 준수 최종 검증

- [X] T026 [P] Add unit tests for storage corruption backup and shared validation helpers in tests/unit/test_storage_and_validation.py
- [X] T027 Update quickstart verification steps to match implemented commands in specs/001-cli-todo-app/quickstart.md
- [X] T028 Validate dependency set and CLI-only scope in pyproject.toml and cli/main.py
- [X] T029 Run full quickstart test command set and record final adjustments in specs/001-cli-todo-app/quickstart.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: 즉시 시작 가능
- **Foundational (Phase 2)**: Setup 완료 후 진행, 모든 사용자 스토리를 차단함
- **User Stories (Phase 3-6)**: Foundational 완료 후 진행
- **Polish (Phase 7)**: 원하는 사용자 스토리 완료 후 진행

### User Story Dependencies

- **US1 (P1)**: Foundational 완료 후 즉시 시작 가능, MVP
- **US2 (P2)**: Foundational 완료 후 시작 가능, 테스트 데이터는 fixture로 독립 주입 가능
- **US3 (P3)**: Foundational 완료 후 시작 가능, 완료 대상 항목은 테스트 fixture로 준비 가능
- **US4 (P4)**: Foundational 완료 후 시작 가능, 삭제 대상 항목은 테스트 fixture로 준비 가능

### Within Each User Story

- 테스트 태스크를 먼저 작성하고 실패(Red)를 확인한다.
- 서비스 구현이 CLI 구현보다 먼저다.
- 동일 파일을 수정하는 태스크는 순차 실행한다.
- 각 태스크 완료 후 즉시 커밋한다.

### Parallel Opportunities

- `T003` 와 `T004` 는 서로 다른 파일 영역이어서 병렬 가능
- `T006` 와 `T007` 은 병렬 가능
- 각 사용자 스토리의 contract test와 integration test는 병렬 가능
- 다른 사용자 스토리의 테스트 작성은 Foundational 완료 후 병렬 착수 가능

---

## Parallel Example: User Story 1

```bash
# US1 테스트 병렬 실행
Task: "Add CLI contract tests for `todo add` success and validation errors in tests/contract/test_add_command.py"
Task: "Add integration tests for persisted todo creation with due date and priority in tests/integration/test_add_todo.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Phase 1 완료
2. Phase 2 완료
3. Phase 3 완료
4. `todo add` 관련 contract/integration 테스트와 수동 명령 검증 수행
5. MVP 시연

### Incremental Delivery

1. Setup + Foundational 완료
2. US1 추가 후 검증 및 커밋
3. US2 추가 후 검증 및 커밋
4. US3 추가 후 검증 및 커밋
5. US4 추가 후 검증 및 커밋
6. Polish 단계 수행

### Parallel Team Strategy

1. 한 명이 Setup/Foundational 수행
2. 이후 팀원이 각 사용자 스토리 테스트 작성부터 병렬 착수
3. `todo_lib/services.py`, `cli/main.py` 충돌을 줄이기 위해 스토리 단위로 순차 병합

---

## Notes

- 모든 태스크는 하나의 커밋 단위를 기준으로 분해했다.
- `[P]` 태스크는 서로 다른 파일 또는 독립 테스트 파일을 대상으로 한다.
- 추상 인터페이스는 도입하지 않는다.
- REST API, GUI, 웹 인터페이스 관련 태스크는 포함하지 않는다.