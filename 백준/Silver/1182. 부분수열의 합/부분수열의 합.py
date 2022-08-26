N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(1, 1 << N):
    sum_subset = 0
    for j in range(N):
        if i & (1 << j):
            sum_subset += nums[j]
    if sum_subset == S:
        count += 1
    # print(sum_subset)

print(count)