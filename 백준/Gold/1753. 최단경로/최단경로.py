import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = 10**7


def dijkstra(start):
    distance[start] = 0
    heapq.heappush(pq, (0, start))
    while pq:
        w, u = heapq.heappop(pq)
        for weight, nu in graph[u]:
            if distance[nu] > distance[u] + weight:
                distance[nu] = distance[u] + weight
                
                # 값이 갱신되면 (시작점으로부터 거리, 노드번호)를 우선순위큐에 추가
                heapq.heappush(pq, (distance[nu], nu))


graph = {i: [] for i in range(1, V+1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))     # w: 가중치, v: 연결 정점

distance = [INF] * (V+1)
pq = []

dijkstra(K)

for i in range(1, V+1):
    print('INF' if distance[i] == INF else distance[i])