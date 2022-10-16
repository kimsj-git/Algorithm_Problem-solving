from math import sqrt


def is_circle(x, y):
    '''
    점 P1(x1, y1)와 P2(x2, y2) 사이에 원이 지나가는지 판별하는 함수
    (P2에서 C까지 거리) < R < (P1에서 C까지 거리)
    '''
    x1, y1 = x, y + 1
    x2, y2 = x + 1, y
    if ((x2 - R)**2 + y2**2 - R**2) * ((x1 - R)**2 + y1**2 - R**2) < 0:
        return True
    else:
        return False


N = int(input())
R = N // 2
C = (R, 0)

s = R - int(R / sqrt(2))
endX = s
endY = R - s + 1

cnt = 0
x = 0
y = 0
while x + 1 != endX or y + 1 != endY:
    cnt += 1
    # 위(x, y+1), 오른쪽(x+1, y)
    if is_circle(x, y+1):
        y += 1
    elif is_circle(x+1, y):
        x += 1
    else:
        x += 1
        y += 1

print((cnt * 2 + 1) * 4)