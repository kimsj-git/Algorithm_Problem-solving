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


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# L1의 양끝점
p1, p2 = (x1, y1), (x2, y2)
# L2의 양끝점
p3, p4 = (x3, y3), (x4, y4)

flag1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
flag2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

# L1, L2가 일직선 상에 있는 경우
if flag1 == 0 and flag2 == 0:
    if ((min(x1, x2) > x3 and min(x1, x2) > x4) or 
        (max(x1, x2) < x3 and max(x1, x2) < x4) or
        (min(y1, y2) > y3 and min(y1, y2) > y4) or
        (max(y1, y2) < y3 and max(y1, y2) < y4)):
        print(0)
    else:
        print(1)
# ccw 선분 교차
elif flag1 <= 0 and flag2 <= 0:
    print(1)
else:
    print(0)