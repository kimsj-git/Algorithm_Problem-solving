import sys
input = sys.stdin.readline
V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key = lambda x: x[2])

p = {i: i for i in range(1, V+1)}
rank = {i: 0 for i in range(1, V+1)}


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

result = 0
cnt = 0
for edge in edges:
    n1, n2, w = edge[0], edge[1], edge[2]
    if find_set(n1) == find_set(n2):
        continue
    union(n1, n2)
    result += w
    cnt += 1
    if cnt == V-1:
        break

print(result)