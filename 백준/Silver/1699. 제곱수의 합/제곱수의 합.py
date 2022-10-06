N = int(input())

dp = [N] * (N+1)
dp[0] = 0
dp[1] = 1
for i in range(2, N+1):
    for j in range(1, int(i**0.5)+1):
        if dp[i] > dp[i - j**2] + 1:
            dp[i] = dp[i - j**2] + 1

print(dp[N])