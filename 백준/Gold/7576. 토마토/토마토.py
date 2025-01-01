# 7576 토마토

from collections import deque

M, N = map(int, input().split()) # M은 상자의 가로, N은 상자의 세로 칸 수
T = [[] for _ in range(N)]

for i in range(N):
    T[i] = list(map(int, input().split())) # 1: 익은 토마토, 0: 안 익은 토마토, -1: 토마토 없음

# 문제: 토마토가 모두 익을 때까지의 최소 날짜 출력
"""
(1) 각각의 토마토가 익을 때까지의 최소 날짜 중 가장 작은 날짜 출력
(2) 각각의 토마토가 익을 때까지의 최소 날짜 == 가장 가까운 익은 토마토까지의 최단 거리
==> 시작점이 여러개인 BFS 문제 (큐에 시작점을 순차적으로 집어 넣고 시작)

"""

# BFS로 풀이

visit = [[False] * M for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if T[i][j] == 1:
            queue.append((i, j))
            visit[i][j] = True
            dist[i][j] = 0

dr = [0, 0, 1, -1] # 행이동
dc = [1, -1, 0, 0] # 열이동

while len(queue) != 0:
    r, c = queue.popleft()

    for i in range(4):
        # (1) 이동이 불가한 경우 pass
        if r + dr[i] < 0 or N<= r + dr[i]:
            continue
        if c + dc[i] < 0 or M<= c + dc[i]:
            continue

        # (2) 이동은 가능하나 토마토가 존재하지 않는 경우 pass
        if T[r + dr[i]][c + dc[i]] == -1:
            continue

        # (3) 이동도 가능하고, 토마토도 존재하는 경우
        if not visit[r + dr[i]][c + dc[i]] == True:
            queue.append((r + dr[i], c + dc[i]))
            visit[r + dr[i]][c + dc[i]] = True
            dist[r + dr[i]][c + dc[i]] = dist[r][c] + 1

max_dist = -1
impossible = False
for i in range(N):
    for j in range(M):
        if T[i][j] == -1:
            continue # 토마토가 존재하지 않은 경우 다음 줄로 넘어가기
        if dist[i][j] == -1:
            impossible = True
            break # 익은 토마토와 도달 불가능한 토마토가 하나 이상일 경우 탐색 중단
        max_dist = max(max_dist, dist[i][j])
    if impossible:
        break

if impossible:
    print(-1)
else:
    print(max_dist)