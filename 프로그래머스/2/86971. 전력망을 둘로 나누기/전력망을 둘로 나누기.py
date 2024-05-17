from collections import deque


def bfs(start, graph):
    n = len(graph) - 1
    q = deque([start])
    visited = set([start])
    cnt = 1
    while q:
        v = q.popleft()
        for w in range(1, n + 1):
            if graph[v][w] and w not in visited:
                cnt += 1
                q.append(w)
                visited.add(w)
    return cnt


def solution(n, wires):
    answer = n
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for a, b in wires:
        graph[a][b] = True
        graph[b][a] = True
    
    for a, b in wires:
        graph[a][b] = False
        graph[b][a] = False
        
        a_cnt, b_cnt = bfs(a, graph), bfs(b, graph)
        answer = min(answer, abs(a_cnt - b_cnt)) 
        
        graph[a][b] = True
        graph[b][a] = True
    
    return answer