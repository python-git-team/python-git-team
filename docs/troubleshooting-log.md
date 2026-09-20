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
<문제가 무엇이었는지>

### 시도한 명령/절차
<git ...>

### 결과
<무엇이 어떻게 해결됐는지, 주의할 점>

### 왜 이 방법을 선택했는가(Why)
<선택 이유>

---

## 시나리오: git revert
### 참여자
- C

### 상황
Day 3 실습을 위해 `src/list_utils.py`에 임시 주석을 추가한 커밋
`d619824`를 `feature/c-revert` 원격 브랜치에 Push했다.
이미 공유한 커밋의 이력을 삭제하지 않고 변경 내용만 안전하게 되돌려야 했다.

### 시도한 명령/절차
```bash
git log -1 --oneline
git revert d6198240eec28ac38b305bf0a2fc25e24a28d14b
git push
git log --oneline -3
python3 src/list_utils.py
```

### 결과
`0355681` revert 커밋이 새로 생성되어 원격 브랜치에 Push됐다.
기존 커밋과 revert 커밋이 모두 Git 이력에 남았고, 임시 주석은 제거됐다.
`list_utils.py`를 실행한 결과 `[1, 2, 3, 4]`가 출력되어 정상 작동을 확인했다.

### 왜 이 방법을 선택했는가(Why)
이미 원격에 공유한 커밋이므로 이력을 다시 쓰는 `reset`과 강제 Push 대신
변경을 취소하는 새 커밋을 만드는 `git revert`를 사용했다.

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