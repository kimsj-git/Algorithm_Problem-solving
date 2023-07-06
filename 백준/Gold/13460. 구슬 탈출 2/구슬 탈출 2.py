import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[char for char in input().rstrip()] for _ in range(N)]
drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def roll(r, c, direction):
    dr, dc = drc[direction]
    cnt = 0
    while arr[r + dr][c + dc] != "#" and arr[r][c] != "O":
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt


def bfs(red_r, red_c, blue_r, blue_c):
    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    q = deque([(red_r, red_c, blue_r, blue_c, 0)])
    visited[red_r][red_c][blue_r][blue_c] = True
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt >= 10:
            continue

        for i in range(4):
            nrx, nry, rcnt = roll(rx, ry, i)
            nbx, nby, bcnt = roll(bx, by, i)

            # 파란색 빠지는 경우
            if arr[nbx][nby] == "O":
                continue

            # 빨간색 빠지는 경우
            if arr[nrx][nry] == "O":
                return cnt + 1

            # 둘다 빠지지 않고 위치 중복
            if nrx == nbx and nry == nby:
                dx, dy = drc[i]
                if rcnt > bcnt:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if not visited[nrx][nry][nbx][nby]:
                q.append((nrx, nry, nbx, nby, cnt + 1))
                visited[nrx][nry][nbx][nby] = True
    return -1


red_r = red_c = blue_r = blue_c = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == "R":
            red_r = r
            red_c = c
        elif arr[r][c] == "B":
            blue_r = r
            blue_c = c


print(bfs(red_r, red_c, blue_r, blue_c))
