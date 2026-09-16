# Team Member B Mission

## 담당

| 항목              | 내용                     |
| --------------- | ---------------------- |
| Python          | 숫자 유틸                  |
| 문서              | `docs/CONTRIBUTING.md` |
| Troubleshooting | `git reset --soft`     |

---

# DAY 1 — 협업 문서

## Mission 1. CONTRIBUTING.md 작성

파일:

```text
docs/CONTRIBUTING.md
```

다음 내용을 작성한다.

* [ ] Branch 이름 규칙
* [ ] Commit 메시지 규칙
* [ ] PR 작성 규칙
* [ ] Code Review 규칙
* [ ] Conflict 대응 방법

---

# DAY 1 — Python

## Mission 2. Issue 생성

```text
feat: 숫자 평균 계산 함수 추가
```

---

## Mission 3. Branch

```bash
git checkout -b feature/b-math
```

---

## Mission 4. 함수 구현

파일:

```text
src/math_utils.py
```

```python
def calculate_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)
```

사용 예시:

```python
if __name__ == "__main__":
    print(calculate_average([10, 20, 30]))
```

---

## Mission 5. Git / PR

```bash
git add .
git commit -m "feat: add average calculation"
git push -u origin feature/b-math
```

PR에:

```text
Closes #이슈번호
```

작성.

---

# DAY 2 — Code Review

다음 PR을 리뷰한다.

* [ ] A PR
* [ ] D PR

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

A와 함께 `README.md` 충돌을 만든다.

* [ ] 같은 부분 수정
* [ ] Conflict 발생
* [ ] 원인 확인
* [ ] 충돌 해결
* [ ] 결과 확인
* [ ] 문서 기록

---

# DAY 3 — Troubleshooting

## Mission 6. `git reset --soft`

Commit을 하나 만든 후:

```bash
git reset --soft HEAD~1
```

### 확인

* [ ] Commit이 사라졌는지 확인
* [ ] 변경 내용이 유지되는지 확인
* [ ] `git status` 확인
* [ ] 다시 Commit
* [ ] troubleshooting-log.md 기록

---

# DAY 3 — 두 번째 PR

* [ ] 두 번째 Issue 생성
* [ ] CONTRIBUTING 또는 Python 코드 수정
* [ ] Branch 생성
* [ ] Commit
* [ ] Push
* [ ] PR 생성
* [ ] 리뷰 받기
* [ ] 리뷰 반영
* [ ] Merge

---

# B 최종 체크

* [ ] Python 함수 1개 이상
* [ ] PR 2개 이상
* [ ] PR Merge 2개 이상
* [ ] 리뷰 2개 이상
* [ ] 리뷰 반영 1회 이상
* [ ] `reset --soft` 실습
* [ ] 결과물 기여 Commit
* [ ] CONTRIBUTING.md 작성
* [ ] Conflict 실습 참여
