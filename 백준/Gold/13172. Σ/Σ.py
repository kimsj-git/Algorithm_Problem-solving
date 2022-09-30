import math
M = int(input())
dices = [list(map(int, input().split())) for _ in range(M)]
BIG = 1000000007


def recursive_power(x, n, c):
    if n == 1:
        return x % c
    if n % 2 == 0:
        temp = recursive_power(x, n//2, c)
        return (temp**2) % c
    else:
        temp = recursive_power(x, n//2, c)
        return (temp**2 * x) % c


result = 0
for n, s in dices:
    GCD = math.gcd(n, s)
    n //= GCD
    s //= GCD
    
    rn_mod = recursive_power(n, BIG - 2, BIG)
    s_mod = s % BIG
    
    expectation = (s_mod * rn_mod) % BIG
    result += expectation

print(result % BIG)