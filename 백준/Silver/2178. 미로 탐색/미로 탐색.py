N, M = map(int, input().split())

maze = [input() for _ in range(N)]
distance = [[None] * M for _ in range(N)]

queue = [[0, 0]]
distance[0][0] = 0
result = 0
is_found = False
while queue:
    v = queue.pop(0)
    dij = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우 델타이동
    for di, dj in dij:
        w = [v[0]+di, v[1]+dj]
        if 0 <= w[0] < N and 0 <= w[1] < M and distance[w[0]][w[1]] == None and maze[w[0]][w[1]] == '1':
            queue.append(w)
            distance[w[0]][w[1]] = distance[v[0]][v[1]] + 1
        if w[0] == N-1 and w[1] == M-1:
            print(distance[w[0]][w[1]] + 1)
            is_found = True
            break
    if is_found:
        break