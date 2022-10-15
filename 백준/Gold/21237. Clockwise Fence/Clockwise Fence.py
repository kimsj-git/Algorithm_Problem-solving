import sys
input = sys.stdin.readline
'''
ccw[이전방향][현재방향]: CCW이면 1, CW이면 -1
경로의 ccw 값을 모두 더했을 때 CCW이면 3, CW이면 -3이 된다.
   N  E  S  W
N  0 -1  0  1
E  1  0 -1  0
S  0  1  0 -1
W -1  0  1  0
'''
dirs = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
ccw = [
    [0, -1, 0, 1],
    [1, 0, -1, 0],
    [0, 1, 0, -1],
    [-1, 0, 1, 0]
]

N = int(input())
for _ in range(N):
    cnt = 0
    path = input().rstrip()
    for i in range(1, len(path)):
        cnt += ccw[dirs[path[i-1]]][dirs[path[i]]]
    # cnt가 3이면 CCW, -3이면 CW
    if cnt > 0:
        print('CCW')
    else:
        print('CW')