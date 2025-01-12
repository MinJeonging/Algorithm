N, K = map(int, input().split())
V = [int(input()) for _ in range(N)]

# dp[j]: j원을 만드는 경우의 수
dp = [0] * (K + 1)
dp[0] = 1  # 0원을 만드는 경우의 수는 1 (아무 동전도 사용하지 않는 경우)

# 동전별로 경우의 수 업데이트
for coin in V:
    for j in range(coin, K + 1):
        dp[j] += dp[j - coin]

print(dp[K])