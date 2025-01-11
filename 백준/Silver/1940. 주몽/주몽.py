# 1940 주몽

N = int(input())
M = int(input())
A = list(map(int, input().split()))

# 투 포인터로 풀기

A.sort()

start = 0
end = N - 1
count = 0

while start < end: # 종료 조건

    if A[start] + A[end] == M: # 문제 명시 조건
        count += 1
        start += 1
        end -= 1

    else:
        if A[start] + A[end] > M:
            end -= 1

        else:
            start += 1

print(count)
        