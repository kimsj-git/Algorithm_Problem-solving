import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0] * (N + 1)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        parent[b] = a

    x, y = map(int, input().split())

    # x부터 루트노드까지 순서대로 순회하며 방문 표시
    visited = [False] * (N + 1)
    while x != 0:
        visited[x] = True
        x = parent[x]

    # y부터 루트노드까지 순서대로 순회하며 방문 기록되어있는지 확인
    while y != 0:
        if visited[y]:
            print(y)
            break
        else:
            y = parent[y]
