# 10884 쉬운 계단 수

"""
1. 계단 수의 정의
   - 계단 수는 각 자리의 숫자가 인접한 자리와의 차이가 1인 숫자를 의미.
   - 예: 101, 121, 123 등.

2. 문제를 풀기 위한 접근
   - DP을 사용하여 점화식으로 문제 해결.
   - dp[i][j]: i자리 계단 수 중 마지막 자리가 j인 경우의 수.

3. 점화식 도출
   - dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
     (단, j-1 또는 j+1이 범위를 벗어나면 제외)

4. 기저 조건 설정
   - 1자리 계단 수는 마지막 자리가 1~9인 경우 각각 1개.
   - dp[1][0] = 0 (끝자리가 0인 경우 계단 수 없음)
   - dp[1][1] ~ dp[1][9] = 1 (각각 하나씩 가능)
"""

N = int(input())  
MOD = 1000000000  # 나머지 연산에 사용할 값

dp = [[0] * 10 for _ in range(N + 1)]  # dp[i][j]: i자리 계단 수 중 마지막 자리가 j인 경우의 수
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 1자리 계단 수 초기값 설정

# DP로 구현
for i in range(2, N + 1):  # 2자리부터 N자리까지 계산
    for j in range(10):    # 마지막 자리가 0~9인 경우
        if j == 0:  # 끝자리가 0인 경우: 이전 자리 끝자리가 1인 경우만 가능
            dp[i][j] = dp[i - 1][j + 1] % MOD
        elif j == 9:  # 끝자리가 9인 경우: 이전 자리 끝자리가 8인 경우만 가능
            dp[i][j] = dp[i - 1][j - 1] % MOD
        else:  # 끝자리가 1~8인 경우: 이전 자리 끝자리가 j-1 또는 j+1인 경우 가능
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD

result = sum(dp[N]) % MOD  # N자리 계단 수의 총합을 계산하여 나머지 출력
print(result)