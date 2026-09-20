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

## 증빙 자료 (Git History)
```text
* 35e7d60 Merge pull request #32 from python-git-team/docs/b-reset-practice
|\  
| * ad29da0 docs: docs: troubleshooting 작성-b - reset --soft
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
| * | | 36e7c37 fix: SUBMISSION.md 위치 루트로 이동
| * | | de40b77 docs: SUBMISSION.md 뼈대 작성 (#27)
| |/ /  
* | |   80a0c37 Merge pull request #26 from python-git-team/feature/d-date-example
|\ \ \  
| * \ \   1afa708 Merge branch 'main' into feature/d-date-example
| |\ \ \  
| * | | | 501b5c8 docs: stash 실습 기록 추가 (#25)
| * | | | ac5c95e docs: 날짜 함수 사용 예시 추가
| | |/ /  
| |/| |   
* | | |   4a29d30 Merge pull request #10 from python-git-team/feature/contributing
|\ \ \ \  
| * | | | 1b04228 리뷰 확인 후 수정 - 파일 소유권 명시
| * | | | 47dc056 리뷰 확인 후 수정 - 마감기한 & 병합 역할, 정의
| * | | | 3ed7349 docs/CONTRIBUTING.md 파일위치 변경
| * | | | 7795202 docs: 협업 규칙 문서 보완
* | | | |   366e455 Merge pull request #14 from python-git-team/feature/math-utils
|\ \ \ \ \  
| |_|_|/ /  
|/| | | |   
| * | | | 6f35997 fix:테스트 코드 추가(unittest)
| * | | | e2da04c fix: main 반영 및 README 충돌 해결
| * | | | de102e5 Update header format in README.md
| * | | | a85fec8 READ.me 오류 해결
| * | | | 834db10 feat:숫자 평균 계산
* | | | | ae5a75f Merge pull request #16 from python-git-team/feature/c-conflict-test
* | | | | 75fa711 Merge pull request #9 from python-git-team/feature/d-troubleshooting-log
* | | | 32e09b3 Merge pull request #18 from python-git-team/docs/readme-init
* | | | 7437ee0 Merge pull request #20 from python-git-team/feature/b-conflict-test
* | | 7cc7130 Merge pull request #2 from python-git-team/feature/string-utils
* | | 1fa8194 Merge pull request #4 from python-git-team/feature/list-utils
* | 2682fe0 Merge pull request #12 from python-git-team/feature/d-conflict-test
* e4d3090 Merge pull request #6 from python-git-team/feature/date-utils
* 50e36cd Initial commit