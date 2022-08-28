N = int(input())
fish = [list(map(int, input().split())) for _ in range(N)]


# 다음에 먹을 물고기의 좌표(w)와 거리(nearest)를 반환하는 함수
# 조건: 1)최소거리, 2)위, 왼쪽 순서로 우선
def nearest_fish(arr, n, start, shark_size):
    queue = [start]
    distance = [[None] * n for _ in range(n)]   # 거리 함수
    distance[start[0]][start[1]] = 0
    nearest = 0     # 가장 가까운 거리
    edible = []     # 먹을 수 있는 물고기 좌표 저장

    # BFS 탐색
    while queue:
        v = queue.pop(0)
        dij = [[-1, 0], [0, -1], [0, 1], [1, 0]] # 상좌우하 델타이동
        for di, dj in dij:
            w = [v[0] + di, v[1] + dj]  # 주변 좌표
            if (0 <= w[0] < N and 0 <= w[1] < N and distance[w[0]][w[1]] == None):
                # 물고기 없으면: 지나감
                if arr[w[0]][w[1]] == 0:
                    queue.append(w)
                    distance[w[0]][w[1]] = distance[v[0]][v[1]] + 1
                # 큰 물고기: 못지나감(큐에 추가x), 못먹음
                elif arr[w[0]][w[1]] > shark_size:
                    continue
                # 같은 물고기: 지나감, 못먹음
                elif arr[w[0]][w[1]] == shark_size:
                    queue.append(w)
                    distance[w[0]][w[1]] = distance[v[0]][v[1]] + 1
                # 작은 물고기: 먹을 수 있음
                elif 0 < arr[w[0]][w[1]] < shark_size:
                    queue.append(w)
                    distance[w[0]][w[1]] = distance[v[0]][v[1]] + 1
                    
                    edible.append(w)
                    # nearest에 처음으로 저장되는 값이 최소거리(BFS 탐색)
                    if nearest == 0:
                        nearest = distance[w[0]][w[1]]
    
    # <중요> edible에 포함된 좌표를 정렬해줘야, 순서 조건을 만족할 수 있음
    edible.sort()
    for fish in edible:
        if distance[fish[0]][fish[1]] == nearest:
            return fish, nearest
    return False, False


# 먹을 수 있는 물고기 다 찾기까지 걸리는 시간을 반환하는 함수
def sorted_BFS_shark(arr, n, shark):
    result = 0  # 총 시간
    size = 2    # 아기상어 크기
    ate = 0     # 먹은 개수
    arr[shark[0]][shark[1]] = 0
    
    queue = [shark]
    while queue:
        v = queue.pop(0)    # 현재 상어 좌표
        w, time = nearest_fish(arr, n, v, size)   # 다음 먹을 물고기 위치, 걸리는 시간
        
        # 먹을 물고기가 물고기가 없다면, 결과 반환
        if not w:
            return result

        # 아기상어 크기 체크
        ate += 1
        if ate == size:
            size += 1
            ate = 0
        
        # 먹은 후: 시간 체크, 먹은 위치부터 다시 while문 시작
        result += time  # 총 시간 체크
        arr[w[0]][w[1]] = 0         # 먹은 물고기 제거
        queue = [w]                 # 큐 초기화
    return result


# 아기상어 최초 위치 찾기
is_shark = False
for i in range(N):
    for j in range(N):
        if fish[i][j] == 9:
            shark = [i, j]
            is_shark = True
            break
    if is_shark:
        break

print(sorted_BFS_shark(fish, N, shark))