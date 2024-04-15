from collections import deque


def solution(priorities, location):
    answer = 1
    q = deque([(i, priorities[i]) for i in range(len(priorities))])
    while q:
        p = q.popleft()
        if not q or p[1] >= max(q, key=lambda x: x[1])[1]:
            if p[0] == location:
                return answer
            else:
                answer += 1
        else:
            q.append(p)
    
