import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_index = [0] * (n + 1)
for i in range(n):
    inorder_index[inorder[i]] = i


def preorder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return

    # 후위 순회의 마지막 값이 루트
    root = postorder[postEnd]

    # 중위 순회의 루트 값의 인덱스를 기준으로 왼쪽 서브트리, 오른쪽 서브트리로 나뉨
    # mid = inorder.index(root)   # 시간 초과 코드
    mid = inorder_index[root]

    left_cnt = mid - inStart  # 왼쪽 서브트리의 노드 개수
    right_cnt = inEnd - mid  # 오른쪽 서브트리의 노드 개수

    print(root, end=" ")
    preorder(inStart, mid - 1, postStart, postStart + left_cnt - 1)
    preorder(mid + 1, inEnd, postEnd - right_cnt, postEnd - 1)


preorder(0, n - 1, 0, n - 1)
