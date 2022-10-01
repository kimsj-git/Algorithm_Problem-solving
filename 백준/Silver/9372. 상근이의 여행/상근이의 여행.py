import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    graph = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        a, b  = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(N-1)