import sys

input = sys.stdin.readline

V, E = map(int, input().split())

INF = float("inf")
graph = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    s, e, d = map(int, input().split())
    graph[s][e] = d

for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_cycle = INF
for i in range(1, V + 1):
    min_cycle = min(min_cycle, graph[i][i])

if min_cycle == INF:
    print(-1)
else:
    print(min_cycle)
