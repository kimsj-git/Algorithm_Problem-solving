from itertools import combinations as C
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

minDiff = float('inf')
for nums in C(range(N), N//2):
    team1 = []
    team2 = []
    for num in range(N):
        if num in nums:
            team1.append(num)
        else:
            team2.append(num)
    
    add1 = add2 = 0
    for pair in C(team1, 2):
        i, j = pair
        add1 += arr[i][j] + arr[j][i]
    for pair in C(team2, 2):
        i, j = pair
        add2 += arr[i][j] + arr[j][i]
    
    diff = abs(add1 - add2)
    if diff < minDiff:
        minDiff = diff

print(minDiff)