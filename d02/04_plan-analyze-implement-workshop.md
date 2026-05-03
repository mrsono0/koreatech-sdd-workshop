# 2일차 실습 4: Plan, Tasks, Analyze, Implement

## 구현 전 준비

spec이 완성되었으므로 이제 plan과 tasks를 만듭니다. 1일차와 순서는 같지만, 이번에는 `기존 코드와 어떻게 통합할 것인가`를 반드시 plan에 명시해야 합니다.

## Plan 생성

plan에는 아래가 들어가야 합니다.

- 기존 모델에 어떤 필드를 추가할 것인가
- 기존 service에 어떤 조건과 비즈니스 규칙을 넣을 것인가
- 기존 CLI 명령 표면을 어떻게 확장할 것인가
- 기존 테스트를 어떻게 보호할 것인가

Brownfield에서 plan이 중요한 이유는 새 기능 자체보다 `기존 것과 충돌하지 않게 붙이는 방식`이 더 중요하기 때문입니다.

실습 입력 예시:

```text
specs/002-todo-tags/spec.md를 기반으로 구현 계획을 작성해줘.

중요: 기존 todo_lib/ 코드와 통합해야 한다.
- 기존 Todo 모델에 tags 필드를 추가한다.
- 기존 service.py에 태그 필터링 로직을 추가한다.
- 기존 CLI commands.py에 --tag 옵션을 추가한다.
- 기존 테스트가 깨지지 않아야 한다.

기술 스택: 기존과 동일 (Python, Typer, SQLite+SQLAlchemy, pytest)
태그 저장: JSON 컬럼 (단순함 우선 원칙)
```

이 입력이 좋은 이유는 다음과 같습니다.

- 새 기능 설명만 하는 것이 아니라 `기존 코드와 어떻게 통합할지`를 강제합니다.
- Brownfield에서 중요한 `기존 테스트가 깨지지 않아야 한다`는 조건을 명시합니다.
- 새 기술 도입 없이 기존 스택을 유지한다는 점을 plan에 못 박습니다.

생성 후 확인할 산출물 예시:

- `specs/002-todo-tags/plan.md`
- `specs/002-todo-tags/research.md`
- `specs/002-todo-tags/data-model.md`
- `specs/002-todo-tags/contracts/cli-contract.md`
- `specs/002-todo-tags/quickstart.md`

## Tasks 생성

tasks에서는 구현을 작은 단위로 자릅니다.

권장 순서:

1. 기존 동작 회귀 테스트 파악
2. 새 기능 테스트 추가
3. 모델/서비스 확장
4. CLI 옵션과 출력 확장
5. 전체 회귀 검증

실습 입력 예시:

```text
실행 가능한 태스크 목록을 생성해줘. 각 태스크는 하나의 커밋 단위가 되도록 분해해줘.
병렬 실행 가능한 태스크는 [P] 마커를 붙여줘.

중요:
- 기존 todo_lib/models.py, services.py, validation.py, storage.py를 확장하는 순서가 드러나야 한다.
- tests/unit, tests/integration에 태그 관련 테스트를 먼저 쓰고 실패를 확인한 뒤 구현하도록 구성해줘.
- 기존 add/list/done/delete 회귀 검증 태스크를 포함해줘.
- 마지막에는 종료 코드, 성능, 문서 반영까지 포함해줘.
```

좋은 tasks인지 볼 때는 아래를 같이 확인합니다.

- 태그 검증 테스트가 구현보다 먼저 오는가
- 기존 hot spot인 `todo_lib/services.py`, `cli/commands.py` 작업이 너무 크게 뭉치지 않았는가
- 새 기능 테스트와 기존 회귀 테스트가 함께 들어 있는가
- 마지막에 문서, 성능, 종료 코드 검증이 빠지지 않았는가

## Plan / Tasks 커밋

구현 전 산출물은 먼저 고정해 두는 편이 좋습니다. 이렇게 해야 이후 구현 중에 무엇을 기준으로 판단할지 흔들리지 않습니다.

권장 명령 예시:

```powershell
git branch
git status
git add specs/002-todo-tags/plan.md
git add specs/002-todo-tags/research.md
git add specs/002-todo-tags/data-model.md
git add specs/002-todo-tags/contracts
git add specs/002-todo-tags/quickstart.md
git add specs/002-todo-tags/tasks.md
git commit -m "docs: add tag feature plan and tasks"
git log --oneline -3
```

이 단계도 `main`이 아니라 `002-...` feature 브랜치에서 수행합니다. 커밋 전에는 항상 현재 브랜치를 먼저 확인합니다.

## 구현 전 분석: `/speckit.analyze`

spec, plan, tasks가 모두 만들어졌다면 구현 전에 `/speckit.analyze`로 전체 아티팩트가 일관성이 있는지 확인합니다. 이것이 마지막 점검입니다.

대표적으로 확인할 것:

- spec의 요구사항이 tasks에 모두 반영되었는가
- plan의 기술 선택이 기존 구조와 충돌하지 않는가
- 성능, 종료 코드, 회귀 테스트 항목이 빠지지 않았는가

실습 입력 예시:

