from heapq import *

N, K = map(int, input().split())


def BFS(n, cnt):
    pq = []
    heappush(pq, (cnt, n))
    visited = set()
    visited.add(n)

    while pq:
        cnt, n = heappop(pq)
        if n == K:
            return cnt
        
        if 0 <= 2 * n <= 100000 and 2 * n not in visited:
            heappush(pq, (cnt, 2 * n))
            visited.add(2 * n)
        for i in [n - 1, n + 1]:
            if 0 <= i <= 100000 and i not in visited:
                heappush(pq, (cnt + 1, i))
                visited.add(i)


print(BFS(N, 0))