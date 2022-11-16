from sys import stdin
from collections import Counter


n = int(stdin.readline())
a = sorted(list(map(int,stdin.readline().split())))
m = int(stdin.readline())
b = list(map(int,stdin.readline().split()))

d = Counter(a)

for i in b:
    if i in d:
        print(d[i], end=' ')
    else:
        print(0, end=' ')