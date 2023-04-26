import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

air_purifier = []
for r in range(R):
    if arr[r][0] == -1:
        air_purifier.append((r, 0))

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cw = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ccw = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dust(arr):
    next = [[0] * C for _ in range(R)]
    for r, c in air_purifier:
        next[r][c] = -1
    
    # 1. 확산
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                diffused = 0
                for dr, dc in drc:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                        next[nr][nc] += arr[r][c] // 5
                        diffused += arr[r][c] // 5
                next[r][c] += arr[r][c] - diffused
    
    # 2-1. 공기청정기 윗부분
    r1 = air_purifier[0][0]
    r, c = r1, 0
    for i in range(4):
        # 시계방향 순서로 이동하며 경로에 있는 먼지 이동시키기
        dr, dc = cw[i]
        while 0 <= r <= r1 and 0 <= c < C:
            nr, nc = r + dr, c + dc
            if 0 <= nr <= r1 and 0 <= nc < C:
                if next[r][c] != -1:
                    next[r][c] = next[nr][nc]
                if next[nr][nc] == -1:
                    next[r][c] = 0
                r, c = nr, nc
            else:
                break

    # 2-2. 공기청정기 아랫부분
    r2 = air_purifier[1][0]
    r, c = r2, 0
    for i in range(4):
        # 반시계방향 순서로 이동하며 경로에 있는 먼지 이동시키기
        dr, dc = ccw[i]
        while r2 <= r < R and 0 <= c < C:
            nr, nc = r + dr, c + dc
            if r2 <= nr < R and 0 <= nc < C:
                if next[r][c] != -1:
                    next[r][c] = next[nr][nc]
                if next[nr][nc] == -1:
                    next[r][c] = 0
                r, c = nr, nc
            else:
                break
    
    return next


for _ in range(T):
    arr = dust(arr)

print(sum(sum(arr, start=[])) + 2)