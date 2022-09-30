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
        
        # x에 저장된 최소비용이 현재 뽑힌 노드 (d, x)의 d보다 작으면
        # 노드가 저장된 이후 visited[x]가 갱신된 것이므로 큐의 다음 노드로 넘어간다.
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