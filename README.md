# 친구 3~5명과 함께 프로그램 만드는 법 연습하기

## 1. 프로젝트 개요

4명이 함께 간단한 **Python 유틸리티 프로그램**을 개발하며 GitHub 협업 과정을 경험한다.

이번 프로젝트의 핵심은 복잡한 프로그램을 만드는 것이 아니라,

> **Issue → Branch → Commit → Push → Pull Request → Review → 수정 → Merge**

의 전체 협업 과정을 직접 경험하는 것이다.

## 2. 팀원 역할

| 팀원 | Python 담당 | 문서 담당 | Git Troubleshooting |
| :---| :--- | :--- | :--- |
| 차종민 | 문자열 유틸 | README.md | `commit --amend` |
| 김성훈 | 숫자 유틸 | CONTRIBUTING.md | `reset --soft` |
| 홍용재 | 리스트 유틸 | conflict-resolution.md | `revert` |
| 손재현 | 날짜 유틸 | troubleshooting-log.md / SUBMISSION.md | `stash / stash pop` |

## 3. 프로젝트 구조

```bash
python-git-team
├── README.md
├── SUBMISSION.md
├── docs/
│   ├── CONTRIBUTING.md
│   ├── conflict-resolution.md
│   └── troubleshooting-log.md
└── src/
    ├── __init__.py
    ├── string_utils.py
    ├── math_utils.py
    ├── date_utils.py
    └── list_utils.py
```

## 4. GitHub Flow를 선택한 이유

1. 작업 단위별로 브랜치를 분리하여 다름 사람과의 공동 작업으로 인한 충돌을 줄일 수 있다.
2. PR과 코드 리뷰를 통해 main 브랜치를 안정적으로 유지할 수 있다.
3. 소규모 팀에서 작업 흐름을 단순하게 유지할 수 있다.