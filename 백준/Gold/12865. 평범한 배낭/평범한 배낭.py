N, K = map(int, input().split())
items = [0]

for _ in range(N):
    weight, value = map(int, input().split())
    items.append((weight, value))

dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N+1):              # 물건 인덱스 순회
    for j in range(1, K+1):          # dp[j]: i번째 물건까지 넣었을 때 j 무게에서 최대 가치
        w = items[i][0]     # 물건의 무게
        v = items[i][1]     # 물건의 가치
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][K])