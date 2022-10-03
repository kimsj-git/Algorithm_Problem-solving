from itertools import combinations_with_replacement as C
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for combi in C(nums, M):
    print(*combi)