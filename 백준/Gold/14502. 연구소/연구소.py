# 14502 연구소
from itertools import combinations
from collections import deque

# 입력 받기
N, M = map(int, input().split())
B = [[0] for _ in range(N)]

for i in range(N):
    B[i] = list(map(int, input().split()))

cells = [(i, j) for i in range(N) for j in range(M) if B[i][j] == 0]

max_safe =0
for combination in combinations(cells, 3): # 튜플도 조합 가능
    for row, col in combination: # 벽 세우기
        B[row][col] = 1

    # BFS 수행

    visit = [[False] * M for _ in range(N)]
    queue = deque()
    for i in range(N):
        for j in range(M):
            if B[i][j] == 2: # 바이러스가 시작점
                queue.append((i, j))
                visit[i][j] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while len(queue) != 0:
        r, c = queue.popleft()

        for i in range(4):
            if r + dr[i] < 0 or r + dr[i] >= N:
                continue
            if c + dc[i] < 0 or c + dc[i] >= M:
                continue
            if (B[r + dr[i]][c + dc[i]] != 1) and (not visit[r + dr[i]][c + dc[i]]): # 벽이 아니라면 방문 가능
                queue.append((r + dr[i], c + dc[i]))
                visit[r + dr[i]][c + dc[i]] = True

    # 바이러스가 접근 불가능한 최대 개수 계산
    safe = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] == False and B[i][j] == 0:
                safe += 1
    if max_safe < safe:
        max_safe = safe

    for row, col in combination: # 벽 허물기
        B[row][col] = 0

print(max_safe)