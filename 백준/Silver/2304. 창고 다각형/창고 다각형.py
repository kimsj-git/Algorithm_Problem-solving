N = int(input())

max_idx = 0
max_height = 0
pillars = []
for _ in range(N):
    idx, height = map(int, input().split())
    pillars.append([idx, height])
    if idx > max_idx:
        max_idx = idx
    if height > max_height:
        max_height = height

heights = [0] * (max_idx + 1)
for idx, height in pillars:
    heights[idx] = height

max_count = heights.count(max_height)

total_area = 0
area = 0
i = 0
while heights[i] < max_height:
    if heights[i] > area:
        area = heights[i]
    total_area += area
    i += 1
# while문을 빠져나오면 i는 최대값의 인덱스가 됨.

# 최대값 기둥이 모두 없어질때까지
while max_count:
    total_area += max_height
    if heights[i] == max_height:
        max_count -= 1
    i += 1

# 인덱스 뒤에서 앞으로 순회
area = 0
j = max_idx
while heights[j] < max_height:
    if heights[j] > area:
        area = heights[j]
    total_area += area
    j -= 1

print(total_area)