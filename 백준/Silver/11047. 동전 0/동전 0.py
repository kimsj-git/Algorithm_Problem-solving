N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0
idx = N - 1
while K:
    for i in range(idx, -1, -1):
        if coins[i] <= K:
            coin = coins[i]
            idx = i - 1
            break
    count += K // coin
    K -= coin * (K // coin)

print(count)