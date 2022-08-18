T = int(input())


def sums_dp(N):
    sums = [0, 1, 2, 4]
    for i in range(4, N+1):
        sums.append(sums[i-1] + sums[i-2] + sums[i-3])
    return sums[N]
    

for tc in range(1, T+1):
    n = int(input())
    print(sums_dp(n))