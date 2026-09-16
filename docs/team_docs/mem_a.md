# Team Member A Mission

## 담당

| 항목              | 내용                   |
| --------------- | -------------------- |
| Python          | 문자열 유틸               |
| 문서              | `README.md`          |
| Troubleshooting | `git commit --amend` |

---

# DAY 1 — 기본 기능 구현

## Mission 1. Issue 생성

Issue 제목:

```text
feat: 문자열 유틸 함수 추가
```

---

## Mission 2. Branch 생성

```bash
git checkout -b feature/a-string
```

---

## Mission 3. Python 구현

파일:

```text
src/string_utils.py
```

함수:

```python
def reverse_string(text):
    return text[::-1]
```

사용 예시:

```python
if __name__ == "__main__":
    print(reverse_string("hello"))
```

### 체크

* [ ] 파일 생성
* [ ] 함수 구현
* [ ] 사용 예시 작성
* [ ] 실행 확인

---

## Mission 4. Git

```bash
git add .
git commit -m "feat: add string utility"
git push -u origin feature/a-string
```

---

## Mission 5. Pull Request

PR 생성 후 반드시:

```text
Closes #이슈번호
```

작성.

* [ ] PR 생성
* [ ] Issue 연결
* [ ] PR 설명 작성

---

# DAY 2 — Code Review

## Mission 6. 다른 팀원 PR 리뷰

다음 PR을 리뷰한다.

* [ ] B PR
* [ ] C PR

리뷰는 단순한

```text
LGTM
```

으로 끝내지 않는다.

### 예시

```text
빈 문자열을 입력했을 때의 사용 예시도 추가하면 좋을 것 같습니다.
```

---

## Mission 7. 내 PR 리뷰 반영

* [ ] 리뷰 확인
* [ ] 리뷰 의견 최소 1개 반영
* [ ] 수정 Commit
* [ ] 리뷰 답글 작성
* [ ] PR Merge

---

# DAY 2 — Conflict Mission

## README Conflict

B와 함께 `README.md`의 같은 부분을 수정한다.

### 수행

* [ ] 충돌 발생
* [ ] Conflict Marker 확인
* [ ] 충돌 내용 비교
* [ ] 해결 방향 결정
* [ ] Marker 제거
* [ ] Commit
* [ ] Push
* [ ] Merge
* [ ] 해결 과정 기록

---

# DAY 3 — Troubleshooting

## Mission 8. `git commit --amend`

다음 상황을 만든다.

```bash
git commit -m "update"
```

그 후 Commit 메시지를 수정한다.

```bash
git commit --amend -m "feat: add string utility"
```

### 확인

* [ ] 기존 Commit 메시지 확인
* [ ] amend 실행
* [ ] 변경된 Commit 확인
* [ ] `git log` 확인
* [ ] troubleshooting-log.md 기록

---

# DAY 3 — 두 번째 PR

## Mission 9. 두 번째 Issue

README 또는 문자열 코드의 간단한 개선 작업을 Issue로 만든다.

예:

```text
docs: improve README usage example
```

---

## Mission 10. 두 번째 PR

* [ ] Issue 생성
* [ ] Branch 생성
* [ ] 수정
* [ ] Commit
* [ ] Push
* [ ] PR 생성
* [ ] 리뷰 받기
* [ ] 리뷰 반영
* [ ] Merge

---

# A 최종 체크

* [ ] Python 함수 1개 이상
* [ ] PR 2개 이상
* [ ] PR Merge 2개 이상
* [ ] 다른 팀원 PR 리뷰 2개 이상
* [ ] 리뷰 반영 1회 이상
* [ ] `commit --amend` 실습
* [ ] 결과물 기여 Commit
* [ ] README.md 작성
* [ ] Conflict 실습 참여
