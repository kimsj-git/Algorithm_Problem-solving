import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return int(x*y / gcd(x, y))

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))