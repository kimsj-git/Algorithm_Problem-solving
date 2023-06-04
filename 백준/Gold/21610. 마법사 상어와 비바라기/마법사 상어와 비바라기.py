import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(M)]

drc = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def cycle(clouds: list, i: int):
    if i == M:
        return
    di, si = moves[i]   # di: 방향 종류, si: 이동거리
    dr, dc = drc[di - 1]

    # 1. 비 내리기
    rain_spots = []
    visited = [[False] * N for _ in range(N)]
    for r, c in clouds:
        # 1-1. 구름 칸 이동
        r = (r + dr * si) % N
        c = (c + dc * si) % N
        # 1-2. 이동 후 연산
        arr[r][c] += 1
        rain_spots.append((r, c))
        visited[r][c] = True
    
    # 2. 물복사 버그
    for r, c in rain_spots:
        for dr, dc in diag:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] > 0:
                arr[r][c] += 1
    
    # 3. 구름 생성
    new_clouds = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] >= 2 and not visited[r][c]:
                arr[r][c] -= 2
                new_clouds.append((r, c))

    cycle(new_clouds, i + 1)
    

cycle([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)], 0)
print(sum(sum(arr, start=[])))
