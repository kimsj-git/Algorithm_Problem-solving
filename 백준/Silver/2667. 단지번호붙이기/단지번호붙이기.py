import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [[int(char) for char in input().strip()] for _ in range(N)]
drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

village_cnt = 0
houses = []
for sr in range(N):
    for sc in range(N):
        if arr[sr][sc] == 0: continue

        village_cnt += 1
        queue = deque([(sr, sc)])
        arr[sr][sc] = 0
        house_cnt = 1
        while queue:
            r, c = queue.popleft()
            for dr, dc in drc: 
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                    house_cnt += 1
                    arr[nr][nc] = 0
                    queue.append((nr, nc))
        houses.append(house_cnt)

print(village_cnt)
print('\n'.join(map(str, sorted(houses))))