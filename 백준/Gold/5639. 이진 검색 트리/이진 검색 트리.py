import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

N = len(preorder)


def pre2post(s, e):
    if s > e:
        return

    # 1. 전위 순회: 첫번째 값이 root 노드
    root = preorder[s]

    # 2. 이진 검색 트리: root보다 작은 값은 왼쪽 트리, 큰 값은 오른쪽 트리
    # 2-1. root 기준 오른쪽 트리가 시작되는 인덱스 값(mid) 찾기
    mid = e + 1  # 오른쪽 트리 없는 경우의 값
    for i in range(s + 1, e + 1):
        if preorder[i] > root:
            mid = i
            break

    # 3. 후위 순회: root, left, right 분할 후 left -> right -> root 순서로 순회
    # 3-1. root 기준 왼쪽 트리 순회
    pre2post(s + 1, mid - 1)
    # 3-2. root 기준 오른쪽 트리 순회
    pre2post(mid, e)
    # 3-3. 왼쪽, 오른쪽 트리 순회가 끝나면 root값 출력
    print(root)


pre2post(0, N - 1)
