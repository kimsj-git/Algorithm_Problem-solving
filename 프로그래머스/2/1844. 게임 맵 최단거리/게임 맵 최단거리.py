from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    q = deque([(0, 0, 1)])
    while q:
        r, c, cnt = q.popleft()
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maps[nr][nc] == 1:
                if nr == n - 1 and nc == m - 1:
                    return cnt + 1
                q.append((nr, nc, cnt + 1))
                visited[nr][nc] = True
    
    return -1