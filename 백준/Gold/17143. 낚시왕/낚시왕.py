import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]

drc = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]  # 0 상 하 우 좌

arr = [[[] for _ in range(C)] for _ in range(R)]
is_shark = [True] * M
shark_data = {i: [] for i in range(M)}

for i, shark in enumerate(sharks):
    r, c, s, d, z = shark
    arr[r - 1][c - 1].append(i)
    shark_data[i] = [r - 1, c - 1, s, d, z]

shark_sum = 0
for fisher_c in range(C):
    # 1. 상어 잡기
    for fisher_r in range(R):
        if arr[fisher_r][fisher_c]:
            shark_idx = arr[fisher_r][fisher_c].pop()
            shark_sum += shark_data[shark_idx][4]
            is_shark[shark_idx] = False
            break

    # 2. 상어 이동
    for i in range(M):
        if is_shark[i]:
            sr, sc, speed, d, size = shark_data[i]
            arr[sr][sc].remove(i)
            dr, dc = drc[d]
            if dr:
                # 2-1. 상/하 이동하는 경우
                nc = sc
                cnt = (sr + dr * speed) // (R - 1)
                remain = (sr + dr * speed) % (R - 1)
                if cnt % 2:
                    nr = R - 1 - remain
                    nd = 2 if d == 1 else 1
                else:
                    nr = remain
                    nd = d
            else:
                # 2-2. 좌/우 이동하는 경우
                nr = sr
                cnt = (sc + dc * speed) // (C - 1)
                remain = (sc + dc * speed) % (C - 1)
                if cnt % 2:
                    nc = C - 1 - remain
                    nd = 4 if d == 3 else 3
                else:
                    nc = remain
                    nd = d
            arr[nr][nc].append(i)
            shark_data[i] = [nr, nc, speed, nd, size]

    # 3. 같은 자리에 있는 상어들 중 가장 큰 상어만 남기기
    for r in range(R):
        for c in range(C):
            if len(arr[r][c]) >= 2:
                # 3-1. 크기 가장 큰 상어를 그룹에서 제거
                shark_group = [[i] + shark_data[i] for i in arr[r][c]]
                shark_group.sort(key=lambda x: x[5])
                shark_group.pop()
                # 3-2. 남은 상어들의 is_shark 값 False로 변경
                for shark in shark_group:
                    i = shark[0]
                    is_shark[i] = False
                    arr[r][c].remove(i)

print(shark_sum)
