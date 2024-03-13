from itertools import permutations


def is_prime(x):
    if x == 0 or x == 1:
        return False
    if x == 2:
        return True
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            return False
    return True


def solution(numbers):
    n = len(numbers)
    prime_numbers = set([])
    for i in range(1, 1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(numbers[j])
        for permu in permutations(subset, len(subset)):
            num = int(''.join(permu))
            if is_prime(num):
                prime_numbers.add(num)
    return len(prime_numbers)