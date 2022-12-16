import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

result = []
cnt = 0
flag = False
for i in range(N-1, -1, -1):
    if A[i] == 0:
        result.append(B[i])
        cnt += 1
        if cnt == M:
            print(*result)
            flag = True
            break

if not flag:
    for i in range(M):
        result.append(C[i])
        cnt += 1
        if cnt == M:
            print(*result)
            break