import sys
from collections import deque

sys.setrecursionlimit(10**4)
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def fire_storm(arr: list[list[int]], end_cnt: int, cnt: int, L: list):
    """
    end_cnt회 파이어스톰 시전하는 함수.
    """
    global result

    if cnt == end_cnt:
        result = arr
        return

    n = 2 ** L[cnt]  # 부분 배열 한 변의 길이

    # 1. 부분 격자 90도 회전한 배열 구하기
    turn_arr = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for start_r in range(0, 2**N, n):
        for start_c in range(0, 2**N, n):
            # dr, dc는 start_r, start_c로부터의 차이값
            for dr in range(n):
                for dc in range(n):
                    # 회전 전 좌표 (r, c)
                    r = start_r + dr
                    c = start_c + dc

                    # 회전 후 좌표 (nr, nc)
                    ndr, ndc = dc, n - 1 - dr
                    nr = start_r + ndr
                    nc = start_c + ndc

                    # 회전 후 좌표의 배열 값을 회전 전 좌표의 배열 값으로 저장
                    turn_arr[nr][nc] = arr[r][c]

    # 2. 얼음 녹인 후의 배열 구하기
    melt_arr = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for r in range(2**N):
        for c in range(2**N):
            if turn_arr[r][c] == 0:
                melt_arr[r][c] = 0
                continue

            ice_cnt = 0
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 2**N and 0 <= nc < 2 ** N and turn_arr[nr][nc]:
                    ice_cnt += 1
            if ice_cnt >= 3:
                melt_arr[r][c] = turn_arr[r][c]
            else:
                melt_arr[r][c] = turn_arr[r][c] - 1

    fire_storm(melt_arr, end_cnt, cnt + 1, L)


def ice_size_bfs(arr):
    max_cnt = 0
    for r in range(2**N):
        for c in range(2**N):
            if arr[r][c]:
                ice_cnt = 1
                q = deque([(r, c)])
                visited = [[False] * 2**N for _ in range(2**N)]
                visited[r][c] = True
                arr[r][c] = 0
                while q:
                    vr, vc = q.popleft()
                    for dr, dc in drc:
                        nr, nc = vr + dr, vc + dc
                        if 0 <= nr < 2**N and 0 <= nc < 2 ** N and arr[nr][nc]:
                            ice_cnt += 1
                            q.append((nr, nc))
                            arr[nr][nc] = 0
                max_cnt = max(ice_cnt, max_cnt)
    return max_cnt


result = []
fire_storm(arr, Q, 0, L)

print(sum(sum(result, start=[])))
print(ice_size_bfs(result))
