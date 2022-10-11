N, M = map(int, input().split())
S = [input() for _ in range(N)]
cnt = 0
for _ in range(M):
    word = input()
    if word in S:
        cnt += 1
print(cnt)