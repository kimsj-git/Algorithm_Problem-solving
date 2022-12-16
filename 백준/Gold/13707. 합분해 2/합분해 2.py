import math
N, K = map(int, input().split())
print(math.comb(N + K - 1, K - 1) % 1000000000)