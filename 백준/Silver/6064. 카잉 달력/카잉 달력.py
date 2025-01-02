# 6064 카잉달력
T = int(input())

# 큐로 풀이 (브루트포스) => 시간초과
for _ in range(T):
    M, N, x, y = map(int, input().split())

    if M < N: # M >= N
        M, N = N, M
        x, y = y, x

    found = False
    # y일때 <y, y>
    first = y
    for i in range(M):
        if first == x:
            print(y + i * N)
            found = True
            break

        first += N
        if first > M:
            first -= M
            
    if not found:
        print(-1)