# Previous Results

## 1. Issue와 리스트 유틸 구현 계약 확정

# 작업 결과

- GitHub Issue [#3](https://github.com/python-git-team/python-git-team/issues/3)을 생성했다.
- Issue 제목은 `feat: 리스트 중복 제거 함수 추가`이며 목적, 작업 내용, 완료 조건을 기록했다.
- 현재 브랜치가 사용자가 지정한 `feature/list-utils`임을 확인했다.

## 구현 계약

- 대상 파일: `src/list_utils.py`
- 함수: `remove_duplicates(items)`
- 구현 방식: `list(dict.fromkeys(items))`
- 최초 등장 순서를 유지한다.
- 입력 원본을 변경하지 않고 새 리스트를 반환한다.
- 숫자, 문자열, 튜플 등 해시 가능한 항목을 지원한다.
- 빈 리스트는 빈 리스트를 반환한다.
- 직접 실행 예시는 `[1, 2, 2, 3, 3, 4]`를 받아 `[1, 2, 3, 4]`를 출력한다.

## 검증

- 생성된 Issue의 번호, 제목, 본문과 Open 상태를 GitHub 화면에서 확인했다.
- `loom task validate`와 `loom validate --strict`가 통과했다.

## 다음 행동

- 다음 의존 Task에서 위 계약에 따라 `src/list_utils.py`를 구현하고 로컬 검증 및 컨벤션 커밋을 수행한다.
