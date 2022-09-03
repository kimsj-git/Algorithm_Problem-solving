import math

N = int(input())
chars = input()
chickens = chars.count('C')
elses = N - chickens

if elses == 0:
    result = chickens
else:
    result = math.ceil(chickens / (elses + 1))
print(result)