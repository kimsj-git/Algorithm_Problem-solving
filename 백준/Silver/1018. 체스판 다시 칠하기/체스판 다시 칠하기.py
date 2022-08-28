N, M = map(int, input().split())

# N행 M열 크기의 보드
board = [input() for _ in range(N)]
min_change = N*M
for i in range(N - 7):
    for j in range(M - 7):
        # (i, j) 좌표를 시작으로 하는 8*8 행렬을 순회
        count1 = 0  # 시작칸 흰색으로 칠하기
        count2 = 0  # 시작칸 검은색으로 칠하기
        for di in range(8):
            for dj in range(8):
                ni = i + di
                nj = j + dj
                if di%2 == dj%2:    # (0,0), (0,2), (1,3), ...
                    if board[ni][nj] == 'B':
                        count1 += 1
                    else:
                        count2 += 1
                else:               # (0,1), (1,0), ...
                    if board[ni][nj] == 'W':
                        count1 += 1
                    else:
                        count2 += 1
        temp = min(count1, count2)
        if temp < min_change:
            min_change = temp
print(min_change)