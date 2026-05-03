# 2일차 실습 6: Merge 전 검토와 병합

## merge 전 확인 — 무엇을 체크하는가

`main`에 merge하기 전에 `이 브랜치가 정말 merge할 준비가 되었는가`를 확인합니다. 이번 과정은 d01과 동일하게 GitHub 웹 UI merge가 아니라 로컬 저장소에서 `git merge --no-ff`로 병합합니다. 체크리스트를 통과한 브랜치만 merge합니다.

## 기본 원칙

- merge는 항상 로컬 `main` 브랜치에서 수행합니다.
- 병합 흔적을 남기기 위해 `git merge --no-ff`를 사용합니다.
- merge가 끝난 뒤에만 `git push origin main`으로 원격에 반영합니다.
- merge 명령을 치기 직전에 반드시 현재 브랜치를 다시 확인합니다.

## Step 1: `fix/issue-3-sort` 브랜치 검토 및 merge

버그 수정 브랜치를 먼저 merge합니다. 버그 수정은 변경 범위가 작고 영향 설명이 명확하므로 먼저 처리하는 편이 좋습니다.

검토 포인트:

- 재현 테스트가 있는가
- 수정 범위가 좁은가
- 의도하지 않은 변경이 섞이지 않았는가

권장 명령 예시:

```powershell
git branch
git status
git checkout main
git branch
git pull origin main
git merge --no-ff fix/issue-3-sort -m "merge: fix issue-3 sort"
git push origin main
```

여기서 첫 `git branch`는 `merge를 어디에서 실행할 것인가`를 확인하는 단계입니다. `fix/issue-3-sort` 브랜치 위에서 merge 명령을 치지 않도록 먼저 확인합니다.

## Step 2: `002-todo-tag` 브랜치 검토 및 merge

새 기능 브랜치는 다음 항목을 봅니다.

- spec, plan, tasks와 구현이 맞는가
- 기존 기능 회귀가 없는가
- 새 기능 동작이 CLI에서 설명 가능한가
- 커밋과 테스트 흐름이 납득 가능한가

권장 명령 예시:

```powershell
git branch
git status
git checkout main
git branch
git pull origin main
git merge --no-ff 002-todo-tag -m "merge: add todo tag feature"
git push origin main
```

feature 브랜치 merge도 동일합니다. 병합 직전 현재 브랜치가 `main`인지 눈으로 확인한 뒤 진행해야 로컬 merge 실습이 안전해집니다.

## Step 3: 최종 상태 확인

merge 후에는 아래를 다시 확인합니다.

- `main` 기준 전체 테스트
- 새 기능 동작 여부
- 기준선 이후 변경 내용 설명 가능 여부

## 권장 체크리스트

- 브랜치 목적이 명확하다.
- 테스트가 모두 통과한다.
- 불필요한 파일이나 임시 변경이 없다.
- merge 후 `main`이 안정 상태다.
- merge commit이 로컬 이력에 명확히 남아 있다.
- merge 직전과 merge 직후 현재 브랜치를 확인했다.

## 왜 검토 순서가 중요한가

- 작은 버그 수정이 먼저 들어가면 이후 기능 브랜치 검토가 단순해집니다.
- 기능 브랜치가 큰 경우, bugfix와 섞여 있으면 리뷰 난도가 급격히 올라갑니다.
- 로컬 merge를 사용하면 병합 직후 테스트와 로그를 내 컴퓨터에서 바로 확인할 수 있습니다.

## 다음 단계

merge까지 끝났다면 `07_change-management-workshop.md`에서 변경 요청이 왔을 때 어디서부터 다시 시작할지 연습합니다.
