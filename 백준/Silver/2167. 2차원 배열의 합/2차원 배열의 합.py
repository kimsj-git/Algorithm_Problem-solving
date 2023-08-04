import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

"""
arr
1 2 3
4 5 6
7 8 9

acc
0 0  0  0
0 1  3  6
0 5  12 21
0 12 27 45
"""

acc = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        acc[i][j] = acc[i][j - 1] + acc[i - 1][j] - acc[i - 1][j - 1] + arr[i - 1][j - 1]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(acc[x][y] - acc[x][j-1] - acc[i-1][y] + acc[i-1][j-1])
