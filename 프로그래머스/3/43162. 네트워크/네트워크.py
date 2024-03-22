from collections import deque


def solution(n, computers):
    visited = [False] * n
    count = 0
    for computer in range(n):
        if not visited[computer]:
            count += 1
            q = deque([computer])
            while q:
                node = q.popleft()
                for i in range(n):
                    if computers[node][i] and not visited[i]:
                        visited[i] = True
                        q.append(i)
    
    return count