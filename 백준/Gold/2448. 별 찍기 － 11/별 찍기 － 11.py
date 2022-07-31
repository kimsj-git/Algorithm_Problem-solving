import sys
input = sys.stdin.readline

N = int(input())

def triangle(x):
    if x == 3:
        return ['  *  ', ' * * ', '*****']
    
    unit = triangle(x//2)
    result = []
    for line in unit:
        result.append(' '*(x//2) + line + ' '*(x//2))
    for line in unit:
        result.append(line + ' ' + line)

    return result

print('\n'.join(triangle(N)))