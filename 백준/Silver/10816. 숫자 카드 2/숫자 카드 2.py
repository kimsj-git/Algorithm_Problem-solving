import sys, bisect
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

cards.sort()

result = []
for num in nums:
    lower_bound = bisect.bisect_left(cards, num)
    upper_bound = bisect.bisect_right(cards, num)
    result.append(upper_bound - lower_bound)

print(*result)