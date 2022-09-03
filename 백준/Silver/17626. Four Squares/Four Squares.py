n = int(input())

squres_dp = [0] * (n+1)
squres_dp[1] = 1
for i in range(2, n+1):
    result = 4
    j = 1
    while j ** 2 <= i:
        temp = squres_dp[i - j ** 2] + 1
        result = min(result, temp)
        j += 1
    squres_dp[i] = result

print(squres_dp[n])