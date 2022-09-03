N = int(input())
# 연결 관계를 저장하는 배열
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    node1, node2 = map(int, input().split())
    arr[node1].append(node2)
    arr[node2].append(node1)

# DFS 이용, 1번 노드부터 시작해서 부모-자식 관계 저장
parent = [None] * (N+1)     # parent[i]: i번 노드의 부모 노드 저장
parent[1] = 0
stack = [1]                 # 시작 노드: 1번
while stack:
    v = stack.pop()
    for w in arr[v]:
        if not parent[w]:
            parent[w] = v       # 부모 노드 저장
            stack.append(w)

for i in range(2, N+1):
    print(parent[i])