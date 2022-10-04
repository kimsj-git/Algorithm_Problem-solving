import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = {i: i for i in range(n + 1)}
rank = {i: 0 for i in range(n + 1)}


def find_set(x):
    while p[x] != x:
        x = p[x]
    return x


def union(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1 


for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    elif cmd == 1:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')