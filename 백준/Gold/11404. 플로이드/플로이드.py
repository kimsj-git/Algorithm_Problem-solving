import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s][e] = min(cost, graph[s][e])

'''
플로이드-워셜 점화식
a->b 최단거리는 a->b 직접 연결한 거리와 k 노드를 거쳐가는 거리(a->k->b) 중 최단거리 
'''
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
    print(*graph[i][1:])