'''
벨만-포드 알고리즘
음의 간선이 존재할 때 최소비용 구하기
'''

import sys
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
distance = {i: INF for i in range(1, N+1)}  # 1번 도시부터 i번 도시까지의 최소시간
distance[1] = 0
edges = []  # 간선 정보 저장

for _ in range(M):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

# (정점 - 1)번 반복
for _ in range(N-1):
    # 모든 간선 확인
    for edge in edges:
        s, e, w = edge
        # distance[s] 값이 INF면 현재 s정점을 지나가지 못하므로 제외
        # 현재 간선(s->e)을 지날 때 비용이 더 작으면 distance[e] 갱신
        if distance[s] != INF and distance[e] > distance[s] + w:
            distance[e] = distance[s] + w

# 음의 순환 확인: 모든 간선 한번 더 확인한다.
result = True
for edge in edges:
    s, e, w = edge
    if distance[s] != INF and distance[e] > distance[s] + w:
        result = False
        break

if result:
    for i in range(2, N+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
else:
    print(-1)