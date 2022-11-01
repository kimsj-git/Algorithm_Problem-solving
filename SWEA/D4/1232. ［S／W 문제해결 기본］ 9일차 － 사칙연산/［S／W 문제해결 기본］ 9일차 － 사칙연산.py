'''
트리를 후위 순회하면 사칙연산의 후위 표기식이 되는 것을 이용
'''


# 후위 순회 함수
def postorder(v):
    global postfix
    if tree[v][2] != 0:
        postorder(tree[v][2])
    if tree[v][3] != 0:
        postorder(tree[v][3])
    postfix.append(tree[v][1])  # 후위표현식 postfix에 토큰 저장


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [[0,0,0,0]]
    for _ in range(N):
        data = list(input().split())
        if len(data) == 4:
            tree.append([int(data[0]), data[1], int(data[2]),int(data[3])])
        else:
            tree.append([int(data[0]), data[1], 0, 0])

    postfix = []
    postorder(1)

    # 후위표현식 계산
    stack = []
    for token in postfix:
        if token.isdecimal():
            stack.append(int(token))
        else:
            if token == '+':
                p1 = stack.pop()
                p2 = stack.pop()
                stack.append(p2 + p1)
            elif token == '-':
                p1 = stack.pop()
                p2 = stack.pop()
                stack.append(p2 - p1)
            elif token == '*':
                p1 = stack.pop()
                p2 = stack.pop()
                stack.append(p2 * p1)
            elif token == '/':
                p1 = stack.pop()
                p2 = stack.pop()
                stack.append(p2 / p1)
    result = stack.pop()

    print(f'#{tc} {int(result)}')