# Conflict #2 — 날짜 유틸 Python 파일

## 충돌 발생

- 대상: `src/date_utils.py`의 실행 예시 부분
- 공통 기준: `e4d3090` (D의 PR #12가 병합되기 전 `main`)
- C 변경: `28c5c80`에서 `2026-09-18` 예시 추가
- D 변경: PR #12의 `505c480`에서 `2026-09-17` 예시 추가

D의 PR #12가 먼저 `main`에 병합되었으므로, C는 병합 직전 커밋에서 독립 브랜치를 만들어 변경했다. 그 브랜치에서 `git merge --no-commit --no-ff origin/main`을 실행하자 `src/date_utils.py`가 `UU` 상태가 되었고 `<<<<<<< HEAD`, `=======`, `>>>>>>> origin/main` 마커가 나타났다. 두 브랜치가 파일 끝의 같은 부분에 서로 다른 실행 예시를 추가한 것이 원인이다.

## 해결

D가 제시하고 `main`에 병합된 날짜값 `2026-09-17`을 남겼다. D 쪽 예시는 `format_date` 함수의 `return` 뒤에 들여쓰기되어 실행되지 않으므로, `if __name__ == "__main__":` 블록을 함수 바깥으로 옮겼다. 충돌 마커를 모두 제거했다.

## 검증

- `python3 src/date_utils.py` → `2026년 09월 17일`
- Python 구문 검사와 충돌 마커 부재 확인 → 통과
- `git -c core.whitespace=cr-at-eol diff --check` → 통과

해결한 코드는 C 브랜치의 merge commit에 기록한다. 원격 push와 PR 병합은 별도 단계에서 진행한다.
