import sys
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N+1):
    graph[i][i] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = []
for i in range(1, N+1):
    result.append((sum(graph[i][1:]), i))

result.sort(key=lambda x: [x[0], x[1]])
print(result[0][1])