# Context

## Loom 코드 계약

아래 항목은 Loom 코드에 고정된 runtime 동작 계약입니다. 관련 흐름을 바꾸기 전 `loom contract show <id>`로 확인합니다.

- `task-execution`: Task 실행 전 prompt/context/previous-results에 들어가는 입력 경계입니다. 명령: `loom contract show task-execution`. Source: `loom/application/context_pack.py`, `loom/application/team_policy.py`
- `done-guardrail`: Task를 DONE으로 인정하기 전에 필요한 산출물과 상태 전이를 검증하는 계약입니다. 명령: `loom contract show done-guardrail`. Source: `loom/application/services.py`

## Project Memory

# python-git-team

Loom 프로젝트 메모리 루트입니다.

이 파일은 `loom init`으로 생성되며 `loom analyze-repo`로 보강할 수 있습니다.

## Workspace Policy

- Output language: `ko`
- Agent provider: `claude`
- Agent model: `adapter-default`
- Reasoning effort: `high`
- Required branch: `feature/list-utils`
- Dirty branch switch: `blocked`
- Commit policy: `required`
- Include `.loom` metadata in Git: `yes`
- Read-only parallel execution: `allowed`
- Validation environment: `auto`
- Previous Task result limit: `2`
- Workspace required docs: -
- Loom fixed guardrails and verified Team required policies take precedence over this Workspace Policy.

## Job

- Title: 프로젝트 협업 기반 구성
- Goal: Loom 작업공간을 초기화하고 미션에서 요구한 기본 폴더 구조와 팀 미션 문서를 현재 브랜치에 커밋한다.
- Branch: feature/list-utils
- Task count: `1`

## Task

- Title: Loom과 미션 폴더 구조 초기화
- Description: 현재 feature/list-utils 브랜치에서 Loom 메타데이터와 통제 에이전트 파일을 보존하고, 미션이 요구한 src/docs/team 기본 폴더 구조를 추적 가능하게 만들며, 기존 team_docs 변경사항을 컨벤션에 맞춰 커밋한다.
- Expected output: Loom 초기화 파일, src/docs/team 폴더 골격, team_docs 문서, macOS 임시 파일 제외 규칙이 커밋된다.
- Done condition: loom validate --strict가 통과하고, 필수 디렉터리가 존재하며, .DS_Store를 제외한 현재 변경사항이 컨벤션 커밋에 포함되고 git status에 커밋 대상 변경이 남지 않는다.
- In scope: .loom/, AGENTS.md, CLAUDE.md, .gitignore, docs/team_docs/, src/, team/ 기본 구조 및 관련 Git 커밋
- Out of scope: 리스트 유틸 함수 구현, 다른 팀원의 담당 파일 내용 작성, push와 PR 생성
- Validation hint: loom validate --strict; 디렉터리 구조 확인; git diff --check; git status --short; git log -2 --oneline
- Required docs: `docs/team_docs/mission.md`, `docs/team_docs/mem_c.md`
- Memory refs: -
- Document outputs: -
- Document output exceptions: -
- Source proposal: `-`
- Status: PENDING
- Assigned agent: -

## Advisor Source Prompt

No Advisor source prompt recorded for this Task.

## Inclusion Policy

- Mandatory execution files: `prompt.md`, `context.md`, and `previous-results.md`.
- Always included: project memory, current Job/Task metadata, and Job notes.
- Previous results: up to the latest 2 recorded results from earlier Tasks in this Job.
- Job context refs: explicit Job-scoped references selected by the controlling agent or user.
- Task required docs: mandatory Task-scoped documents; missing refs block validation and execution.
- Task memory refs: mandatory Task-scoped workflow memory references; missing or non-memory refs block validation and execution.
- Repository documents, validation documents, and skill rules: included only through explicit Job context refs, Task required docs, or Task memory refs.
- Verified Team Policy Snapshot: included before Active Memory; required policy cannot be overridden by lower-priority context.
- Active workflow memory with an `always` category is included automatically while its status is `ACTIVE`.
- `task_selected` and `reference_only` memory is included only through explicit Task memory refs.
- Consumed proposals, rejected proposals, resolved memory, superseded memory, and archived memory are excluded.
- Unreferenced repository files and results from other Jobs are not included.
- `AGENTS.md` and `CLAUDE.md` remain session-level controlling-agent entrypoints and are not treated as task context artifacts by default.

