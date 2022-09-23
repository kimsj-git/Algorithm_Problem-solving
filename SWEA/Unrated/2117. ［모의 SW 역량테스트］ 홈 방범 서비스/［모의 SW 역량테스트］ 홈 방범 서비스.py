def find(x, y, k):
    cnt = 0
    for dx in range(-k + 1, k):
        for dy in range(-k + 1, k):
            nx = x + dx
            ny = y + dy
            if abs(dx) + abs(dy) < k and 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for K in range(1, N+2):
        cnt_max = 0
        for i in range(N):
            for j in range(N):
                cnt_temp = find(i, j, K)
                if cnt_temp > cnt_max:
                    cnt_max = cnt_temp

        margin = M * cnt_max - (K*K + (K-1)*(K-1))
        
        if margin >= 0 and cnt_max > result:
            result = cnt_max

    print(f'#{tc} {result}')