# 14502
from itertools import combinations
import copy
from collections import deque

# 입력 받기
N, M = map(int, input().split())
A = [[0] for _ in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))

# 임의의 3개의 빈 칸 선정
filled = set()
maxSafeArea = 0
for i in range(N):
    for j in range(M):
        if A[i][j] == 1 or A[i][j] == 2: # 빈칸이 아닌 경우
            filled.add(i * M + j)

for combination in combinations(list(range(N * M)), 3):
    impossible = False
    B = copy.deepcopy(A) # 모든 조합마다 A deepcopy
    for space in combination:
        if space in filled:
            impossible = True
            break
        B[space // M][space % M] = 1
    if impossible: # space가 하나라도 채워져있는 공간이면 pass
        continue

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
    safeArea = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] == False and B[i][j] == 0:
                safeArea += 1
    if maxSafeArea < safeArea:
        maxSafeArea = safeArea

print(maxSafeArea)