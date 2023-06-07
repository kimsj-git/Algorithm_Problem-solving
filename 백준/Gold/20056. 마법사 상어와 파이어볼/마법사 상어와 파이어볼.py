import sys

sys.setrecursionlimit(10**4)
input = sys.stdin.readline

N, M, K = map(int, input().split())
fires = [list(map(int, input().split())) for _ in range(M)]

for i, fire in enumerate(fires):
    r, c, m, s, d = fire
    fires[i][0] = r - 1
    fires[i][1] = c - 1

drc = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def move_fire(fires, cnt):
    global final_fires

    if cnt == K:
        final_fires = fires
        return

    # 1. 파이어볼 이동, 이동 후 위치 체크
    arr = [[[] for _ in range(N)] for _ in range(N)]
    for i, fire in enumerate(fires):
        r, c, m, s, d = fire
        dr, dc = drc[d]
        r = (r + dr * s) % N
        c = (c + dc * s) % N
        fires[i] = [r, c, m, s, d]
        arr[r][c].append(i)

    # 2. 이동 후 연산
    new_fires = []
    for r in range(N):
        for c in range(N):
            if len(arr[r][c]) >= 2:
                # 2-1. 합쳐진 후 생기는 파이어볼
                new_m = 0
                new_s = 0
                new_d = fires[arr[r][c][0]][4] % 2  # 첫번째 파이어볼의 방향의 홀짝
                d_flag = True  # 방향 홀짝이 모두 같으면 True, 아니면 False
                for i in arr[r][c]:
                    new_m += fires[i][2]
                    new_s += fires[i][3]
                    if fires[i][4] % 2 != new_d:
                        d_flag = False

                new_m //= 5
                new_s //= len(arr[r][c])
                new_d = 0 if d_flag else 1

                if new_m > 0:
                    for j in range(0, 7, 2):
                        new_fires.append([r, c, new_m, new_s, new_d + j])

            elif len(arr[r][c]) == 1:
                # 2-2. 합쳐지지 않은 파이어볼
                new_fires.append(fires[arr[r][c][0]])

    move_fire(new_fires, cnt + 1)


final_fires = []
move_fire(fires, 0)
ans = 0
for i in range(len(final_fires)):
    ans += final_fires[i][2]
print(ans)
