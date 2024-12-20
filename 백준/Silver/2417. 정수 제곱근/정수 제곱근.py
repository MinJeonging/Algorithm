N = int(input())

# 이분탐색으로 구현

low = 0
high = 2 ** 32

ans = 1 # 음이 아닌 정수

while low <= high:
    mid = (low + high) // 2
    if mid ** 2 < N:
        low = mid + 1
    else:
        ans = mid
        high = mid - 1

print(ans)