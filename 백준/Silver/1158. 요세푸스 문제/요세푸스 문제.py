from collections import deque

N, K = map(int, input().split())

queue = deque()

for i in range(K, N + 1):
    queue.append(i)
for i in range(1, K):
    queue.append(i)

ans = []

while True:
    ans.append(queue.popleft())

    if len(queue) == 0:
        break

    for _ in range(K - 1):
        u = queue.popleft()
        queue.append(u)

print("<", end = "")
for i in range(N - 1):
    print(ans[i], end = ", ")
print(ans[-1], end = ">")