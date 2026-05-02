# Feature Specification: CLI 기반 ToDo 관리 앱

**Feature Branch**: `001-cli-todo-app`
**Created**: 2026-05-02
**Status**: Draft
**Input**: User description: "CLI 기반의 ToDo 관리 앱을 만듭니다. 사용자: 터미널을 사용하는 개인 개발자. 주요기능: 1. ToDo 항목 추가, 2. 전체 목록 조회, 3. 항목 완료 처리, 4. 항목 삭제"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - ToDo 항목 추가 (Priority: P1)

개발자가 터미널에서 새로운 할 일을 추가한다.
제목은 필수이며, 마감일과 우선순위는 선택적으로 지정할 수 있다.

**Why this priority**: 항목 추가는 모든 다른 기능의 전제 조건이며, 앱의 핵심 입력 경로다.

**Independent Test**: `todo add "회의록 작성"` 명령 실행 후 항목이 저장되고 확인 메시지가 출력되면 독립적으로 검증 완료.

**Acceptance Scenarios**:

1. **Given** 사용자가 터미널에 있고, **When** `todo add "회의록 작성"` 실행, **Then** 고유 ID가 부여된 항목이 저장되고 성공 메시지가 출력된다.
2. **Given** 사용자가 마감일을 지정하고 싶을 때, **When** `todo add "보고서 제출" --due 2026-05-10` 실행, **Then** 마감일이 함께 저장된다.
3. **Given** 사용자가 우선순위를 지정하고 싶을 때, **When** `todo add "버그 수정" --priority high` 실행, **Then** 우선순위가 함께 저장된다.
4. **Given** 제목 없이 추가를 시도할 때, **When** `todo add` 실행, **Then** 오류 메시지와 사용법이 출력된다.

---

### User Story 2 - 전체 목록 조회 (Priority: P2)

개발자가 저장된 ToDo 항목 전체를 터미널에서 조회한다.
완료/미완료 상태 및 우선순위 기준으로 필터링할 수 있다.

**Why this priority**: 추가된 항목을 확인하는 핵심 읽기 경로이며, 완료·삭제 기능보다 선행되어야 한다.

**Independent Test**: 항목이 최소 2개 이상 저장된 상태에서 `todo list` 실행 시 목록이 출력되면 독립 검증 완료.

**Acceptance Scenarios**:

1. **Given** 저장된 항목이 있을 때, **When** `todo list` 실행, **Then** 전체 항목이 ID·제목·마감일·우선순위·완료여부와 함께 출력된다.
2. **Given** 미완료 항목만 보고 싶을 때, **When** `todo list --status pending` 실행, **Then** 미완료 항목만 필터링되어 출력된다.
3. **Given** 완료 항목만 보고 싶을 때, **When** `todo list --status done` 실행, **Then** 완료 항목만 필터링되어 출력된다.
4. **Given** 우선순위 기준으로 보고 싶을 때, **When** `todo list --priority high` 실행, **Then** 해당 우선순위 항목만 출력된다.
5. **Given** 저장된 항목이 없을 때, **When** `todo list` 실행, **Then** "항목이 없습니다" 메시지가 출력된다.

---

### User Story 3 - 항목 완료 처리 (Priority: P3)

개발자가 완료한 할 일을 ID로 완료 상태로 변경한다.

**Why this priority**: 목록 조회가 동작한 이후에 의미 있으며, 삭제보다 안전한 상태 변경이다.

**Independent Test**: 저장된 항목의 ID로 `todo done <ID>` 실행 후 해당 항목 상태가 완료로 변경되면 독립 검증 완료.

**Acceptance Scenarios**:

1. **Given** 미완료 항목이 있을 때, **When** `todo done 1` 실행, **Then** 해당 항목이 완료 상태로 변경되고 확인 메시지가 출력된다.
2. **Given** 이미 완료된 항목에 대해, **When** `todo done 1` 실행, **Then** "이미 완료된 항목입니다" 안내 메시지가 출력된다.
3. **Given** 존재하지 않는 ID를 입력할 때, **When** `todo done 999` 실행, **Then** "존재하지 않는 항목입니다" 오류 메시지가 출력된다.

---

### User Story 4 - 항목 삭제 (Priority: P4)

개발자가 더 이상 필요 없는 할 일을 ID로 삭제한다.

**Why this priority**: 기본 CRUD 중 삭제는 마지막 단계이며, 다른 스토리에 의존한다.

**Independent Test**: 저장된 항목의 ID로 `todo delete <ID>` 실행 후 해당 항목이 목록에서 사라지면 독립 검증 완료.

**Acceptance Scenarios**:

