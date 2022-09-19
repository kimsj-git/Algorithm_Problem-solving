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


p1 = tuple(map(int, input().split()))
p2 = tuple(map(int, input().split()))
p3 = tuple(map(int, input().split()))
print(ccw(p1, p2, p3))