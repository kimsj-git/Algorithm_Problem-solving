import sys
input = sys.stdin.readline

N = int(input())
frames = [tuple(map(int, input().split())) for _ in range(N)]

result = []
for i in range(N):
    w, h = frames[i]
    cnt = 1
    for j in range(N):
        if j != i:
            nw, nh = frames[j]
            if w < nw and h < nh:
                cnt += 1
    result.append(cnt)

print(*result)