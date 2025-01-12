# 14719 빗물

H, W = map(int, input().split())
wall = list(map(int, input().split()))
A = [[0] * W for _ in range(H)]

for j in range(W):
    if wall[j] == 0:
        continue
    for i in range(H - wall[j], H):
        A[i][j] = 1

# 브루트포스 (양측에 벽이 있으면 rain 증가)
rain = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == 1: # 빈 칸만 탐색
            continue

        left_bool = False
        right_bool = False
        left = j
        right = j

        while left > 0 and not left_bool:
            left -= 1
            if A[i][left] == 1:
                left_bool = True

        if not left_bool: # 백트래킹
            continue 

        while right < W - 1 and not right_bool:
            right += 1
            if A[i][right] == 1:
                right_bool = True

        if left_bool and right_bool:
            rain += (right - left - 1) 

            # 중복 계산 방지를 위해 벽으로 막아버리기
            for k in range(left, right + 1):
                A[i][k] = 1

print(rain)