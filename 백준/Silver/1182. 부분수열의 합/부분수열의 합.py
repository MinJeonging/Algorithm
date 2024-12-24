import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())
suyeol = list(map(int, input().split()))
ans = 0

for i in range(1, N + 1):
    for combination in combinations(suyeol, i):
        if sum(combination) == S:
            ans += 1

print(ans)