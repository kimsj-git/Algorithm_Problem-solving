import sys
input = sys.stdin.readline

T = int(input())

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

numbers = list(map(int, input().split()))

prime_count = 0
for number in numbers:
    if is_prime(number):
        prime_count += 1

print(prime_count)