from collections import deque

T = 10
for tc in range(1, T+1):
    tc = int(input())
    deq = deque(list(map(int, input().split())))
    
    i = 0
    while deq[-1] != 0:
        deq.rotate(-1)
        if deq[-1] - (i + 1) > 0:
            deq[-1] -= (i + 1)
        else:
            deq[-1] = 0
        
        i = (i + 1) % 5
    
    print(f"#{tc} {' '.join(map(str, deq))}")