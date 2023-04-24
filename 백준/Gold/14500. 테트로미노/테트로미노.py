import sys
input = sys.stdin.readline
from itertools import combinations as C

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_val = max([max(arr[i]) for i in range(N)])
visited = [[False] * M for _ in range(N)]

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maxV = 0


def dfs(v, cnt, acc):
    global maxV
    
    if cnt == 4:
        if maxV < acc:
            maxV = acc
        return
    
    if maxV >= acc + max_val * (4 - cnt):
        return
    
    r, c = v
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs((nr, nc), cnt + 1, acc + arr[nr][nc])
            visited[nr][nc] = False


def t_shape(v):
    r, c = v
    result = 0
    for comb in C(drc, 3):
        temp = arr[r][c]
        for dr, dc in comb:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                temp += arr[nr][nc]
            else:
                break
        else:
            if result < temp:
                result = temp
    return result


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs((i, j), 1, arr[i][j])
        visited[i][j] = False
        t_val = t_shape((i, j))
        if maxV < t_val:
            maxV = t_val

print(maxV)