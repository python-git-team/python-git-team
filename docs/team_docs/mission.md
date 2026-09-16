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
