from heapq import *
import sys
input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]

heapify(cards)

cnt = 0
for _ in range(N-1):
    num1 = heappop(cards)
    num2 = heappop(cards)
    cnt += num1 + num2
    heappush(cards, num1 + num2)

print(cnt)