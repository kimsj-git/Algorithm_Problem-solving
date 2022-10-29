def DFS(i, j, turn):
    global maxV
    visited.append(cafe[i][j])

    if turn == 0:
        dij = [[1, -1], [1, 1]]
    elif turn == 1:
        dij = [[1, 1], [-1, 1]]
    elif turn == 2:
        dij = [[-1, 1], [-1, -1]]
    elif turn == 3:
        dij = [[-1, -1]]

    for k in range(len(dij)):
        w = [i + dij[k][0], j + dij[k][1]]

        if w[0] == i_start and w[1] == j_start:
            if len(visited) > maxV:
                maxV = len(visited)
            return

        if 0 <= w[0] < N and 0 <= w[1] < N and cafe[w[0]][w[1]] not in visited:
            DFS(w[0], w[1], turn + k)
            visited.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    maxV = -1
    for i_start in range(N):
        for j_start in range(N):
            visited = []
            DFS(i_start, j_start, 0)
    
    print(f'#{tc} {maxV}')