import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = {i: [] for i in range(N)}
visited = [False] * 2001

flag = False
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(v, depth):
    # print('Print', v, depth)
    global flag
    visited[v] = True
    if depth == 4:
        flag = True
        return
    for w in graph[v]:
        if not visited[w]:
            visited[w] = True
            DFS(w, depth + 1)
            visited[w] = False

for i in range(N):
    DFS(i, 0)
    visited[i] = False
    if flag:
        print(1)
        break
else:
    print(0)