import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
INF = float('inf')

# N: 구역의 개수
N = int(input())
# populations[i]: i번 구역의 인구 수
populations = [0] + list(map(int, input().split()))
# graph[i]: i번 구역과 인접한 구역 번호 리스트
graph = {i: list(map(int, input().split()))[1:] for i in range(1, N+1)}


# 구역 번호 리스트를 받아서 연결된 구역들의 인구 합을 반환하는 함수
def BFS(nums: list) -> int:
    q = deque([nums[0]])
    visited = set()
    visited.add(nums[0])
    
    # result: 첫번째 구역과 연결된 구역들의 인구 합
    result = populations[nums[0]]
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if nx not in visited and nx in nums:
                result += populations[nx]
                q.append(nx)
                visited.add(nx)
    return result


minV = INF				# 두 선거구 인구 차이의 최소값 저장
SUM = sum(populations)	# 전체 인구 합

for i in range(1, N//2 + 1):
    for combi in combinations(range(1, N+1), i):
        # 구역1, 구역2 각각에 포함된 구역 번호 리스트
        nums1 = list(combi)
        nums2 = list(i for i in range(1, N+1) if i not in nums1)
        # 구역1, 구역2 각각의 인구 합
        sum1 = BFS(nums1)
        sum2 = BFS(nums2)
		
        # 전체 인구합과 같다면(제외된 선거구가 없다면)
        if sum1 + sum2 == SUM:
            diff = abs(sum1 - sum2)
            if minV > diff:
                minV = diff		# 최소값 갱신

if minV == INF:
    print(-1)
else:
    print(minV)