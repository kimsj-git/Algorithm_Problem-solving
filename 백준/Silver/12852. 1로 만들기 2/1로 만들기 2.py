from collections import deque
N = int(input())
visited = set()


def BFS(n, cnt, route):
    q = deque([(n, cnt, route)])
    while q:
        n, cnt, route = q.popleft()
        if n == 1:
            return cnt, route

        if n % 3 == 0 and 1 <= n // 3 and n // 3 not in visited:
            visited.add(n // 3)
            q.append((n // 3, cnt + 1, route + [n // 3]))
        if n % 2 == 0 and 1 <= n // 2 and n // 2 not in visited:
            visited.add(n // 2)
            q.append((n // 2, cnt + 1, route + [n //2]))
        if 1 <= n - 1 and n - 1 not in visited:
            visited.add(n - 1)
            q.append((n - 1, cnt + 1, route + [n - 1]))


cnt, route = BFS(N, 0, [N])
print(cnt)
print(*route)