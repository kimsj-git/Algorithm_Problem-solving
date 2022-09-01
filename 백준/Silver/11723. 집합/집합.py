import sys
input = sys.stdin.readline

M = int(input())
all_set = set([i for i in range(1, 21)])
S = set()
for _ in range(M):
    input_str = input().strip()
    if input_str == 'all':
        S = all_set
    elif input_str == 'empty':
        S = set()
    else:
        cmd, x = input_str.split()
        x = int(x)
        if cmd == 'add':
            S.add(x)
        elif cmd == 'remove':
                S.discard(x)
        elif cmd == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif cmd == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)