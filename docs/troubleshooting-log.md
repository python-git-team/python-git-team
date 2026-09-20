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