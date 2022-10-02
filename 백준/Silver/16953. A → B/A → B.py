from collections import deque
A, B = map(int, input().split())


def BFS(n, cnt):
    deq = deque([(n, cnt)])
    visited = set()
    visited.add(n)

    while deq:
        n, cnt = deq.popleft()
        if n == B:
            return cnt
        
        # 현재 값에 2가지 연산을 한 결과 값이
        # 1) B보다 작거나 같고
        # 2) 과거에 연산된 결과에 없는 새로운 결과라면
        # 결과 값과 연산 횟수를 큐에 추가
        if n * 2 <= B and n * 2 not in visited:
            deq.append((n * 2, cnt + 1))
            visited.add(n * 2)
        if n * 10 + 1 <= B and n * 10 + 1 not in visited:
            deq.append((n * 10 + 1, cnt + 1))
            visited.add(n * 10 + 1)
    
    # 만들 수 없는 경우 -1 반환
    return -1


print(BFS(A, 1))