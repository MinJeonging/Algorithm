# 2003 수들의 합2

N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 0
start = 0
end = 0
current_sum = A[0]

while True:
    # 조건이 만족하는지 체크
    if current_sum == M:
        count += 1

    # 투포인터 이동
    if current_sum < M:
        # 종료 조건
        if end == N - 1:
            break
        end += 1
        current_sum += A[end]
    elif current_sum > M:
        start += 1
        current_sum -= A[start - 1]
    else:
        start += 1
        current_sum -= A[start - 1]
    
print(count)
