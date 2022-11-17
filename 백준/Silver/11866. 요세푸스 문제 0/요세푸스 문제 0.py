from collections import deque
d = deque()
result = []
n, k = map(int, input().split())
for i in range(1, n+1):
    d.append(i)
while d:
    for i in range(k-1):
        d.append(d.popleft())
    result.append(d.popleft())

print('<', end='')
print(', '.join(map(str,result)), end='')
print('>')

