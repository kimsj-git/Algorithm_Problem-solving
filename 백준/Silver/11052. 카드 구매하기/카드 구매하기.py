N = int(input())
packs = [0] + list(map(int, input().split()))

# 카드를 0개 ~ N개 살때 최대값
prices = [0] * (N+1) 

prices[1] = packs[1]                        # 카드 1개 살때 최대값
prices[2] = max(packs[1] * 2, packs[2])     # 카드 2개 살때 최대값

def prices_dp(n):
    for i in range(3, n+1):
        temp = []
        for j in range(i+1):
            temp.append(prices[i-j] + packs[j])
        prices[i] = max(temp)
    return prices[n]

print(prices_dp(N))