# 2일차 실습 3: 새 기능용 Spec 작성

## 무엇을 만들 것인가

Todo 항목에 태그를 붙일 수 있게 합니다. 예를 들어 `회의 준비`라는 할 일에 `업무`, `중요` 같은 태그를 붙이고, 나중에 특정 태그가 붙은 항목만 조회할 수 있게 합니다.

## 왜 새 Spec을 만드는가

기존 `specs/001-.../spec.md`를 수정하고 싶은 충동이 생길 수 있습니다. 하지만 그렇게 하면 안 됩니다. 기존 spec은 1일차 기준선의 설계 문서입니다. 이것을 바꾸면 기준선 코드와 설계 문서가 맞지 않게 됩니다.

새 기능은 항상 새 spec 폴더에 별도로 만듭니다. `/speckit.specify`를 실행하면 새 브랜치와 새 폴더가 자동으로 생성됩니다.

## Step 1: `issues.md` 파일 생성 또는 갱신

`issues.md`는 코드가 아닌 작업 목록 관리 파일입니다. 기능 브랜치가 생성되기 전에 `오늘 무엇을 할 것인가`를 `main` 브랜치에서 먼저 기록합니다.

중요한 이유:

- `/speckit.specify`를 실행하면 새 브랜치로 이동합니다.
- 따라서 `issues.md`는 반드시 그 전에 `main`에서 정리하는 편이 안전합니다.

작업 전 확인 명령:

```powershell
git branch
git status
git checkout main
git branch
git status
```

핵심은 `issues.md`를 수정하기 전에 현재 브랜치가 정말 `main`인지 확인하는 것입니다. 브랜치 확인 없이 바로 파일을 고치면 이전 feature 브랜치 위에 실습 메모를 섞어 버릴 수 있습니다.

예시 `issues.md` 내용:

```md
# 프로젝트 이슈 목록

## 미결
- [ ] #1 feat: Todo 항목에 태그 필드 추가 (최대 5개, 각 20자 이내)
- [ ] #2 feat: 태그로 목록 필터링 (todo list --tag 태그명)
- [ ] #3 fix: 마감일 없는 항목 정렬 시 오류 발생

## 진행 중

## 완료
```

여기서 `#1`, `#2`는 오늘 만들 새 기능의 입력이 되고, `#3`은 뒤에서 bugfix 워크숍에 사용할 이슈입니다.

### main 브랜치에서 `issues.md` 커밋하기

`issues.md`는 새 feature 브랜치가 생기기 전에 `main`에서 먼저 기록하고 커밋합니다. 그래야 `/speckit.specify`가 새 브랜치를 만들 때 이 이슈 목록이 출발점에 포함됩니다.

권장 명령 예시:

```powershell
git branch
git status
git checkout main
git branch
git add issues.md
git commit -m "docs: add day 2 issues"
git log --oneline -3
```

이 단계는 `main`을 직접 개발용으로 수정하는 것이 아니라, 오늘 실습 입력 문서를 기준선에 남기는 작업입니다.

### 왜 여기서 먼저 커밋하는가

- `/speckit.specify`는 현재 기준 브랜치에서 새 feature 브랜치를 만듭니다.
- 따라서 `issues.md`를 먼저 커밋해야 새 브랜치가 같은 이슈 맥락을 가진 채 시작합니다.
- 이후 기능 구현을 끝내면 2일차는 d01과 동일하게 로컬 `main`에서 `git merge --no-ff`로 병합합니다.

## Step 2: `/speckit.specify` 실행

`/speckit.specify`를 실행하면 새 브랜치가 자동으로 생성됩니다. 예를 들면 `002-todo-tag` 같은 형태입니다. 기존 001 브랜치와는 완전히 분리됩니다.

실습 입력 예시:

```text
기존 Todo 앱에 태그 기능을 추가하고 싶어.

추가할 기능:
1. Todo 항목 생성 시 태그를 선택적으로 추가할 수 있다
	- 태그는 최대 5개까지 허용
	- 각 태그는 20자 이내
	- 태그 없이도 Todo 생성 가능 (기존 기능 유지)
2. 목록 조회 시 태그로 필터링할 수 있다
	- todo list --tag 태그명 형식

이슈 번호: #1, #2
기존 Todo 기능(추가/조회/완료/삭제)은 그대로 유지되어야 해.
```

