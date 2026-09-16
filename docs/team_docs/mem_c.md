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
