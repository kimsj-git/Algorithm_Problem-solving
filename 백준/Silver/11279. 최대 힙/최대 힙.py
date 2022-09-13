import sys
input = sys.stdin.readline

N = int(input())

heap = []   # 최대힙

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(heap[0])
            leaf = heap.pop()
            if heap:
                heap[0] = leaf
                idx = 0
                last_idx = len(heap) - 1
                while 2 * idx + 1 <= last_idx:
                    c1_idx = 2 * idx + 1
                    c2_idx = 2 * idx + 2
                    child_idx = c1_idx    # 자식노드 인덱스
                    if c2_idx <= last_idx and heap[c1_idx] < heap[c2_idx]:
                        child_idx = c2_idx
                    if heap[idx] < heap[child_idx]:
                        heap[idx], heap[child_idx] = heap[child_idx], heap[idx]
                    else:
                        break
                    idx = child_idx
        else:
            print(0)
    else:
        heap.append(x)
        idx = len(heap) - 1
        while idx:
            parent_idx = (idx - 1) // 2     # 부모노드 인덱스
            if heap[parent_idx] < heap[idx]:
                heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
            else:
                break
            idx = parent_idx