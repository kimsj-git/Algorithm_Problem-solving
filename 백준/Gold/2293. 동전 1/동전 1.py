n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)      # dp[j]: j원이 되는 경우의 수

for i in coins:                 # i: 동전 값
    for j in range(i, k + 1):   # j: dp 인덱스
        if j == i:
            dp[j] += 1
        else:
            dp[j] += dp[j - i]

print(dp[k])