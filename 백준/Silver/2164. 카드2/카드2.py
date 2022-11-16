from collections import deque

n = int(input())

data = deque([i for i in range(1, n+1)])

while True:
    if len(data) == 1:
        print(data[0])
        break
    data.append(data[1])
    data.popleft()
    data.popleft()