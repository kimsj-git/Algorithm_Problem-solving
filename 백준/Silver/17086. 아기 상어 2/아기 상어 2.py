from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
drc = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(r, c):
    visited = [[False] * M for _ in range(N)]
    q = deque([(r, c, 0)])
    visited[r][c] = True
    
    while q:
        r, c, depth = q.popleft()
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if arr[nr][nc] == 1:
                    return depth + 1
                q.append((nr, nc, depth + 1))
                visited[nr][nc] = True


max_dist = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            safe_dist = bfs(i, j)
            max_dist = max(max_dist, safe_dist)

print(max_dist)