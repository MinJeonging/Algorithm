# 11726

N = int(input())
mod = 10007

# a_n 은 2 * n의 타일을 1 * 2나 2 * 1의 타일로 채우는 방법의 수.
dp = [0] * 1002
dp[1] = 1
dp[2] = 2

for idx in range(3, N + 1):
    dp[idx] = dp[idx - 1] + dp[idx - 2]
    dp[idx] %= mod # 숫자가 과도하게 커지는 것을 방지하기 위해 나머지 정리의 원리 활용 

print(dp[N])