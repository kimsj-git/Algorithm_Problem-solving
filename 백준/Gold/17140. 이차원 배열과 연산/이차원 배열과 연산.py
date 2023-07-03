import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]


def change_row(arr):
    # 1. 수의 등장 횟수, 수의 크기 순으로 정렬
    for i, row in enumerate(arr):
        nums_cnt = {}
        for num in row:
            if nums_cnt.get(num):
                nums_cnt[num] += 1
            else:
                nums_cnt[num] = 1
        sorted_nums = sorted(nums_cnt.items(), key=lambda item: [item[1], item[0]])
        arr[i] = []
        for num, cnt in sorted_nums:
            if num > 0:
                arr[i] += [num, cnt]
        if len(arr[i]) > 100:
            arr[i] = arr[i][:100]

    # 2. 가장 큰 행을 기준으로 모든 행의 크기 변경
    max_row = max([len(arr[i]) for i in range(len(arr))])
    for row in arr:
        row += [0] * (max_row - len(row))

    return arr


def transpose(arr):
    R = len(arr)
    C = len(arr[0])
    transposed_arr = [[0] * R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            transposed_arr[c][r] = arr[r][c]

    return transposed_arr


def change_col(arr):
    transposed_arr = transpose(arr)
    change_row(transposed_arr)

    return transpose(transposed_arr)


def cycle(time, arr):
    global answer

    R, C = len(arr), len(arr[0])
    if 0 <= r - 1 < R and 0 <= c - 1 < C and arr[r - 1][c - 1] == k:
        answer = time
        return
    if time > 100:
        return

    if R >= C:
        cycle(time + 1, change_row(arr))
    else:
        cycle(time + 1, change_col(arr))


answer = -1
cycle(0, arr)
print(answer)
