# 19598 최소 회의실 개수

"""

#### 문제 설명
- 1. 각 회의는 시작 시간과 끝나는 시간이 주어진다.
- 2. 한 회의실에서 동시에 두 개 이상의 회의가 진행될 수 없다.
- 3. 단, 회의는 중단 불가하며, 바로 이어서 다음 회의가 시작될 수 있다.
- 4. 회의의 시작 시간은 끝나는 시간보다 항상 작다. 
- N개의 회의를 모두 진행할 수 있는 최소 회의실 개수를 구하는 문제이다.

---

### 풀이 방법
1. 정렬을 먼저 생각
   - 문제에서 시간 순서대로 회의가 진행되므로, 시작 시간 기준으로 정렬하는 것이 중요하다.
   - 시작 시간이 빠른 순서대로 회의를 처리하며 겹치는지 판단할 수 있다.

2. 우선순위 큐 사용:
   - "최소 회의실"을 요구하므로, 현재 사용 중인 회의실의 가장 빨리 끝나는 시간을 추적해야 한다.
   - `heapq`(최소 힙)은 항상 최솟값을 빠르게 제공하므로 적합하다.

3. 핵심 동작 정의:
   - 각 회의를 처리하면서:
     - 현재 회의의 시작 시간이 가장 빨리 끝나는 시간보다 크거나 같다면:
       - 해당 회의실을 재활용 (최소 힙에서 끝나는 시간 제거).
     - 그렇지 않다면 새로운 회의실이 필요 (끝나는 시간 추가).
   - 반복이 끝나면 최소 힙의 크기가 필요한 회의실의 개수.


"""
import sys
import heapq

input = sys.stdin.readline

# 입력 받기
N = int(input())
meeting_time = []

for _ in range(N):
    meeting = tuple(map(int, input().split()))
    meeting_time.append(meeting)

# 회의 시작 시간을 기준으로 정렬
meeting_time.sort(key=lambda x: x[0])

# 최소 힙 초기화
meeting_room = []

# 회의 시간 관리
for start, end in meeting_time:
    # 힙이 비어 있지 않고, 현재 회의 시작 시간이 가장 빨리 끝나는 회의의 끝나는 시간 이상이면 회의실 재활용
    if meeting_room and meeting_room[0] <= start:
        heapq.heappop(meeting_room)
    
    # 현재 회의를 최소 힙에 추가
    heapq.heappush(meeting_room, end)

# 최소 힙의 크기가 필요한 회의실 개수
print(len(meeting_room))