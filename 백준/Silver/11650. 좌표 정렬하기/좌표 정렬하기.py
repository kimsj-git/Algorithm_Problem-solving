import sys
input = sys.stdin.readline

N = int(input())
dots = [list(map(int, input().split())) for _ in range(N)]

dots.sort()

for dot in dots:
    print(*dot)