import sys

input = sys.stdin.readline


def find_set(x):
    while p[x] != x:
        x = p[x]
    return x


def union(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
        count[x] += count[y]
    else:
        p[x] = y
        count[y] += count[x]
    if rank[x] == rank[y]:
        rank[y] += 1


T = int(input())
for _ in range(T):
    p = {}
    rank = {}
    count = {}
    F = int(input())
    for _ in range(F):
        user1, user2 = input().rstrip().split()
        for user in [user1, user2]:
            if p.get(user) == None:
                p[user] = user
                rank[user] = 0
                count[user] = 1

        if find_set(user1) != find_set(user2):
            union(user1, user2)

        print(count[find_set(user1)])
