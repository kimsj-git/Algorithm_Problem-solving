from collections import deque
N, K = map(int, input().split())
visited = set()


def BFS(n, cnt):
    q = deque([(n, cnt)])
    visited.add(n)

    while q:
        n, cnt = q.popleft()
        if n == K:
            return cnt
        
        if 0 <= n - 1 <= 100000 and n - 1 not in visited:
            q.append((n - 1, cnt + 1))
            visited.add(n - 1)
        if 0 <= n + 1 <= 100000 and n + 1 not in visited:
            q.append((n + 1, cnt + 1))
            visited.add(n + 1)
        if 0 <= 2 * n <= 100000 and 2 * n not in visited:
            q.append((2 * n, cnt + 1))
            visited.add(2 * n)


print(BFS(N, 0))