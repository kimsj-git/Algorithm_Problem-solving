import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return int(x*y / gcd(x, y))

A, B = map(int, input().split())
print(gcd(A, B))
print(lcm(A, B))