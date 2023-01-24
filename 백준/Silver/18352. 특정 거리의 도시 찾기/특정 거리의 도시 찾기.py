# 시작점 고정, 최단 경로, 가중치 => 다익스트라
# 모든 정점 -> 모든 정점으로 최단 경로 => 플로이드 워셜

import sys
from heapq import *
input = sys.stdin.readline
INF = float('inf')

N, M, K, X = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def dijkstra(start, k):
    visited = {i: INF for i in range(1, N+1)}   # 시작점부터 i 정점까지의 최소거리
    visited[start] = 0

    pq = []
    heappush(pq, (0, start))
    
    while pq:
        d, x = heappop(pq)
        
        if visited[x] < d:
            continue

        for nx in graph[x]:
            nd = d + 1
            
            if visited[nx] > nd:
                visited[nx] = nd
                heappush(pq, (nd, nx))
    
    result = []
    for i in range(1, N+1):
        if visited[i] == k:
            result.append(i)
    
    return result


ans = dijkstra(X, K)
if ans:
    print(*ans, sep='\n')
else:
    print(-1)