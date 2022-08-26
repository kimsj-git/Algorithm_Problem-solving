T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    
    # N: 행, M: 열
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        arr[i][j] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            # 1이면, 인접한 배추 다 뽑기
            if arr[i][j] == 1:
                count += 1      # 지렁이 추가
                
                # BFS 이용, 인접 배추 다 뽑기
                v = (i, j)
                queue = []
                queue.append(v)
                arr[v[0]][v[1]] = 0   # 배추뽑
                while queue:
                    t = queue.pop(0)    # 현재 위치 t
                    # 인접 배추 좌표 w
                    dij = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                    for di, dj in dij:
                        w = (t[0] + di, t[1] + dj)
                        if w[0] < 0 or w[0] >= N or w[1] < 0 or w[1] >= M:
                            continue
                        if arr[w[0]][w[1]] == 1:
                            queue.append(w)
                            arr[w[0]][w[1]] = 0    # 배추뽑
    print(count)