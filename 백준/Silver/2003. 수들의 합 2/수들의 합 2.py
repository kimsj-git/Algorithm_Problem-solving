'''
투포인터 문제
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

s = 0
e = 1
cnt = 0
subsum = A[0]
while True:
    if subsum < M:
        if e < N:
            subsum += A[e]
            e += 1
        else:
            break
    elif subsum == M:
        cnt += 1
        subsum -= A[s]
        s += 1
    else:
        subsum -= A[s]
        s += 1

print(cnt) 