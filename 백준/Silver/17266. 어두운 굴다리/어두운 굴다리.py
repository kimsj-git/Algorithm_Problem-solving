import math

N = int(input())
M = int(input())
lights = list(map(int, input().split()))

left = lights[0]
right = N - lights[-1]

btw = 0
for i in range(0, M - 1):
    temp = math.ceil((lights[i + 1] - lights[i]) / 2)
    if temp > btw:
        btw = temp

print(max(left, right, btw))