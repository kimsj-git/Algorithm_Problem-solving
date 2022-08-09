n, m = map(int, input().split())

def fives(x):
    result = 0
    while x:
        result += x // 5
        x = x // 5
    return result

def twos(x):
    result = 0
    while x:
        result += x // 2
        x = x // 2
    return result

combi_fives = fives(n) - fives(m) - fives(n-m)
combi_twos = twos(n) - twos(m) - twos(n-m)

print(min(combi_fives, combi_twos))