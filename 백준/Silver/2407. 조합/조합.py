from math import factorial as fac
n, m = map(int, input().split())
print(fac(n) // fac(n-m) // fac(m))