import math


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


def calc_len(L: tuple) -> float:
    x1, y1, x2, y2 = L
    length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return length


def intersecting_point(L1, L2):
    x1, y1, x2, y2 = L1
    x3, y3, x4, y4 = L2

    A = y2 - y1
    B = x1 - x2
    E = (y2 - y1) * x1 + (x1 - x2) * y1

    C = y4 - y3
    D = x3 - x4
    F = (y4 - y3) * x3 + (x3 - x4) * y3

    Det = (A * D) - (B * C)
    if Det == 0:
        return False  # 기울기가 같으면 False 반환
    else:
        if (D * E - B * F) % Det == 0:
            x = (D * E - B * F) // Det
        else:
            x = (D * E - B * F) / Det
        if (A * F - C * E) % Det == 0:
            y = (A * F - C * E) // Det
        else:
            y = (A * F - C * E) / Det
        return (x, y)  # 기울기가 다르면 교점 반환


def is_cross(L1: tuple, L2: tuple):
    x1, y1, x2, y2 = L1
    x3, y3, x4, y4 = L2

    p1, p2 = (x1, y1), (x2, y2)
    p3, p4 = (x3, y3), (x4, y4)

    flag1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    flag2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)

    # 1. L1, L2가 한 점을 공유하는 경우
    if len(set([p1, p2, p3, p4])) == 3:
        # 1-1. L1, L2 기울기 다른 경우
        if intersecting_point(L1, L2):
            return (True, intersecting_point(L1, L2))
        # 1-2. L1, L2 기울기 같은 경우
        else:
            # 1-2-1. L1, L2 길이 합이 두 선분을 연결한 길이와 같은 경우 -> 한 점을 공유함
            lenL1 = calc_len(L1)
            lenL2 = calc_len(L2)
            if p1 == p3 and math.isclose(calc_len((*p2, *p4)), lenL1 + lenL2):
                return (True, p1)
            elif p1 == p4 and math.isclose(calc_len((*p2, *p3)), lenL1 + lenL2):
                return (True, p1)
            elif p2 == p3 and math.isclose(calc_len((*p1, *p4)), lenL1 + lenL2):
                return (True, p2)
            elif p2 == p4 and math.isclose(calc_len((*p1, *p3)), lenL1 + lenL2):
                return (True, p2)
            # 1-2-2. 한 선분이 다른 선분에 포함되는 경우
            return (True, 0)

    # 2. 교차하지 않는 경우
    if flag1 > 0 or flag2 > 0:
        return (False, 0)
    # 3. L1, L2가 일직선 상에 있는 경우
    elif flag1 == 0 and flag2 == 0:
        if (
            (min(x1, x2) > x3 and min(x1, x2) > x4)
            or (max(x1, x2) < x3 and max(x1, x2) < x4)
            or (min(y1, y2) > y3 and min(y1, y2) > y4)
            or (max(y1, y2) < y3 and max(y1, y2) < y4)
        ):
            return (False, 0)
        else:
            return (True, 0)
    # 4. 한 점에서 선분 교차
    elif flag1 <= 0 and flag2 <= 0:
        # 4-1. 교차하는 점 구하기
        p = intersecting_point(L1, L2)
        return (True, p)


L1 = tuple(map(int, input().split()))
L2 = tuple(map(int, input().split()))

ans, p = is_cross(L1, L2)

if ans:
    print(1)
    if p:
        print(*p)
else:
    print(0)
