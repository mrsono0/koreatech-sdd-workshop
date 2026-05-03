# 2일차 안내

2일차의 목표는 `기준선을 보호하면서 기존 Todo 앱에 기능을 추가하고 버그를 수정하는 것`입니다.

## 2일차에서 배우는 것

- Brownfield 개발의 의미와 Greenfield와의 차이
- `baseline-v1.0` 기준선을 확인하고 보호하는 작업 순서
- 새 기능은 새 Spec으로 분리하고 기존 spec은 유지해야 하는 이유
- 기존 코드와 통합되는 Plan, Tasks, Analyze, Implement 흐름
- 버그 수정과 기능 추가를 구분하는 방법
- GitHub UI가 아니라 로컬 Git 명령으로 `main`에 merge하는 절차
- 변경 요청이 왔을 때 spec부터 다시 시작해야 하는 경우와 아닌 경우

## 2일차 문서 목록

- `00_learning-guide.md`: 오늘 전체 그림과 교시별 목표
- `01_brownfield-basics.md`: Brownfield, 기준선, 보호 원칙 설명
- `02_baseline-check-workshop.md`: main, 태그, 이력, 앱 동작 확인 실습
- `03_feature-spec-workshop.md`: 새 기능을 새 spec으로 만드는 실습
- `04_plan-analyze-implement-workshop.md`: plan, tasks, analyze, implement 흐름
- `05_bugfix-workshop.md`: 버그 수정 브랜치와 TDD 실습
- `06_merge-review-workshop.md`: merge 전 점검과 브랜치 병합 순서
- `07_change-management-workshop.md`: 요구사항 변경 시 cascade 재실행 판단
- `08_recap-and-retrospective.md`: 2일간 흐름 복기와 현업 적용 계획

## 2일차 완료 기준

- `baseline-v1.0` 태그와 기준선 상태를 설명할 수 있다.
- 새 기능 추가 시 기존 spec을 수정하지 않고 새 spec을 만들 수 있다.
- bugfix는 `/speckit.specify` 없이 별도 `fix/` 브랜치에서 처리할 수 있다.
- 기능 브랜치와 버그 수정 브랜치를 검토한 뒤 로컬에서 `git merge --no-ff`로 `main`에 병합할 수 있다.
- 요구사항 변경이 오면 spec, plan, tasks를 다시 따라가야 하는 이유를 설명할 수 있다.
