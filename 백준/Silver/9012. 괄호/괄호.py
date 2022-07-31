import sys
input = sys.stdin.readline

T = int(input())

def is_vps(str):
    stack = []
    for char in str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

for tc in range(T):
    str = input()
    if is_vps(str):
        print('YES')
    else:
        print('NO')