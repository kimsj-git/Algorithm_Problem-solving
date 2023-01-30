import sys
input = sys.stdin.readline
INF = int(1e9)

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    distance = {i: INF for i in range(1, N+1)}
    distance[1] = 0
    edges = []  # 간선 정보 저장
    for _ in range(M):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(W):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    # (N-1)번 반복
    for _ in range(N-1):
        # 모든 간선에 대해 조사
        for edge in edges:
            s, e, t = edge
            if distance[e] > distance[s] + t:
                distance[e] = distance[s] + t
    
    # 음의 순환 조사
    flag = False
    for edge in edges:
        s, e, t = edge
        if distance[e] > distance[s] + t:
            flag = True
    
    if flag:
        print('YES')
    else:
        print('NO')