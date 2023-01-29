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


L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))

# L1의 양끝점
p1 = (L1[0], L1[1])
p2 = (L1[2], L1[3])
# L2의 양끝점
p3 = (L2[0], L2[1])
p4 = (L2[2], L2[3])

flag1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
flag2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

# flag1, flag2 모두 음수이면 선분 교차
if flag1 < 0 and flag2 < 0:
    print(1)
else:
    print(0)