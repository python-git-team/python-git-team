# Troubleshooting Log

## 시나리오: git commit --amend
### 참여자
- A

### 상황
<문제가 무엇이었는지>

### 시도한 명령/절차
<git ...>

### 결과
<무엇이 어떻게 해결됐는지, 주의할 점>

### 왜 이 방법을 선택했는가(Why)
<선택 이유>

---

## 시나리오: git reset --soft HEAD~1
### 참여자
- B

### 상황
`feature/b-reset-practice` 브랜치에서 `src/math_utils.py`를 수정한 뒤 커밋했는데, 커밋 메시지를 팀 규칙(`type: subject`)에 맞지 않게 작성했다.

```
69b7217 (HEAD -> feature/b-reset-practice) reset --soft 실습:math_utils.py 수정
```

### 시도한 명령/절차
```bash
# 1. 잘못된 메시지로 커밋된 상태 확인
git log --oneline -3

# 2. 마지막 커밋만 취소 (변경 내용은 staged 상태로 유지)
git reset --soft HEAD~1

# 3. 변경 내용이 staged로 남아 있는지 확인
git status
#   Changes to be committed:
#           modified:   src/math_utils.py

# 4. 커밋이 사라지고 HEAD가 이전 커밋(5927620)으로 이동했는지 확인
git log --oneline -3

# 5. 규칙에 맞는 메시지로 재커밋 (git add 불필요)
git commit -m "refactor: math_utils.py 수정 (reset --soft 실습)"
```

### 결과
- `reset --soft HEAD~1` 후 커밋 `69b7217`은 브랜치 기록에서 사라지고, HEAD가 `5927620`(origin/main과 동일)으로 돌아갔다.
- `src/math_utils.py`의 수정 내용은 삭제되지 않고 **staged 상태(Changes to be committed)** 로 남아 있어서, `git add` 없이 바로 재커밋할 수 있었다.
- 규칙에 맞는 메시지로 다시 커밋해 문제를 해결했다.

### 왜 이 방법을 선택했는가(Why)
- 문제는 **커밋 메시지**였고, 코드 수정 내용 자체는 유지해야 했다. `--soft`는 커밋만 취소하고 변경 내용을 staged로 남기므로 목적에 가장 잘 맞았다.
- 메시지만 고치는 방법으로 `git commit --amend`도 있지만, reset은 "커밋을 되돌린 뒤 다시 구성"할 수 있어 여러 파일을 나눠 다시 커밋하는 등 더 유연하게 쓸 수 있다.

---

## 시나리오: git revert
### 참여자
- C

### 상황
<문제가 무엇이었는지>

### 시도한 명령/절차
<git ...>

### 결과
<무엇이 어떻게 해결됐는지, 주의할 점>

### 왜 이 방법을 선택했는가(Why)
<선택 이유>

---

## 시나리오: git stash / git stash pop
### 참여자
- D

### 상황
feature/d-date-example 브랜치에서 date_utils.py 수정 중, main 최신 상태를 확인해야 해서 커밋 없이 다른 브랜치로 이동해야 하는 상황

### 시도한 명령/절차
git stash
git checkout main
git pull origin main
git checkout feature/d-date-example
git stash pop

### 결과
변경사항 유실 없이 stash pop으로 복구 확인. 단, stash 전 __main__ 블록 들여쓰기가 잘못되어 있던 것을 stash pop 이후 발견 — return 문 뒤에 딸려 들어가 함수가 깨지는 상태였음. 들여쓰기 수정 후 python src/date_utils.py로 정상 실행 확인

### 왜 이 방법을 선택했는가(Why)
커밋하지 않은 변경사항을 유지한 채 다른 브랜치를 확인해야 했고, stash는 커밋 이력 없이 임시 보관할 수 있어 적합했음