from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    left = deque([])
    right = deque([])
    string = input().rstrip()
    for char in string:
        if char.isalpha() or char.isnumeric():
            left.append(char)
        elif char == '-' and left:
            left.pop()
        elif char == '<' and left:
            right.appendleft(left.pop())
        elif char == '>' and right:
            left.append(right.popleft())
    print(''.join(left + right))