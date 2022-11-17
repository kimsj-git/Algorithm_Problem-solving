import sys

n = int(sys.stdin.readline())
a = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    a[data] += 1

for j in range(10001):
    if a[j] != 0:
        for k in range(a[j]):
            print(j)