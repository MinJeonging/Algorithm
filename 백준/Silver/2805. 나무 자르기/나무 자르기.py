import sys
input = sys.stdin.readline

N, M = map(int, input().split())
H = list(map(int, input().split()))

ans = 0
low = 0
high = max(H)

# 이분 탐색으로 구현

while low <= high:
    mid = (low + high)//2

    namu = sum(max(0, (i - mid)) for i in H) # 얻은 나무의 길이
    
    if namu >= M: # 조건을 만족하면서 더 나은 정답이 존재하지 않는 경우 정답 확정
        ans = mid
        low = mid + 1

    else: # 조건을 만족하지 않을 시 답변 초기화 후 range 수정
        high = mid - 1

print(ans)