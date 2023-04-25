import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

count = [0] * 7
for num in nums:
    if num % 7:
        count[num % 7] += 1


def is_health(count):
    if 6 <= sum(count[1:]):
        return True
    
    numbers = []
    for i in range(1, 7):
        numbers += [i] * count[i]

    n = len(numbers)
    for i in range(1, n + 1):
        for combi in combinations(numbers, i):
            if sum(combi) % 7 == 4:
                return True
            
    return False

if is_health(count):
    print("YES")
else:
    print("NO")