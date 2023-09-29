import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

remainders= [0] * M     # remainders[i]: M으로 나눈 나머지가 i인 누적합 개수
acc_sum = 0
for i in range(N):
    acc_sum += nums[i]
    remainders[acc_sum % M] += 1

count = remainders[0]
for n in remainders:
    count += n * (n - 1) // 2   # nC2
    
print(count)