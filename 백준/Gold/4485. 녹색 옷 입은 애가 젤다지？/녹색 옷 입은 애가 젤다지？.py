import sys
from heapq import *
input = sys.stdin.readline
INF = float('inf')

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

tc = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [[INF] * N for _ in range(N)]
    visited[0][0] = graph[0][0]
    pq = []
    heappush(pq, (graph[0][0], (0, 0)))

    while pq:
        cost, v = heappop(pq)
        r, c = v[0], v[1]
        if visited[r][c] < cost:
            continue

        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + graph[nr][nc]
                if visited[nr][nc] > new_cost:
                    visited[nr][nc] = new_cost
                    heappush(pq, (new_cost, (nr, nc)))
    
    result = visited[N-1][N-1]
    print(f'Problem {tc}: {result}')
    tc += 1