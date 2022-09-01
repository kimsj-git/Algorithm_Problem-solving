K = int(input())
sides = [list(map(int, input().split())) for _ in range(6)]

max_row = 0     # 최대 가로 길이
max_col = 0     # 최대 세로 길이
max_row_idx = 0 # 최대 가로 길이의 인덱스
max_col_idx = 0 # 최대 세로 길이의 인덱스

for i in range(6):
    if sides[i][0] in [1, 2]:
        if sides[i][1] > max_row:
            max_row = sides[i][1]
            max_row_idx = i
    elif sides[i][0] in [3, 4]:
        if sides[i][1] > max_col:
            max_col = sides[i][1]
            max_col_idx = i

del_col = abs((sides[(max_row_idx - 1) % 6][1]) - (sides[(max_row_idx + 1) % 6][1]))
del_row = abs((sides[(max_col_idx - 1) % 6][1]) - (sides[(max_col_idx + 1) % 6][1]))

area = max_row * max_col - del_row * del_col
print(area * K)