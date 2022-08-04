import sys
input = sys.stdin.readline

N, K = map(int, input().split())

nums = [i for i in range(1, N+1)]

result = []
idx = K-1
count = N-1
while nums:
    result.append(nums.pop(idx))
    if count == 0:
        break
    idx = (idx + K - 1)%(count)
    count -= 1

print('<', end='')
print(*result, sep=', ', end='')
print('>')
