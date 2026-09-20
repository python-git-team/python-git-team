# 제출 문서 인덱스

## 팀 정보
- 팀명: python-git-team
- 저장소: https://github.com/python-git-team/python-git-team

## 팀원별 기여 내역 (Issue & PR)
- 차종민 (A / 문자열 유틸 / README 담당)
  - Issue: #1, #17, #21, #23
  - PR:
    - https://github.com/python-git-team/python-git-team/pull/2
    - https://github.com/python-git-team/python-git-team/pull/18
    - https://github.com/python-git-team/python-git-team/pull/22
    - https://github.com/python-git-team/python-git-team/pull/24

- 김성훈 (B / 숫자 유틸 / CONTRIBUTING 담당)
  - Issue: #7, #13, #19, #31
  - PR:
    - https://github.com/python-git-team/python-git-team/pull/10
    - https://github.com/python-git-team/python-git-team/pull/14
    - https://github.com/python-git-team/python-git-team/pull/20
    - https://github.com/python-git-team/python-git-team/pull/32

- 홍용재 (C / 리스트 유틸 / 충돌 해결 문서 담당)
  - Issue: #3, #15, #29
  - PR:
    - https://github.com/python-git-team/python-git-team/pull/4
    - https://github.com/python-git-team/python-git-team/pull/16
    - https://github.com/python-git-team/python-git-team/pull/30

- 손재현 (D / 날짜 유틸 / 트러블슈팅 및 제출 문서 담당)
  - Issue: #5, #8, #11, #25, #27, #33
  - PR:
    - https://github.com/python-git-team/python-git-team/pull/6
    - https://github.com/python-git-team/python-git-team/pull/9
    - https://github.com/python-git-team/python-git-team/pull/12
    - https://github.com/python-git-team/python-git-team/pull/26
    - https://github.com/python-git-team/python-git-team/pull/28
    - https://github.com/python-git-team/python-git-team/pull/34

## 주요 문서
- 협업 가이드: docs/CONTRIBUTING.md
- 충돌 해결 기록: docs/conflict-resolution.md
- 트러블슈팅 기록: docs/troubleshooting-log.md

