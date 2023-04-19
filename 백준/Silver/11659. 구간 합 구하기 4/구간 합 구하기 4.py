import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

# 누적합 리스트
acc = [0]
for i in range(1, N + 1):
    acc.append(acc[i-1] + nums[i-1])

for _ in range(M):
    i, j = map(int, input().split())
    print(acc[j] - acc[i-1])