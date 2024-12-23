A, B, C, M = map(int, input().split())

piro = 0
ans = 0

for _ in range(24):
    if piro + A > M:
        piro = max(0, piro - C)
    else:
        piro += A
        ans += B

print(ans)