# 17952 과제는 끝나지 않아!

"""

#### 문제 설명
- 1. 과제는 가장 최근에 나온 순서대로 한다. 또한 과제를 받으면 바로 시작한다.
- 2. 과제를 하던 도중 새로운 과제가 나온다면, 하던 과제를 중단하고 새로운 과제를 진행한다.
- 3. 새로운 과제가 끝났다면, 이전에 하던 과제를 이전에 하던 부분부터 이어서 한다. 
- 총 학기 시간, 과제의 등장 시간, 과제별 소요시간과, 과제 점수(만점)를 알 때, 성애가 받을 과제 점수를 구하는 문제이다.

---

### 풀이 방법

#### 1. 후입선출의 방식 -> 스택 자료 구조의 활용
- 새로운 과제 등장 시, (if 1 등장)
-- 이전 과제 중단 후 다시 스택에 추가
-- 과제의 점수, 소요시간을 튜플 자료형으로 스택에 추가
-- 스택의 top 과제를 뽑아 과제 수행
-- 스택이 비거나 학기 시간이 끝날 때까지 수행

"""
import sys 
input = sys.stdin.readline
from collections import deque

N = int(input())
stack = deque()
current = None
score = 0

for _ in range(N):
    homework = list(map(int, input().split()))
    
    if homework[0] == 1:  # 새로운 과제가 추가된 경우
        if current:  # 진행 중이던 과제가 있으면 스택에 추가
            stack.append(current)
        # 새로운 과제 시작
        current = (homework[1], homework[2])  # (점수, 남은 시간)
    
    if current:  # 진행 중인 과제가 있는 경우
        score += current[0] if current[1] == 1 else 0
        current = (current[0], current[1] - 1) if current[1] > 1 else None

    if not current and stack:  # 진행 중인 과제가 없으면 이전 과제를 가져옴
        current = stack.pop()

print(score)