## Job Notes

# Notes

## Context References

No explicit context references recorded for this job.

## Required Documents and Memory

### required-doc: docs/team_docs/mission.md

- Path: `docs/team_docs/mission.md`
- Status: present

# Python Git 협업 프로젝트 Mission

## 1. 프로젝트 개요

4명이 함께 간단한 **Python 유틸리티 프로그램**을 개발하며 GitHub 협업 과정을 경험한다.

이번 프로젝트의 핵심은 복잡한 프로그램을 만드는 것이 아니라,

> **Issue → Branch → Commit → Push → Pull Request → Review → 수정 → Merge**

의 전체 협업 과정을 직접 경험하는 것이다.

---

## 2. 프로젝트 목표

### 필수 Git 협업 경험

* [ ] GitHub Repository 참여
* [ ] Issue 생성
* [ ] Feature Branch 생성
* [ ] Commit
* [ ] Push
* [ ] Pull Request 생성
* [ ] Code Review
* [ ] 리뷰 의견 반영
* [ ] Merge
* [ ] Merge Conflict 해결
* [ ] Git Troubleshooting 실습
* [ ] 협업 문서 작성

### 이번 프로젝트에서 하지 않는 것

보너스 과제는 진행하지 않는다.

다음 항목은 평가 범위에서 제외한다.

* `git rebase -i`
* `CODEOWNERS`
* 리뷰어 자동화
* 기타 보너스 Git 기능

---

# 3. 최종 프로젝트 구조

```text
python-git-team/
├── README.md
├── SUBMISSION.md
│
├── src/
│   ├── string_utils.py
│   ├── math_utils.py
│   ├── list_utils.py
│   └── date_utils.py
│
├── docs/
│   ├── CONTRIBUTING.md
│   ├── conflict-resolution.md
│   └── troubleshooting-log.md
│
└── team/
    ├── member-a.md
    ├── member-b.md
    ├── member-c.md
    └── member-d.md
```

---

# 4. 팀원 역할

| 팀원 | Python 담당 | 문서 담당                                  | Git Troubleshooting |
| -- | --------- | -------------------------------------- | ------------------- |
| A  | 문자열 유틸    | README.md                              | `commit --amend`    |
| B  | 숫자 유틸     | CONTRIBUTING.md                        | `reset --soft`      |
| C  | 리스트 유틸    | conflict-resolution.md                 | `revert`            |
| D  | 날짜 유틸     | troubleshooting-log.md / SUBMISSION.md | `stash / stash pop` |

---

# 5. 모든 팀원이 반드시 달성해야 하는 미션

## PR 미션

각 팀원은 반드시:

* [ ] PR 최소 2개
* [ ] PR 2개 모두 Merge
* [ ] 다른 팀원 PR 리뷰 최소 2개
* [ ] 본인 PR에서 리뷰 의견 최소 1회 반영
* [ ] 리뷰 의견에 답글 작성

---

## Python 미션

각 팀원은 자신의 담당 Python 파일에:

* [ ] 함수 1개 이상 구현
* [ ] 사용 예시 작성
* [ ] 정상 실행 확인
* [ ] 결과물에 기여하는 Commit 생성

---

# 6. Conflict Mission

팀 전체가 **2번의 충돌 실습**을 수행한다.

## Conflict #1 — README.md

### 참가

* A
* B
* C
* D

### 조건

A와 B가 `README.md`의 **같은 부분을 서로 다르게 수정**한다.

### 목표

