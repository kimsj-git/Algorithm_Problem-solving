import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    R, C = map(int, input().split())
    if R > C:
        R, C = C, R
    white = (R*(R+1)*(C-R)//2 + R*(R+1)*(2*R+1)//6) * 2 - R*C
    dark = white - R
    print(white, dark)