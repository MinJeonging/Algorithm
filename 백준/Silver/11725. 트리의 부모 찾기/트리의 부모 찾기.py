# 11725 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

# 입력 받기
N = int(input())
adj = [[] for _ in range(N)]

# 인접리스트 생성
for _ in range(N - 1):
    u, v = map(int, input().split())

    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)

# dfs로 풀이
visit = [False] * N
parent = [-1] * N

def dfs(u):
    visit[u] = True

    for v in adj[u]:
        if not visit[v]:
            parent[v] = u # 부모 노드 저장
            dfs(v)

dfs(0)

for i in range(1, N):
    print(parent[i] + 1)