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


data = list(map(int, input().split()))
P = []
for i in range(4):
    P.append((data[2*i], data[2*i +1]))

p1, p2, p3, p4 = P

if ccw(p1, p2, p3) * ccw(p1, p2, p4) < 0:
    print(1)
else:
    print(0)