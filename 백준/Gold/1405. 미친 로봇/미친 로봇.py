N, e, w, s, n = map(int, input().split())

dxy = [[1, 0], [-1, 0], [0, -1], [0, 1]]        # 동서남북 델타이동
p = {0: e/100, 1: w/100, 2: s/100, 3: n/100}    # 동서남북 이동 확률


def find(v, route, cnt, prob):
    global result
    if cnt == N:
        result += prob
        return
    for i in range(4):
        dx, dy = dxy[i]
        w = (v[0] + dx, v[1] + dy)
        if w not in route:
            find(w, route + [w], cnt + 1, prob * p[i])


result = 0
find((0, 0), [(0, 0)], 0, 1)
print(result)