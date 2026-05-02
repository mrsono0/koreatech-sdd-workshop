<!--
Sync Impact Report
Version change: N/A -> 1.0.0
Modified principles:
- [PRINCIPLE_1_NAME] -> I. 레이어 분리
- [PRINCIPLE_2_NAME] -> II. 테스트 우선 (NON-NEGOTIABLE)
- [PRINCIPLE_3_NAME] -> III. 최소 의존성
- [PRINCIPLE_4_NAME] -> IV. 단순함 우선
- [PRINCIPLE_5_NAME] -> V. CLI 도구 구현
Added sections:
- 프로젝트 범위 및 제약
- 개발 워크플로우 및 품질 게이트
Removed sections:
- 없음
Templates requiring updates:
- ✅ .specify/templates/plan-template.md
- ✅ .specify/templates/spec-template.md
- ✅ .specify/templates/tasks-template.md
- ⚠ pending .specify/templates/commands/*.md (디렉터리 미존재)
Follow-up TODOs:
- 없음
-->

# CLI ToDo App Constitution

## Core Principles

### I. 레이어 분리
비즈니스 로직은 CLI 입출력 처리 코드와 분리된 독립 레이어에 MUST 존재한다.
입출력 파싱, 출력 포맷팅, 터미널 상호작용은 Interface Layer에서만 처리하며,
도메인 규칙과 상태 변경은 Application/Domain Layer에서만 처리한다.
Rationale: 분리된 레이어는 테스트 용이성, 유지보수성, 변경 영향 최소화를 보장한다.

### II. 테스트 우선 (NON-NEGOTIABLE)
모든 구현은 Test-First 방식으로 진행되어야 하며, 테스트 코드 작성 및 실패 확인이
구현 코드 작성보다 MUST 먼저다. 테스트가 없는 구현 코드는 병합할 수 없다.
최소 단위는 Red-Green-Refactor 사이클이며, 신규 기능/수정은 회귀 테스트를 MUST 포함한다.
Rationale: 요구사항을 실행 가능한 명세로 고정해 품질 저하와 회귀를 예방한다.

### III. 최소 의존성
외부 패키지 도입 전 반드시 필요성, 대체 가능성, 유지보수 비용을 검토해야 한다.
새 의존성은 다음을 MUST 충족한다: 명확한 사용 목적, 표준 라이브러리 대체 불가,
보안/라이선스 리스크 검토 기록. 불필요한 의존성 추가는 금지한다.
Rationale: 의존성 표면적을 줄여 빌드 안정성, 보안, 장기 유지보수 비용을 관리한다.

### IV. 단순함 우선
현재 요구사항을 충족하지 않는 추상화, 범용화, 확장 포인트를 선제적으로 만들지 않는다.
구현은 명확하고 직접적인 경로를 MUST 우선 선택하며, 복잡성 추가는 근거를 문서화해야 한다.
Rationale: 과설계를 방지하고 변경 속도와 코드 가독성을 높인다.

### V. CLI 도구 구현
본 프로젝트의 제품 형태는 터미널 환경에서 동작하는 CLI 도구로 한정한다.
REST API 서버, GUI, 웹 인터페이스는 프로젝트 범위 밖이며 요구사항으로 수용하지 않는다.
기능은 커맨드/인자/표준 입출력 중심으로 정의되어야 한다.
Rationale: 목표 사용자 경험을 CLI 생산성 도구에 집중하여 범위 확장을 통제한다.

## 프로젝트 범위 및 제약

- 대상 산출물은 단일 CLI 애플리케이션이다.
- 기본 실행/검증 흐름은 로컬 터미널 환경을 기준으로 한다.
- 인터페이스 관련 변경은 Core Principles V를 위반하지 않아야 한다.
- 설계 제안서와 구현 계획은 레이어 경계, 테스트 전략, 의존성 검토 근거를 포함해야 한다.

## 개발 워크플로우 및 품질 게이트

- 모든 feature는 테스트 시나리오를 먼저 작성하고 실패 상태를 확인한 후 구현한다.
- 구현 PR/리뷰 시 다음 항목을 MUST 검증한다:
	- 레이어 침범 여부 (UI/CLI 코드가 비즈니스 규칙을 직접 포함하지 않는지)
	- 테스트 선행 및 회귀 테스트 존재 여부
	- 신규 의존성 추가 근거 기록 여부
	- 불필요한 추상화 도입 여부
	- CLI 범위 준수 여부
- 품질 게이트 실패 항목이 하나라도 있으면 병합할 수 없다.

## Governance

이 Constitution은 본 저장소의 설계/구현/리뷰 기준에 대해 최상위 규범이다.

- Amendment Procedure: 변경 제안은 변경 이유, 영향 범위, 마이그레이션(필요 시)을 포함한
	문서화된 PR로 제출하고, 승인 후 병합 시점에 효력을 가진다.
- Versioning Policy (Semantic Versioning):
	- MAJOR: 원칙 제거, 원칙 의미의 비호환 재정의, 거버넌스의 강제 규칙 변경
	- MINOR: 신규 원칙/섹션 추가, 기존 원칙의 실질적 요구 확대
	- PATCH: 의미 변화 없는 문구 명확화, 오탈자 수정, 표현 정리
- Compliance Review Expectations: 모든 Plan/Spec/Tasks/Implement 산출물과 코드 리뷰는
	Constitution 준수 여부를 명시적으로 점검해야 하며, 위반 사항은 병합 전에 해소되어야 한다.

**Version**: 1.0.0 | **Ratified**: 2026-05-02 | **Last Amended**: 2026-05-02
