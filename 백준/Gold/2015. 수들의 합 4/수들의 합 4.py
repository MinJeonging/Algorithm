# 2015 수들의 합 4

N, K = map(int, input().split())
A = list(map(int, input().split()))
psum = [0] * N
psum[0] = A[0]

for i in range(1, N):
    psum[i] = psum[i - 1] + A[i]

ans = 0
count = {}
for i in range(N):
    goal = psum[i] - K # psum[i] - goal = K인 goal이 이전에 몇 번 존재했는지 체크

    if goal == 0:
        ans += 1
    if goal in count:
        ans += count[goal]
    if psum[i] not in count:
        count[psum[i]] = 0
    count[psum[i]] += 1

print(ans)