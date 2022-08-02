while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    squares = sorted([a**2, b**2, c**2])
    if squares[0] + squares[1] == squares[2]:
        print('right')
    else:
        print('wrong')
