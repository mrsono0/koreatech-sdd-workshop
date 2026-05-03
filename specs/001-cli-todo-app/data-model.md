# Data Model: CLI 기반 ToDo 관리 앱

## Entity: ToDoItem

### Fields
- `id`: int, PK, auto-increment, 필수
- `title`: str, 필수, 1~200자
- `due_date`: date | null, 선택
- `priority`: enum(`high`, `medium`, `low`), 기본 `medium`
- `is_done`: bool, 기본 `false`
- `created_at`: datetime, 필수 (UTC)
- `updated_at`: datetime, 필수 (UTC)

### Validation Rules
- 제목은 공백만으로 구성될 수 없다.
- `due_date`는 `YYYY-MM-DD` 형식이며 유효한 날짜여야 한다.
- `priority`는 허용값 집합 외 값을 받지 않는다.
- `done/delete` 명령은 존재하는 `id`에만 적용된다.

### State Transitions
- `pending -> done`: `todo done <id>` 명령 시 전이.
- `done -> done`: 멱등 처리(이미 완료 안내 메시지).
- `pending|done -> deleted`: `todo delete <id>` 시 영구 삭제.

## Entity: ToDoRepository (Persistence Model)

### Responsibility
- SQLite 파일 기반 CRUD 제공
- 필터 조회(status, priority)
- 손상 탐지 및 복구 흐름 지원

### Relationships
- `ToDoRepository`는 `ToDoItem` 컬렉션을 관리한다.
- `cli` 레이어는 저장소를 직접 다루지 않고 `todo_lib.services`를 통해 접근한다.

## Derived Query Model
- 기본 정렬: `created_at DESC` (최신 항목 우선)
- 상태 필터:
  - `done` -> `is_done = true`
  - `pending` -> `is_done = false`
- 우선순위 필터:
  - `priority IN {high, medium, low}`
