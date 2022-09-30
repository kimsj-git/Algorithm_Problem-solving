import sys
from heapq import *
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start, end):
    visited = {i: INF for i in range(1, N+1)}   # visited[i]: 시작점에서 i까지 최소비용
    visited[start] = 0
    pq = []
    heapify(pq)
    heappush(pq, (0, start))

    while pq:
        d, x = heappop(pq)
        
        if visited[x] < d:
            continue
        
        for nw, nx in graph[x]:
            nd = d + nw

            if visited[nx] > nd:
                visited[nx] = nd
                heappush(pq, (nd, nx))
    
    return visited[end]


N = int(input())
M = int(input())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

start, end = map(int, input().split())

print(dijkstra(start, end))