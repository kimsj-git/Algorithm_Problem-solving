import sys
input = sys.stdin.readline

N = int(input())

def stars(x):
    if x == 1:
        return ['*']
    
    unit = stars(x//3)
    result = []
    
    for line in unit:
        result.append(line*3)
    for line in unit:
        result.append(line + ' '*(x//3) + line)
    for line in unit:
        result.append(line*3)
    
    return result

print('\n'.join(stars(N)))