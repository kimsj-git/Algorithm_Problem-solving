import sys
input = sys.stdin.readline

def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        prime = True
        for i in range(2, x):
            if x % i == 0:
                prime = False
                break
        return prime

M = int(input())
N = int(input())

primes = []
for i in range(M, N+1):
    if is_prime(i):
        primes.append(i)

if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)