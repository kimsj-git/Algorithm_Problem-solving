import sys

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

'''
index   0  1  2  3  4
nums = [1, 2, 3, 4, 5]
acc  = [0, 1, 3, 6, 10, 15]
nums[i]부터 nums[j]까지의 합 = acc[j+1] - acc[i]
'''

acc = [0]
for i in range(N):
    acc.append(acc[i] + nums[i])

max_sum = float("-inf")
for i in range(0, N - K + 1):
    # nums[i] 부터 nums[i + K - 1]까지의 합
    temp_sum = acc[i + K] - acc[i]
    max_sum = max(max_sum, temp_sum)

print(max_sum)
