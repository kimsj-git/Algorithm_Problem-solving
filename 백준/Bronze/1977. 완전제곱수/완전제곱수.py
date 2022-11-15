m = int(input())
n = int(input())
result = []

for i in range(m,n+1):
    if int(i**(1/2)) == i**(1/2):
        result.append(i)

if len(result) > 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)