import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input().strip()) for i in range(n)]

stk = []
pushpop = []

idx = 1
for number in numbers:
    while idx <= number:
        stk.append(idx)
        idx += 1
        pushpop.append('+')
    if number == stk[-1]:
        stk.pop()
        pushpop.append('-')
    else:
        break

if len(stk) == 0:
    print('\n'.join(pushpop))
else:
    print('NO')