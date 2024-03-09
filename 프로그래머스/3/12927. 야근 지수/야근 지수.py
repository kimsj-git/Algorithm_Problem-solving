from heapq import *

def solution(n, works):
    max_heap = [-x for x in works]
    heapify(max_heap)
    
    for i in range(n):
        max_work = - heappop(max_heap)
        if max_work == 0:
            return 0
        heappush(max_heap, - (max_work - 1))

    answer = sum([x ** 2 for x in max_heap])
    return answer