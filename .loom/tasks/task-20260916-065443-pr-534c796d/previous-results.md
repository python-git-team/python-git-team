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

## 2. remove_duplicates 구현과 로컬 검증

# 작업 결과

- `src/list_utils.py`에 `remove_duplicates(items)`를 구현했다.
- `dict.fromkeys()`를 사용해 최초 등장 순서를 유지하면서 중복을 제거한다.
- 함수 설명 docstring과 직접 실행 가능한 `__main__` 예시를 추가했다.
- GitHub Issue [#3](https://github.com/python-git-team/python-git-team/issues/3)의 구현 조건을 충족했다.

## 검증

- `python3 src/list_utils.py` 출력: `[1, 2, 3, 4]`
- `python3 -m py_compile src/list_utils.py`: 통과
- 기본 중복 제거: 통과
- 비연속 중복과 최초 등장 순서 유지: 통과
- 빈 리스트: 통과
- 문자열 항목: 통과
- 입력 원본 비변경 및 새 리스트 반환: 통과
- `git diff --check -- src/list_utils.py`: 통과

## 남은 위험과 다음 행동

- 구현 범위는 계약대로 해시 가능한 항목으로 제한된다.
- 다음 Task에서 브랜치를 push하고 Issue #3과 연결된 PR을 생성한다.
