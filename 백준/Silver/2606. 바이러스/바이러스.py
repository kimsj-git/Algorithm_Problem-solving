N = int(input())
M = int(input())
graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

# DFS
visited = [False] * (N+1)
stack = [1]
while stack:
    v = stack.pop()
    if not visited[v]:
        visited[v] = True
        for w in range(1, N+1):
            if graph[v][w] and not visited[w]:
                stack.append(w)

print(visited.count(True) - 1)