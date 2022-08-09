N = int(input())

result = 0
while N:
    result += N // 5
    N = N // 5

print(result)