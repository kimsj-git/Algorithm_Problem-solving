from heapq import *
INF = float('inf')


def dijkstra(start, end):
    distance = {i: INF for i in range(1, N+1)}
    distance[start] = 0     # distance[i]: start부터 i 정점까지의 최단거리
    pq = []
    heapify(pq)
    heappush(pq, (0, start))

    while pq:
        w, u = heappop(pq)
        for weight, nu in graph[u]:
            updated_dist = distance[u] + weight
            if distance[nu] > updated_dist:
                distance[nu] = updated_dist
                heappush(pq, (updated_dist, nu))
    
    return distance[end]


N, E = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))     # s: 시작점, (w, e): (가중치, 연결점)
    graph[e].append((w, s))     # 무향 그래프

v1, v2 = map(int, input().split())

# 1. 경로 순서 1 -> v1 -> v2 -> N 의 최단경로
result1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
# 2. 경로 순서 1 -> v2 -> v1 -> N 의 최단경로
result2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

ans = min(result1, result2)

if ans < INF:
    print(ans)
else:
    print(-1)