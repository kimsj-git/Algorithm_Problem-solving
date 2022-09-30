import sys
from heapq import *
input = sys.stdin.readline
INF = float('inf')

N, M, X = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    s, e, time = map(int, input().split())
    graph[s].append((time, e))


def dijkstra(start, end):
    visited = {i: INF for i in range(1, N+1)}
    visited[start] = 0
    pq = []
    heappush(pq, (0, start))
    
    while pq:
        t, x = heappop(pq)
        if visited[x] < t:
            continue
        for time, nx in graph[x]:
            nt = visited[x] + time
            if visited[nx] > nt:
                visited[nx] = nt
                heappush(pq, (nt, nx))

    return visited[end]


maxT = 0
for i in range(1, N+1):
    temp = dijkstra(i, X) + dijkstra(X, i)
    if temp > maxT:
        maxT = temp

print(maxT)