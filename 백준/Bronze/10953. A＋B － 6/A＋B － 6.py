import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    A, B = map(int, input().split(','))
    print(A+B)
