import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
r = c = N // 2  # 시작 좌표

drc = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 좌하우상 델타이동


def move_sand(arr, tr, tc, dir):
    """
    토네이도 한칸 이동 후 상태 반환.
    반환값: 1) 변화한 모래 격자(arr), 2) 격자 밖으로 나간 모래 양(sand_out)
    """
    dr, dc = drc[dir]
    sand = arr[tr + dr][tc + dc]  # 모래 양
    arr[tr + dr][tc + dc] = 0

    sand_out = 0
    moved_sand = 0

    points = []
    # 1% 좌표
    r1, c1 = (tr, tc - 1) if dr else (tr - 1, tc)
    r2, c2 = (tr, tc + 1) if dr else (tr + 1, tc)
    points += [(r1, c1, 0.01), (r2, c2, 0.01)]
    # 2% 좌표
    r3, c3 = (tr + dr, tc - 2) if dr else (tr - 2, tc + dc)
    r4, c4 = (tr + dr, tc + 2) if dr else (tr + 2, tc + dc)
    points += [(r3, c3, 0.02), (r4, c4, 0.02)]
    # 7% 좌표
    r5, c5 = (tr + dr, tc - 1) if dr else (tr - 1, tc + dc)
    r6, c6 = (tr + dr, tc + 1) if dr else (tr + 1, tc + dc)
    points += [(r5, c5, 0.07), (r6, c6, 0.07)]
    # 10% 좌표
    r7, c7 = (tr + 2 * dr, tc - 1) if dr else (tr - 1, tc + 2 * dc)
    r8, c8 = (tr + 2 * dr, tc + 1) if dr else (tr + 1, tc + 2 * dc)
    points += [(r7, c7, 0.1), (r8, c8, 0.1)]
    # 5% 좌표
    r9, c9 = (tr + 3 * dr, tc) if dr else (tr, tc + 3 * dc)
    points += [(r9, c9, 0.05)]
    # alpha 좌표
    ra, ca = (tr + 2 * dr, tc) if dr else (tr, tc + 2 * dc)

    for r, c, ratio in points:
        if 0 <= r < N and 0 <= c < N:
            arr[r][c] += int(sand * ratio)
        else:
            sand_out += int(sand * ratio)
        moved_sand += int(sand * ratio)

    if 0 <= ra < N and 0 <= ca < N:
        arr[ra][ca] += sand - moved_sand
    else:
        sand_out += sand - moved_sand

    return (arr, sand_out)


sand_total = 0
for i in range(1, N):
    if i % 2:
        # 1. i칸 좌측 이동, i칸 하측 이동
        for dir in [0, 1]:
            for _ in range(i):
                arr, sand_out = move_sand(arr, r, c, dir)
                sand_total += sand_out
                dr, dc = drc[dir]
                r += dr
                c += dc

    else:
        # 2. i칸 우측 이동, i칸 상측 이동
        for dir in [2, 3]:
            for _ in range(i):
                arr, sand_out = move_sand(arr, r, c, dir)
                sand_total += sand_out
                dr, dc = drc[dir]
                r += dr
                c += dc

# 3. (N-1)칸 좌측 이동
for _ in range(N - 1):
    arr, sand_out = move_sand(arr, r, c, 0)
    sand_total += sand_out
    dr, dc = drc[0]
    r += dr
    c += dc

print(sand_total)
