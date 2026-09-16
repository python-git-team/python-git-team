# 문제 해결 기록

## Loom 기본 브랜치 불일치

- 최초 foreground 실행에서 Loom의 기본 필수 브랜치가 `develop`로 설정되어 있었고, 현재 변경사항 때문에 브랜치 전환이 차단됐다.
- 사용자가 지정한 실제 작업 브랜치가 `feature/list-utils`임을 재확인했다.
- `loom config policy --required-branch feature/list-utils`로 Workspace Policy를 수정한 뒤 Task 실행을 다시 시작했다.
- 변경사항을 버리거나 stash하지 않았으며 기존 사용자 파일을 보존했다.

## 변경사항 검사 경고

- 기존 `team_docs`가 CRLF 줄바꿈을 사용해 모든 줄이 후행 공백으로 판정됐다.
- 문서 내용은 유지하고 LF로 정규화했다.
- `mission.md`와 Loom의 `context.md`에 충돌 마커를 설명하는 예제가 있어 Git이 이를 잔존 충돌 마커로 감지한다. 이 파일들은 의도된 교육·실행 기록이므로 검사 범위에서 제외했다.
