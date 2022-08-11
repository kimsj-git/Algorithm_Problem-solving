for _ in range(1, 11):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    # 델타이동: 좌, 우, 상
    dij = [[0, -1], [0, 1], [-1, 0]]

    i = j = 0
    for end in range(100):
        if data[99][end] == 2:
            i = 99
            j = end

    while i > 0:
        for k in range(3):          # 좌, 우, 상 순서로 이동해보기
            ni = i + dij[k][0]
            nj = j + dij[k][1]
            if 0 <= ni < 100 and 0 <= nj < 100 and data[ni][nj] == 1:
                data[i][j] = 0      # 왔던 길 지우기
                i, j = ni, nj

    print(f'#{tc} {j}')