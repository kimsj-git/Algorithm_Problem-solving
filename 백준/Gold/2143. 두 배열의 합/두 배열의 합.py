import sys

input = sys.stdin.readline


T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# 누적 합
sum_A = [0] * (n + 1)
sum_B = [0] * (m + 1)

for i in range(1, n + 1):
    sum_A[i] += sum_A[i - 1] + A[i - 1]
for i in range(1, m + 1):
    sum_B[i] += sum_B[i - 1] + B[i - 1]

# key: 부분합 값, value: 해당 값을 가진 부분배열 개수
partial_sum_A = {}
partial_sum_B = {}

for i in range(1, n + 1):
    for j in range(i, n + 1):
        sum_ij = sum_A[j] - sum_A[i - 1]
        if partial_sum_A.get(sum_ij):
            partial_sum_A[sum_ij] += 1
        else:
            partial_sum_A[sum_ij] = 1

for i in range(1, m + 1):
    for j in range(i, m + 1):
        sum_ij = sum_B[j] - sum_B[i - 1]
        if partial_sum_B.get(sum_ij):
            partial_sum_B[sum_ij] += 1
        else:
            partial_sum_B[sum_ij] = 1

cnt = 0
for key, value in partial_sum_A.items():
    if partial_sum_B.get(T - key):
        cnt += value * partial_sum_B[T - key]

print(cnt)
