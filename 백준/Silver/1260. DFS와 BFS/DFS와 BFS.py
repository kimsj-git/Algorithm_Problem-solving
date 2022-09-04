from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = 1
    graph[n2][n1] = 1

# DFS
visited = [False] * (N+1)
stack = [V]
dfs = []
while stack:
    v = stack.pop()
    if not visited[v]:
        visited[v] = True
        dfs.append(v)
        for w in range(N, 0, -1):
            if graph[v][w] and not visited[w]:
                stack.append(w)

# BFS
visited = [False] * (N+1)
queue = deque([V])
visited[V] = True
bfs = [V]
while queue:
    v = queue.popleft()
    for w in range(1, N+1):
        if graph[v][w] and not visited[w]:
            visited[w] = True
            queue.append(w)
            bfs.append(w)

print(*dfs, sep=' ')
print(*bfs, sep=' ')