## 증빙 자료 (Git History) - [git log --oneline --graph --all]
```
* 5237686 (HEAD -> feature/d-submission-update, origin/feature/d-submission-update) docs: SUBMISSION.md 팀
원별 링크 및 Git 증빙 반영 (#33)
*   35e7d60 (origin/main, origin/HEAD, main) Merge pull request #32 from python-git-team/docs/b-reset-practice
|\  
| * ad29da0 (origin/docs/b-reset-practice) docs: docs: troubleshooting 작성-b - reset --soft
| * 11cee8b rest --soft 실습완료
* |   9ff7daf Merge pull request #22 from python-git-team/chore/add-src-init
|\ \  
| * | 7ebffd3 chore: src파일에 __init__.py 생성
* | |   23957e2 Merge pull request #24 from python-git-team/docs/jm-troubleshooting
|\ \ \  
| * | | a746960 docs: troubleshooting 작성
* | | |   681ec70 Merge pull request #30 from python-git-team/feature/c-revert
|\ \ \ \  
| |_|_|/  
|/| | |   
| * | | fcf7a65 docs: git revert 실습 결과 기록
| * | | 0355681 Revert "chore: revert 실습용 변경 추가"
| * | | d619824 chore: revert 실습용 변경 추가
* | | |   5927620 Merge pull request #28 from python-git-team/feature/d-submission
|\ \ \ \  
| |/ / /  
|/| | |   
| * | | 36e7c37 (origin/feature/d-submission) fix: SUBMISSION.md 위치 루트로 이동
| * | | de40b77 docs: SUBMISSION.md 뼈대 작성 (#27)
| |/ /  
* | |   80a0c37 Merge pull request #26 from python-git-team/feature/d-date-example
|\ \ \  
| * \ \   1afa708 (origin/feature/d-date-example) Merge branch 'main' into feature/d-date-example
| |\ \ \  
| * | | | 501b5c8 docs: stash 실습 기록 추가 (#25)
| * | | | ac5c95e docs: 날짜 함수 사용 예시 추가
| | |/ /  
| |/| |   
* | | |   4a29d30 Merge pull request #10 from python-git-team/feature/contributing
|\ \ \ \  
| * | | | 1b04228 (origin/feature/contributing) 리뷰 확인 후 수정 - 파일 소유권 명시
| * | | | 47dc056 리뷰 확인 후 수정 - 마감기한 & 병합 역할, 정의
| * | | | 3ed7349 docs/CONTRIBUTING.md 파일위치 변경
| * | | | 7795202 docs: 협업 규칙 문서 보완
* | | | |   366e455 Merge pull request #14 from python-git-team/feature/math-utils
|\ \ \ \ \  
| |_|_|/ /  
|/| | | |   
| * | | | 6f35997 (origin/feature/math-utils) fix:테스트 코드 추가(unittest)
| * | | |   e2da04c fix: main 반영 및 README 충돌 해결
| |\ \ \ \  
| | | |/ /  
| | |/| |   
| * | | | de102e5 Update header format in README.md
| * | | | a85fec8 READ.me 오류 해결
| * | | | 834db10 feat:숫자 평균 계산
* | | | |   ae5a75f Merge pull request #16 from python-git-team/feature/c-conflict-test
|\ \ \ \ \  
| |_|/ / /  
|/| | | |   
| * | | | fab6f94 (origin/feature/c-conflict-test) docs: link conflict resolution issue and PR
| * | | |   7dbbc10 fix: resolve date utility merge conflict
| |\ \ \ \  
| * | | | | 28c5c80 feat: add alternate date example
| | |/ / /  
| |/| | |   
* | | | |   75fa711 Merge pull request #9 from python-git-team/feature/d-troubleshooting-log
|\ \ \ \ \  
| |_|_|_|/  
|/| | | |   
| * | | | 5cc73b2 docs: troubleshooting-log 기본 구조 작성
| | |_|/  
| |/| |   
* | | |   32e09b3 Merge pull request #18 from python-git-team/docs/readme-init
|\ \ \ \  
| * \ \ \   0408fb3 (origin/docs/readme-init) fix: main 브랜치 병합 및 README 충돌 해결
| |\ \ \ \  
| |/ / / /  
|/| | | |   
* | | | |   7437ee0 Merge pull request #20 from python-git-team/feature/b-conflict-test
|\ \ \ \ \  
| * | | | | fe9aa38 첫째 줄 수정 : conflict-test
| * | | | | 37577b2 docs: README 수정  (conflict test)
|/ / / / /  
| * / / / ae2991f docs: README 초기작업
|/ / / /  
* | | |   7cc7130 Merge pull request #2 from python-git-team/feature/string-utils
|\ \ \ \  
| * | | | 2a65fa9 chore: 빈문자열과 한글 입력도 확인
| * | | | bd619de feat: add string reverse utility
| |/ / /  
* | | |   1fa8194 Merge pull request #4 from python-git-team/feature/list-utils
|\ \ \ \  
| |_|_|/  
|/| | |   
| * | | 435f36a (origin/feature/list-utils) refactor: 리스트 유틸 타입 힌트 추가
| * | | fdc046a docs: 리스트 유틸 설명 문구 정리
| * | | d23bb92 docs: 리스트 유틸 설명 한국어로 수정
| * | | 0708799 fix: .gitkeep 파일 추적 제외
| * | | 5c3f203 fix: PR에서 로컬 참고 문서 추적 제외
| * | | b6eb340 fix: 로컬 Loom 파일 추적 제외
| * | | ccce855 chore: record review pending state
| * | | b89c86f chore: record pull request progress
| * | | 79de979 chore: record list utility task completion
| * | | ba83a8b feat: add list utility
| * | | 8f197cc chore: record issue task completion
| * | | acb1a64 chore: record list utility contract
| * | | fc8387e chore: plan list utility implementation
| * | | 3eb1bd5 chore: record loom task completion
| * | | 6ac6d49 chore: initialize loom workspace structure
| |/ /  
* | |   2682fe0 Merge pull request #12 from python-git-team/feature/d-conflict-test
|\ \ \  
| |_|/  
|/| |   
| * | 505c480 (origin/feature/d-conflict-test) feat: 날짜 함수 예시값 수정 (conflict 실습용)
|/ /  
* |   e4d3090 Merge pull request #6 from python-git-team/feature/date-utils
|\ \  
| |/  
|/|   
| * c7ed6ef (origin/feature/date-utils) fix: docstring 오타 및 띄어쓰기 수정
| * 9931d0f fix: format_date 함수 타입 힌트 및 주석 추가
| * f7e7489 feat: 날짜 형식 변환 함수 추가 (#5)
|/  
* 50e36cd Initial commit
```