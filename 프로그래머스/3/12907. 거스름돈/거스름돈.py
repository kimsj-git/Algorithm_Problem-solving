def solution(n, money):
    dp = [1] + [0] * n
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
    return dp[n]