import sys

input = sys.stdin.readline


def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]


def merge(x, y):
    def link(x, y):
        if rank[x] > rank[y]:
            p[y] = x
        else:
            p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

    link(find_set(x), find_set(y))


def is_cross(L1: tuple, L2: tuple) -> bool:
    def ccw(a, b, c):
        ab = (b[0] - a[0], b[1] - a[1])
        bc = (c[0] - b[0], c[1] - b[1])
        cross = ab[0] * bc[1] - ab[1] * bc[0]
        if cross > 0:
            return 1
        elif cross < 0:
            return -1
        else:
            return 0

    x1, y1, x2, y2 = L1
    x3, y3, x4, y4 = L2

    # L1의 양끝점
    p1, p2 = (x1, y1), (x2, y2)
    # L2의 양끝점
    p3, p4 = (x3, y3), (x4, y4)

    flag1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    flag2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

    # L1, L2가 일직선 상에 있는 경우
    if flag1 == 0 and flag2 == 0:
        if (
            (min(x1, x2) > x3 and min(x1, x2) > x4)
            or (max(x1, x2) < x3 and max(x1, x2) < x4)
            or (min(y1, y2) > y3 and min(y1, y2) > y4)
            or (max(y1, y2) < y3 and max(y1, y2) < y4)
        ):
            return False
        else:
            return True
    # ccw 선분 교차
    elif flag1 <= 0 and flag2 <= 0:
        return True
    else:
        return False


N = int(input())

p = {i: i for i in range(N)}
rank = {i: 0 for i in range(N)}

lines = []
for i in range(N):
    L1 = tuple(map(int, input().split()))

    for j in range(i):
        L2 = lines[j]
        if is_cross(L1, L2) and find_set(i) != find_set(j):
            merge(i, j)

    lines.append(L1)

for i in range(N):
    p[i] = find_set(i)

# 그룹 개수, 최대 선분 개수 구하기
group_cnt = 0
count = {i: 0 for i in range(N)}  # count[i]: i번 그룹에 속한 선분의 개수
for i in range(N):
    if p[i] == i:
        group_cnt += 1
    count[p[i]] += 1

print(group_cnt)
print(max(count.values()))
