# 20922 겹치는 건 싫어

# 입력 받기
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 10 ** 5 이하의 정수 배열 초기화
count = [0] * 100001

start = 0
end = 0
count[A[start]] += 1 # 등장 횟수 계산

# 투포인터로 구현
max_length = 0
good = True # 조건 만족 여부
while True:
    if good:
        max_length = max(max_length, end - start + 1) # 최대 길이 저장

        if end == N - 1: 
            break

        end += 1
        count[A[end]] += 1
        if count[A[end]] == K + 1:
            good = False
    else:
        start += 1
        count[A[start - 1]] -= 1
        if count[A[start - 1]] == K:
            good = True

print(max_length)
