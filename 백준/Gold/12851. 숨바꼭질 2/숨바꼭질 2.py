from collections import deque
N, K = map(int, input().split())
visited = [-1] * 100001
count = [0] * 100001


def BFS(n):
    q = deque([n])
    visited[n] = 0
    
    while q:
        x = q.popleft()
        if x == K:
            count[x] += 1
        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx <= 100000 and (visited[nx] == -1 or visited[nx] >= visited[x] + 1):
                visited[nx] = visited[x] + 1
                q.append(nx)


BFS(N)
print(visited[K])
print(count[K])