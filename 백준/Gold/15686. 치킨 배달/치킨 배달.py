import sys
from itertools import combinations as C
input = sys.stdin.readline


def dist(A, B):
    ar, ac = A
    br, bc = B
    return abs(ar - br) + abs(ac - bc)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

houses = []     # 가정집 좌표 리스트
chickens = []   # 치킨집 좌표 리스트

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

minSum = float('inf')
for combi in C(chickens, M):
    distSum = 0
    for house in houses:
        minD = 2 * N
        for chicken in combi:
            minD = min(minD, dist(house, chicken))
        distSum += minD
    minSum = min(minSum, distSum)

print(minSum)