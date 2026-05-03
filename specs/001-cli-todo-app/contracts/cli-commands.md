# CLI Contract: ToDo Command Interface

## Command Surface

### `todo add "<title>" [--due YYYY-MM-DD] [--priority high|medium|low]`
- Purpose: 새 ToDo 항목 생성
- Inputs:
  - `title` (required): 문자열, 공백만 불가
  - `--due` (optional): `YYYY-MM-DD`
  - `--priority` (optional): `high|medium|low`, 기본 `medium`
- Success Output (stdout): 생성된 항목 ID와 요약
- Error Output (stderr): 입력 검증 실패 메시지 + 사용법
- Exit Codes:
  - `0`: 성공
  - `2`: 입력값 오류
  - `1`: 내부/저장소 오류

### `todo list [--filter done|pending] [--priority high|medium|low]`
- Purpose: ToDo 목록 조회
- Inputs:
  - `--filter` (optional): `done|pending`
  - `--priority` (optional): `high|medium|low`
- Success Output (stdout): 표 형식 목록 또는 "항목이 없습니다"
- Error Output (stderr): 필터 값 오류 시 메시지
- Exit Codes: `0` 성공, `2` 입력 오류, `1` 내부 오류

### `todo done <id>`
- Purpose: 항목 완료 처리
- Inputs:
  - `id` (required): 양의 정수
- Success Output (stdout): 완료 처리 메시지
- Error Output (stderr): 없는 ID 또는 형식 오류
- Exit Codes: `0` 성공, `2` 입력 오류, `1` 내부 오류

### `todo delete <id>`
- Purpose: 항목 삭제
- Inputs:
  - `id` (required): 양의 정수
- Success Output (stdout): 삭제 확인 메시지
- Error Output (stderr): 없는 ID 또는 형식 오류
- Exit Codes: `0` 성공, `2` 입력 오류, `1` 내부 오류

## Behavioral Rules
- 명령 실패 시 데이터 무결성을 보장해야 한다.
- `todo done`은 이미 완료된 항목에 대해 멱등 메시지를 반환한다.
- CLI는 비즈니스 로직을 직접 수행하지 않고 `todo_lib`를 호출한다.
- 저장소 손상 감지 시 원본 백업 파일을 남기고 복구 안내를 출력한다.
