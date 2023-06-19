from itertools import permutations as P

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = []
for permu in P(nums, M):
    result.append(permu)

result = sorted(list(set(result)))
for item in result:
    print(*item)