```text
specs/002-todo-tags/ 안의 모든 아티팩트를 코드 생성 전 종합 분석해 주세요.

특히 아래를 중점적으로 봐줘.
- 태그 기능 요구가 tasks에 빠짐없이 반영되었는가
- 기존 Todo 기능 회귀 테스트가 포함되었는가
- JSON 컬럼 선택과 storage 호환 전략이 plan에 충분히 설명되었는가
- 종료 코드와 성능 검증 항목이 누락되지 않았는가
```

analyze 결과를 읽을 때는 `무엇이 잘못됐는가`보다 `어느 문서로 되돌아가 고쳐야 하는가`를 먼저 판단합니다.

- spec 문장이 부족하면 `spec.md`
- 설계 방향이 어긋나면 `plan.md`
- 구현 순서나 검증 누락이면 `tasks.md`

## 구현 시작: `/speckit.implement`

이제 실제 코드를 만듭니다. 1일차와 동일한 방식으로 Phase별로 진행합니다. 이번에는 특히 `기존 테스트가 깨지지 않는가`를 각 Phase 후에 확인합니다.

### Phase 0: 환경 준비

- 현재 브랜치 확인
- 테스트 실행 준비
- 기존 앱 상태 재확인

실습 입력 예시:

```text
tasks.md를 기준으로 Setup과 Foundational 단계만 먼저 진행해줘.

중요:
- 기존 테스트를 깨지 않도록 가장 작은 변경만 적용해줘.
- 태그 기능에 필요한 검증 규칙과 저장소 준비까지만 하고 멈춰줘.
- 끝나면 어떤 테스트를 먼저 돌려야 하는지 알려줘.
```

이 단계에서는 한 번에 끝내려고 하지 말고, 기반 준비만 끝낸 뒤 테스트로 상태를 확인합니다.

### Phase 1 이후: 기능 구현

아래 패턴을 반복합니다.

1. 테스트 작성
2. 실패 확인
3. 구현
4. 같은 테스트 재실행
5. 회귀 확인

실습 입력 예시 1: User Story 1만 구현

```text
tasks.md에서 태그 추가와 관련된 첫 번째 사용자 스토리 범위만 구현해줘.

- tests/unit/test_validation.py, tests/unit/test_todo_service.py, tests/integration/test_add_command.py의 관련 테스트를 먼저 작성하고 실패를 확인해줘.
- 그 다음 todo_lib/models.py, validation.py, services.py, cli/commands.py를 최소한으로 수정해 통과시켜줘.
- 끝나면 멈추고 변경 내용과 실행한 테스트를 요약해줘.
```

실습 입력 예시 2: 목록 필터링 스토리만 구현

```text
tasks.md에서 태그 목록 조회와 필터 조합에 해당하는 작업만 진행해줘.

- 기존 list 기능 회귀가 깨지지 않는지 함께 확인해줘.
- --tag, --filter, --priority가 AND 조건으로 동작하도록 구현해줘.
- 테스트를 먼저 작성하고 같은 테스트를 다시 실행해 결과를 보여줘.
```

실습 입력 예시 3: 마지막 polish만 구현

```text
남은 polish 단계만 진행해줘.

- 종료 코드 검증 테스트
- 100개 Todo 기준 성능 검증
- quickstart 반영
- 전체 테스트와 coverage 실행
```

Phase 2 이후도 동일한 패턴으로 진행합니다. `Phase N 진행 -> 테스트 확인 -> 다음 Phase`를 반복합니다.

## 구현 완료 후 최종 확인

- 새 기능 테스트 통과
- 기존 기능 테스트 통과
- CLI 수동 확인 가능
- plan과 실제 구현이 크게 어긋나지 않음

권장 최종 확인 예시:

```powershell
uv run pytest tests/unit tests/integration --cov=todo_lib --cov=cli --cov-report=term-missing
uv run todo add "회의 준비" --tag work --tag urgent
uv run todo list --tag work
```

여기서 중요한 것은 새 기능만 보는 것이 아니라, 기존 `done`, `delete`, 태그 없는 `add/list`까지 함께 살아 있는지 확인하는 것입니다.

## 구현 결과 커밋

최종 검증 후 기능 브랜치 변경을 커밋합니다.

권장 명령 예시:

```powershell
git branch
git status
git add cli todo_lib tests specs/002-todo-tags
git commit -m "feat: add todo tags"
git log --oneline -3
```

이 커밋은 feature 브랜치의 구현 완료 상태를 남기는 것이고, merge는 그 다음 단계에서 로컬 `main`에서 수행합니다.

## 실습 전체 순서 요약

1. feature 브랜치에서 `/speckit.plan` 실행
2. plan 산출물 검토
3. feature 브랜치에서 `/speckit.tasks` 실행
4. tasks 검토 및 필요 시 수정
5. `/speckit.analyze`로 문서 일관성 확인
6. `/speckit.implement`를 phase별로 나눠 실행
7. 각 phase 후 테스트와 회귀 확인
8. 최종 검증 후 feature 브랜치에서 구현 커밋
9. 이후 `main`으로 돌아가 로컬 `git merge --no-ff` 수행

## 다음 단계

새 기능 추가 흐름을 마쳤다면 `05_bugfix-workshop.md`에서 버그 수정 흐름을 별도로 연습합니다.
