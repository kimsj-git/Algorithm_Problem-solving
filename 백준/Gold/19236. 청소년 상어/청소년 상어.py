import sys
import copy
input = sys.stdin.readline

drc = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

arr = [[0] * 4 for _ in range(4)]   # 물고기 배치. (fish, direction): 물고기 번호, 방향. 0: 빈자리, -1: 상어 
fish_list = [0] * 17                # 물고기 정보. fish_list[i]: i번 물고기의 (방향, r, c) 저장

for r in range(4):
    row = list(map(int, input().split()))
    for c in range(4):
        fish = row[2 * c]
        direction = row[2 * c + 1] - 1
        arr[r][c] = (fish, direction)
        fish_list[fish] = (direction, r, c)


# 물고기 이동 함수
def move_fish(arr, fish_list):
    # 1. i: 물고기 번호, 1 ~ 16번 순회
    for i in range(1, 17):
        if fish_list[i]:
            dir, r, c = fish_list[i]
            
            # 2. 반시계 방향으로 45도 회전하며 이동 가능한 위치 찾기
            for j in range(8):
                ndir = (dir + j) % 8
                dr, dc = drc[ndir]
                nr, nc = r + dr, c + dc
                if 0 <= nr < 4 and 0 <= nc < 4 and arr[nr][nc] != -1:
                    # 3-1. 물고기 없는 칸
                    if arr[nr][nc] == 0:
                        arr[nr][nc] = (i, ndir)
                        arr[r][c] = 0
                        fish_list[i] = (ndir, nr, nc)
                    # 3-2. 물고기 있는 칸: 교환
                    else:
                        other_fish, other_dir = arr[nr][nc]
                        # 물고기 배치도 업데이트
                        arr[r][c] = arr[nr][nc]
                        arr[nr][nc] = (i, ndir)
                        # 물고기 정보 업데이트
                        fish_list[other_fish] = (other_dir, r, c)
                        fish_list[i] = (ndir, nr, nc)
                    break


# 상어 이동 DFS
initial_fish, initial_direction = arr[0][0]
maxV = initial_fish     # 상어가 먹은 물고기 합의 최대값. 초기값은 처음 먹은 물고기 번호
arr[0][0] = -1          # 상어 위치 체크
fish_list[initial_fish] = 0     # 처음 먹힌 물고기 체크


def move_shark(v, arr, fish_list):
    global maxV

    # 1. 물고기 움직이기
    move_fish(arr, fish_list)
    
    # 2. 상어 움직이기
    sum_fish, dir, r, c = v
    dr, dc = drc[dir]
    arr[r][c] = 0      # 상어 위치 해제

    # 2-1. 상어가 이동할 수 있는 위치들 확인
    next_spots = []
    while True:
        r += dr
        c += dc
        if 0 <= r < 4 and 0 <= c < 4:
            if arr[r][c] != 0:
                next_spots.append((r, c))
        else:
            break
    
    # 2-2. 상어 이동
    for w in next_spots:
        nr, nc = w                  # 이동할 위치
        fish, ndir = arr[nr][nc]    # 잡아먹힐 물고기 정보
        sum_fish += fish
        
        # 바뀐 정보를 기록하기 위해 deepcopy 이용
        new_arr = copy.deepcopy(arr)
        new_fish_list = copy.deepcopy(fish_list)

        new_arr[nr][nc] = -1    # 상어 위치 체크
        new_fish_list[fish] = 0 # 잡아 먹힌 물고기 체크
        # 2-3. 재귀적으로 탐색
        move_shark((sum_fish, ndir, nr, nc), new_arr, new_fish_list)
        
        # 2-4. 최대값 갱신
        if maxV < sum_fish:
            maxV = sum_fish
        
        # 2-5. 다른 위치로 이동 전 초기화
        sum_fish -= fish


move_shark((initial_fish, initial_direction, 0, 0), arr, fish_list)
print(maxV)