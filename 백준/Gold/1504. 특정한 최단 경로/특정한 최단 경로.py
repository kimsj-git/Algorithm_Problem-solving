from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start, *end):
    distance = {i: INF for i in range(1, N+1)}
    distance[start] = 0     # distance[i]: start부터 i 정점까지의 최단거리
    pq = []
    heappush(pq, (0, start))

    while pq:
        dist_now, u = heappop(pq)
        if distance[u] < dist_now:
            continue
        for weight, nu in graph[u]:
            updated_dist = distance[u] + weight
            if distance[nu] > updated_dist:
                distance[nu] = updated_dist
                heappush(pq, (updated_dist, nu))
    
    return tuple([distance[i] for i in end])


N, E = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))     # s: 시작점, (w, e): (가중치, 연결점)
    graph[e].append((w, s))     # 무향 그래프

v1, v2 = map(int, input().split())

# # 1. 경로 순서 1 -> v1 -> v2 -> N 의 최단경로
# result1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
# # 2. 경로 순서 1 -> v2 -> v1 -> N 의 최단경로
# result2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

# v1 -> 1, v1 -> v2, v1 -> N 을 구하기
d_v1_1, d_v1_v2, d_v1_N = dijkstra(v1, 1, v2, N)

# v2 -> 1, v2 -> N 을 구하기
d_v2_1, d_v2_N = dijkstra(v2, 1, N)

result1 = d_v1_1 + d_v1_v2 + d_v2_N
result2 = d_v2_1 + d_v1_v2 + d_v1_N

ans = min(result1, result2)

if ans < INF:
    print(ans)
else:
    print(-1)