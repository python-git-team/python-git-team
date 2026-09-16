# Team Member D Mission

## 담당

| 항목              | 내용                                         |
| --------------- | ------------------------------------------ |
| Python          | 날짜 유틸                                      |
| 문서              | `troubleshooting-log.md` / `SUBMISSION.md` |
| Troubleshooting | `git stash / stash pop`                    |

---

# DAY 1 — Python

## Mission 1. Issue 생성

```text
feat: 날짜 형식 변환 함수 추가
```

---

## Mission 2. Branch

```bash
git checkout -b feature/d-date
```

---

## Mission 3. 함수 구현

파일:

```text
src/date_utils.py
```

```python
from datetime import datetime


def format_date(date_text):
    date = datetime.strptime(date_text, "%Y-%m-%d")
    return date.strftime("%Y년 %m월 %d일")


if __name__ == "__main__":
    print(format_date("2026-09-14"))
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

* [ ] B PR
* [ ] C PR

구체적인 리뷰 코멘트를 작성한다.

---

## 내 PR

* [ ] 리뷰 확인
* [ ] 리뷰 의견 1개 이상 반영
* [ ] 수정 Commit
* [ ] 리뷰 답글
* [ ] Merge

---

# DAY 2 — Troubleshooting 문서

파일:

```text
docs/troubleshooting-log.md
```

기본 구조를 만든다.

각 팀원의 Troubleshooting 실습 내용을 기록할 수 있도록 구성한다.

* [ ] A — amend
* [ ] B — reset --soft
* [ ] C — revert
* [ ] D — stash/pop

---

# DAY 2 — Conflict Mission

C와 Python 파일 충돌 실습을 진행한다.

* [ ] 충돌 원인 확인
* [ ] Conflict 발생
* [ ] 충돌 내용 확인
* [ ] 코드 선택
* [ ] Conflict Marker 제거
* [ ] Python 실행
* [ ] 정상 작동 확인
* [ ] 해결 과정 기록

---

# DAY 3 — Troubleshooting

## Mission 5. `git stash`

작업 중인 변경사항을 임시 보관한다.

```bash
git stash
```

다른 브랜치로 이동한다.

```bash
git checkout main
```

다시 작업 브랜치로 돌아온다.

```bash
git checkout feature/d-date
```

변경사항을 복구한다.

```bash
git stash pop
```

### 확인

* [ ] 작업 내용 임시 보관
* [ ] 다른 Branch 이동
* [ ] 작업 Branch 복귀
* [ ] `stash pop`
* [ ] 변경 내용 복구 확인
* [ ] troubleshooting-log.md 기록

---

# DAY 3 — 두 번째 PR

* [ ] 두 번째 Issue 생성
* [ ] 문서 또는 Python 코드 수정
* [ ] Branch
* [ ] Commit
* [ ] Push
* [ ] PR
* [ ] 리뷰
* [ ] 리뷰 반영
* [ ] Merge

---

# Mission 6. SUBMISSION.md

최종 제출 문서를 작성한다.

파일:

```text
SUBMISSION.md
```

포함할 내용:

* [ ] GitHub Repository URL
* [ ] 팀원별 Issue 링크
* [ ] 팀원별 PR 링크
* [ ] 팀원별 리뷰 기록
* [ ] 주요 문서 링크
* [ ] Git log 증빙 위치
* [ ] Conflict 해결 기록
* [ ] Troubleshooting 기록

---

# D 최종 체크

* [ ] Python 함수 1개 이상
* [ ] PR 2개 이상
* [ ] PR Merge 2개 이상
* [ ] 리뷰 2개 이상
* [ ] 리뷰 반영 1회 이상
* [ ] `stash / stash pop` 실습
* [ ] 결과물 기여 Commit
* [ ] troubleshooting-log.md 작성
* [ ] SUBMISSION.md 작성
* [ ] Conflict 실습 참여
