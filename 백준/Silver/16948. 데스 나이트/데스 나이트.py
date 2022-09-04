def BFS(n, start, end):
    count = [[None] * n for _ in range(n)]
    queue = [start]
    count[start[0]][start[1]] = 0
    if start == end:
        return 0
    while queue:
        v = queue.pop(0)
        drc = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
        for dr, dc in drc:
            w = [v[0] + dr, v[1] + dc]
            if 0 <= w[0] < n and 0 <= w[1] < n and not count[w[0]][w[1]]:
                queue.append(w)
                count[w[0]][w[1]] = count[v[0]][v[1]] + 1
                if w == end:
                    return count[w[0]][w[1]]
    return -1


N = int(input())
r1, c1, r2, c2 = map(int, input().split())

print(BFS(N, [r1, c1], [r2, c2]))