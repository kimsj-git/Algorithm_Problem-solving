import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = float("inf")


class CityPath:
    def __init__(self):
        self.cost = INF
        self.cities = []


graph = [[CityPath() for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s][e].cost = min(graph[s][e].cost, cost)
    graph[s][e].cities = [s, e]

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b].cost > graph[a][k].cost + graph[k][b].cost:
                graph[a][b].cost = graph[a][k].cost + graph[k][b].cost
                graph[a][b].cities = graph[a][k].cities[:-1] + graph[k][b].cities

for i in range(1, n + 1):
    costs = []
    for j in range(1, n + 1):
        if i == j or graph[i][j].cost == INF:
            costs.append(0)
        else:
            costs.append(graph[i][j].cost)
    print(*costs)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j or graph[i][j].cost == INF:
            print(0)
        else:
            print(len(graph[i][j].cities), *graph[i][j].cities)