1. **Given** 저장된 항목이 있을 때, **When** `todo delete 1` 실행, **Then** 해당 항목이 영구 삭제되고 확인 메시지가 출력된다.
2. **Given** 존재하지 않는 ID를 입력할 때, **When** `todo delete 999` 실행, **Then** "존재하지 않는 항목입니다" 오류 메시지가 출력된다.

---

### Edge Cases

- 저장소 파일이 손상되었거나 읽기 불가한 경우 어떻게 처리하는가?
- 동일한 제목의 항목이 여러 개 존재하는 경우 ID로 구분 가능한가?
- 마감일 형식이 잘못 입력된 경우(예: `--due 99-99-99`) 어떻게 처리하는가?
- 우선순위 값이 유효하지 않은 경우(예: `--priority extreme`) 어떻게 처리하는가?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: 사용자는 제목(필수), 마감일(선택), 우선순위(선택)를 지정해 ToDo 항목을 추가할 수 있어야 한다.
- **FR-002**: 시스템은 각 항목에 고유한 정수 ID를 자동 부여해야 한다.
- **FR-003**: 사용자는 전체 항목 목록을 조회할 수 있어야 한다.
- **FR-004**: 사용자는 완료/미완료 상태 및 우선순위로 목록을 필터링할 수 있어야 한다.
- **FR-005**: 사용자는 항목 ID로 해당 항목을 완료 상태로 변경할 수 있어야 한다.
- **FR-006**: 사용자는 항목 ID로 해당 항목을 영구 삭제할 수 있어야 한다.
- **FR-007**: 시스템은 잘못된 입력(없는 ID, 형식 오류, 필수 값 누락)에 대해 명확한 오류 메시지와 사용법 안내를 제공해야 한다.
- **FR-008**: 항목 데이터는 프로그램 종료 후에도 유지(영속성)되어야 한다.

### Key Entities *(include if feature involves data)*

- **ToDoItem**: 개별 할 일을 표현. 속성: ID(고유 정수), 제목(문자열), 마감일(날짜, 선택), 우선순위(열거형: high/medium/low, 선택, 기본 medium), 완료여부(불리언, 기본 false), 생성일시.
- **ToDoRepository**: ToDo 항목의 영속 저장 및 조회를 담당. 파일 기반 저장소(형식은 기술 스택 결정 이후 확정).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 사용자는 명령어 1회 입력으로 3초 이내에 ToDo 항목을 추가할 수 있다.
- **SC-002**: 사용자는 50개 이상의 항목이 저장된 상태에서도 1초 이내에 목록을 조회할 수 있다.
- **SC-003**: 잘못된 입력 시 100%의 경우에 명확한 오류 메시지와 사용법이 출력된다.
- **SC-004**: 프로그램 재시작 후에도 이전에 저장한 항목이 100% 유지된다.
- **SC-005**: 핵심 4개 기능(추가/조회/완료/삭제) 각각을 독립적으로 테스트할 수 있다.

## Assumptions

- 사용자는 터미널 환경에서 직접 명령어를 입력하는 개인 개발자이다.
- REST API, GUI, 웹 인터페이스는 범위 밖이다. CLI 전용이다.
- 동시 사용자(멀티프로세스 동시 쓰기)는 고려하지 않는다. 단일 사용자 환경이다.
- 기술 스택은 미정이며, 명세서는 언어/프레임워크 중립적으로 작성한다.
- 데이터 저장 형식(JSON, SQLite 등)은 플래닝 단계에서 결정한다.
- 우선순위 값은 high / medium / low 세 가지이며, 미지정 시 medium이 기본값이다.
- 마감일 형식은 YYYY-MM-DD를 기본으로 하되, 플래닝 단계에서 최종 확정한다.

## Constitution Alignment *(mandatory)*

- **Layer Separation**: CLI 입력 파싱(Interface Layer)과 ToDo CRUD 비즈니스 로직(Application/Domain Layer)은 분리된 모듈로 구현한다. CLI 레이어는 파싱·출력만 담당하고, 도메인 레이어는 저장소 독립적으로 테스트 가능해야 한다.
- **Test-First Evidence**: 각 User Story의 Acceptance Scenario가 실패 테스트 케이스로 먼저 작성된다. FR-001~FR-008 각각에 대응하는 테스트가 구현 전에 존재해야 한다.
- **Dependency Review**: 기술 스택 미정 단계에서 외부 의존성 없음. 플래닝 단계에서 필요 패키지 도입 시 표준 라이브러리 대체 불가 근거를 명시한다.
- **Simplicity Check**: 플러그인 시스템, 원격 동기화, 알림 기능 등 현재 요구사항 외 추상화는 추가하지 않는다.
- **CLI Scope Guardrail**: 본 명세서에는 REST API, GUI, 웹 인터페이스 관련 요구사항이 없다. CLI 커맨드·인자·표준 입출력만 정의한다.
