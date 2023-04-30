import sys
input = sys.stdin.readline

N, C = map(int, input().split())

houses = [int(input()) for _ in range(N)]
houses.sort()

# 1. 공유기 사이의 거리를 기준으로 이분탐색
s = 1                       # 공유기 사이의 최소거리
e = houses[-1] - houses[0]  # 공유기 사이의 최대거리

result = 0
while s <= e:
    mid = (s + e) // 2
    # 2. 공유기 사이의 최소거리가 mid일 때 공유기 설치되는 집의 개수를 count
    prev_house = houses[0]
    count = 1
    for i in range(1, N):
        if houses[i] - prev_house >= mid:
            count += 1
            prev_house = houses[i]

    # 3-1. 공유기 개수가 많거나 같을 경우: 공유기 간격을 넓혀서 다시 이분탐색
    if count >= C:
        s = mid + 1
        result = mid
    # 3-2. 공유기 개수가 적을 경우: 공유기 간격을 좁혀서 다시 이분탐색
    elif count < C:
        e = mid - 1 # 문제 조건인 공유기 개수를 만족하지 않으므로 result 갱신은 하지 않는다.

print(result)