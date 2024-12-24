#21318

import sys

input = sys.stdin.readline

N = int(input())
akbo = list(map(int, input().split()))

# akbo를 순차적으로 순회하면서 조건을 만족하는 경우만 1로 갱신.
mistake = [1 if akbo[i] > akbo[i + 1] else 0 for i in range(N - 1)]

# 누적합으로 풀이.
psum = [0] * (N - 1)

for idx in range(N - 1): # 마지막은 고려 안해도 됨.

    if idx == 0:
        psum[idx] = mistake[idx]
    else:
        psum[idx] = psum[idx - 1] + mistake[idx]

Q = int(input())
for _ in range(Q):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1

    if x == y:
        print(0)
        continue

    # x ~ y-1(마지막은 무조건 0) 까지의 mistake의 합
    ans = psum[y - 1]
    if x > 0:
        ans -= psum[x - 1] # 시작 인덱스 - 1 을 빼주어야 함 주의.

    print(ans)