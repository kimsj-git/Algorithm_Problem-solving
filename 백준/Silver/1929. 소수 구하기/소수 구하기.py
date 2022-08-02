import sys
input = sys.stdin.readline

def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        prime = True
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                prime = False
                break
        return prime

M, N = map(int, input().split())

for i in range (M, N+1):
    if is_prime(i):
        print(i)
