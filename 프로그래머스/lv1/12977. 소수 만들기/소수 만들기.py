import math
from itertools import combinations

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    cnt = 0
    for comb in combinations(nums, 3):
        if is_prime(sum(comb)):
            cnt += 1

    return cnt