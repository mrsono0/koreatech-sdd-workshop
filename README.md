# 1일차 안내

1일차의 목표는 `새 프로젝트를 SDD 방식으로 시작해서 baseline-v1.0까지 완성하는 것`입니다.

## 1일차에서 배우는 것

- Git과 GitHub의 최소 필수 개념
- HTTPS + PAT 방식으로 GitHub 원격 저장소 연결하기
- GitHub Spec Kit 기반 Greenfield 개발 흐름
- Constitution, Spec, Clarify, Analyze, Plan, Tasks, Implement의 역할 차이
- 브랜치 생성, 커밋, merge `--no-ff`, push까지의 기본 협업 흐름

## 1일차 문서 목록

- `00_learning-guide.md`: 오늘 전체 그림과 교시별 목표
- `01_git-github-basics.md`: Git/GitHub를 처음 쓰는 학습자를 위한 기초 설명
- `02_environment-setup.md`: 도구 설치와 GitHub 연결 준비
- `03_sdd-greenfield-workshop.md`: 1일차 Greenfield 실습 안내 허브
- `04_sdd-philosophy.md`: 2교시 SDD 철학과 단계 구분
- `05_constitution-workshop.md`: 3교시 Constitution 작성
- `06_specify-workshop.md`: 4교시 Specify 작성
- `07_clarify-workshop.md`: 5교시 Clarify
- `08_plan-tasks-workshop.md`: 6교시 Plan / Tasks / Analyze
- `09_implement-baseline-workshop.md`: 7교시 Implement / 기준선 생성
- `10_speckit-folder-structure.md`: `.github`와 `.specify` 구조 해설 참고 문서

## 1일차 완료 기준

- 개발 환경이 정상 동작한다.
- GitHub 원격 저장소를 HTTPS + PAT로 연결할 수 있다.
- `/speckit.constitution`부터 `/speckit.implement`까지 흐름을 설명할 수 있다.
- baseline-v1.0 태그가 있는 기준선을 만든다.

# `/speckit.constitution` 실습

```
/speckit.constitution 이프로젝트는 CLI 기반 ToDo 관리 앱을 만듭니다.
터미널에서 사용하는 생산성 관리 도구로 REST API나 GUI는 프로젝트의 범위 밖입니다.
아래의 5가지 원칙을 constitution으로 작성합니다.
원칙1. 레이어 분리
비즈니스 로직은 사용자 인터페이스와 분리된 독립 레이어에서 구현한다.
원칙2. 테스트 우선
테스트 코드가 구현 코드보다 먼저 작성된다.
테스트 없는 구현코드는 혀용하지 않는다.
원치3. 최소 의존성
외부 패키지 설치 전 반드시 필요성을 검토합니다.
불필요한 의존성은 추가하지 않습니다.
원칙4. 단순함 우선
지금 당장 필요하지 않는 추상화 레이어는 만들지 않는다.
명확하고 직접적인 구현을 선호한다.
원치5. CLI 도구 구현
이 프로젝트는 터미널 CLI 도구를 만든다.
REST API 서버, GUI, 웹 인터페이스는 이 프로젝트의 범위 밖입니다.
```

# `/speckit.specify` 실습

```
/speckit.specify 
CLI 기반의 ToDo 관리 앱을 만듭니다.
사용자: 터미널을 사용하는 개인 개발자 
주요기능:
1. ToDo 항목 추가: 제목(필수), 마감일(선택), 우선순위(선택)
2. 전체 목록 조회: 완료/미완료/우선순위로 필터링 가능
3. 항목 완료 처리: 항목 ID로 완료 표시
4. 항목 삭제: 항목 ID로 삭제
기술스택은 아직 미정
```

# `/speckit.clarify` 실습

```
specs/001-cli-todo-app/spec.md의 [NEEDS CLARIFICATION] 항목들을 하나씩 해소하고자합니다.
각 항목에 대해 선택지를 제시하고, 내가 선택하면 spec.md를 업데이트합니다.
```
