# Research: CLI 기반 ToDo 관리 앱

## Decision 1: 영속 저장소는 SQLite 파일(로컬) + SQLAlchemy ORM 사용
- Decision: SQLite 단일 파일을 기본 저장소로 사용하고 SQLAlchemy ORM으로 접근한다.
- Rationale: 사용자 요구(서버 불필요, 로컬 파일 기반)와 의존성 제약(typer, sqlalchemy) 충족. 스키마 진화와 테스트 격리가 용이하다.
- Alternatives considered:
  - JSON 파일 직접 저장: 단순하지만 동시성/무결성/쿼리 필터 확장성 부족.
  - 순수 sqlite3 모듈: 의존성 감소는 가능하나 모델 매핑/테스트 유지보수 비용 증가.

## Decision 2: ID 전략은 SQLite AUTOINCREMENT 정수 ID
- Decision: `id INTEGER PRIMARY KEY AUTOINCREMENT` 사용.
- Rationale: CLI에서 사용자가 참조하기 쉽고, 삭제 후에도 ID 재사용이 없어 추적성이 높다.
- Alternatives considered:
  - UUID: 충돌 위험은 낮지만 CLI 입력성이 떨어짐.
  - 제목 기반 키: 중복 제목 허용 요구와 충돌.

## Decision 3: 날짜/우선순위 검증 규칙 고정
- Decision: `--due`는 `YYYY-MM-DD` 엄격 검증, `--priority`는 `high|medium|low`만 허용(기본 `medium`).
- Rationale: 스펙의 가정과 성공 기준을 테스트 가능한 규칙으로 고정한다.
- Alternatives considered:
  - 자유 형식 날짜 파싱: 사용자 편의성은 있으나 모호성/오입력 리스크 증가.
  - 우선순위 숫자형: 가독성 저하 및 CLI 인지 비용 증가.

## Decision 4: 저장소 손상 대응은 Fail-safe + 백업 보존
- Decision: DB 열기 실패/무결성 실패 시 원본 DB를 `.corrupt.<timestamp>.bak`으로 보관하고, 사용자에게 복구 안내를 출력한 뒤 빈 DB 초기화 옵션을 제공한다.
- Rationale: 데이터 손상 시 원본 보존과 서비스 연속성 간 균형을 맞춘다.
- Alternatives considered:
  - 즉시 종료만 수행: 데이터 보존은 되나 서비스 중단.
  - 자동 무조건 초기화: 빠르지만 데이터 유실 위험 큼.

## Decision 5: Test-First 실행 단위
- Decision: Story 단위로 Contract/Integration 테스트를 먼저 작성하고 실패(Red) 확인 후 구현한다.
- Rationale: Constitution의 NON-NEGOTIABLE 원칙 준수 및 회귀 방지.
- Alternatives considered:
  - 구현 후 테스트: 개발 속도는 빠를 수 있으나 품질 게이트 위반.
  - E2E만 작성: 원인 파악이 어려워 유지보수성 저하.