같은 파일의 같은 부분을 수정했을 때 발생하는 Merge Conflict를 경험한다.

### 확인

```text
<<<<<<< HEAD
=======
>>>>>>> branch-name
```

### 해결 과정

* [ ] Conflict 발생 확인
* [ ] 충돌 원인 확인
* [ ] 충돌 내용 비교
* [ ] 팀원 간 최종 내용 결정
* [ ] Conflict Marker 제거
* [ ] Commit
* [ ] Push
* [ ] Merge
* [ ] 해결 과정 문서 기록

---

# 7. Conflict #2 — Python 파일

### 참가

* C
* D
* A
* B

### 조건

C와 D가 같은 Python 파일의 **비슷한 부분을 동시에 수정**한다.

### 목표

Python 코드에서 직접 Merge Conflict를 경험한다.

### 해결 과정

* [ ] Conflict 발생
* [ ] 충돌 내용 확인
* [ ] 필요한 코드 선택
* [ ] Conflict Marker 제거
* [ ] Python 코드 실행
* [ ] 정상 작동 확인
* [ ] Commit
* [ ] Push
* [ ] Merge
* [ ] 해결 과정 문서 기록

---

# 8. Git Troubleshooting Mission

각 팀원은 담당 Git 명령어를 직접 실습한다.

| 팀원 | 명령어                     | 목표                  |
| -- | ----------------------- | ------------------- |
| A  | `git commit --amend`    | 최근 Commit 수정        |
| B  | `git reset --soft`      | Commit 취소 + 변경사항 유지 |
| C  | `git revert`            | 원격 Commit 되돌리기      |
| D  | `git stash / stash pop` | 작업 임시 보관 및 복구       |

실습 결과는 반드시

```text
docs/troubleshooting-log.md
```

에 기록한다.

---

# 9. GitHub 설정 Mission

팀장은 Repository에서 다음 사항을 확인한다.

* [ ] 팀원 4명 모두 Repository 참여
* [ ] `main` Branch Protection 설정
* [ ] `main` 직접 Push 금지
* [ ] PR을 통해서만 Merge
* [ ] 최소 1명 Approve 필요

---

# 10. Issue / PR 규칙

모든 작업은 Issue를 먼저 생성한다.

PR에는 반드시 Issue 연결 내용을 작성한다.

예:

```text
Closes #12
```

### Commit 예시

```text
feat: add string utility
fix: handle empty string
docs: update contributing guide
```

---

# 11. 최종 제출물

프로젝트 종료 시 다음 파일이 존재해야 한다.

```text
README.md
SUBMISSION.md

src/
├── string_utils.py
├── math_utils.py
├── list_utils.py
└── date_utils.py

docs/
├── CONTRIBUTING.md
├── conflict-resolution.md
└── troubleshooting-log.md

team/
├── member-a.md
├── member-b.md
├── member-c.md
└── member-d.md
```

---

# 12. 최종 제출 체크리스트

## GitHub

* [ ] Repository URL 확인
* [ ] 4명 모두 Repository 참여
* [ ] Branch Protection 적용
* [ ] main 직접 Push 금지

## Issue / PR

* [ ] A PR 2개 이상
* [ ] B PR 2개 이상
* [ ] C PR 2개 이상
* [ ] D PR 2개 이상
* [ ] 모든 PR에 Issue 연결
* [ ] 모든 팀원 리뷰 2개 이상
* [ ] 실질적인 리뷰 코멘트 존재
* [ ] 리뷰 → 수정 → 답글 과정 존재

## Conflict

* [ ] Conflict #1 해결
* [ ] Conflict #2 해결
* [ ] conflict-resolution.md 기록

## Troubleshooting

* [ ] A — amend
* [ ] B — reset --soft
* [ ] C — revert
* [ ] D — stash/pop

## 문서

* [ ] README.md
* [ ] SUBMISSION.md
* [ ] CONTRIBUTING.md
* [ ] conflict-resolution.md
* [ ] troubleshooting-log.md

