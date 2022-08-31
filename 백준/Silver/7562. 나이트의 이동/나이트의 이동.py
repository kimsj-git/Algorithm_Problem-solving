# BFS 함수: 체스판 한 변 길이(n), 시작점(start), 종점(end) 받아서
# 최소 이동 횟수 반환
def BFS(n, start, end):
    count = [[None] * n for _ in range(n)]
    queue = [start]
    count[start[0]][start[1]] = 0

    while queue:
        v = queue.pop(0)
        if v == end:
            return count[v[0]][v[1]]
        dij = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
        for di, dj in dij:
            w = [v[0]+di, v[1]+dj]
            if 0 <= w[0] < n and 0 <= w[1] < n and not count[w[0]][w[1]]:
                queue.append(w)
                count[w[0]][w[1]] = count[v[0]][v[1]] + 1
                if w == end:
                    return count[w[0]][w[1]]


T = int(input())
for tc in range(T):
    l = int(input())    # 체스판 한 변의 길이
    knight_start = list(map(int, input().split()))
    knight_end = list(map(int, input().split()))

    print(BFS(l, knight_start, knight_end))