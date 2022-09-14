K = int(input())

# 포화 이진트리, 중위 순회
# 루트 노드를 찾고, 양쪽 서브트리에서 루트 노드 찾는 것을 반복

tree = list(map(int, input().split()))
level = [[] for _ in range(K)]


# start: 서브트리의 시작 인덱스, end: 서브트리의 끝 인덱스
# depth: 서브트리 루트노드의 깊이 
def inorder(start, end, depth):
    if start == end:
        level[depth].append(tree[start])
        return
    
    # 루트노드의 인덱스(root): 중간값(포화이진트리, 중위순회)
    root = (start + end) // 2
    # depth 값에 해당하는 level 리스트에 노드 값을 추가
    level[depth].append(tree[root])
    
    # 양옆 서브트리를 재귀호출
    inorder(start, root - 1, depth + 1)
    inorder(root + 1, end, depth + 1)


inorder(0, len(tree) - 1, 0)

for nodes in level:
    for node in nodes:
        print(node, end=' ')
    print()