## 증빙

* [ ] GitHub Repository URL
* [ ] 팀원별 Issue 링크
* [ ] 팀원별 PR 링크
* [ ] 리뷰 기록
* [ ] Conflict 해결 기록
* [ ] Git log 결과

---

# 프로젝트 완료 조건

다음 조건을 **모두 만족하면 프로젝트 완료**이다.

> 4명 모두 Python 결과물에 기여하고
> 각자 PR 2개 이상을 생성하고 Merge하며
> 다른 팀원의 PR을 2개 이상 리뷰하고
> 최소 1회의 리뷰 의견을 실제 코드 또는 문서에 반영한다.

또한 팀 전체가

> **Conflict 2회 + Git Troubleshooting 4종**

을 직접 수행하고 문서로 남겨야 한다.

**보너스 과제는 진행하지 않는다.**

### required-doc: docs/team_docs/mem_c.md

- Path: `docs/team_docs/mem_c.md`
- Status: present

# Team Member C Mission

## 담당

| 항목              | 내용                            |
| --------------- | ----------------------------- |
| Python          | 리스트 유틸                        |
| 문서              | `docs/conflict-resolution.md` |
| Troubleshooting | `git revert`                  |

---

# DAY 1 — Python

## Mission 1. Issue 생성

```text
feat: 리스트 중복 제거 함수 추가
```

---

## Mission 2. Branch

```bash
git checkout -b feature/c-list
```

---

## Mission 3. 함수 구현

파일:

```text
src/list_utils.py
```

```python
def remove_duplicates(items):
    return list(dict.fromkeys(items))
```

사용 예시:

```python
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 3, 4]))
```

---

## Mission 4. Git / PR

* [ ] Commit
* [ ] Push
* [ ] PR 생성
* [ ] `Closes #이슈번호` 작성

---

# DAY 2 — Code Review

다음 PR을 리뷰한다.

* [ ] A PR
* [ ] B PR

실질적인 리뷰 코멘트를 작성한다.

---

## 내 PR

* [ ] 리뷰 확인
* [ ] 리뷰 의견 1개 이상 반영
* [ ] 수정 Commit
* [ ] 리뷰 답글
* [ ] Merge

---

# DAY 2 — Conflict Mission

D와 같은 Python 파일의 비슷한 부분을 수정한다.

### 수행

* [ ] 동일 파일 수정
* [ ] Conflict 발생
* [ ] Conflict Marker 확인
* [ ] 필요한 코드 선택
* [ ] Marker 제거
* [ ] Python 실행
* [ ] 정상 작동 확인
* [ ] Commit
* [ ] Push
* [ ] Merge

---

# DAY 3 — Troubleshooting

## Mission 5. `git revert`

원격에 Push된 Commit을 되돌린다.

```bash
git revert <commit-hash>
```

### 확인

* [ ] 기존 Commit 확인
* [ ] revert 실행
* [ ] 새로운 revert Commit 확인
* [ ] Push
* [ ] Git log 확인
* [ ] troubleshooting-log.md 기록

---

# DAY 3 — 두 번째 PR

* [ ] 두 번째 Issue 생성
* [ ] 리스트 함수 또는 문서 수정
* [ ] Branch
* [ ] Commit
* [ ] Push
* [ ] PR
* [ ] 리뷰
* [ ] 리뷰 반영
* [ ] Merge

---

# C 최종 체크

* [ ] Python 함수 1개 이상
* [ ] PR 2개 이상
* [ ] PR Merge 2개 이상
* [ ] 리뷰 2개 이상
* [ ] 리뷰 반영 1회 이상
* [ ] `git revert` 실습
* [ ] 결과물 기여 Commit
* [ ] conflict-resolution.md 작성
* [ ] Conflict 실습 참여

## Verified Team Policies

No verified Team Policy Snapshot is active.

## Active Workflow Memory

No active workflow memory recorded.
