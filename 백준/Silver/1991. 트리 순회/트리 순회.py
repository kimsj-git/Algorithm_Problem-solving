import sys
input = sys.stdin.readline

N = int(input())

tree = {}
for _ in range(N):
    parent, left, right = input().strip().split()
    tree[parent] = [left, right]


# 전위 순회
def preorder(node):
    print(node, end='')         # 부모
    if tree[node][0] != '.':
        preorder(tree[node][0]) # 왼쪽
    if tree[node][1] != '.':
        preorder(tree[node][1]) # 오른쪽
    # 두 자식 모두 '.'이면, 재귀 이전의 부모노드로 돌아감


# 중위 순회
def inorder(node):
    if tree[node][0] != '.':
        inorder(tree[node][0])  # 왼쪽
    print(node, end='')         # 부모
    if tree[node][1] != '.':
        inorder(tree[node][1])  # 오른쪽


# 후위 순회
def postorder(node):
    if tree[node][0] != '.':
        postorder(tree[node][0]) # 왼쪽
    if tree[node][1] != '.':
        postorder(tree[node][1]) # 오른쪽
    print(node, end='')          # 부모


preorder('A')
print()
inorder('A')
print()
postorder('A')