import sys

sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def make_postorder(preorder, inorder, inorder_index, preStart, preEnd, inStart, inEnd):
    if preStart > preEnd or inStart > inEnd:
        return
    
    root = preorder[preStart]
    
    mid = inorder_index[root]
    left_cnt = mid - inStart
    right_cnt = inEnd - mid

    make_postorder(preorder, inorder, inorder_index, preStart + 1, preStart + left_cnt, inStart, mid - 1)
    make_postorder(preorder, inorder, inorder_index, preEnd - right_cnt + 1, preEnd, mid + 1, inEnd)
    print(root, end=' ')


T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder = []

    inorder_index = [0] * (n + 1)
    for i in range(n):
        inorder_index[inorder[i]] = i
    
    make_postorder(preorder, inorder, inorder_index, 0, n - 1, 0, n - 1)
    print()