이 입력의 핵심은 `무엇을 추가할지`, `입력 제약이 무엇인지`, `기존 기능을 유지해야 한다는 점`, `어떤 이슈 번호와 연결되는지`를 한 번에 넣는 것입니다.

## Step 3: 자동 생성된 브랜치와 Spec 확인

아래를 확인합니다.

- 현재 브랜치 이름
- 새로 생긴 `specs/002-.../spec.md`
- 기능 설명이 기존 앱 확장 요구를 제대로 반영하는지

권장 확인 명령:

```powershell
git branch
git status
```

`/speckit.specify` 직후에는 `main`에 그대로 남아 있다고 가정하지 말고, 생성된 feature 브랜치로 실제 이동했는지 먼저 확인합니다.

이 단계가 끝나면 보통 아래를 확인합니다.

- 현재 브랜치가 `002-...` 같은 feature 브랜치인가
- `specs/002-.../spec.md`가 생성되었는가
- `.specify/feature.json`이 새 feature 디렉터리를 가리키는가

## Step 4: `/speckit.clarify` 실행

AI가 질문을 제시하면 기능 규칙이 모호하지 않도록 답합니다.

예시로 자주 나오는 질문:

- 입력 형식은 무엇인가
- 최대 개수나 길이 제한은 무엇인가
- 기존 필터와 새 필터는 어떻게 결합되는가
- 출력에 새 정보가 포함되는가

이번 실습에서 실제로 정리해야 하는 답변 예시는 아래와 같습니다.

1. 같은 Todo 생성 요청에서 동일한 태그가 반복 입력되면 어떻게 처리되는가?
	- 같은 태그가 반복되면 입력 오류로 처리하고 저장하지 않는다.
2. Todo 생성 시 여러 태그는 어떤 CLI 입력 형식으로 받는가?
	- `todo add`에서 `--tag` 옵션을 반복해 입력한다.
3. 태그 비교는 대소문자를 구분하는가?
	- 태그는 소문자로 정규화해 저장하고 대소문자 구분 없이 비교한다.
4. `--tag`는 기존 `--filter`, `--priority`와 함께 사용할 수 있는가?
	- 함께 사용할 수 있고, 모든 조건을 동시에 만족하는 Todo만 반환한다.
5. 목록 조회 결과에 태그를 표시하는가?
	- 태그가 있는 Todo는 목록 조회 결과에 태그를 함께 표시한다.

즉, clarify는 `질문에 답하는 단계`이지만 실무적으로는 `입력 형식, 비교 규칙, 필터 결합 규칙, 출력 계약`을 고정하는 단계입니다.

## Step 5: Spec 커밋

clarify까지 끝난 뒤 새 spec 관련 변경을 커밋합니다.

이 단계에서도 커밋 전에 먼저 현재 브랜치를 확인합니다. spec 커밋은 `main`이 아니라 방금 생성된 feature 브랜치에서 남겨야 합니다.

권장 명령 예시:

```powershell
git branch
git status
git add specs/002-todo-tags/spec.md
git add specs/002-todo-tags/checklists/requirements.md
git add .specify/feature.json
git commit -m "docs: add todo tag spec"
git log --oneline -3
```

실습 중 `.github/copilot-instructions.md` 같은 학습 보조 파일이 함께 바뀌었다면 `git status`를 보고 이번 spec 작업과 직접 관련된 파일만 선택적으로 추가합니다.

### 이후 로컬 merge는 어떻게 연결되는가

이 단계에서 바로 merge하지는 않습니다. 순서는 아래와 같습니다.

1. `main`에서 `issues.md` 커밋
2. `/speckit.specify`로 feature 브랜치 생성
3. `/speckit.clarify`까지 끝낸 뒤 feature 브랜치에서 spec 커밋
4. 이후 plan, tasks, analyze, implement를 진행
5. 최종 검토 후 `main`으로 돌아가 로컬 `git merge --no-ff` 실행

즉, `issues.md`는 `main`에 남기고, spec 이후 산출물은 feature 브랜치에 쌓고, 마지막에 로컬 merge로 `main`에 통합하는 구조입니다.

## 실습 포인트

- 기존 spec을 고치지 않는다.
- 새 기능은 새 브랜치와 새 spec에서 시작한다.
- clarify는 구현이 아니라 요구사항을 선명하게 만드는 단계다.

## 다음 단계

spec이 완성되면 `04_plan-analyze-implement-workshop.md`에서 구현 전 설계와 작업 분해를 진행합니다.
