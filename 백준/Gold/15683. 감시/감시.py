import sys
from copy import deepcopy
input = sys.stdin.readline

# 상하좌우 델타이동
u, d, l, r = (-1, 0), (1, 0), (0, -1), (0, 1)
# CCTV 종류에 따른 감시방향들 (dirs[i]: i번 CCTV의 감시방향들)
dirs = {
    1: [[u], [d], [l], [r]],
    2: [[u, d], [l, r]],
    3: [[u, r], [u, l], [d, r], [d, l]],
    4: [[u, l, r], [d, l, r], [u, d, l], [u, d, r]],
    5: [[u, d, l, r]]
}

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cctvs = []      # 각 CCTV의 종류, 좌표 저장
for i in range(N):
    for j in range(M):
        if arr[i][j] in range(1, 6):
            cctvs.append([arr[i][j], (i, j)])

minV = N * M    # 사각지대 최소값 저장
zeros = 0       # 사각지대 초기값(arr에서 0의 개수)
for row in arr:
    zeros += row.count(0)


def DFS(i, result, arr):
    '''
    모든 CCTV의 모든 감시방향에 대해 재귀적으로 탐색하여 minV 갱신.
    i: CCTV 순서, result: 사각지대 개수, arr: 사무실 상태
    '''
    global minV
    
    # 2. 마지막 CCTV까지 처리한 경우
    if i == len(cctvs):
        # 2-1. minV 갱신
        if result < minV:
            minV = result
        # 2-2. 이전 단계 DFS로 돌아감
        return
    
    cctv = cctvs[i]     # 조작할 CCTV
    cctv_num = cctv[0]  # CCTV 종류
    
    # 1. 하나의 감시 방향에 대해 사무실 상태 변경 후 다음 CCTV로 DFS 이동
    for dir in dirs[cctv_num]:
        # 1-1. deepcopy를 통해 "현재 사무실 상태"를 저장
        arr_copy = deepcopy(arr)
        temp = result
        # 1-2. 사무실 상태 변경
        for drc in dir:
            r, c = cctv[1][0], cctv[1][1]
            dr, dc = drc
            nr, nc = r + dr, c + dc
            while 0 <= nr < N and 0 <= nc < M and arr_copy[nr][nc] != 6:
                if arr_copy[nr][nc] == 0:
                    arr_copy[nr][nc] = 9
                    temp -= 1
                nr += dr
                nc += dc         
        # 1-3. 다음 CCTV로 DFS 이동
        DFS(i+1, temp, arr_copy)


DFS(0, zeros, arr)
print(minV)