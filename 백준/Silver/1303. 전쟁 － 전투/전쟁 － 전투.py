# 1303 전쟁 - 전투
from collections import deque

N, M = map(int, input().split())
A = [[0] * N for _ in range(M)]

for i in range(M): # 배열 생성
    A[i] = list(input()) # 문자 단위로 쪼개기

W_count = 0
B_count = 0

def bfs(N, M, A, enemy):

    visit = [[False] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if A[i][j] == enemy:
                visit[i][j] = True
    queue = deque()

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    strength = 0
    for i in range(M):
        for j in range(N):
            if not visit[i][j]:
                queue.append((i, j))
                visit[i][j] = True
                walk = 1

                while len(queue) != 0:
                    r, c = queue.popleft()

                    for k in range(4): # 반복문 변수 중복 주의
                        move_r = r + dr[k]
                        move_c = c + dc[k]

                        if move_r < 0 or move_r > M - 1:
                            continue
                        if move_c < 0 or move_c > N - 1:
                            continue
                        if not visit[move_r][move_c]:
                            queue.append((move_r, move_c))
                            visit[move_r][move_c] = True
                            walk += 1

                strength += (walk) ** 2
                
    return strength

# W의 bfs
W_count = bfs(N, M, A,'B')
B_count = bfs(N, M, A,'W')

print(W_count, B_count, sep = ' ')