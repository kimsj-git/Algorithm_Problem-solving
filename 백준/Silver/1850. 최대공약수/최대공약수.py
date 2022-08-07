import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

A, B = map(int, input().split())
digits = gcd(A, B)
result = ''
for _ in range(digits):
    result += '1'
print(result)
