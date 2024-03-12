from heapq import *


def solution(operations):
    min_heap = []
    max_heap = []
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        if cmd == 'I':
            heappush(min_heap, num)
            heappush(max_heap, -num)
        elif cmd == 'D' and num == 1 and max_heap:
            max_val = - heappop(max_heap)
            min_heap.remove(max_val)
        elif cmd == 'D' and num == -1 and min_heap:
            min_val = heappop(min_heap)
            max_heap.remove(-min_val)
            
    if min_heap:
        return [-heappop(max_heap), heappop(min_heap)]
    else:
        return [0, 0]
