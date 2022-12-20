def acc(x):
    return (x + 1) * x // 2

T = int(input())
for _ in range(T):
    result = 0
    O_list = input().split('X')
    for Os in O_list:
        result += acc(len(Os))
    print(result)